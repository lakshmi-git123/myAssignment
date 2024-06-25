FROM python:3.9

WORKDIR /api-service

COPY . /api-service

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4040

CMD ["python", "api-service.py"]
