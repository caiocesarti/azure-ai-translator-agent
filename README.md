🇺🇸 **English version: [README.en.md](README.en.md)**

# Azure AI Technical Article Translator

> **Agente de tradução técnica automatizado, baseado em Azure OpenAI (GPT-5) e LangChain. Oferece recursos de extração de dados HTML direcionada e localização contextual para artigos.**

O **Azure AI Technical Translator** é uma ferramenta de automação projetada para traduzir artigos técnicos com alta fidelidade, preservando a formatação de código e a terminologia específica.
Este projeto utiliza **Azure OpenAI (GPT-5)** e **LangChain** para orquestrar o fluxo de tradução, com um foco especial em "Targeted Scraping" para limpar ruídos de web (menus, ads).

## 🚀 Funcionalidades

*   **Extração Inteligente**: Scraper configurado para identificar tags semânticas (`<article>`, `<main>`) e ignorar "lixo" visual.
*   **Tradução Contextual**: Prompt System especializado em terminologia técnica (DevOps, Cloud, IA).
*   **Segurança**: Gerenciamento de credenciais via variáveis de ambiente.
*   **Persistência**: Salva os artigos traduzidos automaticamente em Markdown.

## 🛠️ Tecnologias

*   Python 3.12+
*   Azure OpenAI
*   LangChain
*   BeautifulSoup4

## 📦 Como Usar

1.  **Clone o repositório**
2.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure o ambiente**:
    *   Renomeie `.env.example` para `.env`
    *   Insira suas chaves do Azure.
4.  **Execute**:
    ```bash
    python -m src.app
    ```

## 📐 Arquitetura

Para entender o fluxo de dados e a estrutura de componentes, consulte:
- [Diagrama de Arquitetura](docs/architecture.md)
- [Decisões Técnicas](docs/technical_decisions.md)

## 🧪 Testes

O projeto inclui uma suite de testes automatizados com pytest:

```bash
# Instalar dependências de teste
pip install pytest pytest-cov pytest-mock

# Executar todos os testes
python -m pytest -v

# Executar com relatório de cobertura
python -m pytest --cov=src --cov-report=html
```

**Cobertura de Testes:**
- `test_extraction_service.py`: Testa scraping, limpeza de HTML, priorização de tags
- `test_translation_service.py`: Testa integração Azure OpenAI (com mocks)
- `test_app.py`: Testa fluxo completo end-to-end

## 🔮 Roadmap

- [x] Testes automatizados com pytest
- [x] Logging estruturado
- [ ] Suporte a múltiplos idiomas via CLI
- [ ] API REST para integração web
- [ ] Containerização com Docker
- [ ] CI/CD com GitHub Actions

## � Autor

**Caio Cesar**  
📧 [caiocesardeveloper@gmail.com](mailto:caiocesardeveloper@gmail.com)

## �📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
