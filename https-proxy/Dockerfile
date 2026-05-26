FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/ .

EXPOSE 443

CMD ["python", "https-proxy.py"]
