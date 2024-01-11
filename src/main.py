"""Module main."""
from src.app.database import operations

import click


@click.command("retrieve_currency")
@click.option("--currency", type=click.STRING, default="USD")
def retrieve_currency(currency: str) -> None:
    """Click command to retrieve the currency exchange data and store in database."""
    currency_update = operations.retrieve_data(currency)

    if currency_update:
        operations.store_data(currency_update)

    return


if __name__ == "__main__":
    retrieve_currency()
