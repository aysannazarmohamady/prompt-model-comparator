# main.py
import json
import csv
from openai_model import call_openai

with open("prompts.json", "r") as f:
    prompts = json.load(f)

models = ["gpt-3.5-turbo", "gpt-4"]

with open("results.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "category", "model", "prompt", "response"])

    for prompt_data in prompts:
        prompt_text = prompt_data["task"]
        for model in models:
            response = call_openai(prompt_text, model=model)
            writer.writerow([
                prompt_data["id"],
                prompt_data["category"],
                model,
                prompt_text,
                response.strip().replace("\n", " ")
            ])
            print(f"Prompt {prompt_data['id']} done with {model}")
