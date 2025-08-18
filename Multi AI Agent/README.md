# Multi AI Agent

## Overview
Multi AI Agent is a modular Python project designed to orchestrate and manage multiple AI agents for various tasks. The architecture separates backend, core logic, frontend UI, configuration, and common utilities, making it easy to extend and maintain.

## Features
- Modular structure for backend, core, frontend, config, and common utilities
- Custom exception handling and logging
- Configurable settings
- Extensible AI agent core
- Simple UI frontend

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
1. **Clone the repository**
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```sh
   python -m app.main
   ```

## Configuration
- Edit `app/config/settings.py` to adjust application settings.

## Logging
- Logs are stored in the `logs/` directory.

## Extending the Project
- Add new AI agents in `app/core/ai_agent.py`.
- Add new API endpoints in `app/backend/api.py`.
- Add or modify UI components in `app/frontend/ui.py`.

## License
MIT License

## Author
Rohan Agarwal