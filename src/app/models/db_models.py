"""Module for database models."""
from src.app.database import db
from sqlalchemy import Column, Float, Integer, Date


class CurrencyUpdate(db.Base):
    __tablename__ = "currency_update"

    id = Column(Integer, primary_key=True)
    usd_value = Column(Float)
    eur_value = Column(Float)
    updated_at = Column(Date)
