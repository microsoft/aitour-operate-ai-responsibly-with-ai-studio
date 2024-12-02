# Demo 6 - Cloud Evaluation

The goal of this demo is to demonstrate the ability to run evaluations in the cloud. You will view the results in the Azure AI Foundry portal.

## Demo delivery tips

### Prior to delivery

1. Have [Azure AI Foundry](https://ai.azure.com) open in the browser and navigate to the respective project for the demo.
1. Open the `evaluate.py` file located at `src/api/evaluate`.
1. Within the `evaluate.py` file, navigate to the `evaluate_remote` function.
1. In `evaluate.py`, comment out the `run_orchestrator`, `evaluate_orchestrator` and `evaluate_image` functions. This will avoid running a local and image evaluation, respectively.
1. In `evaluate.py`, comment out lines **453, 456-464** as these lines are only for local and image evaluations.

> [!NOTE]
> It is recommended, if delivered live, to pre-run the evaluation before you get on stage. The evaluation can range from 5-30 mins. A video recording with no audio has been provided if you would prefer to speak over a prerecorded and edited version for speed.

### During delivery

1. Scroll through the `evaluate_remote` function and discuss the similarity in evaluator setup compared to a local evaluation.
1. Run the `evaluate.py` script in the terminal to show the beginning stages of running an evaluation in the cloud.
1. Select the **AI Studio URI** link in the terminal to navigate to the evaluation in the **Azure AI Foundry** portal.
1. Show in the **Azure AI Foundry** portal that the evaluation is in progress.
1. View the evaluation results in the **Azure AI Foundry** portal.