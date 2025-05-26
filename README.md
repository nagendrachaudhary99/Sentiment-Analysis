# Sentiment Analysis Project

A FastAPI-based web service for sentiment analysis using Hugging Face Transformers.

## Project Structure

- `app/`: Main application code
- `docs/`: Documentation (MkDocs)
- `.hf_cache/`: Custom Hugging Face cache directory

## Setup

See the [setup documentation](docs/docs/setup.md) for detailed setup instructions.

Quick setup:

```bash
# Create a virtual environment
python -m venv venv310

# Activate the environment
source venv310/bin/activate

# Install required packages
pip install -r requirement.txt
```

## Documentation

This project includes comprehensive MkDocs documentation.

To build and serve the documentation:

```bash
# Navigate to the docs directory
cd docs

# Install MkDocs if not already installed
pip install mkdocs

# Build the documentation site
mkdocs build

# Serve documentation locally
mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000/`.


## Running the API

To start the FastAPI server:

```bash
uvicorn app:app --port 5000
```

The API will be available at `http://localhost:5000`.

## Tools and Technologies

- Python
- FastAPI
- Hugging Face Transformers
- MkDocs 