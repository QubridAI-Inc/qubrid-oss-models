# Qwen3.7-Max

Frontier chat-completion model from Alibaba Cloud’s Qwen 3.7 line — optimized for high-quality instruction following, multilingual dialogue, and production agent workflows on the Qubrid platform.

## Overview

**Qwen3.7-Max** is a proprietary **chat-completion** model built on the Qwen 3.7 architecture. It is suited for customer support summarization, agent orchestration, RAG-backed assistants, and general-purpose conversational AI where strong reasoning and long context matter.

| | |
|---|---|
| **Model ID** | `Qwen/Qwen3.7-Max` |
| **Category** | Chat |
| **Model type** | `chat-completion` |
| **Context length** | 128K tokens |
| **Model size** | Undisclosed |

## Pricing

| | Rate |
|---|---|
| **Input** | $2.50 / 1M tokens |
| **Output** | $7.50 / 1M tokens |
| **Dedicated GPU deployment** | From $1.25 / GPU / hr |

## Model details

| Field | Value |
|:------|:------|
| **Provider** | Alibaba (Cloud) |
| **Hugging Face** | [Qwen/Qwen3.7-Max](https://huggingface.co/Qwen/Qwen3.7-Max) |
| **Architecture** | Proprietary Qwen 3.7 architecture |
| **Training data** | Large-scale multilingual pretraining corpus with instruction and alignment tuning (not publicly disclosed) |
| **Context length** | 128K tokens |
| **Model size** | Undisclosed |
| **Category** | Chat |
| **Model type** | chat-completion |

## Quick start

Set `QUBRID_API_KEY` and call the API via your preferred SDK:

| Language | Example |
|:---------|:--------|
| [Python](./Python/chat.py) | OpenAI Python SDK |
| [JavaScript](./JavaScript/chat.js) | OpenAI Node SDK |
| [Go](./Go/main.go) | Native HTTP client |
| [cURL](./cURL/request.sh) | Shell / REST |

**Base URL:** `https://platform.qubrid.com/v1`
