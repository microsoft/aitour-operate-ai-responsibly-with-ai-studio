import json
from azure.identity import DefaultAzureCredential
from promptflow.evals.synthetic import AdversarialSimulator, AdversarialScenario
import json
import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from typing import Optional, List, Dict, Any
import asyncio
from promptflow.evals.evaluators import ContentSafetyEvaluator


azure_ai_project = {
    "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
    "resource_group_name": os.environ.get("AZURE_OPENAI_RESOURCE_GROUP"),
    "project_name": os.environ.get("AZURE_OPENAI_NAME"),
    "credential": DefaultAzureCredential(),
}   


def call_endpoint(query):
    endpoint = os.getenv("ENDPOINT_URL", "https://yzspkl6zntec6-cog.openai.azure.com/")
    deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default")
        
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        azure_ad_token_provider=token_provider,
        api_version="2024-05-01-preview",
    )
        

    completion = client.chat.completions.create(
        model=deployment,
        messages= [
        {
        "role": "user",
        "content": "What are the differences between Azure Machine Learning and Azure AI services?"
        }],
        max_tokens=800,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )

    # Convert the response to JSON
    completion_json = completion.to_json()

    # Parse the JSON response
    response_dict = json.loads(completion_json)

    # Extract the desired value (content of the assistant's message)
    my_variable = response_dict['choices'][0]['message']['content']

    # Print the extracted value
    #print(my_variable)

simulator = AdversarialSimulator(azure_ai_project=azure_ai_project)

async def callback(
    messages: List[Dict],
    stream: bool = False,
    session_state: Any = None,  # noqa: ANN401
    context: Optional[Dict[str, Any]] = None,
) -> dict:
    messages_list = messages["messages"]
    # get last message
    latest_message = messages_list[-1]
    query = latest_message["content"]
    context = None
    # call your own deployment endpoint
    copilot_response = call_endpoint(query)
    
    # we are formatting the response to follow the openAI chat protocol format
    formatted_response = {
        "content": copilot_response["answer"],
        "role": "assistant",
        "context": 
            {
            "citations": copilot_response["context"],
        },
    }
    messages["messages"].append(formatted_response)
    return {"messages": messages["messages"], "stream": stream, "session_state": session_state, "context": context}

async def main():
    outputs = await simulator(
        scenario=AdversarialScenario.ADVERSARIAL_SUMMARIZATION, 
        max_conversation_turns=1,
        max_simulation_results=3,
        target=callback,
        jailbreak=False
    )
    print(outputs)

    print(outputs.to_eval_qa_json_lines())
    with open("adv_qa_pairs.jsonl", "w") as f:
        f.write(outputs.to_eval_qa_json_lines())


'''    with open("adv_qa_pairs.jsonl", "r") as f:
        json_line_as_json = json.loads(f.readline())

    content_safety_evaluator = ContentSafetyEvaluator(project_scope=azure_ai_project)

    content_safety_eval_result = content_safety_evaluator(
        question=json_line_as_json["question"], answer=json_line_as_json["answer"]
    )'''


# Ensure the main function is run in the event loop
if __name__ == "__main__":
    asyncio.run(main())