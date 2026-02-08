from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_model_client():
    openai_model_client= OpenAIChatCompletionClient(
            model="nvidia/nemotron-3-nano-30b-a3b:free",
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
            model_info={
                "vision": False,
                "function_calling": True,
                "json_output": False,
                "structured_output":True,
                "family": "unknown",
                "max_tokens": 8192,
            }
    )
    return openai_model_client