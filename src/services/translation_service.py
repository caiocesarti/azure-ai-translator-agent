from langchain_openai.chat_models.azure import AzureChatOpenAI
from src.utils.config import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def translate_article(text: str, target_language: str) -> str:
    """
    Translates text using Azure OpenAI with a technical translator persona.
    """
    try:
        # Initialize Client using Config
        client = AzureChatOpenAI(
            azure_endpoint=Config.ENDPOINT,
            api_key=Config.API_KEY,
            api_version=Config.API_VERSION,
            deployment_name=Config.DEPLOYMENT_NAME,
            # Note: For strict reasoning models (o1/preview), temperature might need to be removed/fixed.
            # We follow the prototype validation (temperature=1 or omitted if problematic).
            # If Config.TEMPERATURE is set, we use it.
            temperature=Config.TEMPERATURE,
            max_retries=1
        )
        
        messages = [
            ("system", "Você atua como tradutor especializado em textos técnicos. REGRAS: 1) Preserve termos técnicos em inglês (ex: RAG, CI/CD, API, LLM). 2) Mantenha blocos de código intactos. 3) Use headers Markdown (##) para separar seções."),
            ("user", f"Traduza o seguinte texto para {target_language}, mantendo a formatação técnica:\n\n{text}")
        ]
        
        response = client.invoke(messages)
        return response.content
        
    except Exception as e:
        logger.error("Erro na tradução", exc_info=True, extra={
            "target_language": target_language,
            "text_length": len(text)
        })
        return f"Error: {e}"
