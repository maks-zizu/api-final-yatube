# Yatube API

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.1-0C4B33?logo=django)
![DRF](https://img.shields.io/badge/DRF-3.15-red)

## Описание

Yatube API — это программный интерфейс для социальной сети **Yatube**.
С помощью REST‑эндпоинтов front‑разработчики могут:

- читать ленту публикаций с пагинацией;
- создавать, редактировать и удалять свои посты;
- прикреплять изображения и указывать сообщество;
- оставлять комментарии и управлять ими;
- подписываться на авторов и просматривать список подписок;
- получать токены (**JWT**) для аутентификации.

Полное интерактивное описание расположено по адресу `/redoc/` после запуска сервера.

---

## Технологии

| Название              | Версия | Назначение               |
| --------------------- | ------ | ------------------------ |
| Python                | 3.12   | Язык разработки          |
| Django                | 5.1    | Веб‑фреймворк            |
| Django REST framework | 3.15   | Создание API             |
| djoser + Simple JWT   | latest | Аутентификация JWT       |
| SQLite 3 / PostgreSQL | —      | БД (по умолчанию SQLite) |

> ⚙️ Проект совместим с Black и flake8.

---

## Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/<your_username>/yatube_api.git
cd yatube_api
```

### 2. Создайте и активируйте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  
# Windows: venv\Scripts\activate
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Примените миграции и создайте суперпользователя

```bash
python yatube_api/manage.py migrate
python yatube_api/manage.py createsuperuser
```

### 5. Запустите сервер

```bash
python yatube_api/manage.py runserver
```

Теперь API доступно по адресу `http://127.0.0.1:8000/api/`, а документация — по `http://127.0.0.1:8000/redoc/`.

---

## Переменные окружения (опционально)

Если используете PostgreSQL, добавьте файл `.env` в корень и задайте:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<имя_бд>
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
DB_HOST=localhost
DB_PORT=5432
```

---

## Примеры запросов

Ниже приведены короткие примеры с использованием **curl**. Все ответы возвращаются в формате JSON.

### Получить токен

```bash
curl -X POST http://127.0.0.1:8000/api/v1/jwt/create/ \
     -H "Content-Type: application/json" \
     -d '{"username": "regular_user", "password": "iWannaBeAdmin"}'
```

**Ответ**

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

### Создать пост

```bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/ \
     -H "Authorization: Bearer <access_token>" \
     -H "Content-Type: application/json" \
     -d '{"text": "Мой первый пост!"}'
```

### Получить ленту с пагинацией

```bash
curl "http://127.0.0.1:8000/api/v1/posts/?limit=5&offset=10"
```

### Добавить комментарий

```bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/42/comments/ \
     -H "Authorization: Bearer <access_token>" \
     -d '{"text": "Отличный пост!"}'
```

### Подписаться на автора

```bash
curl -X POST http://127.0.0.1:8000/api/v1/follow/ \
     -H "Authorization: Bearer <access_token>" \
     -d '{"following": "john_doe"}'
```

---
