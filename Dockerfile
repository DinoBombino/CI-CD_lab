# Базовый образ Python 3.12 (slim — лёгкий)
FROM python:3.12-slim

# Рабочая папка в контейнере
WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Запускаем Gunicorn как продакшн-сервер
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]