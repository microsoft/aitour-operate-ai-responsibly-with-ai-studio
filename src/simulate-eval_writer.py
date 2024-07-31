from pathlib import Path
from azure.identity import DefaultAzureCredential
from promptflow.evals.synthetic import AdversarialSimulator, AdversarialScenario
from typing import List, Dict, Any, Optional

import os

azure_ai_project = {
    "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
    "resource_group_name": os.environ.get("AZURE_OPENAI_RESOURCE_GROUP"),
    "project_name": os.environ.get("AZURE_OPENAI_NAME"),
    "credential": DefaultAzureCredential(),
}    

from api.agents.orchestrator import write_article

request = "Can you find the latest camping trends and what folks are doing in the winter?"
instructions = "Can you find the relevant information needed and good places to visit"

response = write_article(request, instructions)

for item in response:
    print(item)

'''simulator = AdversarialSimulator(azure_ai_project=azure_ai_project)

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
    response_from_writer_agent = get_research(request, instructions, feedback)

    formatted_response = {
        "content": response_from_writer_agent["article"],
        "role": "assistant",
        "context": {
            "citations": response_from_writer_agent["web"],
        },
    }
    messages["messages"].append(formatted_response)
    return {"messages": messages["messages"], "stream": stream, "session_state": session_state, "context": context}


    outputs = await simulator(
        scenario=AdversarialScenario.ADVERSARIAL_CONTENT_GEN_UNGROUNDED, 
        max_conversation_turns=1,
        max_simulation_results=5,
        target=callback,
        jailbreak=False
    )'''