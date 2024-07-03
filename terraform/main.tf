provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "bucket" {
  name          = "${var.project_id}-storage-bucket"
  location      = var.region
  force_destroy = true
}

resource "google_firestore_index" "index" {
  # Example Firestore index configuration
}

resource "google_cloud_run_service" "service" {
  name     = "myassignment"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/myassignment"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

output "cloud_run_url" {
  value = google_cloud_run_service.service.status[0].url
}



