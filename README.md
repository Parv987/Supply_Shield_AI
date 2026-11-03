# SupplyShield AI

Autonomous Supply Chain Risk & Recovery Platform: evidence-grounded risk detection, impact analysis and recovery planning using RAG and agentic AI (LangGraph).

> Decision support only. No real purchasing, supplier or logistics action is ever executed. Use synthetic or public data only.

## First scenario
Supplier shipment delay that may cause an inventory shortage (details to be confirmed by the team; see `data/sample_scenarios.json`).

## Workflow
Scenario intake -> Risk assessment -> Evidence retrieval -> Impact analysis -> Recovery planning -> Validation -> Report -> Human review

## Structure and owners
| Folder | Owner |
|---|---|
| `app/` (Streamlit UI) | Arnav |
| `orchestration/` (LangGraph) | Shikhar |
| `risk/` | Aditya |
| `retrieval/` | Manish |
| `recovery/` | Arnav |
| `validation/` + `tests/test_evaluation.py` | Parv |
| `schemas/` | Shared (agree together) |

## Setup
```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux:        source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in placeholders locally; never commit .env
```

## Run tests
```bash
python -m pytest
```

## Working agreements
- Short-lived branches (`feature/risk-engine`), small PRs, no direct pushes to `main`.
- Do not change shared schemas or another owner's module without discussing first.
- Never invent supplier data, prices, lead times or citations; return clear errors, not fabricated success.

## Decisions log
Record scope/schema decisions in `docs/decisions.md` (create when needed).
