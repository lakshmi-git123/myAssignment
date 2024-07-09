FROM python:3.9-slim

ARG GCP_SA_KEY
ENV GOOGLE_APPLICATION_CREDENTIALS="myassignment-426912-04f2ed64ffc3.json"

RUN echo "${GCP_SA_KEY}" > myassignment-426912-04f2ed64ffc3.json

WORKDIR /assignment

COPY . /assignment

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4040

ENV PORT=4040

CMD ["python", "assignment.py"]
