---
title: Deployment of a Gradio application with Docker to Hugging Face Spaces
emoji: "🤖"
colorFrom: "blue"
colorTo: "green"
sdk: "docker"
sdk_version: "1.0"
app_file: "Dockerfile"
pinned: "false"
---

## Dependency Management

This project uses `pip-tools` to manage Python dependencies. The workflow separates direct dependencies (specified in `requirements.in`) from the fully resolved dependency tree (stored in `requirements.txt`).

### Files:
- `requirements.in`: Contains the list of direct dependencies for the project.
- `requirements.txt`: Auto-generated file with pinned versions of all direct and transitive dependencies.

### How to Install Dependencies:
To install the dependencies, use the `requirements.txt` file:
```bash
pip install -r requirements.txt
