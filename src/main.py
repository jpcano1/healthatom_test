"""Module main."""
from src.app.database.operations import retrieve_data, store_data

import click


@click.command("retrieve_currency")
@click.option("--currency", type=click.STRING, default="USD")
def retrieve_currency(currency: str) -> int:
    """Click command to retrieve the currency exchange data and store in database."""
    currency_update = retrieve_data(currency)

    if currency_update:
        store_data(currency_update)

    return 0


if __name__ == "__main__":
    retrieve_currency()
