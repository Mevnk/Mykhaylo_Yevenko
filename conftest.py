import pytest
def pytest_addoption(parser):
    parser.addoption("--access-token", action="store", help="API access token")
