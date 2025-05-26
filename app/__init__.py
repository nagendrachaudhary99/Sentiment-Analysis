from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import os

# Set up custom cache directory for Hugging Face
os.environ["TRANSFORMERS_CACHE"] = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".hf_cache")

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="API for sentiment analysis using Hugging Face Transformers",
    version="1.0.0",
)

# Define request models
class SentimentRequest(BaseModel):
    text: str

# Initialize the sentiment analysis pipeline
try:
    sentiment_pipeline = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")
except Exception as e:
    print(f"Error loading model: {e}")
    sentiment_pipeline = None

@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to the Sentiment Analysis API"}

@app.post("/sentiment")
async def analyze_sentiment(request: SentimentRequest):
    """
    Analyze the sentiment of the provided text.
    
    Returns the emotion classification for the text.
    """
    if sentiment_pipeline is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Please try again later.")
    
    try:
        result = sentiment_pipeline(request.text)
        return {
            "text": request.text,
            "sentiment": result[0]["label"],
            "score": result[0]["score"],
            "all_scores": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "healthy", "model_loaded": sentiment_pipeline is not None}

# If this file is run directly, start the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
