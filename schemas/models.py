"""Shared data contracts. Agree changes as a team before editing."""
from typing import Optional

from pydantic import BaseModel


class Scenario(BaseModel):
    scenario_id: str  # e.g. "SCN-001"
    product_id: str  # e.g. "SKU-100"
    available_stock: int  # units
    expected_demand: int  # units over demand_window_days
    demand_window_days: int
    shipment_delay_days: int
    supplier_id: Optional[str] = None


class EvidenceItem(BaseModel):
    source_id: str
    document_name: str
    snippet: str
    page_or_section: Optional[str] = None
    relevance_score: Optional[float] = None
