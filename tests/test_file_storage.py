import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)
        self.storage.save()

    def test_all_with_cls(self):
        objs = self.storage.all(BaseModel)
        self.assertIn("BaseModel.{}".format(self.obj.id), objs)

    def test_all_without_cls(self):
        objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.obj.id), objs)

    def test_delete(self):
        self.storage.delete(self.obj)
        objs = self.storage.all()
        self.assertNotIn("BaseModel.{}".format(self.obj.id), objs)

if __name__ == "__main__":
    unittest.main()

