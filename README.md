# MLOps Assignment: Containerized ML Experiment Tracker

## Overview

In this assignment, you will build and deploy a **containerized ML
Experiment Tracking Service** backed by **PostgreSQL running in
Docker**.

This activity focuses on core MLOps practices including:

-   Containerization with Docker
-   Service integration (API + Database)
-   Reproducibility
-   Automated testing
-   CI/CD with GitHub Actions
-   Publishing Docker images to Docker Hub

------------------------------------------------------------------------

## Objective

You will:

-   Build a Python REST API (Flask or FastAPI)
-   Store experiment metadata in PostgreSQL
-   Run PostgreSQL using the official Docker image
-   Containerize the Python application
-   Implement CI/CD using GitHub Actions
-   Push your Docker image to Docker Hub

------------------------------------------------------------------------

## Application: ML Experiment Tracker

### Experiment Schema

Each experiment must contain:

-   `id` (auto-generated primary key)
-   `model_name` (string)
-   `dataset_name` (string)
-   `accuracy` (float)
-   `loss` (float)
-   `timestamp` (auto-generated)

------------------------------------------------------------------------

# Part 1: API Requirements

You must implement the following endpoints:

## 1️⃣ Health Check

    GET /health

Returns a status message confirming the service is running.

------------------------------------------------------------------------

## 2️⃣ Create Experiment

    POST /experiments

Example JSON body:

``` json
{
  "model_name": "resnet50",
  "dataset_name": "cifar10",
  "accuracy": 0.91,
  "loss": 0.23
}
```

Stores the experiment in PostgreSQL.

------------------------------------------------------------------------

## 3️⃣ Get All Experiments

    GET /experiments

Returns all stored experiments.

------------------------------------------------------------------------

## 4️⃣ Filter by Model Name

    GET /experiments?model_name=resnet50

Returns experiments filtered by model name.

------------------------------------------------------------------------

# Part 2: PostgreSQL Setup Using Docker

You must use the official PostgreSQL Docker image.

### Run PostgreSQL:

``` bash
docker run --name ml-postgres -e POSTGRES_DB=mltracker -e POSTGRES_USER=mluser -e POSTGRES_PASSWORD=mlpassword -p 5432:5432 -d postgres:latest
```

------------------------------------------------------------------------

## Database Requirements

-   The `experiments` table must be created automatically when the app
    starts.
-   Database connection must use environment variables.
-   The application must NOT rely on a locally installed PostgreSQL.

### Required Environment Variables

-   `DB_HOST`
-   `DB_PORT`
-   `DB_NAME`
-   `DB_USER`
-   `DB_PASSWORD`

Example when running your app container:

``` bash
docker run -p 8000:8000 -e DB_HOST=host.docker.internal -e DB_PORT=5432 -e DB_NAME=mltracker -e DB_USER=mluser -e DB_PASSWORD=mlpassword <your_dockerhub_username>/ml-tracker:latest
```

------------------------------------------------------------------------

# Part 3: Dockerization of Application

## Dockerfile Requirements

Your Dockerfile must:

-   Use an official Python base image (e.g., `python:3.10-slim`)
-   Set a working directory
-   Copy `requirements.txt`
-   Install dependencies
-   Copy source code
-   Expose port 8000
-   Run the app using CMD

### Build Docker Image

``` bash
docker build -t <your_dockerhub_username>/ml-tracker:latest .
```

------------------------------------------------------------------------

# Part 4: Testing

## Requirements

You must write at least:

-   One test for experiment creation
-   One test for experiment retrieval

Use `pytest`.

Tests must pass:

-   Locally
-   In CI (GitHub Actions)

------------------------------------------------------------------------

# Part 5: GitHub Repository Structure

Your public repository must contain:

    app.py
    requirements.txt
    Dockerfile
    tests/
    .github/workflows/ci.yml
    README.md

README must include:

-   Project description
-   How to run PostgreSQL container
-   How to build Docker image
-   How to run Docker container with environment variables
-   Docker Hub image link

------------------------------------------------------------------------

# Part 6: CI/CD Pipeline

Your GitHub Actions workflow must:

1.  Trigger on push to `main`
2.  Set up Python
3.  Install dependencies
4.  Run pytest
5.  Build Docker image
6.  Log into Docker Hub using GitHub secrets
7.  Push image to Docker Hub

## Required Repository Secrets

-   `DOCKERHUB_USERNAME`
-   `DOCKERHUB_TOKEN`

------------------------------------------------------------------------

# Submission

Submit:

-   GitHub repository link
-   Docker Hub image link
-   Screenshot of successful GitHub Actions workflow

------------------------------------------------------------------------

# Evaluation Criteria

  Criteria                  Marks
  ------------------------- ---------
  API functionality         20
  PostgreSQL integration    20
  Dockerfile correctness    20
  Unit testing              15
  CI pipeline correctness   15
  Docker image published    10
  **Total**                 **100**

------------------------------------------------------------------------

# Bonus (Optional)

-   Use Docker network instead of `host.docker.internal`
-   Add database migrations
-   Add experiment deletion endpoint
-   Implement automatic version tagging in CI/CD

------------------------------------------------------------------------

This assignment simulates a minimal production-style ML service using
Docker and PostgreSQL.
