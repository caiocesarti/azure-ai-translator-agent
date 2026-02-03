import pytest

@pytest.fixture
def sample_html_with_article():
    """HTML de exemplo com tag <article> e ruído"""
    return '''
    <html>
        <head><script>alert('test')</script></head>
        <body>
            <nav>Menu Principal</nav>
            <article>
                <h1>Technical Article About RAG</h1>
                <p>This article explains CI/CD and API design.</p>
                <pre><code>def example(): pass</code></pre>
            </article>
            <div class="comments-area">
                <p>Comment 1</p>
                <p>Comment 2</p>
            </div>
            <footer>Footer content</footer>
        </body>
    </html>
    '''

@pytest.fixture
def sample_html_without_article():
    """HTML sem tag <article>, apenas <body>"""
    return '''
    <html>
        <body>
            <div class="content">
                <h1>Simple Content</h1>
                <p>Basic paragraph.</p>
            </div>
        </body>
    </html>
    '''

@pytest.fixture
def mock_azure_response():
    """Mock de resposta do Azure OpenAI"""
    class MockResponse:
        content = "# Artigo Técnico Sobre RAG\n\nEste artigo explica CI/CD e design de API."
    return MockResponse()
