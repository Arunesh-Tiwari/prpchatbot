import unittest
from app.chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = Chatbot()

    def test_greeting(self):
        response = self.bot.process_message("Hello")
        self.assertIn(response, ["Hi there! How can I assist you today?", "Hello! What can I do for you?"])

    def test_unknown(self):
        response = self.bot.process_message("What's up?")
        self.assertEqual(response, "I'm not sure I understand. Could you rephrase?")
