"""
Integração com LLM para classificação de solicitações acadêmicas.
"""

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