import os
import json
from promptflow.core import AzureOpenAIModelConfiguration
from threading import Thread
from opentelemetry import trace
from opentelemetry.trace import set_span_in_context
from promptflow.client import load_flow

model_config = AzureOpenAIModelConfiguration(
        azure_deployment==os.environ["AZURE_OPENAI_4_EVAL_DEPLOYMENT_NAME"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
    )


friendliness_eval = load_flow(source="api/evaluate/prompty/friendliness.prompty", model={"configuration": model_config})

class ArticleEvaluator:
    def __init__(self, model_config):
        self.evaluators = [
            friendliness_eval
        ]

    def __call__(self, *, response: str, **kwargs):
        output = {}
        for evaluator in self.evaluators:
            result = json.loads(evaluator(
                response=response
            ))
            print(f"Result from evaluator: {result}")       
            if not isinstance(result, dict):
                raise ValueError(f"Evaluator returned non-dict result: {result}")
            output.update(result)
        return output

def evaluate_article(data, trace_context):
    print("starting offline evals")

    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("run_evaluators", context=trace_context) as span:
        span.set_attribute("inputs", json.dumps(data))
        configuration = model_config
        evaluator = ArticleEvaluator(configuration)
        results = evaluator(query=data['query'], context=data['context'], response=data['response'])
        resultsJson = json.dumps(results)
        span.set_attribute("output", resultsJson)

        print("results: ", resultsJson)

def evaluate_article_in_background(request, instructions, research, products, article):
    eval_data = {
        "query": json.dumps({
            "request": request,
            "instructions": instructions,
        }),
        "context": json.dumps({
            "research": research,
            "products": products,
        }),
        "response": json.dumps(article)
    }

    # propagate trace context to the new thread
    span = trace.get_current_span()
    trace_context = set_span_in_context(span)
    thread = Thread(target=evaluate_article, args=(eval_data, trace_context,))
    thread.start()