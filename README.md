# Sentiment Analysis Project

A FastAPI-based web service for sentiment analysis using Hugging Face Transformers.

## Project Repository

GitHub Repository: [https://github.com/nagendrachaudhary99/Sentiment-Analysis](https://github.com/nagendrachaudhary99/Sentiment-Analysis)

## What This Project Does

This project is a sentiment analysis API that uses Hugging Face's Transformers library to analyze the sentiment of text. The API:

- Processes text input through a pre-trained sentiment analysis model
- Returns emotional classification for the given text
- Provides a simple web interface via FastAPI for easy interaction
- Includes comprehensive documentation

## How to Run the Project

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/nagendrachaudhary99/Sentiment-Analysis.git
   cd Sentiment-Analysis
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv310
   source venv310/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Hugging Face cache (to prevent space errors):
   ```bash
   export TRANSFORMERS_CACHE=$(pwd)/.hf_cache
   mkdir -p .hf_cache
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn app:app --port 5000
   ```

6. Access the API at http://localhost:5000 or the documentation at http://localhost:5000/docs

### Using Documentation

To build and view the documentation:

```bash
cd docs
pip install mkdocs
mkdocs build
mkdocs serve
```

The documentation will be available at http://127.0.0.1:8000/

## Configuration and Setup Notes

- Python 3.10 or higher is required
- The app uses the SamLowe/roberta-base-go_emotions model from Hugging Face
- First-time model download may take a few minutes depending on your internet connection
- Custom Hugging Face cache location is used to prevent disk space issues

## Demo

[View the project demo here](https://drive.google.com/drive/folders/your-video-link) - Replace with your actual video link

The demo includes:
- App running and processing sentiment analysis requests
- Documentation navigation
- Test execution

## API Endpoints

- `/`: Welcome message
- `/classify`: POST endpoint that accepts text and returns sentiment analysis
- `/docs`: Swagger UI documentation
- `/redoc`: ReDoc documentation

## CI/CD

This project uses GitHub Actions for continuous integration. Workflows include:
- Linting with ruff
- Unit tests for the API endpoints
- Documentation build verification

You can view the passing CI tests in the [GitHub Actions tab](https://github.com/nagendrachaudhary99/Sentiment-Analysis/actions).

## Technologies Used

- FastAPI
- Hugging Face Transformers
- MkDocs for documentation
- Python virtual environments
- GitHub Actions 