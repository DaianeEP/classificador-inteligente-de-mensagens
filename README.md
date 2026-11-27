# Classificador Inteligente de Mensagens

## Descrição

Projeto desenvolvido para a etapa **P0** da capacitação [TrendsIA Sistemas Agentes](https://github.com/DaianeEP/trendsia-sistemas-agentes).

O objetivo é utilizar Inteligência Artificial para classificar automaticamente solicitações acadêmicas em categorias pré-definidas, interpretando o contexto e a intenção da mensagem sem depender exclusivamente de palavras-chave.

O projeto foi desenvolvido para utilização de um Large Language Model (LLM) na classificação semântica de solicitações acadêmicas. A arquitetura da aplicação foi estruturada para integração com modelos de IA disponibilizados pelo ambiente da capacitação (Devel), permitindo a classificação das mensagens com base na intenção do usuário levando em consideração os diferentes contextos para uma mesma solicitação.


## Categorias

- **Pedagógico:** Dúvidas sobre aulas, notas, professores e conteúdo.
- **Financeiro:** Boletos, mensalidades, bolsas e negociações.
- **Documentos:** Histórico escolar, declarações, certificados e atestados de matrícula e conclusão.
- **Matrícula:** Inscrição, rematrícula, trancamento e transferência.
- **Justificativa de Ausência:** Atestados médico e abono de faltas.
- **Outros:** Solicitações gerais que exigem triagem humana.

## Tecnologias

- **Linguagem:** Python
- **Framework Web:** Flask
- **Cominicação HTTP:** Requests
- **Modelos de IA:** Qwen 3.5 (LLM Institucional)
- **Infraestrutura e Versionamento:** Docker, Git e GitHub
- **Testes:** Pytest

## Estrutura do Projeto

```text
classificador-inteligente-de-mensagens/
├── src/
│   ├── app.py
│   ├── llm.py
│   └── config.py
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

---

## Descrição da Estrutura

### src/

Contém o código-fonte principal da aplicação.

- **app.py:** API Flask responsável pelos endpoints da aplicação.
- **llm.py:** integração com o LLM institucional e classificação das mensagens.
- **config.py:** gerenciamento das configurações e variáveis de ambiente.

### tests/

Contém os testes automatizados do projeto.

- **test_llm.py:** valida o comportamento da geração de prompts.

### Arquivos de Configuração

- **.env.example:** modelo de variáveis de ambiente.
- **.dockerignore:** arquivos ignorados durante a criação da imagem Docker.
- **.gitignore:** arquivos ignorados pelo Git.
- **Dockerfile:** define a construção da imagem Docker.
- **requirements.txt:** dependências do projeto.
- **README.md:** documentação do projeto.

---

## Como Executar

### Executar Localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python src/app.py
```

A aplicação ficará disponível em:

```text
http://localhost:8080
```

---

## Endpoint de Status

Acesse:

```text
http://localhost:8080
```

Resposta:

```json
{
  "status": "online",
  "projeto": "Classificador Inteligente de Mensagens"
}
```

---

## Endpoint de Classificação

### Requisição

```http
POST /classificar
```

Exemplo:

```json
{
  "texto": "Preciso solicitar meu histórico escolar"
}
```

### Resposta

```json
{
  "categoria": "Documentos",
  "mensagem": "Preciso solicitar meu histórico escolar"
}
```

---

## Exemplo de Uso

Classificação de uma solicitação acadêmica.

### Entrada

```json
{
  "texto": "Preciso solicitar meu histórico escolar"
}
```

### Saída

```json
{
  "categoria": "Documentos",
  "mensagem": "Preciso solicitar meu histórico escolar"
}
```

---

## Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para configuração da integração com o LLM.

Arquivo `.env.example`:

```env
LLM_API_URL=https://llm-internal.softex:9001/v1
LLM_MODEL=qwen3.5:9b-q4_K_M
```

---

## Executar com Docker

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

---

## Testes

Executar os testes automatizados:

```bash
pytest
```

---

## Status do Projeto

✅ Projeto publicado no GitHub

✅ Docker configurado e validado

✅ Aplicação implantada no ambiente Devel LLM

✅ Integração com o LLM institucional concluída

✅ Endpoint `POST /classificar` implementado

✅ Classificação semântica funcional

✅ Nível Básico concluído


## Autora

**Daiane Eleutério Pereira** - Bacharelando em Inteligência Artificial (UNIVESP) | AWS Certified Cloud Practitioner
[LinkedIn](https://www.linkedin.com/in/daianeep/) [GitHub](https://github.com/DaianeEP/)