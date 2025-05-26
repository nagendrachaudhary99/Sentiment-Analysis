# Usage Instructions

This page provides instructions on how to use the Sentiment Analysis project.

## Running the API Server

To start the FastAPI server:

```bash
# Run the FastAPI app
uvicorn app:app --port 5000
```

The API will be available at `http://localhost:5000`.

## Documentation Server

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

## API Endpoints

The following endpoints are available:

- `/sentiment`: Analyze sentiment of provided text
- `/docs`: Swagger UI for API documentation (provided by FastAPI)
- `/redoc`: ReDoc UI for API documentation (provided by FastAPI)

## Example Usage

```python
import requests

# Submit text for sentiment analysis
response = requests.post(
    "http://localhost:5000/sentiment",
    json={"text": "I love this product! It's amazing."}
)

# Print the sentiment analysis result
print(response.json())
``` 