from llm import montar_prompt

texto = input("Digite a solicitação do aluno: ")

prompt = montar_prompt(texto)

print("\nPrompt gerado:")
print(prompt)