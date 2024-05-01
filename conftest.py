import pytest
from dogs_api_client.dogs_api_client import DogsApiClient
from helpers.dogs_api_helper import DogsApiHelper


@pytest.fixture(scope="session")
def dogs_api_client():
    client = DogsApiClient()
    return client


@pytest.fixture(scope="function")
def dogs_api_helper(dogs_api_client):
    helper = DogsApiHelper(dogs_api_client)
    return helper
