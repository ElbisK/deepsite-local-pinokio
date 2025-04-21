# DeepSite Local for Pinokio

This repository provides a fully local version of DeepSite using a local HuggingFace model and a Flask backend.

## 📦 Features

- No HuggingFace token needed
- Uses local model with transformers
- Runs completely offline
- Works with Pinokio via `pinokio.json`

## 🚀 Quickstart

1. Clone or use in Pinokio via:
   ```
   https://github.com/your-username/deepsite-local-pinokio
   ```

2. Make sure Node.js (>=18) and Python (>=3.8) are installed.

3. When Pinokio runs the script, it will:
   - Clone frontend
   - Install frontend dependencies
   - Set up backend with Flask and transformers
   - Start both frontend and backend

## 📡 Endpoints

- Frontend: http://localhost:3000
- Backend (API): http://localhost:5000/predict
