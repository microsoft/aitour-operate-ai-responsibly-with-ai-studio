# Trustworthy AI: Advanced AI risk evaluation and mitigation
[![Azure AI Community Discord](
https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-00001-leestott)

## Session Description

Explore Azure AI Studio’s new tools for generative AI security, privacy, and quality. Shift from reactive risk management to agile, responsible-by-design governance for better observability and efficiency.

## Learning Outcomes

- Azure AI is the vanguard for responsible AI tools
- Gain actionable guidance to help your company develop more safe, trustworthy generative AI apps

## Technology Used

- [Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/)
- [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Azure AI Evaluation SDK](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)
- [Prompty](https://prompty.ai/)
- [Azure App Insights](https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview)
- [Github Actions](https://docs.github.com/actions)

## Required Quota

| Model Name            | Model Version | SKU Name         | Capacity |
|------------------------|--------------|------------------------|---------------|
| gpt-35-turbo          | 1106          | Standard         | 20       |
| text-embedding-ada-002| 2             | Standard         | 20       |
| gpt-4o                | 2024-05-13    | GlobalStandard   | 20       |
| gpt-4                 | 0613          | Standard         | 10       |

## Additional Resources and Continued Learning

Links                             | Description        |
|:----------------------------------|:-------------------|
[Learn Collection](https://aka.ms/operationalize-rai) | Developer tools to operationalize AI responsibly |

## Content Owners

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<table>
<tr>
    <td align="center"><a href="http://learnanalytics.microsoft.com">
        <img src="https://github.com/aprilspeight.png" width="100px;" alt="April Speight
"/><br />
        <sub><b>April Speight
</b></sub></a><br />
            <a href="https://github.com/aprilspeight" title="Lead Presenter">📢</a> 
    </td>
    <td align="center"><a href="http://learnanalytics.microsoft.com">
        <img src="https://github.com/amynic.png" width="100px;" alt="Amy Boyd
"/><br />
        <sub><b>Amy Boyd
</b></sub></a><br />
            <a href="https://github.com/amynic" title="talk">📢</a> 
    </td>
    </td>
    <td align="center"><a href="http://learnanalytics.microsoft.com">
        <img src="https://github.com/gdequeiroz.png" width="100px;" alt="Gabriela de Queiroz
"/><br />
        <sub><b>Gabriela de Queiroz
</b></sub></a><br />
            <a href="https://github.com/gdequeiroz" title="talk">📢</a> 
    </td>
</tr></table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Responsible AI

Microsoft is committed to helping our customers use our AI products responsibly, sharing our learnings, and building trust-based partnerships through tools like Transparency Notes and Impact Assessments. Many of these resources can be found at [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft’s approach to responsible AI is grounded in our AI principles of fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Large-scale natural language, image, and speech models - like the ones used in this sample - can potentially behave in ways that are unfair, unreliable, or offensive, in turn causing harms. Please consult the [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) to be informed about risks and limitations.

The recommended approach to mitigating these risks is to include a safety system in your architecture that can detect and prevent harmful behavior. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) provides an independent layer of protection, able to detect harmful user-generated and AI-generated content in applications and services. Azure AI Content Safety includes text and image APIs that allow you to detect material that is harmful. Within Azure AI Studio, the Content Safety service allows you to view, explore and try out sample code for detecting harmful content across different modalities. The following [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guides you through making requests to the service.

Another aspect to take into account is the overall application performance. With multi-modal and multi-models applications, we consider performance to mean that the system performs as you and your users expect, including not generating harmful outputs. It's important to assess the performance of your overall application using [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). You also have the ability to create and evaluate with [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

You can evaluate your AI application in your development environment using the [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Given either a test dataset or a target, your generative AI application generations are quantitatively measured with built-in evaluators or custom evaluators of your choice. To get started with the azure ai evaluation sdk to evaluate your system, you can follow the [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Once you execute an evaluation run, you can [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).
