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
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):        
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)
        value = int(response.read().decode('utf-8'))
        self.assertEqual(value, 4)

    def test_api_substract(self):        
        url = f"{BASE_URL}/calc/substract/20/12"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)
        value = int(response.read().decode('utf-8'))
        self.assertEqual(value, 8)

    def test_api_multiply(self):        
        url = f"{BASE_URL}/calc/multiply/5/12"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)
        value = int(response.read().decode('utf-8'))
        self.assertEqual(value, 60)

    def test_api_divide(self):        
        url = f"{BASE_URL}/calc/divide/50/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)
        value = float(response.read().decode('utf-8'))
        self.assertEqual(value, 5.0)


    def test_api_power(self):        
        url = f"{BASE_URL}/calc/power/2/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)
        value = int(response.read().decode('utf-8'))
        self.assertEqual(value, 32)


    def test_api_sqrt(self):        
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)
        value = float(response.read().decode('utf-8'))
        self.assertEqual(value, 3.0)


    def test_api_log10(self):        
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)
        value = float(response.read().decode('utf-8'))
        self.assertEqual(value, 2.0)
