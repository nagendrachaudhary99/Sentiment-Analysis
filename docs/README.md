# Documentation for Sentiment Analysis Project

This directory contains the MkDocs-based documentation for the Sentiment Analysis project.

## Setting Up and Serving MkDocs Documentation

To set up and serve the documentation:

```bash
# Navigate to the docs directory (if not already there)
cd docs

# Install MkDocs
pip install mkdocs

# Build the documentation site
mkdocs build

# Serve documentation locally
mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000/`.

## Documentation Structure

- `mkdocs.yml`: Configuration file for MkDocs
- `docs/`: Directory containing the markdown files
  - `index.md`: Home page
  - `setup.md`: Setup instructions
  - `usage.md`: Usage instructions

## Updating Documentation

1. Edit the markdown files in the `docs/` directory
2. Run `mkdocs serve` to preview changes
3. Run `mkdocs build` to build the final documentation site

## Project Setup Commands

### Python & Transformers

```bash
# Verified Transformers is installed and importable
python -c "from transformers import pipeline; print('Transformers is OK')"
```

### Virtual Environment

```bash
# Create a virtual environment
python -m venv venv310

# Activate the environment
source venv310/bin/activate
```

### FastAPI and other packages

```bash
# Install FastAPI
pip install fastapi

# Install cookiecutter
pip install cookiecutter

# Install cookiecutter data science template
pip install cookiecutter-data-science
```

### MkDocs setup

```bash
# Inside 'docs' directory
pip install mkdocs

# Build documentation site
mkdocs build

# Serve documentation locally
mkdocs serve
```

### Hugging Face Cache Fixes

```bash
# Remove default Hugging Face cache to prevent space errors
rm -rf ~/.cache/huggingface

# Set a new cache directory (temporary)
export TRANSFORMERS_CACHE=/Users/nagendrachaudhary/Desktop/sentiment/.hf_cache

# Create the new cache directory
mkdir -p /Users/nagendrachaudhary/Desktop/sentiment/.hf_cache
```

### Uvicorn FastAPI server

```bash
# Run your FastAPI app
uvicorn app:app --port 5000
``` 
////////
# 💬 Sentiment Analysis API with FastAPI & Transformers

This project provides a RESTful API for sentiment classification using Hugging Face's `SamLowe/roberta-base-go_emotions` model via FastAPI. It also includes MkDocs-based documentation for easy navigation and usage instructions.

---

## 🚀 Features

- 🔍 Classifies text into multiple emotion categories
- ⚡ Built using FastAPI for high performance
- 🤗 Uses Hugging Face Transformers pipeline
- 📝 Fully documented with MkDocs

---

## 📁 Project Structure
sentiment/
│
├── app/ # FastAPI app directory
│ └── init.py
│
├── docs/ # MkDocs documentation
│ ├── index.md
│ ├── setup.md
│ └── usage.md
│
├── mkdocs.yml # MkDocs config
├── README.md # This file
└── requirements.txt # Python dependencies

yaml:

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sentiment-api.git
cd sentiment-api

2. Create and Activate Virtual Environment
python -m venv venv310
source venv310/bin/activate

3.Install Required Packages

pip install -r requirements.txt

Or manually:

pip install fastapi uvicorn transformers

Run the Api
# Inside root directory
uvicorn app:app --port 5000

API will be available at: http://127.0.0.1:5000

Swagger UI docs: http://127.0.0.1:5000/docs

Run MkDocs Documentation
cd docs
pip install mkdocs
mkdocs serve
Docs will be served at: http://127.0.0.1:8000

Troubleshooting: Hugging Face Cache Errors
# Clear old cache
rm -rf ~/.cache/huggingface

# Create and point to a new one
mkdir -p /Users/nagendrachaudhary/Desktop/sentiment/.hf_cache
export TRANSFORMERS_CACHE=/Users/nagendrachaudhary/Desktop/sentiment/.hf_cach

Let me know if you want a `requirements.txt` generated too!