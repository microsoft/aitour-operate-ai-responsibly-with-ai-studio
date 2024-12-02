# Demo 7 - Image Evaluation

The goal of this demo is to demonstrate the ability to evaluate images for harm. You will view the results within the Azure AI Foundry portal.

## Demo delivery tips

### Prior to delivery

1. Have [Azure AI Foundry](https://ai.azure.com) open in the browser and navigate to the respective project for the demo.
1. Open the `evaluators.py` file located at `src/api/evaluate`.
1. Within the `evaluators.py` file, navigate to the `ImageEvaluator` class.
1. Open the `evaluate.py` file located at `src/api/evaluate`.
1. Within the `evaluate.py` file, navigate to the `evaluate_image` function.
1. In `evaluate.py`, comment out the `evaluate_remote`, `run_orchestrator`, and `evaluate_orchestrator` functions. This will avoid running a cloud and local text-based evaluation, respectively.
1. In `evaluate.py`, comment out lines **453 - 454** as these lines are only for remote and local text-based evaluations.

> [!NOTE]
> It is recommended, if delivered live, to pre-run the evaluation before you get on stage. The evaluation can take up to 5 mins. A video recording with no audio has been provided if you would prefer to speak over a prerecorded and edited version for speed.

### During delivery

1. Review and discuss the risk and safety metrics within the `ImageEvaluator` class of the `evaluators.py` file.
1. Show the `evaluate_image` function within the `evaluate.py` file.
1. Run the `evaluate.py` script in the terminal to show the beginning stages of running an image evaluation. You can call out that the script starts by compressing the image size.
1. View the image evaluation results in the terminal and then select the **View in Azure AI Studio** link to view the results in the **Azure AI Foundry** portal.
1. If any of the results are greater than **very low**, view and discuss the **Reasoning** within the **Detailed metrics result**. In addition, view the image in question within the project. Images are located within `src/api/images`.