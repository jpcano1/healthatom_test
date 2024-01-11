"""Module for database models."""
from src.app.database import db

from sqlalchemy import Column, Date, Float, Integer, String


class CurrencyUpdate(db.Base):
    """DB model class for currency update."""

    __tablename__ = "currency_update"

    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String)
    value = Column(Float)
    updated_at = Column(Date)
