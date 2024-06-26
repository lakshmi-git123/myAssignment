FROM python:3.9

WORKDIR /api-service

COPY . /api-service

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4040

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/service-account-file.json"

CMD ["python", "api-service.py"]
