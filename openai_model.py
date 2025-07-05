# openai_model.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def call_openai(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message["content"]
