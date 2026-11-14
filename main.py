CATEGORIAS = [
    "Pedagógico",
    "Financeiro",
    "Documentos",
    "Matrícula",
    "Justificativa de Ausência",
    "Outros"
]

texto = input("Digite a solicitação do aluno: ")

print("\nMensagem recebida:")
print(texto)

print("\nCategorias possíveis:")
for categoria in CATEGORIAS:
    print(f"- {categoria}")