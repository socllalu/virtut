# MVP Progress Documentation

## Project Overview
This project aims to build a SaaS platform that provides a virtual tutor and study resource generator for students, particularly those with ADHD. The solution is being developed using:

- **Backend:** FastAPI with Azure OpenAI integration.
- **Frontend:** Streamlit for a simple and effective UI.
- **Deployment Service:** Azure AI for model management.

---

## Completed Steps
### ✅ Environment Setup
- Created a virtual environment using `venv`.
- Installed required dependencies: `fastapi`, `uvicorn`, `openai`, and `python-dotenv`.
- Successfully configured Azure CLI and logged in using `az login`.

### ✅ Azure OpenAI Configuration
- Deployed a **`gpt-35-turbo`** model in Azure OpenAI with **Standard** deployment type.
- Configured `.env` file with:
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_DEPLOYMENT`

### ✅ Backend Development
- Created a FastAPI app with the following endpoints:
  - **`/`** — Health check endpoint.
  - **`/ask`** — Accepts questions and retrieves answers from Azure OpenAI.
- Updated the backend code to align with the latest `openai` library version (>= 1.0.0).
- Successfully tested the `/ask` endpoint with sample questions via Swagger UI and `curl`.

### ✅ Frontend Development
- Implemented a basic Streamlit app that:
  - Accepts user questions via a text area.
  - Connects to the FastAPI backend for AI-generated responses.
  - Displays responses or relevant error messages.

---

## Issues Resolved
✅ Corrected issues with Azure OpenAI's updated syntax in the new `openai` library version.
✅ Resolved `Connection refused` error by ensuring backend and frontend were running concurrently and correctly pointing to the API endpoint.

---

## Next Steps
🔹 Improve frontend UI for better usability and visual appeal.
🔹 Add additional features like personalized content, study resources (e.g., mind maps, flashcards, etc.).
🔹 Implement error handling improvements for a smoother user experience.
🔹 Explore deployment strategies for both the frontend and backend to a live environment.

---

## Useful Commands
**Activate virtual environment:**
```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**Run Backend:**
```bash
uvicorn main:app --reload
```

**Run Frontend:**
```bash
streamlit run frontend/main.py
```

**Test API with `curl`:**
```bash
curl -X 'POST' \
  'http://localhost:8000/ask' \
  -H 'Content-Type: application/json' \
  -d '{"question": "¿Cómo explico el ciclo del agua a un niño de 10 años con TDAH?"}'
```

---

## Notes
If you encounter issues, verify:
- The backend is running on port **8000**.
- The frontend is running on port **8501**.
- The `.env` file is correctly configured with the Azure OpenAI credentials.

---

