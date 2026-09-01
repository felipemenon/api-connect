# API Connect

## Sobre o projeto

A API Connect é uma API REST desenvolvida para realizar o gerenciamento de usuários. O projeto permite cadastrar, listar, consultar, atualizar e remover usuários utilizando os principais métodos do protocolo HTTP.

O objetivo é aplicar na prática conceitos de desenvolvimento back-end, arquitetura REST, comunicação cliente-servidor, manipulação de dados JSON e códigos de status HTTP.

## Tecnologias utilizadas

- Python
- Flask
- JSON
- API REST
- Git
- GitHub
- Apidog para testes das requisições

## Como executar o projeto

### 1. Instalar o Flask

```bash
py -m pip install flask
```

### 2. Executar a aplicação

```bash
py app.py
```

O servidor será iniciado em:

```text
http://127.0.0.1:5000
```

## Endpoints da API

| Método | Endpoint | Finalidade | Status esperado |
|---|---|---|---|
| GET | /usuarios | Lista todos os usuários | 200 OK |
| GET | /usuarios/:id | Busca um usuário pelo ID | 200 ou 404 |
| POST | /usuarios | Cadastra um novo usuário | 201 Created |
| PUT | /usuarios/:id | Atualiza um usuário | 200 ou 404 |
| DELETE | /usuarios/:id | Remove um usuário | 204 ou 404 |

## Exemplo de cadastro

### POST /usuarios

Corpo da requisição:

```json
{
  "nome": "Felipe",
  "email": "felipe@email.com"
}
```

Exemplo de resposta:

```json
{
  "data": {
    "id": 1,
    "nome": "Felipe",
    "email": "felipe@email.com"
  }
}
```

Status HTTP:

```text
201 Created
```

## Validação de dados

Os campos `nome` e `email` são obrigatórios para o cadastro.

Caso algum deles não seja informado, a API retorna:

```json
{
  "error": "Os campos nome e email são obrigatórios"
}
```

com o status:

```text
400 Bad Request
```

## Tratamento de usuário inexistente

Ao realizar uma busca por um ID que não existe, a API retorna:

```json
{
  "erro": "Usuário não encontrado"
}
```

com o status:

```text
404 Not Found
```

## Testes

Os endpoints foram testados utilizando o Apidog, contemplando cenários de sucesso e de erro.

Foram validados os códigos HTTP 200, 201, 400 e 404.