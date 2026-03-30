FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN ls -la

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]