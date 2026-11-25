from openai import OpenAI, DefaultHttpxClient
from config import LLM_API_URL, LLM_MODEL

CATEGORIAS = [
    "Pedagógico",
    "Financeiro",
    "Documentos",
    "Matrícula",
    "Justificativa de Ausência",
    "Outros"
]


def montar_prompt(texto):
    return f"""
Você é um classificador de solicitações acadêmicas.

Classifique a mensagem em apenas uma das categorias abaixo:

- Pedagógico
- Financeiro
- Documentos
- Matrícula
- Justificativa de Ausência
- Outros

Mensagem:
{texto}

Responda somente com o nome da categoria.
"""


def classificar_mensagem(texto):
    prompt = montar_prompt(texto)

    client = OpenAI(
        base_url=LLM_API_URL,
        api_key="qualquer",
        http_client=DefaultHttpxClient(
            verify=False
        )
    )

    resposta = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.choices[0].message.content.strip()
