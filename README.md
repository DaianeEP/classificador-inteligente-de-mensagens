# Classificador Inteligente de Mensagens

## Descrição

Projeto desenvolvido para a etapa **P0** da capacitação [TrendsIA Sistemas Agentes](https://github.com/DaianeEP/trendsia-sistemas-agentes).

O objetivo é utilizar Inteligência Artificial para classificar automaticamente solicitações acadêmicas em categorias pré-definidas, interpretando o contexto e a intenção da mensagem sem depender exclusivamente de palavras-chave.

O projeto utiliza um Large Language Model (LLM) para realizar a classificação semântica das solicitações, permitindo compreender a intenção do usuário mesmo quando diferentes palavras ou formas de escrita são utilizadas.


## Categorias

- **Pedagógico:** Dúvidas sobre aulas, notas, professores e conteúdo.
- **Financeiro:** Boletos, mensalidades, bolsas e negociações.
- **Documentos:** Histórico escolar, declarações, certificados e atestados.
- **Matrícula:** Inscrição, rematrícula, trancamento e transferência.
- **Justificativa de Ausência:** Atestados médico e abono de faltas.
- **Outros:** Solicitações gerais que exigem triagem humana.

## Tecnologias

- **Linguagem:** Python
- **Integração:** Requests / API de LLM
- **Infraestrutura & Versionamento:** Docker, Git e GitHub

## Estrutura

```text
classificador-inteligente-de-mensagens/
├── app.py
├── main.py
├── llm.py
├── requirements.txt
├── README.md
├── Dockerfile
└── .gitignore
```

## Como Executar

1. Clone o repositório: 

```bash
git clone https://github.com/DaianeEP/classificador-inteligente-de-mensagens.git
cd classificador-inteligente-de-mensagens
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente necessárias (quando aplicável).

4. Execute o projeto:

```bash
python main.py
```

## Exemplo de Uso

Entrada:

```text
Preciso solicitar meu histórico escolar.
```

Categoria esperada:

```text
Documentos
```

## Status

🚧 MVP em desenvolvimento

✅ Estrutura inicial concluída

✅ Entrada textual implementada

✅ Projeto publicado no GitHub

✅ Docker configurado e testado

⏳ Integração com LLM em andamento


## Autora

**Daiane Eleutério Pereira** - Bacharelando em Inteligência Artificial (UNIVESP) | AWS Certified Cloud Practitioner
[LinkedIn](https://www.linkedin.com/in/daianeep/) [GitHub](https://github.com/DaianeEP/)