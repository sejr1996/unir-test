import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        print('=== === ===')
        print('por aqui')
        print('BASE_URL', BASE_URL)
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")
        print('=== === ===')

    def test_api_add(self):
        self.assertEqual(11, 11)
        
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        print(response)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
