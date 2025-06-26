FROM python:3.11

RUN apt-get update && apt-get install -y chromium-driver chromium

ENV DISPLAY=:99

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]