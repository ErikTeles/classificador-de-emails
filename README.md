### 📖 Sobre o Projeto
**Classificador de E-mails** é uma aplicação que utiliza modelos de linguagem para analisar e classificar e-mails automaticamente. A aplicação lê arquivos PDF enviados pelo usuário, extrai o conteúdo e retorna:

- **Classificação do e-mail** (ex: Produtivo, Informativo, etc.)
- **Motivo da classificação**
- **Sugestão de resposta**

O projeto inclui um front-end simples em HTML/CSS/JS para envio de arquivos e visualização do resultado, e um backend robusto com FastAPI para processamento dos PDFs e integração com o modelo de linguagem.

---

### 🛠 Tecnologias Utilizadas
* **Python 3.11+**
* **FastAPI** para construção da API
* **Uvicorn** como servidor ASGI
* **pypdf** para leitura de PDFs
* **Groq / modelos de linguagem** para classificação de e-mails
* **HTML, CSS e JavaScript** para interface web
* **Python-Multipart** para upload de arquivos

---

### ⚙️ Funcionalidades
1. **Upload de PDFs:** Permite enviar e-mails em PDF para classificação.
2. **Classificação automática:** Identifica se o e-mail é produtivo ou improdutivo.
3. **Motivo da classificação:** Explica a razão da classificação.
4. **Sugestão de resposta:** Gera uma resposta breve baseada no conteúdo do e-mail.
5. **Front-end funcional:** Interface web para envio de PDFs e visualização do resultado em tempo real.

---

### 🚀 Como Executar Localmente

Antes de tudo, é necessário definir a variável de ambiente com sua chave de API para o modelo de linguagem. Você pode fazer isso de duas formas:

1. **Usando variável de ambiente** (recomendado):  
   - No Windows (PowerShell):
     ```powershell
     setx GROQ_API_KEY "sua_chave_aqui"
     ```
   - No macOS/Linux:
     ```bash
     export GROQ_API_KEY="sua_chave_aqui"
     ```

2. **Ou alterando diretamente no arquivo** `src/services/LLMService.py` (não recomendado para produção).

---

1. **Clonar o repositório:**
    ```bash
    git clone https://github.com/ErikTeles/classificador-de-emails
    cd classificador-de-emails
    ```

2. **Criar o ambiente virtual:**
    ```bash
    python -m venv venv
    ```

3. **Ativar o ambiente virtual:**
    - No Windows:
      ```bash
      venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Instalar as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Rodar o servidor FastAPI:**
    ```bash
    uvicorn src.main:app --reload
    ```

6. **Acessar a aplicação no navegador:**
    ```
    http://localhost:8000
    ```

---

### 🔌 Endpoints da API

#### 1. Upload de PDF
`POST /upload`
* **Body:** arquivo PDF (`multipart/form-data`)
* **Retorno:**
```json
{
  "filename": "email.pdf",
  "response": {
    "classification": "Produtivo",
    "reason": "O e-mail requer uma ação específica do destinatário...",
    "suggested_response": "Prezado João, agradeço pela aprovação..."
  }
}
