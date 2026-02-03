🇧🇷 **Versão em Português: [README.md](README.md)**

# Azure AI Technical Article Translator

> **Automated technical translation agent powered by Azure OpenAI (GPT-5) and LangChain. Features targeted HTML scraping and context-aware localization for engineering articles.**

**Azure AI Technical Translator** is an automation tool designed to translate technical articles with high fidelity, preserving code formatting and domain-specific terminology.
This project leverages **Azure OpenAI (GPT-5)** and **LangChain** to orchestrate the translation pipeline, with a special focus on "Targeted Scraping" to filter out web noise (menus, ads, comments).

## 🚀 Features

*   **Smart Extraction**: Scraper configured to identify semantic tags (`<article>`, `<main>`) and ignore visual clutter.
*   **Context-Aware Translation**: System prompt specialized in technical terminology (DevOps, Cloud, AI).
*   **Security**: Credential management via environment variables.
*   **Persistence**: Automatically saves translated articles as Markdown files.

## 🛠️ Tech Stack

*   Python 3.12+
*   Azure OpenAI
*   LangChain
*   BeautifulSoup4

## 📦 Getting Started

1.  **Clone the repository**
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure environment**:
    *   Rename `.env.example` to `.env`
    *   Add your Azure credentials.
4.  **Run**:
    ```bash
    python -m src.app
    ```

## 📐 Architecture

To understand the data flow and component structure, check out:
- [Architecture Diagram](docs/architecture.md)
- [Technical Decisions](docs/technical_decisions.md)

## 🧪 Testing

This project includes a comprehensive automated test suite with pytest:

```bash
# Install test dependencies
pip install pytest pytest-cov pytest-mock

# Run all tests
python -m pytest -v

# Run with coverage report
python -m pytest --cov=src --cov-report=html
```

**Test Coverage:**
- `test_extraction_service.py`: Tests scraping, HTML cleanup, tag prioritization
- `test_translation_service.py`: Tests Azure OpenAI integration (with mocks)
- `test_app.py`: Tests full end-to-end flow

## 🔮 Roadmap

- [x] Automated tests with pytest
- [x] Structured logging
- [ ] Multi-language support via CLI
- [ ] REST API for web integration
- [ ] Docker containerization
- [ ] CI/CD with GitHub Actions

## 👤 Author

**Caio Cesar**  
📧 [caiocesardeveloper@gmail.com](mailto:caiocesardeveloper@gmail.com)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
