#!/bin/bash

# Sentiment Analysis Project Setup Script

echo "Setting up Sentiment Analysis Project..."

# Create and activate virtual environment
echo "Creating virtual environment..."
python -m venv venv310
source venv310/bin/activate

# Install required packages
echo "Installing required packages..."
pip install fastapi
pip install transformers
pip install uvicorn
pip install mkdocs

# Hugging Face Cache Setup
echo "Setting up Hugging Face cache..."
rm -rf ~/.cache/huggingface
export TRANSFORMERS_CACHE=$(pwd)/.hf_cache
mkdir -p .hf_cache

# Build documentation
echo "Building documentation..."
cd docs
mkdocs build
cd ..

echo "Setup complete!"
echo ""
echo "To start the API server:"
echo "  uvicorn app:app --port 5000"
echo ""
echo "To view documentation:"
echo "  cd docs && mkdocs serve"
echo ""
echo "The documentation will be available at http://127.0.0.1:8000/" 