# Multi AI Agent

## Overview
Multi AI Agent is a modular Python project that blends Backend + Frontend + LLM/GenAI. It provides a FastAPI backend, a Streamlit frontend, and a LangChain/LangGraph-based core that orchestrates one or more LLM agents (Groq models) with optional web search tools.

## Features
- Backend: FastAPI service exposing a /chat endpoint
- Frontend: Streamlit UI to compose a system prompt, pick a model, and chat
- LLM Core: LangChain + LangGraph agent with Groq LLMs (via langchain-groq)
- Tools: Optional Tavily web search integration
- Observability: File-based logging and typed request schema
- Clean configuration via environment variables

## Project Structure
```
app/
  backend/         # API and backend logic
  common/          # Shared utilities (logger, exceptions)
  config/          # Configuration and settings
  core/            # Core AI agent logic
  frontend/        # UI components
logs/              # Log files
requirements.txt   # Python dependencies
setup.py           # Package setup
```

## Getting Started
1) Install Python 3.11+ and clone this repo.

2) Create and activate a virtual environment (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Install dependencies:
```powershell
pip install -r requirements.txt
```

4) Set environment variables (PowerShell):
```powershell
$env:GROQ_API_KEY = "<your_groq_api_key>"
$env:TAVILY_API_KEY = "<optional_tavily_api_key>"
```

5) Run the app (starts backend and frontend):
```powershell
python -m app.main
```

Then open the Streamlit UI at http://localhost:8501 and the backend runs at http://127.0.0.1:9999.

## Configuration
- Edit `app/config/settings.py` to adjust application settings.
- Allowed models: `settings.ALLOWED_MODEL_NAME`.

## Logging
- Logs are stored in the `logs/` directory.

## Extending the Project
- Core/Agents: `app/core/ai_agent.py` (swap model, add tools, change state).
- Backend API: `app/backend/api.py` (add routes, auth, rate limits).
- Frontend UI: `app/frontend/ui.py` (history, multi-turn, model options).
- Settings: `app/config/settings.py` (keys, model allow-list, flags).

## Troubleshooting
- If imports fail for `app.backend`, ensure `app/backend/__init__.py` exists (it does).
- If Tavily search is enabled, set `$env:TAVILY_API_KEY`.
- If Streamlit fails to import in subprocess, ensure the venv is activated before running `python -m app.main`.
- If Groq requests fail, verify `$env:GROQ_API_KEY` is set and the model name is in `ALLOWED_MODEL_NAME`.

## License
MIT License

## Author
Rohan Agarwal