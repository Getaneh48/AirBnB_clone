#!/usr/bin/python3
"""
a module that tests a base model class
"""
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import models
import re


class TestAmenity(unittest.TestCase):
    """
    a unittest class that tests each method
    """

    amenity = None

    @classmethod
    def setUp(self):
        """
        setup resources
        """

        self.amenity = Amenity()

    def test_init(self):
        """
        test for object creation and initialization
        """

        objs = models.storage.all()
        obj_key = f"{self.amenity.__class__.__name__}.{self.amenity.id}"
        self.assertTrue(obj_key in objs.keys(), "Expected: True")

    def test_init_object_created(self):
        """
        test if the object is created
        """

        self.assertIsNotNone(self.amenity)

    def test_init_object_type(self):
        """
        test if the object is type of a specific class
        """

        self.assertIsInstance(self.amenity, BaseModel)

    def test_init_attrib_existence(self):
        """
        tests weither main attributes exists or not
        """

        self.assertTrue(hasattr(self.amenity, "id"), "expected: true")
        self.assertTrue(hasattr(self.amenity, "name"), "expected: true")
        self.assertTrue(hasattr(self.amenity, "created_at"), "expected: true")
        self.assertTrue(hasattr(self.amenity, "updated_at"), "expected: true")

    def test_instance_attribute_type(self):
        """
        tests the instance attribute types
        """

        self.assertIsInstance(getattr(self.amenity, 'created_at'), datetime)
        self.assertIsInstance(getattr(self.amenity, 'updated_at'), datetime)
        # Regular e    xpression for UUID4 format
        id_f = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        self.assertTrue(re.match(id_f, self.amenity.id))

    def test_init_kwargs(self):
        """
        test for object creation and initialization
        using keyword arguments
        """
        self.amenity.name = 'Lexury'

        obj = Amenity(**self.amenity.to_dict())
        objs = models.storage.all()
        t_obj = objs[f"{self.amenity.__class__.__name__}.{self.amenity.id}"]

        self.assertEqual(self.amenity.name, 'Lexury', "Expected: Lexury")

    def test_is_sub_class_of(self):
        """
        test if the model is a sub class of BaseModel
        """

        self.assertIsInstance(self.amenity, BaseModel)

    def test_to_dict(self):
        """
        test if the method returns the correct
        dictionary representation of an object
        """
        self.amenity.id = 'ddd'
        self.amenity.name = 'lexury'
        self.amenity.created_at = datetime.strptime(
                                                  '2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")
        self.amenity.updated_at = datetime.strptime(
                                                  '2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")

        d = self.amenity.to_dict()
        c_at = f"'created_at': '2024-03-09T16:24:10.920194'"
        u_at = f"'updated_at': '2024-03-09T16:24:10.920194'"
        name = f"'name': 'lexury'"
        cl = f"'__class__': 'Amenity'"
        out = f"{{'id': 'ddd', {c_at}, {u_at}, {name}, {cl}}}"

        self.assertTrue(isinstance(d, dict), "Expected: dictionary")
        self.assertEqual(str(d), out, "Expected to be Equal")

    def test_str(self):
        """
        test's the string representation of an object
        """

        oid = "7bee5af0-a962-4f35-b860-d7bd9300d955"
        self.amenity.id = oid
        self.amenity.created_at = datetime(2024, 3, 9, 17, 46, 27, 449165)
        self.amenity.updated_at = datetime(2024, 3, 9, 17, 46, 27, 449170)
        obj_str = str(self.amenity)

        cat = "'created_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449165)"
        uat = "'updated_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449170)"
        output = f"[Amenity] ({oid}) {{'id': '{oid}', {cat}, {uat}}}"

        self.assertEqual(obj_str, output, "equal expected")

    def test_save(self):
        """
        tests if the modified model is saved to a file
        """
        self.amenity.name = "lexury"
        self.amenity.save()

        all_obj = models.storage.all()
        obj = all_obj[self.amenity.__class__.__name__ + '.' +
                      str(self.amenity.id)]
        self.assertEqual(obj.name, self.amenity.name, "Expect: lexury")
