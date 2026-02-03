import pytest
from unittest.mock import patch, mock_open
from src.app import main


class TestApp:
    """Test suite for app.py (integration tests)"""
    
    @patch('builtins.input', return_value='invalid-url')
    @patch('src.app.logger')
    def test_url_validation_rejects_invalid(self, mock_logger, mock_input):
        """Testa que URLs sem http:// são rejeitadas"""
        main()
        
        # Verifica que logger.error foi chamado
        assert mock_logger.error.called
        error_message = mock_logger.error.call_args[0][0]
        assert "URL inválida" in error_message
    
    @patch('builtins.input', return_value='https://example.com')
    @patch('src.app.extract_text_from_url', return_value=None)
    @patch('src.app.logger')
    def test_handles_extraction_failure(self, mock_logger, mock_extract, mock_input):
        """Testa comportamento quando extração falha"""
        main()
        
        # Verifica que erro de extração foi logado
        assert any("extração" in str(call).lower() for call in mock_logger.error.call_args_list)
    
    @patch('builtins.input', return_value='https://example.com')
    @patch('src.app.extract_text_from_url', return_value='Sample text')
    @patch('src.app.translate_article', return_value='Texto traduzido')
    @patch('builtins.open', new_callable=mock_open)
    @patch('src.app.os.makedirs')
    @patch('src.app.logger')
    def test_successful_translation_flow(self, mock_logger, mock_makedirs, mock_file, mock_translate, mock_extract, mock_input):
        """Testa fluxo completo: URL → Extração → Tradução → Arquivo"""
        main()
        
        # Verifica que o arquivo foi escrito
        assert mock_file.called
        mock_file().write.assert_called_once_with('Texto traduzido')
        
        # Verifica que sucesso foi logado
        assert any("Sucesso" in str(call) for call in mock_logger.info.call_args_list)
