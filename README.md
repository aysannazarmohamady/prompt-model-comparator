# prompt-model-comparator

This project runs the same prompts through multiple LLMs (starting with OpenAI models) and stores the responses for comparison.

## Files
- `main.py`: Runs prompts and collects responses
- `openai_model.py`: Handles OpenAI API calls
- `prompts.json`: List of prompts to test
- `results.csv`: Output file
- `config.py`: Store your OpenAI API key

## How to run
1. Install dependencies:
```bash
pip install -r requirements.txt
