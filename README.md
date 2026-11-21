# Classificador Inteligente de Mensagens

## Descrição

Projeto desenvolvido para a etapa **P0** da capacitação [TrendsIA Sistemas Agentes](https://github.com/DaianeEP/trendsia-sistemas-agentes).

O objetivo é utilizar Inteligência Artificial para classificar automaticamente solicitações acadêmicas em categorias pré-definidas, interpretando o contexto e a intenção da mensagem sem depender exclusivamente de palavras-chave.

O projeto foi desenvolvido para utilização de um Large Language Model (LLM) na classificação semântica de solicitações acadêmicas. A arquitetura da aplicação foi estruturada para integração com modelos de IA disponibilizados pelo ambiente da capacitação, permitindo a classificação das mensagens com base na intenção do usuário e não apenas em palavras-chave.


## Categorias

- **Pedagógico:** Dúvidas sobre aulas, notas, professores e conteúdo.
- **Financeiro:** Boletos, mensalidades, bolsas e negociações.
- **Documentos:** Histórico escolar, declarações, certificados e atestados.
- **Matrícula:** Inscrição, rematrícula, trancamento e transferência.
- **Justificativa de Ausência:** Atestados médico e abono de faltas.
- **Outros:** Solicitações gerais que exigem triagem humana.

## Tecnologias

- **Linguagem:** Python
- **Framework Web:** Flask
- **Cominicação HTTP:** Requests
- **Modelos de IA:** LLM (Lhama - ambiente da capacitação)
- **Infraestrutura e Versionamento:** Docker, Git e GitHub
- **Testes:** Pytest

## Estrutura

```text
classificador-inteligente-de-mensagens/
├── src/
│   ├── app.py
│   └── llm.py
│
├── tests/
│   └── test_llm.py
│
├── .env.example
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## Descrição da Estrutura

### src/
Contém o código-fonte principal da aplicação.

- **app.py**: API Flask responsável pelos endpoints da aplicação.
- **llm.py**: lógica de geração do prompt de classificação.

### tests/
Contém os testes automatizados do projeto.

- **test_llm.py**: valida o comportamento da função de geração de prompts.

### Arquivos de configuração

- **.env.example**: modelo de variáveis de ambiente.
- **.dockerignore**: arquivos ignorados durante o build do Docker.
- **.gitignore**: arquivos ignorados pelo Git.
- **Dockerfile**: define a criação da imagem Docker.
- **requirements.txt**: dependências do projeto.
- **README.md**: documentação do projeto.


## Como Executar

### Executar localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a aplicação:

```bash
python src/app.py
```

A API será disponibilizada em:

```text
http://localhost:8080
```

### Testar a aplicação

No navegador, acesse:

```text
http://localhost:8080
```

Retorno esperado:

```json
{
  "status": "online",
  "projeto": "Classificador Inteligente de Mensagens",
  "categorias": [
    "Pedagógico",
    "Financeiro",
    "Documentos",
    "Matrícula",
    "Justificativa de Ausência",
    "Outros"
  ]
}
```

### Executar com Docker

Construir a imagem:

```bash
docker build -t classificador-inteligente .
```

Executar o container:

```bash
docker run -p 8080:8080 classificador-inteligente
```

A aplicação ficará disponível em:

```text
http://localhost:8080
```

## Exemplo de Uso

Exemplo da classificação esperada após integração completa com LLM.

## Status

🚧 MVP em desenvolvimento

✅ Estrutura inicial concluída

✅ Entrada textual implementada

✅ Projeto publicado no GitHub

✅ Docker configurado e testado

✅ Estrutura preparada para integração com LLM

⏳ Evolução para classificação semântica em andamento


## Autora

**Daiane Eleutério Pereira** - Bacharelando em Inteligência Artificial (UNIVESP) | AWS Certified Cloud Practitioner
[LinkedIn](https://www.linkedin.com/in/daianeep/) [GitHub](https://github.com/DaianeEP/)