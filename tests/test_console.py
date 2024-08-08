import unittest
from models import storage
from console import HBNBCommand
from models.base_model import BaseModel
from io import StringIO
import sys

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_with_parameters(self):
        cmd = 'create BaseModel name="My_little_house" age=30 height=1.75'
        sys.stdout = StringIO()
        self.console.onecmd(cmd)
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output)
        obj = storage.all().get(f"BaseModel.{output}")
        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, "My little house")
        self.assertEqual(obj.age, 30)
        self.assertEqual(obj.height, 1.75)

if __name__ == "__main__":
    unittest.main()

