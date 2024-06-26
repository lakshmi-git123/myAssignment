
# Flask Firestore API

This repository contains a Flask application that interacts with Google Firestore. The application is containerized using Docker and deployed using a CI/CD pipeline with GitHub Actions and Terraform for GCP infrastructure.

## Project Structure

```
my-flask-firestore-api/
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── api-service.py
├── Dockerfile
├── requirements.txt
├── README.md
└── terraform/

## Prerequisites

- Docker
- Google Cloud SDK
- Terraform
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

   docker build -t DI-PY-api .
   docker run -p 5000:5000 -v $(pwd)/service-account-file.json:/app/service-account-file.json DI-PY-api
   ```

3. Access the API at http://localhost:4040

### CI/CD Pipeline

1. Push your code to the `main` branch of your GitHub repository. The GitHub Actions workflow will build, package, and deploy your application to Google Cloud Run.

2. The Terraform configuration will set up the required infrastructure on GCP.

### Terraform(WIP)

1. Initialize Terraform:

   cd terraform
   terraform init

2. Apply the Terraform configuration:

   terraform apply -var="project_id=YOUR_GCP_PROJECT_ID" -var="region=YOUR_GCP_REGION"

## Endpoints

- `POST /add_person`: Add a person record.
- `GET /get_person/<record_id>`: Get a person record by ID.


