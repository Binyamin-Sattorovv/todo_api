# 🚀 Todo API

Простое Todo-приложение на FastAPI и PostgreSQL.

## 📌 Возможности

- Создание задачи
- Получение списка задач
- Отметка задачи как выполненной
- Удаление задачи
- REST API
- PostgreSQL база данных
- SQLAlchemy ORM
- Pydantic валидация
- CORS для подключения Frontend

---

## 🛠 Технологии

- Python 3
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

---

## 📂 Структура проекта

```text
app/
│
├── main.py        # API маршруты
├── models.py      # SQLAlchemy модели
├── schemas.py     # Pydantic схемы
├── crud.py        # CRUD операции
├── database.py    # Подключение к БД
│
└── frontend/
    └── index.html
```

---

## ⚙️ Установка

### 1. Клонировать проект

```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

---

## 🗄 Настройка PostgreSQL

Создать базу данных:

```sql
CREATE DATABASE todo_db;
```

Указать данные подключения в `database.py`:

```python
DATABASE_URL = "postgresql://postgres:password@localhost/todo_db"
```

---

## ▶ Запуск сервера

```bash
uvicorn main:app --reload
```

или

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Endpoints

### Получить все задачи

```http
GET /tasks
```

### Создать задачу

```http
POST /tasks
```

Body:

```json
{
  "title": "Read book"
}
```

### Обновить задачу

```http
PUT /tasks/{task_id}
```

Body:

```json
{
  "completed": true
}
```

### Удалить задачу

```http
DELETE /tasks/{task_id}
```

---

## 📸 Frontend

Frontend написан на:

- HTML
- CSS
- JavaScript

Возможности:

- Добавление задач
- Отображение списка задач
- Отметка выполнения
- Удаление выполненных задач

---

## 📚 Что я изучил

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- CRUD операции
- REST API
- Dependency Injection
- CORS
- Frontend ↔ Backend взаимодействие

---

## 👨‍💻 Бинямин

Создано в процессе изучения Backend-разработки на Python.
