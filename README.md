# Django To-do List

Projeto de lista de tarefas (To-do List) desenvolvido com Django e Bootstrap.

## Funcionalidades
- Adicionar tarefas
- Editar tarefas
- Deletar tarefas
- Marcar tarefas como concluídas
- Interface responsiva com Bootstrap

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```
2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```
3. **Instale as dependências:**
   ```bash
   pip install django
   ```
4. **Aplique as migrações:**
   ```bash
   python manage.py migrate
   ```
5. **Rode o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```
6. **Acesse no navegador:**
   - http://127.0.0.1:8000/

## Estrutura do Projeto
- `todoApp/` — Projeto Django principal
- `todo_list/` — Aplicação de tarefas
- `Templates/` — Templates HTML com Bootstrap

## Melhorias visuais
- Navbar e rodapé personalizados
- Tabela de tarefas estilizada
- Layout responsivo

## Autor
- Gabriel Victor
