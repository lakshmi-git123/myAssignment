
# Flask Bigquery API

This repository contains a Flask application that interacts with Google Bigquery. The application is containerized using Docker and deploys using a CI/CD pipeline with GitHub Actions into Google Cloud Run.

## Project Structure

```
my-flask-Bigquery-api/
├── .github/
│   └── workflows/
│       └── cloudbuild.yaml
├── assignment.py
├── Dockerfile
├── requirements.txt
├── README.md



## Prerequisites

- Docker
- Google Cloud SDK
- GitHub repository with secrets configured:
  - `GCP_PROJECT_ID`: Your Google Cloud project ID.
  - `GCP_SA_KEY`: Your Google Cloud service account key in JSON format.
  - `GCP_REGION`: The region where you want to deploy your Cloud Run service (e.g., `us-central1`).
## Setup and Deployment

### Local Setup

1. Clone the repository:

   git clone https://github.com/lakshmi-git123/myAssignment.git
   cd myAssignment


2. Build and run the Docker container locally:

   docker build -t myassignment .
   docker run -p 4040:4040 -v $(pwd)/service-account-file.json:myassignment-426912-04f2ed64ffc3.json myassignment
   ```

3. Access the API at http://localhost:4040

### CI/CD Pipeline

 Push your code to the `main` branch of your GitHub repository. The GitHub Actions workflow will build, package, and deploys application to Google Cloud Run.



- `POST /add_person`: Add a person record.
- `GET /get_person/<record_id>`: Get a person record by ID.

- 



