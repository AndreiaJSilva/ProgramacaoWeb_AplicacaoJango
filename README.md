# ProgramacaoWeb_AplicacaoJango
Projeto da disciplina de Programação Web utilizando Jango Python no BackEnd, desenvolvimento de uma aplicação de uma fármácia

## 🚀 Tecnologias utilizadas

- Python 3.12
- Django 5.2.1

## 📦 Instalação

Siga os passos abaixo para rodar o projeto localmente.

### 1. Clone o repositório

git clone https://github.com/AndreiaJSilva/ProgramacaoWeb_AplicacaoJango.git
cd farmacia

### 2. Crie e ative o ambiente virtual
python -m venv venv
#### Ative o venv:
#### Windows:
venv\Scripts\activate
#### Linux/macOS:
source venv/bin/activate

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Execute as migrações
python manage.py migrate

### 5. Rode o servidor
python manage.py runserver

Acesse o projeto em: http://localhost:8000

## 🛠 Estrutura do Projeto
- manage.py — Comando de gerenciamento
- core/ — Aplicativo(s) Django
- templates/ — Templates HTML (se houver)
- static/ — Arquivos estáticos (CSS, JS, imagens)




