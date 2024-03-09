#!/usr/bin/python3
"""
a module that tests a base model class
"""
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
import models


class TestCity(unittest.TestCase):
    """
    a unittest class that tests each method
    """

    city = None

    def setUp(self):
        """
        setup resources
        """

        self.city = City()

    def test_init(self):
        """
        test for object creation and initialization
        """

        objs = models.storage.all()
        obj_key = f"{self.city.__class__.__name__}.{self.city.id}"
        self.assertTrue(obj_key in objs.keys(), "Expected: True")

    def test_init_kwargs(self):
        """
        test for object creation and initialization
        using keyword arguments
        """
        self.city.state_id = 'bbb'
        self.city.name = 'Bahirdar'

        obj = City(**self.city.to_dict())
        objs = models.storage.all()
        t_obj = objs[f"{self.city.__class__.__name__}.{self.city.id}"]

        self.assertEqual(self.city.id, t_obj.id, "expected to be equal")
        self.assertEqual(self.city.state_id, 'bbb', "Expected: bbb")
        self.assertEqual(self.city.name, 'Bahirdar', "Expected: Bahirdar")

    def test_is_sub_class_of(self):
        """
        test if the model is a sub class of BaseModel
        """

        self.assertIsInstance(self.city, BaseModel)

    def test_to_dict(self):
        """
        test if the method returns the correct
        dictionary representation of an object
        """

        self.city.id = 'ddd'
        self.city.state_id = 'bbb'
        self.city.name = 'jima'
        self.city.created_at = datetime.strptime(
                                                  '2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")
        self.city.updated_at = datetime.strptime(
                                                  '2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")

        d = self.city.to_dict()
        c_at = f"'created_at': '2024-03-09T16:24:10.920194'"
        u_at = f"'updated_at': '2024-03-09T16:24:10.920194'"
        s_id = f"'state_id': 'bbb'"
        name = f"'name': 'jima'"
        cl = f"'__class__': 'City'"
        out = f"{{'id': 'ddd', {c_at}, {u_at}, {s_id}, {name}, {cl}}}"

        self.assertTrue(isinstance(d, dict), "Expected: dictionary")
        self.assertEqual(str(d), out, "Expected to be Equal")

    def test_str(self):
        """
        test's the string representation of an object
        """

        oid = "7bee5af0-a962-4f35-b860-d7bd9300d955"
        self.city.id = oid
        self.city.created_at = datetime(2024, 3, 9, 17, 46, 27, 449165)
        self.city.updated_at = datetime(2024, 3, 9, 17, 46, 27, 449170)
        obj_str = str(self.city)

        cat = "'created_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449165)"
        uat = "'updated_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449170)"
        output = f"[City] ({oid}) {{'id': '{oid}', {cat}, {uat}}}"

        self.assertEqual(obj_str, output, "equal expected")

    def test_save(self):
        """
        tests if the modified model is saved to a file
        """
        self.city.name = "raya"
        self.city.save()

        all_obj = models.storage.all()
        obj = all_obj[self.city.__class__.__name__ + '.' +
                      str(self.city.id)]
        self.assertEqual(obj.name, self.city.name, "Expect: raya")
