FROM python:3.9
WORKDIR /app

COPY static/ /app/static/
COPY templates/ /app/templates/
COPY *.py /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]
