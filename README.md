# 🚀 DevOps Zero to Production

> A hands-on DevOps portfolio project focused on building a production-like CI/CD workflow from scratch using Azure DevOps and modern DevOps practices.

This repository documents my journey of learning DevOps by building a real-world project instead of following isolated tutorials. Every feature is introduced incrementally, following the same approach used in professional software teams.

The goal is not only to learn the tools, but also to understand how they work together in a complete DevOps ecosystem.

---

# 🎯 Objectives

* Learn DevOps through practical, production-like scenarios.
* Build a complete CI/CD pipeline using Azure DevOps.
* Understand Docker and Kubernetes workflows.
* Learn security best practices with SonarCloud and Snyk.
* Implement monitoring using Prometheus, Grafana and Loki.
* Practice troubleshooting and incident response.
* Build a public portfolio demonstrating practical DevOps skills.

---

# 🛠 Tech Stack

## Cloud & CI/CD

* Azure DevOps
* YAML Pipelines
* Git
* GitHub

## Scripting

* Bash
* Python

## Application

* FastAPI
* Uvicorn

## Code Quality

* Ruff
* Pytest

## Containers

* Docker
* Kubernetes *(coming soon)*

## Security

* SonarCloud
* Snyk

## Monitoring

* Prometheus *(coming soon)*
* Grafana *(coming soon)*
* Loki *(coming soon)*

## Messaging

* Kafka *(coming soon)*

---

# 📂 Repository Structure

```text
.
├── .azuredevops/         # Azure DevOps YAML pipelines
├── app/                  # FastAPI demo application
├── azure-pipelines/      # Pipeline examples and templates
├── docker/               # Docker resources
├── docs/                 # Documentation
├── labs/                 # Linux, Bash and DevOps labs
├── monitoring/           # Monitoring configuration
├── scripts/              # Reusable Bash scripts
├── terraform/            # Infrastructure as Code (future)
├── tests/                # Automated API tests
├── .gitignore
├── LICENSE
└── README.md
```

---

# 📚 Learning Roadmap

## Foundation

* [x] Linux fundamentals
* [x] Bash scripting
* [x] Git & GitHub
* [x] Azure DevOps setup
* [x] First Azure Pipeline
* [x] Project validation script

## CI/CD

* [x] Docker image build
* [ ] Multi-stage pipelines
* [ ] Pipeline variables
* [ ] Pipeline conditions
* [ ] Build artifacts
* [ ] Release workflows

## Code Quality

* [x] Ruff
* [x] Automated API tests with Pytest
* [ ] Test coverage

## Security

* [x] SonarCloud
* [x] Snyk
* [ ] Security gates

## Containers

* [x] Docker image build
* [ ] Docker image publishing
* [ ] Container best practices

## Kubernetes

* [ ] Deployments
* [ ] Services
* [ ] ConfigMaps
* [ ] Secrets
* [ ] Liveness Probes
* [ ] Readiness Probes

## Monitoring

* [ ] Prometheus
* [ ] Grafana
* [ ] Loki
* [ ] Alerting

## Production Scenarios

* [ ] Troubleshooting labs
* [ ] Incident response
* [ ] Performance analysis
* [ ] Interview simulations

---

# 🚦 Current CI Pipeline

Current pipeline currently performs:

* Repository checkout
* Project validation
* Python dependency installation
* Ruff linting
* Automated API tests with Pytest
* SonarCloud static code analysis
* Snyk dependency vulnerability scanning
* Docker image build

Additional stages will be introduced incrementally throughout the project.

---

# 📖 What You'll Find Here

This repository is intentionally built commit by commit.

Each commit introduces a new concept and reflects how a real DevOps project evolves over time instead of presenting a finished solution.

Topics covered include:

* Linux
* Bash
* Azure DevOps
* YAML Pipelines
* Docker
* Kubernetes
* CI/CD
* Monitoring
* Security
* Troubleshooting
* Production best practices

---

# 💡 Why This Repository?

Most DevOps tutorials focus on individual tools.

This project focuses on how those tools work together in a production-like workflow.

The objective is to gain practical experience that closely resembles day-to-day work in a DevOps team.

---

# 📝 Commit Convention

This repository follows the Conventional Commits specification.

Examples:

```text
feat(docker): add Dockerfile
feat(k8s): deploy demo application

ci(azure): add initial pipeline
ci(validation): add project validation script

test: add API endpoint tests

fix(pipeline): handle missing README
fix(docker): reduce image size

docs: update project roadmap

refactor(scripts): improve validation script

chore: update dependencies
```

---

# 🚀 Next Milestones

* Refactor the CI pipeline into multiple stages
* Publish Docker images
* Add SonarCloud Quality Gates
* Implement build artifacts
* Deploy to Kubernetes
* Configure monitoring
* Implement alerting
* Solve production-like incidents

---

# 📄 License

This project is licensed under the MIT License.