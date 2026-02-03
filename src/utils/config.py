
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview")
    DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-5-mini")
    
    # Senior Logic: Preview models often don't support temperature
    # We set it to 1 by default, or None if the model is strictly reasoning
    TEMPERATURE = 1
