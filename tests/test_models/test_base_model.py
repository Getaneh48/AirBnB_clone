#!/usr/bin/python3
"""
a module that tests a base model class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    a unittest class that tests each method
    """

    model = None

    def setUp(self):
        md = {
            "id": '1',
            "my_number": 100,
            "created_at": "2024-03-07T13:56:37.408197",
            "updated_at": "2024-03-07T13:56:37.408198"
        }

        self.model = BaseModel(**md)

    def test_init(self):
        """
        test for object creation and initialization
        """

        bmodel = BaseModel()
        self.assertTrue('created_at' in bmodel.__dict__, "expected: True")
        self.assertTrue('updated_at' in bmodel.__dict__, "expected: True")
        self.assertTrue(isinstance(bmodel.created_at, datetime), "Expected: True")
        self.assertTrue(isinstance(bmodel.updated_at, datetime), "Expected: True")

    def test_init_kwargs(self):
        """
        test for object creation and initialization
        using keyword arguments
        """

        obj_dict = {
            "id": '1',
            "my_number": 100,
            "created_at": "2024-03-07T13:56:37.408197",
            "updated_at": "2024-03-07T13:56:37.408198"
        }

        obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, '1', "Expected: 1")
        self.assertEqual(obj.my_number, 100, "Expected: 100")
        self.assertEqual((obj.created_at).isoformat(), "2024-03-07T13:56:37.408197", "Expected: 2024-03-07T13:56:37.408197")
        self.assertEqual((obj.updated_at).isoformat(), "2024-03-07T13:56:37.408198", "Expected: 2024-03-07T13:56:37.408198")

    def test_to_dict(self):
        """
        test if the method returns the correct
        dictionary representation of an object
        """

        d = self.model.to_dict()
        self.assertEqual(d["id"], self.model.id, f"Expected: {self.model.id}")
        self.assertEqual(d["my_number"], self.model.my_number, f"Expected: {self.model.my_number}")
        self.assertEqual(d["created_at"], self.model.created_at.isoformat(), f"Expected: {self.model.created_at.isoformat()}")
        self.assertEqual(d["updated_at"], self.model.updated_at.isoformat(), f"Expected: {self.model.updated_at.isoformat()}")

    def test_str(self):
        """
        test's the string representation of an object
        """

        obj_str = str(self.model)
        ntest_dict = "[BaseModel] (1) {'id': '1', 'my_number': 100, 'created_at': datetime.datetime(2024, 3, 7, 13, 56, 37, 408197), 'updated_at': datetime.datetime(2024, 3, 7, 13, 56, 37, 408198)}"
        self.assertEqual(obj_str, ntest_dict, "expected equal") 
