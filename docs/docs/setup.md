# Setup Instructions

This page documents all the steps needed to set up the Sentiment Analysis project environment.

## Prerequisites

- Python 3.10 or higher
- pip package manager
- Git

## Environment Setup

### Virtual Environment

Create and activate a Python virtual environment:

```bash
# Create a virtual environment
python -m venv venv310

# Activate the environment
source venv310/bin/activate
```

### Required Packages

Install FastAPI and other required packages:

```bash
# Install FastAPI
pip install fastapi

# Install cookiecutter
pip install cookiecutter

# Install cookiecutter data science template
pip install cookiecutter-data-science
```

### Transformers Setup

Verify Transformers installation:

```bash
# Verify Transformers is installed and importable
python -c "from transformers import pipeline; print('Transformers is OK')"
```

### Hugging Face Cache Configuration

Fix Hugging Face cache issues:

```bash
# Remove default Hugging Face cache to prevent space errors
rm -rf ~/.cache/huggingface

# Set a new cache directory (temporary)
export TRANSFORMERS_CACHE=/Users/nagendrachaudhary/Desktop/sentiment/.hf_cache

# Create the new cache directory
mkdir -p /Users/nagendrachaudhary/Desktop/sentiment/.hf_cache
```

## VS Code Extensions

The following VS Code extensions are recommended:

- ms-python.python
- ms-python.vscode-pylance
- charliermarsh.ruff
- ms-python.pylint
- george-alisson.html-preview-vscode
- ms-toolsai.jupyter and its dependencies
- foxundermoon.shell-format
- aaron-bond.better-comments
- github.vscode-github-actions
- github.copilot
- github.copilot-chat
- github.vscode-pull-request-github

You can install these using the provided script:

```bash
# Make the script executable
chmod +x install-extensions.sh

# Run the script
./install-extensions.sh
``` 