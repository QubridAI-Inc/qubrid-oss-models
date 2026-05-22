#!/usr/bin/env sh
curl -X POST "https://platform.qubrid.com/v1/chat/completions" \
  -H "Authorization: Bearer QUBRID_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "Qwen/Qwen3.7-Max",
  "messages": [
    {
      "role": "user",
      "content": "Summarize this support ticket into bullet-point next steps for the agent."
    }
  ],
  "temperature": 0.7,
  "max_tokens": 500
}'
