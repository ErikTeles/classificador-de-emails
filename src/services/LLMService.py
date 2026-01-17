import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def classify_email_stream(email_text: str):
    stream = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """Você é um assistente que ajuda classificando 
                documentos PDF que são referentes a e-mails dos usuários.
                Classifique o conteúdo do PDF em uma das seguintes categorias:
                
                1. Produtivo - Emails que requerem uma ação ou resposta específica
                (ex.: solicitações de suporte técnico, atualização sobre casos em aberto,
                dúvidas sobre o sistema);
                2. Improdutivo - Emails que não necessitam de uma ação imediata
                (ex.: mensagens de felicitações, agradecimentos).
                
                Além disso, forneça uma sugestão de resposta breve para os e-mails classificados.
                Responda EXCLUSIVAMENTE em um JSON válido e sem markdown, com os campos: "classification, reason, suggested_response".
                """,
            },
            {
                "role": "user",
                "content": email_text,
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=True,
    )

    full_response = ""

    for chunk in stream:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content

    return full_response