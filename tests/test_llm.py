from src.llm import montar_prompt


def test_montar_prompt():
    texto = "Preciso solicitar meu histórico escolar"

    resultado = montar_prompt(texto)

    assert texto in resultado
    assert "Categorias disponíveis" in resultado