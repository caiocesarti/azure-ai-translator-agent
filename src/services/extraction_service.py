
import requests
from bs4 import BeautifulSoup
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def extract_text_from_url(url: str) -> str:
    """
    Extracts text from a given URL with 'Senior' precision.
    Prioritizes <article> and <main> tags to avoid menu/footer noise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. Clean up script, styles, and "noise" specific elements
        # Explicitly remove comments, action bars, and sidebars often found inside <article>
        noise_selectors = [
            "script", "style", "nav", "footer", "header", "aside",
            # Common class/id names for comments and UI junk
            ".comments-area", "#comments", ".action-bar", ".crayons-article-actions", 
            ".crayons-layout__sidebar", ".article-wrapper__footer"
        ]
        
        for selector in noise_selectors:
            for element in soup.select(selector):
                element.decompose()
            
        # 2. Targeted Extraction (V2 Logic)
        # Priority: <article> -> <main> -> <div class="content"> -> body
        main_content = (
            soup.find('article') or 
            soup.find('main') or 
            soup.find('div', class_='content') or 
            soup.body
        )
        
        if main_content:
            text = main_content.get_text(separator=' ')
        else:
            text = soup.get_text(separator=' ')
            
        # 3. Text Cleanup
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        return '\n'.join(chunk for chunk in chunks if chunk)
        
    except Exception as e:
        logger.error(f"Falha ao extrair URL {url}", exc_info=True)
        return None
