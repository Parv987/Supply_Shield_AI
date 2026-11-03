"""Shared workflow state (owner: Shikhar). Initial sketch from the kickoff doc."""
from typing import Any, TypedDict


class SupplyChainState(TypedDict, total=False):
    scenario: dict[str, Any]
    risk_assessment: dict[str, Any]
    retrieved_evidence: list[dict[str, Any]]
    impact_analysis: dict[str, Any]
    recovery_options: list[dict[str, Any]]
    validation_results: dict[str, Any]
    final_report: dict[str, Any]
    errors: list[str]
    status: str
