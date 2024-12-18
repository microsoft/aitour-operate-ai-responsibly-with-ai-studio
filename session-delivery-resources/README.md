## How To Use

Welcome,

The following resources are intended for a presenter to learn and deliver the session.

We're glad you are here and look forward to your delivery of this amazing content. As an experienced presenter, we know you know HOW to present so this guide will focus on WHAT you need to present. It will provide you a full run-through of the presentation created by the presentation design team.

Along with the video of the presentation, this document will link to all the assets you need to successfully present including PowerPoint slides and demo instructions &
code.

1. Read this document in its entirety.
1. Watch the video presentation
1. Ask questions of the Lead Presenter

## File Summary

| Resources          | Links                            | Description |
|-------------------|----------------------------------|-------------------|
| PowerPoint        | [Presentation](https://aka.ms/AAryyth) | Slides |
| Videos            | [Microsoft Ignite Recording](https://ignite.microsoft.com/sessions/BRK113?source=sessions) | Example of a similar version of this session |

## Get Started

This repository is designed to help you deliver this session and is divided in to the following sections:

| [Slides](#slides) | [Demos](#demos) | [Deployment](#deployment--preparation) | 
|-------------------|---------------------------|--------------------------------------
| 45 slides - 45 minutes| 10 demos | Demo setup

## Slides

The [slides](https://aka.ms/AAryyth) have presenter notes in each part of the session

### Timing

| Time        | Description 
--------------|-------------
0:00 - 5:00   | Intro to the session 
5:00 - 8:00   | Multi-Agent Creative Writing Copilot
08:00 - 10:00 | Govern
10:00 - 14:00 | Map
14:00 - 24:00 | Mitigate
24:00 - 36:00 | Measure
36:00 - 42:00 | Operate
42:00 - 45:00 | Session review

## Deployment / Preparation

[Instructions and prerequisites are outlined here](https://github.com/Azure-Samples/contoso-creative-writer/tree/trustworthy-ai-demo?tab=readme-ov-file#vs-code-dev-containers). 

**Only** use the **trustworthy-ai-demo** branch. Deploying locally is recommended as multiple people have consistently encountered errors or quota issues when deploying via GitHub Codespaces. When deploying in VS Code, ensure that you are on the **trusthworthy-ai-demo** branch as it does not default to that branch. You should **only** use the **Sweden Central** region for this sample. For this session, only complete the **Getting Started**, **Deployment**, **Testing the Sample**, and **Evaluating Results** sections.

Prior to testing the sample or running evaluation results, you will need to modify the `azure_deployment` listed in the following agent promptys (located at `src/api/agents`):

- writer
- researcher
- product

The `azure_deployment` should be `gpt-4o` given that `gpt-4o-mini` is not a valid deployment name in this sample. You're welcome to manually execute a `gpt-4o-mini` deployment for a faster demo experience, however `gpt-4o` will suffice. Please note that `azd up` will **not** deploy a `gpt-4o-mini` deployment for you.

Evaluations can take anywhere from 3 mins - 30 mins. Therefore, it's suggested to have already completed the evaluation runs **prior** to starting the session. The current dataset includes 11 text inputs and 8 images. You can trim the number of examples to 3 text and 2 images for a shorter run time.

For text evaluation, remove rows in `src/api/evaluate/eval_inputs.jsonl`.

For images evaluation, update `/src/api/evaluate/evaluate.py`, to `range(1,4)` for the line `for image_num in range(1, 9):` (currently line 458).

## Demos

| Demo 	                                                                                               | Minutes | Video |
-------------------------------------------------------------------------------------------------------|---------|----------------- | 
|  0 - [Multi-Agent Creative Writer](/session-delivery-resources/demo0-multi-agent-creative-writer.md) |  1:21      |[aka.ms/AAtl1ag](https://aka.ms/AAtl1ag)  |
|  1 - [Model Catalog](/session-delivery-resources/demo1-model-catalog.md)         |1:54  |[aka.ms/AAtk56m](https://aka.ms/AAtk56m)|
|  2 - [Evaluate Models with Your Own Data](/session-delivery-resources/demo2-evaluate-models-own-data.md) |  1:35      |[aka.ms/AAtkk2a](https://aka.ms/AAtkk2a) |
|  3 - [System Message](/session-delivery-resources/demo3-system-message.md) |   0:37    |[aka.ms/AAtl1al](https://aka.ms/AAtl1al)  |
|  4 - [Custom Evaluator](/session-delivery-resources/demo4-custom-evaluator.md) |  0:15      |[aka.ms/AAtk56k](https://aka.ms/AAtk56k)  |
|  5 - [Local Evaluation](/session-delivery-resources/demo5-local-evaluation.md) |  1:18      |[aka.ms/AAtl1ah](https://aka.ms/AAtl1ah)  |
|  6 - [Cloud Evaluation](/session-delivery-resources/demo6-cloud-evaluation.md) |  1:48     |[aka.ms/AAtl1ae](https://aka.ms/AAtl1ae) |
|  7 - [Image Evaluation](/session-delivery-resources/demo7-image-evaluation.md) |  1:40     |[aka.ms/AAtk56o](https://aka.ms/AAtk56o) |
|  8 - [GitHub Actions](/session-delivery-resources/demo8-github-actions.md) |   0:56    |[aka.ms/AAtk56n](https://aka.ms/AAtk56n) |
|  9 - [Online Evaluation & App Insights](/session-delivery-resources/demo9-online-evaluation-app-insights.md) |  1:38     |[aka.ms/AAtkk27](https://aka.ms/AAtkk27) |

## Change Log

Here is a log of the changes made to this file:

| Date       | Changes |
|------------|---------|
| 2024.09.16 | Added Change log, Additional language section with *coming soon* notice |
| 2024.11.27 | Updated Session Delivery Resources README.md |
| 2024.12.02 | Add links to demos and slide deck |
