# tecweb-2026-2-projeto1B

Reimplementação da aplicação de anotações **Get-it** utilizando o framework Django.

## Link da aplicação (deploy)

> **TODO:** adicione aqui a URL pública da aplicação após o deploy (Tarefa 04).

### Como fazer o deploy no Render

O projeto já vem pronto para deploy no [Render](https://render.com) através do
arquivo `render.yaml` (cria o serviço web + banco PostgreSQL automaticamente):

1. Suba o repositório para o GitHub.
2. Crie uma conta gratuita no Render e acesse **New > Blueprint**.
3. Conecte este repositório — o Render lê o `render.yaml` e provisiona tudo.
4. Aguarde o build/deploy e copie a URL pública gerada para o campo acima.

## Funcionalidades

- **CRUD de anotações** (Tarefa 01): criar, listar, editar e excluir anotações.
- **Sistema de tags** (Tarefa 02): cada anotação pode ter no máximo uma tag
  (relação Many-to-One / `ForeignKey`). Páginas `/tags/` (lista de tags) e
  `/tags/<id>/` (anotações de uma tag). Tags não são duplicadas e anotações
  podem ser criadas sem tag.
- **PostgreSQL em container Docker** (Tarefa 03) no lugar do SQLite.

## Como rodar localmente

1. Ative o ambiente virtual e instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Suba o banco PostgreSQL no Docker (é necessário ter o Docker em execução):

   ```bash
   docker compose up -d
   ```

3. Aplique as migrações:

   ```bash
   python manage.py migrate
   ```

4. Rode o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

A aplicação ficará disponível em `http://localhost:8000/`.

## Configuração do banco

As credenciais do banco são lidas de variáveis de ambiente (com valores padrão
iguais aos do `docker-compose.yml`):

| Variável            | Padrão      |
| ------------------- | ----------- |
| `POSTGRES_DB`       | `getit`     |
| `POSTGRES_USER`     | `getit`     |
| `POSTGRES_PASSWORD` | `getit`     |
| `POSTGRES_HOST`     | `localhost` |
| `POSTGRES_PORT`     | `5432`      |
