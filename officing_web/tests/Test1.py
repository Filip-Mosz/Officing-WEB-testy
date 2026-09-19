from django.test import TestCase
from django.urls import resolve

class Test1(TestCase): #have to have Test in name (convention)
    def test1(self): #OK
        assert 1 + 2 == 3

    def test2(self): #fail
        assert 1 + 2 == 4

    def testUrl1(self): #fail
        match = resolve("/api/hello/")
        assert match.url_name == "hello"

    def testUrl2(self): #fail
        response = self.client.get("/api/hello/")
        assert response.status_code == 200
