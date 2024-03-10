#!/usr/bin/python3
"""
a module that tests a base model class
"""
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
import models
import re


class TestPlace(unittest.TestCase):
    """
    a unittest class that tests each method
    """

    place = None

    @classmethod
    def setUp(self):
        """
        setup resources
        """

        self.place = Place()

    def test_init(self):
        """
        test for object creation and initialization
        """

        objs = models.storage.all()
        obj_key = f"{self.place.__class__.__name__}.{self.place.id}"
        self.assertTrue(obj_key in objs.keys(), "Expected: True")

    def test_init_object_created(self):
        """
        test if the object is created
        """

        self.assertIsNotNone(self.place)

    def test_init_object_type(self):
        """
        test if the object is type of a specific class
        """

        self.assertIsInstance(self.place, BaseModel)

    def test_init_attrib_existence(self):
        """
        tests weither main attributes exists or not
        """

        self.assertTrue(hasattr(self.place, "id"), "expected: true")
        self.assertTrue(hasattr(self.place, "name"), "expected: true")
        self.assertTrue(hasattr(self.place, "created_at"), "expected: true")
        self.assertTrue(hasattr(self.place, "updated_at"), "expected: true")
        self.assertTrue(hasattr(self.place, "city_id"), "expected: true")
        self.assertTrue(hasattr(self.place, "user_id"), "expected: true")
        self.assertTrue(hasattr(self.place, "description"), "expected: true")
        self.assertTrue(hasattr(self.place, "number_rooms"), "expected: true")
        self.assertTrue(hasattr(self.place, "number_bathrooms"),
                        "expected: true")
        self.assertTrue(hasattr(self.place, "max_guest"), "expected: true")
        self.assertTrue(hasattr(self.place, "price_by_night"),
                        "expected: true")
        self.assertTrue(hasattr(self.place, "latitude"), "expected: true")
        self.assertTrue(hasattr(self.place, "longitude"), "expected: true")
        self.assertTrue(hasattr(self.place, "amenity_ids"), "expected: true")

    def test_instance_attribute_type(self):
        """
        tests the instance attribute types
        """

        self.assertIsInstance(getattr(self.place, 'created_at'), datetime)
        self.assertIsInstance(getattr(self.place, 'updated_at'), datetime)
        # Regular e    xpression for UUID4 format
        id_f = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        self.assertTrue(re.match(id_f, self.place.id))

    def test_init_kwargs(self):
        """
        test for object creation and initialization
        using keyword arguments
        """
        self.place.name = 'place'

        obj = Place(**self.place.to_dict())
        objs = models.storage.all()
        t_obj = objs[f"{self.place.__class__.__name__}.{self.place.id}"]

        self.assertEqual(self.place.name, 'place', "Expected: place")

    def test_is_sub_class_of(self):
        """
        test if the model is a sub class of BaseModel
        """

        self.assertIsInstance(self.place, BaseModel)

    def test_to_dict(self):
        """
        test if the method returns the correct
        dictionary representation of an object
        """
        self.place.id = 'ddd'
        self.place.name = 'piasa'
        self.place.created_at = datetime.strptime(
                                                  '2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")
        self.place.updated_at = datetime.strptime(
                                                  '2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")

        d = self.place.to_dict()
        c_at = f"'created_at': '2024-03-09T16:24:10.920194'"
        u_at = f"'updated_at': '2024-03-09T16:24:10.920194'"
        name = f"'name': 'piasa'"
        cl = f"'__class__': 'Place'"
        out = f"{{'id': 'ddd', {c_at}, {u_at}, {name}, {cl}}}"

        self.assertTrue(isinstance(d, dict), "Expected: dictionary")
        self.assertEqual(str(d), out, "Expected to be Equal")

    def test_str(self):
        """
        test's the string representation of an object
        """

        oid = "7bee5af0-a962-4f35-b860-d7bd9300d955"
        self.place.id = oid
        self.place.created_at = datetime(2024, 3, 9, 17, 46, 27, 449165)
        self.place.updated_at = datetime(2024, 3, 9, 17, 46, 27, 449170)
        obj_str = str(self.place)

        cat = "'created_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449165)"
        uat = "'updated_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449170)"
        output = f"[Place] ({oid}) {{'id': '{oid}', {cat}, {uat}}}"

        self.assertEqual(obj_str, output, "equal expected")

    def test_save(self):
        """
        tests if the modified model is saved to a file
        """
        self.place.name = "mexico"
        self.place.save()

        all_obj = models.storage.all()
        obj = all_obj[self.place.__class__.__name__ + '.' +
                      str(self.place.id)]
        self.assertEqual(obj.name, self.place.name, "Expect: mexico")
