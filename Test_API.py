import unittest
import requests
from fastapi.testclient import TestClient
from main import app, Food


class TestFoodAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.test_food = Food(Nom="test", type="test", adress="test", note=3)

    def test_create_food(self):
        response = self.client.post("http://localhost:8000/foods", json=self.test_food.dict())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["Nom"], "test")

    def test_read_foods(self):
        response = self.client.get("http://localhost:8000/foods")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_read_food(self):
        self.client.post("http://localhost:8000/foods", json=self.test_food.dict())
        response = self.client.get(f"/foods/{self.test_food.Nom}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["Nom"], "test")

    def test_update_food(self):
        self.client.post("http://localhost:8000/foods", json=self.test_food.dict())
        new_food = Food(Nom="test", type="updated", adress="updated", note=4)
        response = self.client.put(f"/foods/{self.test_food.Nom}", json=new_food.dict())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["type"], "updated")
        self.assertEqual(response.json()["note"], 4)

    def test_delete_food(self):
        self.client.post("http://localhost:8000/foods", json=self.test_food.dict())
        response = self.client.delete(f"/foods/{self.test_food.Nom}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Food deleted successfully")


if __name__ == "__main__":
    unittest.main()
