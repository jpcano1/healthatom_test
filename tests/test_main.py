"""Module to test main."""

from src.main import retrieve_currency

from unittest.mock import MagicMock, patch


@patch("src.main.retrieve_data")
@patch("src.main.store_data")
def test_retrieve_currency(mock_store_data, mock_retrieve_data, cli_runner):
    mock_retrieve_data.return_value = None

    result = cli_runner.invoke(retrieve_currency, ["--currency", "USD"])

    assert mock_retrieve_data.called
    assert not mock_store_data.called
    assert result.exit_code == 0

    mock_retrieve_data.return_value = MagicMock()

    result = cli_runner.invoke(retrieve_currency, ["--currency", "USD"])

    assert mock_retrieve_data.called
    assert mock_store_data.called
    assert result.exit_code == 0
