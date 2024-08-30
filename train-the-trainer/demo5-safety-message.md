# Demo 5 - Add safety message to agent Prompty files

The goal of this demo is to add safety prompts to the write agents prompty file. Initially the prompty lacks safety and behavioral guardrails, which are crucial for preventing the generation of harmful content. By adding safety prompts, you’ve introduced an essential layer of risk mitigation, ensuring that the Creative Writing Copilot is better equipped to avoid producing harmful content. This includes instructions to steer clear of harmful content, ungrounded fabrications, copyright infringements, jailbreaks, and manipulative content.

Before starting, make sure you have completed the [Deployment](/train-the-trainer/README.md#deployment--preparation) steps


## Demo delivery tips

> [!NOTE]
> This demo is a good candidate to run live, however a [video recording with no audio](https://aka.ms/AAs1kev) has been provided

1. In the Creative Writer Agent solution navigate to the ```writer.prompty``` file. Filepath = ```src/api/agents/write/writer.prompty```.
2. Open the file to find a standard prompty file and navigate down to the 'Final Instructions' section. Below this is where you will paste the safety messages, before the 'user:' section
3. Find the [safety_system_message.prompty](../src/safety_system_message.prompty) file in **this repo** and copy its contents into the ```writer.prompty``` file in the creative writing agent solution

![Safety system message added to the writer.prompty](/train-the-trainer/img/writer-prompty-with-safety-messages.png)
