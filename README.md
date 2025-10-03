# Ticketmaster Agent

This project demonstrates a simple implementation of the Claude Agent SDK to retrieve events in an area with the Ticketmaster API.

0. Define environment variables

```
TICKETMASTER_API_KEY = <your_api_key>
ANTHROPIC_API_KEY = <your_api_key>
```

1. Install required dependencies

```
npm i -g @anthropic-ai/claude-code
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install "fastapi[standard]"
```

2. Run FastAPI server

```
fastapi dev main.py
```
