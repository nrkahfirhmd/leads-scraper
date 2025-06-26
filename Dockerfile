FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r dealflow_assistant/requirements.txt
CMD ["uvicorn", "dealflow_assistant.main:app", "--host", "0.0.0.0", "--port", "8000"]