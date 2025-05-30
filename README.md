��#   d i o - b a n k 
 
# DIO Bank

Sistema web de gerenciamento de usuários, papéis (roles) e postagens com autenticação JWT. Construído com **Flask**, **SQLAlchemy** e **SQLite**, este projeto simula as operações básicas de um sistema administrativo/bancário, com funcionalidades completas de autenticação, autorização e persistência de dados.

---

## 🧩 Funcionalidades

- 🔐 **Login com JWT**
- 👤 CRUD de **Usuários** com controle de acesso por função (`admin`)
- 🧑‍💼 CRUD de **Roles (papéis de usuário)**
- 📝 CRUD de **Postagens**
- 🔎 Validação de permissões com decorators
- ⚙️ Banco de dados via SQLAlchemy **ou** SQLite puro (`schema.sql`)
- 🧪 Blueprint modular para controle de usuários, autenticação e papéis

---

## 🛠 Tecnologias e Bibliotecas

- Python 3.11+
- Flask
- Flask-JWT-Extended
- Flask-Migrate
- Flask-SQLAlchemy
- SQLite (`sqlite3`)
- Click (comandos de terminal)
- SQLAlchemy ORM
- Decorators personalizados

---

## 📁 Estrutura de Diretórios

dio-bank/
├── app.py
├── models.py
├── schema.sql
├── requirements.txt
├── src/
│ ├── app.py
│ ├── utils.py
│ └── controllers/
│ ├── auth.py
│ ├── role.py
│ └── user.py
└── README.md




 
