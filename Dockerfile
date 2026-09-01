FROM python:3.12-slim

# Actualiza el sistema operativo para corregir las vulnerabilidades de OpenSSL
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

WORKDIR /home/myapp
COPY requirements.txt /home/myapp/
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["python", "sample_app.py"]
