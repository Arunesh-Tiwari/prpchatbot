import unittest
from app.data_handler import DataHandler

class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.data_handler = DataHandler()

    def test_save_and_load_user_data(self):
        test_data = {"users": ["test_user"]}
        self.data_handler.save_user_data(test_data, file="data/test_user_data.json")
        loaded_data = self.data_handler.load_user_data(file="data/test_user_data.json")
        self.assertEqual(test_data, loaded_data)
