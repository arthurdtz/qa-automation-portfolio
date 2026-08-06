import os
import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def headers():
    return {"x-api-key": API_KEY}