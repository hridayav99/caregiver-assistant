#!/bin/bash
python3 mcp_server/medlineplus_server.py &
sleep 2
adk web --host=0.0.0.0 --port=8080 my_caregiver_assistant_app/