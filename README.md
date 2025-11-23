# 🍳 Django Recipes Project

Projeto de estudos focado em aprender e documentar os fundamentos do Django de forma prática e progressiva.

## 📖 Sobre o Projeto

Este repositório foi criado com propósito educacional, onde cada commit representa um conceito específico do Django. A ideia é facilitar o aprendizado através de exemplos práticos e também servir como material de consulta futura.

## 🎯 Objetivo

- **Aprendizado progressivo**: Cada commit introduz um novo conceito
- **Documentação prática**: Commits descritivos explicam o que foi implementado
- **Consulta rápida**: Fácil navegação pelo histórico para revisar conceitos específicos
- **Boas práticas**: Aplicação de padrões e convenções do Django

## 🚀 Tecnologias

- **Python** 3.13.9
- **Django** 5.2.8
- **SQLite3** (banco de dados padrão)

## 💻 Como Executar

### Pré-requisitos

- Python 3.12+ instalado

### Instalação

```bash
# Clone o repositório
git clone https://github.com/EduFBasso/django-project1.git
cd django-project1

# Crie um ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Instale as dependências
pip install django

# Execute as migrações
python manage.py migrate

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/`

## 📚 Conceitos Abordados

### ✅ Fundamentos

- Configuração inicial do projeto Django
- Estrutura de um projeto Django
- Apps e organização de código

### ✅ URLs e Views

- Sistema de roteamento (URLs)
- Views baseadas em funções
- Passagem de parâmetros via URL

### ✅ Templates

- Sistema de templates do Django
- Renderização de templates
- Context data (passagem de dados para templates)
- Uso de variáveis no template: `{{ variavel }}`

### 🔄 Em desenvolvimento

- Models e ORM
- Forms e validação
- Arquivos estáticos (CSS, JS, imagens)
- Sistema de autenticação

## 📝 Navegando pelos Commits

Cada commit possui uma mensagem descritiva que explica:

- O que foi implementado
- Qual conceito está sendo demonstrado
- Exemplos práticos de uso

Use `git log` para navegar pela história do projeto e entender a evolução:

```bash
git log --oneline --decorate
```

## 🤝 Contribuições

Este é um projeto de estudos pessoal, mas sugestões e melhorias são sempre bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar como material de estudo.

---

## 🌐 English Version

# 🍳 Django Recipes Project

A learning-focused project designed to understand and document Django fundamentals through progressive, practical implementation.

## 📖 About

This repository was created for educational purposes, where each commit represents a specific Django concept. The goal is to facilitate learning through practical examples while serving as future reference material.

## 🎯 Goals

- **Progressive learning**: Each commit introduces a new concept
- **Practical documentation**: Descriptive commits explain what was implemented
- **Quick reference**: Easy navigation through history to review specific concepts
- **Best practices**: Application of Django patterns and conventions

## 🚀 Technologies

- **Python** 3.13.9
- **Django** 5.2.8
- **SQLite3** (default database)

## 💻 How to Run

### Prerequisites

- Python 3.12+ installed

### Installation

```bash
# Clone the repository
git clone https://github.com/EduFBasso/django-project1.git
cd django-project1

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Access: `http://127.0.0.1:8000/`

## 📚 Covered Concepts

### ✅ Fundamentals

- Initial Django project setup
- Django project structure
- Apps and code organization

### ✅ URLs and Views

- Routing system (URLs)
- Function-based views
- URL parameter passing

### ✅ Templates

- Django template system
- Template rendering
- Context data (passing data to templates)
- Using variables in templates: `{{ variable }}`

### 🔄 In development

- Models and ORM
- Forms and validation
- Static files (CSS, JS, images)
- Authentication system

## 📝 Navigating Through Commits

Each commit has a descriptive message explaining:

- What was implemented
- Which concept is being demonstrated
- Practical usage examples

Use `git log` to navigate through the project history and understand its evolution:

```bash
git log --oneline --decorate
```

## 🤝 Contributions

This is a personal learning project, but suggestions and improvements are always welcome! Feel free to open issues or pull requests.

## 📄 License

This project is under the MIT License. Feel free to use it as study material.

---

**Made with ❤️ for learning Django**
