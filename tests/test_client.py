"""Module for client tests."""
from src.app import client

import responses
from unittest.mock import patch


@responses.activate
def test_make_request(mock_os_getenv):
    responses.add(
        responses.GET,
        "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx",
        json={"your": "response"},
        status=200,
    )

    result = client.make_request("USD", query_date="2024-01-01")

    assert result == {"your": "response"}
    assert len(responses.calls) == 1


@responses.activate
@patch("src.app.client.logger")
def test_check_response(mock_logger):
    responses.add(
        responses.GET,
        "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx",
        json={"error": "response"},
        status=400,
    )

    _ = client.make_request("USD", query_date="2024-01-01")

    assert mock_logger.error.called
