FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir
COPY web-app.py /app/
EXPOSE 5000
CMD ["python", "web-app.py"]
