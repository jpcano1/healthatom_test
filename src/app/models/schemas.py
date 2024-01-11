"""Module for PyDantic models."""

from pydantic import BaseModel
from datetime import date


class CurrencyUpdateCreate(BaseModel):
    """PyDantic model for currency update model."""

    id: int
    usd_value: float
    eur_value: float
    updated_at: date

    class Config:
        """Additional Config."""

        orm_mode = True
