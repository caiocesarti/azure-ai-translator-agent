```mermaid
flowchart TD
    Start([Usuário insere URL]) --> Valid{URL Válida?}
    
    Valid -->|Não| Error([Exibe Erro])
    Valid -->|Sim| Scraper[Extraction Service]
    
    Scraper --> Clean{Limpeza HTML}
    Clean -->|Remove scripts/styles| Clean2[Remove UI noise]
    Clean2 -->|Busca article/main| Extract[Extrai texto limpo]
    
    Extract --> Translator[Translation Service]
    
    Translator --> Config[Config Module]
    Config -->|Carrega .env| Creds[Azure Credentials]
    
    Translator --> LangChain[LangChain Client]
    LangChain -->|System + User Prompt| Azure[Azure OpenAI<br/>GPT-5-mini]
    
    Azure -->|Retorna Tradução| Gen[Gera Conteúdo Markdown]
    Gen --> Save[Salva em output/]
    
    Save --> End([Arquivo .md gerado])
    
    Scraper -.->|Logs| Logger[Logger Module]
    Translator -.->|Logs| Logger
    Valid -.->|Logs| Logger
    Save -.->|Logs| Logger
    Logger -.->|Arquivo| LogFile[logs/translator.log]
    
    style Scraper fill:#e1f5ff
    style Translator fill:#fff4e1
    style Azure fill:#ffe1e1
    style Config fill:#e1ffe1
    style Logger fill:#f0f0f0
    style Valid fill:#fff0e1
```

## Componentes

### 1. Extraction Service
- **Responsabilidade**: Scraping inteligente de artigos web.
- **Técnica**: Prioriza tags semânticas (`<article>`, `<main>`).
- **Limpeza**: Remove elementos de navegação, comentários e scripts.

### 2. Translation Service
- **Engine**: Azure OpenAI via LangChain.
- **Prompt**: System message especializado em terminologia técnica.
- **Output**: Markdown formatado.

### 3. Config Module
- **Segurança**: Gerencia credenciais via `.env`.
- **Flexibilidade**: Suporta diferentes modelos e versões de API.

### 4. Logger Module
- **Observabilidade**: Logging estruturado com timestamps.
- **Destinos**: Console (stdout) + arquivo (`logs/translator.log`).
- **Níveis**: INFO para fluxo normal, ERROR para falhas.

## Fluxo de Dados

1. URL → Scraper (HTML bruto)
2. Scraper → Translator (Texto limpo)
3. Translator → Azure OpenAI (Texto + Prompt)
4. Azure → Translator (Tradução)
5. Translator → Filesystem (Arquivo .md)
