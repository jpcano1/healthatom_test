"""Module for API calling and storing Money Exchange."""

from dotenv import find_dotenv, load_dotenv
from loguru import logger
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

load_dotenv(find_dotenv())

BASE_URL = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx"


def get_adapter(total_retry: int = 3, read_retry: int = 20, connect_retry: int = 20) -> HTTPAdapter:
    """
    Get an adapter for making requests.

    :param total_retry: Total number of times to retry.
    :param read_retry: Total number of times to retry on read.
    :param connect_retry: Total number of times to retry on connect.
    :return: The adapter object.
    """
    retry_strategy = Retry(
        total=total_retry,
        status_forcelist=[499, 500, 501, 502, 503, 504],
        backoff_factor=0.5,
        read=read_retry,
        connect=connect_retry,
    )

    return HTTPAdapter(max_retries=retry_strategy)


def make_request(currency: str, query_date: str, timeout: int = 20):
    """
    Make a request to the API and return the currency obtained.

    :param currency: The currency to obtain. May be USD or EUR.
    :param query_date: The date to query.
    :param timeout: The request timeout in seconds.
    :return: The response from the API.
    """
    adapter = get_adapter()

    time_series = "F073.TCO.PRE.Z.D" if currency == "USD" else "F072.CLP.EUR.N.O.D"

    params = {
        "user": os.getenv("API_USER"),
        "pass": os.getenv("API_KEY"),
        "function": "GetSeries",
        "firstdate": query_date,
        "lastdate": query_date,
        "timeseries": time_series,
    }

    with requests.Session() as session:
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        response = session.get(
            BASE_URL, timeout=timeout, hooks={"response": check_response}, params=params
        )

        return response.json()


def check_response(r: requests.Response, *_, **__) -> None:
    """Create a hook for checking request response."""
    if not r.ok and 400 <= r.status_code < 499:
        message = (
            f"Error in request:\n"
            f"{r.request.method} - {r.url}\n"
            f"{r.status_code} - {r.reason} - {r.text}"
        )
        logger.error(message)
