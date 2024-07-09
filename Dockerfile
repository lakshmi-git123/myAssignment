FROM python:3.9-slim

ARG GCP_SA

RUN echo "${GCP_SA_KEY}" > myassignment-426912-04f2ed64ffc3.json

ENV GOOGLE_APPLICATION_CREDENTIALS="myassignment-426912-04f2ed64ffc3.json"

WORKDIR /assignment

COPY . /assignment

RUN pip install --no-cache-dir -r requirements.txt


ENV PORT=8000

EXPOSE 8000

CMD ["python", "assignment.py"]
