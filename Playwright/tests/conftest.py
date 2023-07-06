import pytest
import requests
from config import *


@pytest.fixture()
def get_users():
     r = requests.get(url_get_list)
     return r