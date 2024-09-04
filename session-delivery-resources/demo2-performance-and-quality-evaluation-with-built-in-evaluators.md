# Demo 2 - Performance and quality evaluation with built-in evaluators

The goal of this demo is to demonstrate the use of the ``ArticleEvaluator`` class for evaluating the quality and performance of AI-generated content in a Creative Writing Copilot. This demo will showcase how to use built-in evaluators such as Groundedness, Relevance, Coherence, and Fluency to assess AI-generated articles. Additionally, we will explore the evaluation process, including tracing and asynchronous evaluations using background threads.

Before starting, make sure you have completed the [Deployment](/session-delivery-resources/README.md#deployment--preparation) steps

> [!NOTE]
> Currently you must have your deployment running in East US 2 data center and the Azure AI Studio project be in that location too for this demo to run.


## Demo delivery tips
> [!NOTE]
> This demo is a good candidate to run live, however a [video recording with no audio](https://aka.ms/AAs1s41) has been provided


### Prior to delivery

1. Open your VS Code and from the repository, open the files: `evaluators.py`, `evaluate.py`. Have these files ready for the demo.
2. In the terminal, navigate to the `src/api` and run the command `python -m evaluate.evaluate` to start the evaluation process. Make sure it is running successfully.

### During the delivery

1. Open the `evaluators.py` file and walk through the code segments mentioned on the slide deck.
2. Open the `evaluate.py` file and show the code segments mentioned on the slide deck.
3. In the termnnal, show the evaluation process running and the output of the evaluation. Discuss the results shown.


Back to all [Demo Instructions](/session-delivery-resources/README.md#demos)