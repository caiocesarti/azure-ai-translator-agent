import pytest
from unittest.mock import Mock, patch
from bs4 import BeautifulSoup
from src.services.extraction_service import extract_text_from_url


class TestExtractionService:
    """Test suite for extraction_service.py"""
    
    def test_removes_scripts_and_styles(self, sample_html_with_article):
        """Verifica que <script> e <style> são removidos"""
        with patch('src.services.extraction_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.text = sample_html_with_article
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            result = extract_text_from_url("https://example.com")
            
            assert "alert('test')" not in result
            assert "Technical Article" in result
    
    def test_removes_navigation_elements(self, sample_html_with_article):
        """Valida remoção de nav, footer, comments"""
        with patch('src.services.extraction_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.text = sample_html_with_article
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            result = extract_text_from_url("https://example.com")
            
            assert "Menu Principal" not in result
            assert "Footer content" not in result
            assert "Comment 1" not in result
            assert "Technical Article" in result
    
    def test_prioritizes_article_tag(self, sample_html_with_article):
        """Verifica que <article> é priorizado sobre <body>"""
        with patch('src.services.extraction_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.text = sample_html_with_article
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            result = extract_text_from_url("https://example.com")
            
            # Deve conter conteúdo do <article>
            assert "RAG" in result
            assert "CI/CD" in result
            # Não deve conter conteúdo fora do <article>
            assert "Menu Principal" not in result
    
    def test_handles_request_exception(self):
        """Testa tratamento de erro de rede"""
        with patch('src.services.extraction_service.requests.get') as mock_get:
            mock_get.side_effect = Exception("Network error")
            
            result = extract_text_from_url("https://invalid-url.com")
            
            assert result is None
    
    def test_preserves_code_blocks(self, sample_html_with_article):
        """Garante que blocos <code> são preservados"""
        with patch('src.services.extraction_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.text = sample_html_with_article
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            result = extract_text_from_url("https://example.com")
            
            assert "def example()" in result
