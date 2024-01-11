"""Module for configuration tests."""

import pytest
from unittest.mock import patch


@pytest.fixture(autouse=True)
@patch("os.getenv")
def mock_os_getenv(mock_getenv):
    """Mock os getenv."""
    mock_getenv.side_effect = lambda x: "mock_value" if x in ("API_USER", "API_KEY") else None
    yield mock_getenv
