"""Module for database operations."""

from src.app import client
from src.app.database import db
from src.app.models import db_models, schemas

from datetime import datetime
from loguru import logger

db.Base.metadata.create_all(bind=db.engine)
session = db.Session()


def retrieve_data(currency: str) -> schemas.CurrencyUpdateCreate | None:
    """Retrieve and store currency data."""
    logger.info("Data retrieval started...")
    query_date = datetime.utcnow()

    result = client.make_request(currency, query_date.strftime('%Y-%m-%d'))
    try:
        response_model = schemas.Response.model_validate(result)
    except ValueError as err:
        logger.error(f"PyDantic model validation error: {err}")
        return None

    logger.info("Data retrieval finished.")

    value = response_model.series.obs_data[0].value

    currency_update = schemas.CurrencyUpdateCreate(
        currency=currency, value=value, updated_at=query_date.date()
    )

    return currency_update


def store_data(currency_update: schemas.CurrencyUpdateCreate) -> None:
    """Store data from currency update."""
    logger.info("Data storing started")
    try:
        db_item = db_models.CurrencyUpdate(**currency_update.model_dump())
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        logger.info("Data stored successfully")
    except Exception as err:
        logger.error(f"Error inserting in database {err}")
