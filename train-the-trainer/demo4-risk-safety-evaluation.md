# Demo 4 - Risk and safety evaluation with built-in evaluators

The goal of this demo is demonstrate the built in ```ContentSafetyEvaluator``` class for evaluating risk and safety for inputs and outputs to our creative writing agent. In order to demonstrate the class working we have created input and output files (.jsonl) that contain adversarial data that is evaluated. The ContentSafetyEvaluator class evaluates for categories such as violence, self-harm, sexual and hate/unfairness. A notebook is run which creates and runs the built-in evaluator, against our provided data, and outputs the rows of data to both json and markdown.

Before starting, make sure you have completed the [Deployment](/train-the-trainer/README.md#deployment--preparation) steps

## Demo delivery tips

> [!NOTE]
> It is recommended this demo, if delivered live, is pre-run before you get on stage. The evaluations can take up to 1 min each to run and provide results. A [video recording with no audio](https://aka.ms/AAs1kev) has been provided if you would prefer to speak over a prerecorded and edited version for speed.

### Prior to delivery

1. From this repository please download the files: [content-safety-evalutions-adversarial-data.ipynb](/src/content-safety-evaluations-adversarial-data.ipynb), [adversarial_input.jsonl](/src/adversarial_input.jsonl) and [adversarial_output.jsonl](/src/adversarial_output.jsonl)
2. Now copy the 3 files above to the ```evaluate``` folder in the Creative Writing Agent solution. Filepath = ```src/api/evaluate/```.
3. Open the [content-safety-evalutions-adversarial-data.ipynb](/src/content-safety-evaluations-adversarial-data.ipynb) within the Creative Writing Agent solution.
![Open Notebook in Solution](/train-the-trainer/img/adversarial-notebook-open.png)
4. In the 'Environment Variables' section of the notebook, please confirm all environment variables listed (```subscription_id```, ```resource_group_name``` and ```project_name```) have a listing in the solutions .env file (at the root of the solution).
![Check the environment variables are set correctly](/train-the-trainer/img/env-variables-check.png)
5. **Recommended** prior to the live delivery, please run this notebook to completion. Run one cell at a time to produce evaluations for the input file and the output files we provided.
6. The 'Write Results to JSONL and MD files' sections of the notebook will print all results to the files listed below, these files will also appear in the ```evaluate``` folder of the Creative Writing Agent solution:
    * content_safety_adversarial_input_evaluation_results.jsonl
    * content_safety_adversarial_input_evaluation_results.md
    * content_safety_adversarial_output_evaluation_results.jsonl
    * content_safety_adversarial_output_evaluation_results.md

![Show .jsonl and .md files output](/train-the-trainer/img/show-output-files.png)

### During delivery

1. Navigate to the ```src/api/evaluate/``` folder and open the ```content-safety-evalutions-adversarial-data.ipynb```
2. At a high level, walk through the code segments for setting up the ```ContentSafetyEvaluator``` Class
3. Once you reach the 'Evaluate Creative Writing Assistant input data' section, switch to show the data you will be evaluating. Show the ```adversarial_input.jsonl``` file contents to show it encourages dangerous behaviour
4. Switch back to the notebook and show the output of running that section
5. Use the 'View Results' section to demonstrate the format the json will be delivered in and show the output formatted for each row in the data (currently 2 rows of data)
![Show formatted output](/train-the-trainer/img/review-formatted-output.png)
6. Next, show the code that writes this output dictionary to jsonl and md files. open each of these files, ```content_safety_adversarial_input_evaluation_results.jsonl``` and ```content_safety_adversarial_input_evaluation_results.md``` to demonstrate the output
7. Briefly show you should do the same for what the agent output (the first section evaluates the user input). Discuss the results shown.