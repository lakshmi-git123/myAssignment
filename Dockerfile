FROM python:3.9-slim

WORKDIR /assignment

COPY . /assignment

RUN pip install --no-cache-dir -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="myassignment-426912-04f2ed64ffc3.json"

ENV PORT=4040

EXPOSE 4040

CMD ["python", "assignment.py"]
