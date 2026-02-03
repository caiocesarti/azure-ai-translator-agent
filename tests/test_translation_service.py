import pytest
from unittest.mock import Mock, patch
from src.services.translation_service import translate_article


class TestTranslationService:
    """Test suite for translation_service.py"""
    
    @patch('src.services.translation_service.AzureChatOpenAI')
    def test_translation_preserves_technical_terms(self, mock_client_class, mock_azure_response):
        """Valida que termos técnicos permanecem em inglês"""
        mock_client = Mock()
        mock_client.invoke.return_value = mock_azure_response
        mock_client_class.return_value = mock_client
        
        text = "This article explains RAG, CI/CD, and API design."
        result = translate_article(text, "pt-br")
        
        assert "RAG" in result
        assert "CI/CD" in result
        assert "API" in result
    
    @patch('src.services.translation_service.AzureChatOpenAI')
    def test_handles_azure_api_error(self, mock_client_class):
        """Testa tratamento de erro da API do Azure"""
        mock_client = Mock()
        mock_client.invoke.side_effect = Exception("Azure API Error")
        mock_client_class.return_value = mock_client
        
        result = translate_article("Test text", "pt-br")
        
        assert "Error:" in result
