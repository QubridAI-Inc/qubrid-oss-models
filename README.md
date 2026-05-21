<div align="center">

# Qubrid Models Registry

**A unified, provider-organized registry of frontier AI models - built for gateways, agents, and inference infrastructure.**

[![GitHub stars](https://img.shields.io/github/stars/QubridAI-Inc/qubrid-oss-models?style=for-the-badge&logo=github&color=1a1a2e)](https://github.com/Qubrid-AI/qubrid-oss-models/stargazers)
[![Models](https://img.shields.io/badge/models-62-blue?style=for-the-badge)](providers/)
[![Providers](https://img.shields.io/badge/providers-13-purple?style=for-the-badge)](providers/)
[![License](https://img.shields.io/github/license/QubridAI-Inc/qubrid-oss-models?style=for-the-badge&color=22c55e)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](#contributing)

*One registry. Every major provider. Zero guesswork.*

[Explore Models](#repository-structure) · [Categories](#model-categories) · [Contributing](#contributing) · [Roadmap](#roadmap)

</div>

---

## Table of Contents

- [Why This Exists](#why-this-exists)
- [Features](#features)
- [Quick Stats](#quick-stats)
- [Supported Providers](#supported-providers)
- [Model Categories](#model-categories)
- [Featured Models](#featured-models)
- [Repository Structure](#repository-structure)
- [Example Folder Structure](#example-folder-structure)
- [Use Cases](#use-cases)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [Built By Qubrid](#built-by-qubrid)

---

## Why This Exists

The AI model landscape is fragmented. Model IDs, capabilities, and release cadences differ across OpenAI, Anthropic, Google, Qwen, DeepSeek, and dozens of other labs - each with its own naming scheme, documentation, and API surface.

**Qubrid Models Registry** solves that fragmentation with a single, predictable layout:

| Problem | How this registry helps |
|--------|-------------------------|
| Scattered provider docs | One tree: `providers/{Provider}/{Family}/{model}` |
| Inconsistent discovery | Browse by vendor, product line, or capability category |
| Hard-to-scale integrations | Stable paths for gateways, SDKs, and automation |
| No shared mental model | Same hierarchy for every provider |

Whether you are routing traffic in production, benchmarking frontier models, or scaffolding an agent framework - start here.

---

## Features

| | |
|---|---|
| **Provider-first layout** | Every model lives under its vendor - no flat, unmaintainable lists |
| **Standardized depth** | `Provider → Family → Model` - three levels, every time |
| **Multi-provider coverage** | 13 labs, 62 frontier models, one repository |
| **Discoverability** | Logical folders map to how teams actually talk about models |
| **Scalable architecture** | Add providers, families, or models without restructuring the tree |
| **Infrastructure-ready** | Designed for sync jobs, metadata layers, and API gateways |

---

## Quick Stats

| Metric | Count |
|:-------|------:|
| **Total models** | 62 |
| **Providers** | 13 |
| **General LLMs** | 35 |
| **Coding models** | 5 |
| **Vision-language models** | 5 |
| **Thinking / reasoning models** | 4 |
| **OCR models** | 1 |
| **Open-weight models** | 10 |

---

## Supported Providers

| Provider | Families | Models | Focus |
|:---------|:---------|-------:|:------|
| [**OpenAI**](providers/OpenAI/) | GPT-5, GPT-4, GPT-OSS | 7 | Frontier + OSS |
| [**Anthropic**](providers/Anthropic/) | Opus, Sonnet, Haiku | 6 | Claude 4.x lineup |
| [**Google**](providers/Google/) | Gemini | 4 | Pro & Flash tiers |
| [**Qwen**](providers/Qwen/) | General, Coder, VL, Thinking, Open-Weight | 23 | Broadest coverage |
| [**DeepSeek**](providers/DeepSeek/) | V3, V4, Reasoning | 6 | Efficiency + reasoning |
| [**Moonshot AI**](providers/MoonshotAI/) | Kimi | 4 | Long-context agents |
| [**NVIDIA**](providers/NVIDIA/) | Nemotron | 3 | Enterprise Nemotron |
| [**Mistral AI**](providers/MistralAI/) | Mistral | 1 | Open-weight instruct |
| [**Meta**](providers/Meta/) | Llama | 1 | Llama 3.3 |
| [**Tencent**](providers/Tencent/) | Hunyuan | 1 | OCR |
| [**MiniMax AI**](providers/MiniMaxAI/) | MiniMax | 1 | M2.5 |
| [**Microsoft**](providers/Microsoft/) | Fara | 1 | Agentic 7B |
| [**ZAI**](providers/ZAI/) | GLM | 2 | GLM-4.7 & GLM-5 |

---

## Model Categories

Models are grouped by **capability**, not just vendor. Use these categories when routing, benchmarking, or tagging workloads.

<details>
<summary><strong>General LLMs</strong> - chat, completion, and broad instruction-following</summary>

<br>

Default frontier models for production assistants, RAG pipelines, and general-purpose agents.

**Examples:** `gpt-5.4`, `claude-opus-4-7`, `gemini-2.5-pro`, `Qwen3-Max`, `DeepSeek-V3.2`, `Kimi-K2.6`

**Typical paths:** `providers/OpenAI/GPT-5/`, `providers/Anthropic/Opus/`, `providers/Qwen/General/`

</details>

<details>
<summary><strong>Coding Models</strong> - software engineering, patches, and repo-scale context</summary>

<br>

Optimized for code generation, refactoring, and IDE/agent integrations.

**Examples:** `Qwen3-Coder-Plus`, `Qwen3-Coder-Next`, `Qwen3-Coder-480B-A35B-Instruct`

**Path:** `providers/Qwen/Coder/`

</details>

<details>
<summary><strong>Vision-Language Models</strong> - image + text understanding and multimodal agents</summary>

<br>

Unified perception and language for document AI, UI agents, and visual QA.

**Examples:** `Qwen3-VL-Plus`, `Qwen3-VL-235B-A22B-Instruct`, `gemini-3.1-pro-preview`

**Path:** `providers/Qwen/Vision-Language/`

</details>

<details>
<summary><strong>Thinking / Reasoning Models</strong> - extended deliberation and chain-of-thought</summary>

<br>

Higher-latency, higher-depth inference for math, planning, and complex tool use.

**Examples:** `DeepSeek-R1-0528`, `Kimi-K2-Thinking`, `Qwen3-Next-80B-A3B-Thinking`

**Paths:** `providers/DeepSeek/Reasoning/`, `providers/Qwen/Thinking/`, `providers/MoonshotAI/Kimi/`

</details>

<details>
<summary><strong>OCR Models</strong> - document text extraction and layout understanding</summary>

<br>

Specialized vision pipelines for scanned documents and structured capture.

**Example:** `HunyuanOCR` → `providers/Tencent/Hunyuan/HunyuanOCR/`

</details>

<details>
<summary><strong>Open-Weight Models</strong> - self-hosted and on-prem inference</summary>

<br>

Run on your GPUs, your VPC, or your sovereign cloud - no proprietary lock-in.

**Examples:** `Qwen3.5-397B-A17B`, `gpt-oss-120b`, `Llama-3.3-70B-Instruct`, `Mistral-7B-Instruct-v0.3`

**Paths:** `providers/Qwen/Open-Weight/`, `providers/OpenAI/GPT-OSS/`, `providers/Meta/Llama/`

</details>

---

## Featured Models

| Model | Provider | Path | Best for |
|:------|:---------|:-----|:---------|
| **GPT-5.4** | OpenAI | [`providers/OpenAI/GPT-5/gpt-5.4`](providers/OpenAI/GPT-5/gpt-5.4/) | Flagship production workloads |
| **Claude Opus 4.7** | Anthropic | [`providers/Anthropic/Opus/claude-opus-4-7`](providers/Anthropic/Opus/claude-opus-4-7/) | Maximum capability Claude |
| **Gemini 2.5 Pro** | Google | [`providers/Google/Gemini/gemini-2.5-pro`](providers/Google/Gemini/gemini-2.5-pro/) | Multimodal Google stack |
| **Qwen3-Max** | Qwen | [`providers/Qwen/General/Qwen3-Max`](providers/Qwen/General/Qwen3-Max/) | Top-tier general Qwen |
| **DeepSeek-V4-Pro** | DeepSeek | [`providers/DeepSeek/V4/DeepSeek-V4-Pro`](providers/DeepSeek/V4/DeepSeek-V4-Pro/) | Next-gen efficiency |
| **Kimi-K2.6** | Moonshot AI | [`providers/MoonshotAI/Kimi/Kimi-K2.6`](providers/MoonshotAI/Kimi/Kimi-K2.6/) | Long-context agents |

---

## Repository Structure

Every model is a **leaf directory** under a consistent three-level hierarchy:

```
providers/
└── {Provider}/
    └── {Family}/
        └── {model-id}/
```

<details>
<summary><strong>Full registry tree</strong> (click to expand)</summary>

```
providers/
├── Anthropic/
│   ├── Opus/          → claude-opus-4-7, claude-opus-4-6, claude-opus-4-5
│   ├── Sonnet/        → claude-sonnet-4-6, claude-sonnet-4-5
│   └── Haiku/         → claude-haiku-4-5-20251001
├── DeepSeek/
│   ├── Reasoning/     → deepseek-r1-distill-llama-70b, DeepSeek-R1-0528
│   ├── V3/            → DeepSeek-V3, DeepSeek-V3.2
│   └── V4/            → DeepSeek-V4-Flash, DeepSeek-V4-Pro
├── Google/
│   └── Gemini/        → gemini-3.1-pro-preview, gemini-3-flash-preview, …
├── Meta/
│   └── Llama/         → Llama-3.3-70B-Instruct
├── Microsoft/
│   └── Fara/          → Fara-7B
├── MiniMaxAI/
│   └── MiniMax/       → MiniMax-M2.5
├── MistralAI/
│   └── Mistral/       → Mistral-7B-Instruct-v0.3
├── MoonshotAI/
│   └── Kimi/          → Kimi-K2.6, Kimi-K2-Thinking, …
├── NVIDIA/
│   └── Nemotron/      → NVIDIA-Nemotron-3-Super-120B-A12B, …
├── OpenAI/
│   ├── GPT-OSS/       → gpt-oss-120b
│   ├── GPT-4/         → gpt-4o, gpt-4o-mini, gpt-4.1
│   └── GPT-5/         → gpt-5.4, gpt-5.4-mini, gpt-5.4-nano
├── Qwen/
│   ├── Coder/
│   ├── General/
│   ├── Vision-Language/
│   ├── Thinking/
│   └── Open-Weight/
├── Tencent/
│   └── Hunyuan/       → HunyuanOCR
└── ZAI/
    └── GLM/           → GLM-4.7, GLM-5
```

</details>

---

## Example Folder Structure

**Add a new model** - create a leaf folder under the correct provider and family:

```
providers/OpenAI/GPT-5/gpt-5.4/
providers/Anthropic/Opus/claude-opus-4-7/
providers/Qwen/Coder/Qwen3-Coder-Plus/
providers/DeepSeek/V4/DeepSeek-V4-Pro/
```

**Navigate programmatically:**

```text
provider  = "Qwen"
family    = "Vision-Language"
model_id  = "Qwen3-VL-Plus"
path      = f"providers/{provider}/{family}/{model_id}"
```

**Gateway routing pseudo-config:**

```yaml
routes:
  - id: frontier-general
    path: providers/OpenAI/GPT-5/gpt-5.4
  - id: frontier-reasoning
    path: providers/DeepSeek/Reasoning/DeepSeek-R1-0528
  - id: coding
    path: providers/Qwen/Coder/Qwen3-Coder-Plus
```

---

## Use Cases

| Use case | How teams use this registry |
|:---------|:----------------------------|
| **AI gateways** | Map stable paths → upstream provider endpoints |
| **Routing systems** | Policy-based model selection by category and SLA |
| **Benchmarking** | Fixed catalog for eval harnesses and leaderboards |
| **Agent frameworks** | Discover reasoning vs. general models per task |
| **Inference platforms** | Seed deployment manifests and model cards |
| **SDK generation** | Auto-generate typed enums from folder structure |
| **Playgrounds** | Populate model pickers with verified IDs |

---

## Contributing

We welcome contributions - new providers, families, model folders, and documentation improvements.

1. **Fork** the repository
2. **Create a branch** - `add/provider-model-name`
3. **Add the model** under `providers/{Provider}/{Family}/{model-id}/`
4. **Open a pull request** with provider, model ID, and category

### Adding a provider

```
providers/NewProvider/
└── ProductLine/
    └── model-id/
```

Keep names aligned with official provider documentation. Prefer lowercase kebab-case for API-style IDs (e.g. `claude-opus-4-7`) and preserve vendor casing for branded releases (e.g. `DeepSeek-V4-Pro`) where already established in this registry.

<details>
<summary><strong>Contribution checklist</strong></summary>

- [ ] Model folder is a leaf (no nested model dirs)
- [ ] Path follows `providers/Provider/Family/model`
- [ ] README stats updated if model count changes
- [ ] Category documented in PR description

</details>

---

## Roadmap

| Phase | Planned capability |
|:------|:-------------------|
| **Metadata** | `model.yaml` per leaf - version, modality, release date |
| **Pricing** | Reference token pricing and batch discounts |
| **Benchmarks** | Linked eval scores (MMLU, HumanEval, etc.) |
| **Context windows** | Max input/output tokens per model |
| **API compatibility** | OpenAI-compatible, Anthropic, Gemini flags |
| **Multimodal tags** | Text, image, audio, video capability matrix |
| **Automated syncing** | CI pipeline to validate against provider APIs |

---

## Built By Qubrid

**[Qubrid](https://qubrid.com)** builds AI infrastructure for teams shipping production inference - unified access to frontier and open-weight models, with the operational depth startups and enterprises expect.

This registry is the **canonical model catalog** behind Qubrid's gateway, routing, and deployment stack. Open-sourced so the community can discover, integrate, and extend the same foundation.

---

<div align="center">

### If this registry saves you time, star the repo - it helps others find it.

[![Star on GitHub](https://img.shields.io/github/stars/Qubrid-AI/qubrid-oss-models?style=social)](https://github.com/Qubrid-AI/qubrid-oss-models/stargazers)

**62 models · 13 providers · 1 tree**

*Maintained by [Qubrid AI](https://qubrid.com) · [MIT License](LICENSE)*

</div>
