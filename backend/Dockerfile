
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY backend/requirements/ /app/requirements/

RUN pip install --no-cache-dir \
    -r /app/requirements/development.txt

COPY backend/ /app/

COPY ml/ /app/ml/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
