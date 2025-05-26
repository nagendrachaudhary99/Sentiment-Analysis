#!/bin/bash

# Script to set up and serve MkDocs documentation

# Create necessary directories if they don't exist
mkdir -p docs

# Install MkDocs if not already installed
pip install mkdocs

# Build the documentation
echo "Building documentation..."
mkdocs build

# Serve the documentation
echo "Starting documentation server at http://127.0.0.1:8000/"
echo "Press Ctrl+C to stop the server"
mkdocs serve 