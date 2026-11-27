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

    if not LLM_API_URL:
        raise ValueError(
            "Configuração ausente: LLM_API_URL não definida."
        )

    if not LLM_MODEL:
        raise ValueError(
            "Configuração ausente: LLM_MODEL não definido."
        )

    prompt = montar_prompt(texto)

    try:

        client = OpenAI(
            base_url=LLM_API_URL,
            api_key="qualquer",
            http_client=DefaultHttpxClient(
                verify=False,
                timeout=30.0
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

        if not resposta.choices:
            raise ValueError(
                "O LLM retornou uma resposta vazia."
            )

        conteudo = resposta.choices[0].message.content

        if not conteudo:
            raise ValueError(
                "O conteúdo retornado pelo LLM está vazio."
            )

        return conteudo.strip()

    except ValueError:
        raise

    except Exception as erro:

        raise RuntimeError(
            f"Falha de comunicação com o LLM: {str(erro)}"
        )