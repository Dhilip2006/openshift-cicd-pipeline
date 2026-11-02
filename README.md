# OpenShift CI/CD Pipeline

## Project Overview

This project demonstrates the implementation of a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions, OpenShift and Tekton.

The pipeline automates code validation, linting, unit testing, application building and deployment.

## Objectives

- Automate code integration using GitHub Actions.
- Perform code quality checks using flake8.
- Execute unit tests using nose.
- Automate pipeline tasks using Tekton.
- Deploy the application on OpenShift.
- Verify successful application deployment.

## Technologies Used

| Technology | Purpose |
|---|---|
| GitHub | Source code management |
| GitHub Actions | Continuous Integration |
| OpenShift | Application deployment |
| Tekton | CI/CD pipeline automation |
| Python | Application development |
| flake8 | Code linting |
| nose | Unit testing |
| Buildah | Container image building |

## CI/CD Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions checks out the source code.
3. Linting checks the code quality.
4. Unit tests validate the application.
5. OpenShift Pipelines execute Tekton tasks.
6. Buildah builds the application container image.
7. The application is deployed on OpenShift.
8. Application logs are checked to verify deployment.

## Pipeline Tasks

- Cleanup
- Git Clone
- Lint
- Unit Tests
- Buildah
- Deploy

## Expected Outcome

A successfully executed CI/CD pipeline that automates code validation, testing, container image building and application deployment using OpenShift and Tekton.