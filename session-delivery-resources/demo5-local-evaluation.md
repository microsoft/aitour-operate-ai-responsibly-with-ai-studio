# Demo 5 - Local Evaluation

The goal of this demo is to demonstrate the ability to run an evaluation locally and view the results in the Azure AI Foundry portal.

## Demo delivery tips

### Prior to delivery

1. Have [Azure AI Foundry](https://ai.azure.com) open in the browser and navigate to the respective project for the demo.
1. Open the `evaluators.py` file located at `src/api/evaluate`.
1. In `evaluate.py`, comment out the `evaluate_remote` and `evaluate_image` functions. This will avoid running a cloud and image evaluation, respectively.
1. In `evaluate.py`, comment out lines **454-464** as these lines are only for cloud and image evaluations.

> [!NOTE]
> It is recommended, if delivered live, to pre-run the evaluation before you get on stage. The evaluation can take up 30 mins. A video recording with no audio has been provided if you would prefer to speak over a prerecorded and edited version for speed.

### During delivery

1. Show the location of the **Friendliness** evaluator in the `evaluators.py` file.
1. Show the location of the built-in evaluators in the `evaluators.py` file (within the `ArticleEvaluator` class).
1. Discuss column mapping for the built-in evaluators at a high level. Highlight the requirement for the dataset to consist of a **response**, **context**, and **query**.
1. View the evaluation results in the **Azure AI Foundry** portal. Discuss the **Metric dashboard** and **Detailed metrics result**.