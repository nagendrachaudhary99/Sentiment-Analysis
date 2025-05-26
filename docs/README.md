# Sentiment Analysis Project Documentation

This directory contains the MkDocs-based documentation for the Sentiment Analysis project.

## 📚 Documentation Structure

- `mkdocs.yml`: Configuration file for MkDocs
- `docs/`: Directory containing the markdown files
  - `index.md`: Home page
  - `setup.md`: Setup instructions
  - `usage.md`: Usage instructions

## 🚀 Setting Up and Serving Documentation

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

## ✏️ Updating Documentation

1. Edit the markdown files in the `docs/` directory
2. Run `mkdocs serve` to preview changes
3. Run `mkdocs build` to build the final documentation site

## 📋 Project Setup Commands Reference

### Python Environment

```bash
# Create a virtual environment
python -m venv venv310

# Activate the environment
source venv310/bin/activate

# Verify Transformers installation
python -c "from transformers import pipeline; print('Transformers is OK')"
```

### Package Installation

```bash
# Install required packages
pip install fastapi transformers uvicorn mkdocs

# Alternative: Install all requirements at once
pip install -r requirements.txt
```

### Hugging Face Cache Configuration

```bash
# Set a custom cache directory to prevent space errors
export TRANSFORMERS_CACHE=$(pwd)/.hf_cache
mkdir -p .hf_cache
```

### Running the Application

```bash
# Start the FastAPI server
uvicorn app:app --port 5000
```

## 🔗 Useful Links

- GitHub Repository: [https://github.com/nagendrachaudhary99/Sentiment-Analysis](https://github.com/nagendrachaudhary99/Sentiment-Analysis)
- FastAPI Documentation: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- MkDocs Documentation: [https://www.mkdocs.org/](https://www.mkdocs.org/)
- Hugging Face Transformers: [https://huggingface.co/docs/transformers/](https://huggingface.co/docs/transformers/)

## ⚠️ Troubleshooting Common Issues

### Hugging Face Cache Errors

When downloading models from Hugging Face, you might encounter disk space errors or permission issues:

```bash
# Error: No space left on device or permission errors when downloading models

# Solution 1: Clear the default cache
rm -rf ~/.cache/huggingface

# Solution 2: Set a custom cache location in your project directory
export TRANSFORMERS_CACHE=$(pwd)/.hf_cache
mkdir -p .hf_cache
```

### Large Files with Git

When pushing to GitHub, you might encounter issues with large files:

```bash
# Error: File exceeds GitHub's file size limit of 100MB

# Solution: Add large files to .gitignore before committing
echo "venv310/" >> .gitignore
echo "*.dylib" >> .gitignore
echo "*.so" >> .gitignore
echo "**/*.dylib" >> .gitignore
echo "**/*.so" >> .gitignore
echo "**/__pycache__/" >> .gitignore
echo ".hf_cache/" >> .gitignore

# If files are already tracked:
git rm -r --cached venv310
git rm -r --cached .hf_cache
```

### Model Loading Errors

If you encounter issues loading the model:

```bash
# Error: Model 'SamLowe/roberta-base-go_emotions' not found

# Solution: Check internet connection and try downloading explicitly
python -c "from transformers import AutoTokenizer, AutoModelForSequenceClassification; tokenizer = AutoTokenizer.from_pretrained('SamLowe/roberta-base-go_emotions'); model = AutoModelForSequenceClassification.from_pretrained('SamLowe/roberta-base-go_emotions')"
```

### MkDocs Building Errors

If MkDocs fails to build:

```bash
# Error: No such file or directory 'docs/docs'

# Solution: Ensure you're in the correct directory structure
# Your file structure should be:
# sentiment/
# ├── docs/
# │   ├── mkdocs.yml
# │   └── docs/
# │       ├── index.md
# │       ├── setup.md
# │       └── usage.md

# If you're getting this error, make sure you're running mkdocs commands from the directory containing mkdocs.yml
```

### Python Import Errors

```bash
# Error: No module named 'fastapi' or other import errors

# Solution: Check that you've activated your virtual environment and installed all requirements
source venv310/bin/activate
pip install -r requirements.txt

# Verify installation
pip list | grep fastapi
```

### Memory Errors When Loading Models

```bash
# Error: CUDA out of memory or general memory errors

# Solution: Use a smaller model or run on CPU only
# Add this to your code:
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Forces CPU-only mode
```

## 🔄 GitHub Workflow Tips

When setting up a CI/CD workflow on GitHub, ensure:

1. Your `.github/workflows/ci.yml` file is properly configured
2. Your tests don't require downloading large models during CI runs
3. Your `.gitignore` file properly excludes virtual environments and large files
4. You've set proper timeouts in case model downloads take too long

Example of force-pushing when needed:
```bash
git push -u origin main --force
```

Remember that force-pushing overwrites history, so use it carefully!