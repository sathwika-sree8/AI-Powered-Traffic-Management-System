# Use official Python image
FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
