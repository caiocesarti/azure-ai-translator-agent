
import os
from datetime import datetime
from src.services.extraction_service import extract_text_from_url
from src.services.translation_service import translate_article
from src.utils.logger import setup_logger

logger = setup_logger(__name__, "translator.log")

def main():
    logger.info("🚀 Azure AI Technical Translator Starting...")
    
    url = input("Cole a URL do artigo técnico: ").strip()
    
    # Validate URL format
    if not url.startswith(('http://', 'https://')):
        logger.error("URL inválida. Deve começar com http:// ou https://")
        return
    
    lang = "pt-br"
    
    # 1. Extraction
    logger.info(f"Extraindo conteúdo de {url} (Modo Sênior/Targeted)...")
    text = extract_text_from_url(url)
    
    if text:
        # 2. Translation
        logger.info("Enviando para o Azure OpenAI (isso pode levar alguns segundos)...")
        translated_text = translate_article(text, lang)
        
        # 3. Persistence (Output to Markdown file)
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{output_dir}/article_translated_{timestamp}.md"
        
        if "Error:" not in translated_text:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(translated_text)
            
            logger.info(f"✅ Sucesso! Artigo salvo em: {filename}")
            logger.info("="*40)
        else:
            logger.error("Falha na tradução")
            logger.error(translated_text)
            
    else:
        logger.error("Falha na extração do texto")

if __name__ == "__main__":
    main()
