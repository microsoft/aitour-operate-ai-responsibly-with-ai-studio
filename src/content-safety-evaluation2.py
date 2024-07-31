import os
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions, TextCategory
import json
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

folder = Path(__file__).parent.absolute().as_posix()

def analyze_text(text):
    print(f"Analyzing text: {text}")
    # analyze text
    key = os.environ["CONTENT_SAFETY_KEY"]
    endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

    # Create an Azure AI Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

    # Contruct request
    request = AnalyzeTextOptions(text="text")

    # Analyze text
    try:
        response = client.analyze_text(request)
    except HttpResponseError as e:
        print("Analyze text failed.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    hate_result = next(item for item in response.categories_analysis if item.category == TextCategory.HATE)
    self_harm_result = next(item for item in response.categories_analysis if item.category == TextCategory.SELF_HARM)
    sexual_result = next(item for item in response.categories_analysis if item.category == TextCategory.SEXUAL)
    violence_result = next(item for item in response.categories_analysis if item.category == TextCategory.VIOLENCE)

    if hate_result:
        print(f"Hate severity: {hate_result.severity}")
    if self_harm_result:
        print(f"SelfHarm severity: {self_harm_result.severity}")
    if sexual_result:
        print(f"Sexual severity: {sexual_result.severity}")
    if violence_result:
        print(f"Violence severity: {violence_result.severity}")

def process_file(file_name):
    with open(file_name, "r") as file:
        for line_number, line in enumerate(file, start=1):
            # Parse the current line as JSON
            data = json.loads(line.strip())
            # Extract the text field
            text = data.get('text', '')
            if text:
                print(f"Analyzing text: {text}")
                #print(f"Now evaluating line {line_number}: {text}")
                analyze_text(text)
            else:
                print("Warning: No 'text' field found or 'text' field is empty.")

if __name__ == "__main__":
    # Path to your JSONL file in the same directory
    jsonl_file_path = folder + '/adv_articles.jsonl'
    
    # Process the file
    process_file(jsonl_file_path)