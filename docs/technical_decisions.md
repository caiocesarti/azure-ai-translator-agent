# Decisões Técnicas

Este documento explica as escolhas de arquitetura e as soluções para desafios encontrados durante o desenvolvimento.

## 1. Por que LangChain?

**Problema**: Integração direta com a API do Azure OpenAI requer gerenciamento manual de autenticação, retry logic e versionamento.

**Solução**: LangChain abstrai essas complexidades e oferece:
- Cliente `AzureChatOpenAI` pré-configurado.
- Suporte nativo a diferentes versões de API.
- Facilita futuras expansões (ex: adicionar RAG ou Agents).

**Trade-off**: Adiciona uma dependência, mas o ganho em produtividade e manutenibilidade compensa.

---

## 2. Targeted Scraping vs. Full-Page Scraping

**Problema Inicial**: A primeira versão (Colab V1) extraía todo o `<body>`, incluindo menus, sidebars e comentários. Isso:
- Desperdiçava tokens (custo).
- Poluía o contexto da tradução.

**Solução (V2)**: Implementamos busca hierárquica:
```python
main_content = (
    soup.find('article') or 
    soup.find('main') or 
    soup.find('div', class_='content') or 
    soup.body
)
```

**Resultado**: Redução significativa no tamanho do input (excluindo menus, sidebars e comentários), tradução mais focada.

---

## 3. Resolução de Erros do Azure OpenAI

### Erro 404 - "Resource Not Found"
**Causa**: Versão da API (`2024-xx-xx`) incompatível com o modelo `gpt-5-mini` (lançado em 2025).

**Solução**: Atualizar para `api_version="2025-04-01-preview"`.

**Aprendizado**: Modelos preview exigem versões de API específicas. Sempre consultar a documentação do Azure.

---

### Erro 400 - "Unsupported value: temperature"
**Causa**: Modelos de raciocínio (como `gpt-5-mini`) não permitem ajuste de temperatura.

**Solução**: Remover o parâmetro `temperature` ou fixá-lo em `1`.

**Código**:
```python
client = AzureChatOpenAI(
    azure_endpoint=Config.ENDPOINT,
    api_version=Config.API_VERSION,
    deployment_name=Config.DEPLOYMENT_NAME,
    temperature=1,  # Obrigatório para gpt-5-mini
    max_retries=1
)
```

**Aprendizado**: Modelos preview têm restrições diferentes dos modelos GA (Generally Available).

---

## 4. Estrutura de Serviços

**Decisão**: Separar lógica em `services/` e `utils/`.

**Justificativa**:
- **Testabilidade**: Cada serviço pode ser testado isoladamente.
- **Escalabilidade**: Fácil adicionar novos serviços (ex: `summarization_service.py`).
- **Padrão Corporativo**: Reflete arquitetura usada em empresas (ex: microserviços).

---

## 5. Segurança: `.env` e `.gitignore`

**Problema**: Credenciais hardcoded no código são um risco de segurança crítico.

**Solução**:
1. Usar `python-dotenv` para carregar variáveis de ambiente.
2. Adicionar `.env` ao `.gitignore`.
3. Fornecer `.env.example` como template.

**Resultado**: O repositório pode ser público sem expor chaves secretas.

---

## 6. Output em Markdown

**Decisão**: Salvar traduções como arquivos `.md` em vez de `.txt` ou `.docx`.

**Justificativa**:
- **Universalidade**: Markdown é renderizado nativamente no GitHub, VS Code e navegadores.
- **Preservação de Estrutura**: Títulos, listas e código ficam formatados.
- **Leveza**: Arquivos de texto puro (sem overhead de formatos binários).

---

## Próximas Melhorias

### ✅ Concluído
- **Testes Automatizados**: pytest com 12 testes (unitários e integração).
- **Logging Estruturado**: Substituição de `print()` por `logging.Logger`.

### 🔜 Pendente
1. **Suporte a múltiplos idiomas**: Adicionar parâmetro CLI para escolher idioma de destino.
2. **Batch Processing**: Traduzir múltiplas URLs de uma vez.
3. **CI/CD**: GitHub Actions para rodar testes em cada commit.
