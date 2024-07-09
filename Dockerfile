FROM python:3.9-slim


WORKDIR /assignment


COPY . /assignment

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4040

ENV PORT=4040
#ENV GOOGLE_APPLICATION_CREDENTIALS="/app/service-account-file.json"

ENV GOOGLE_APPLICATION_CREDENTIALS="${{ secrets.GCP_SA_KEY }}"

CMD ["python", "assignment.py"]
