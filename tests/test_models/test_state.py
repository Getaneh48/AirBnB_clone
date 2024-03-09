#!/usr/bin/python3
"""
a module that tests a base model class
"""
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
import models


class TestState(unittest.TestCase):
    """
    a unittest class that tests each method
    """

    user = None

    def setUp(self):
        """
        setup resources
        """

        self.state = State()

    def test_init(self):
        """
        test for object creation and initialization
        """
        self.state.name = "addis"
        self.state.save()

        self.assertEqual(self.state.name, "addis", "Expected: addis")

    def test_init_kwargs(self):
        """
        test for object creation and initialization
        using keyword arguments
        """

        obj_dict = {
            "name": "Wollo",
        }

        obj = State(**obj_dict)
        self.assertEqual(obj.name, 'Wollo', "Expected: Wollo")

    def test_is_sub_class_of(self):
        """
        test if the State model is a sub class of BaseModel
        """

        self.assertIsInstance(self.state, BaseModel)

    def test_to_dict(self):
        """
        test if the method returns the correct
        dictionary representation of an object
        """

        self.state.id = 'aaa'
        self.state.name = 'Gonder'
        self.state.created_at = datetime.strptime('2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")
        self.state.updated_at = datetime.strptime('2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")

        d = self.state.to_dict()
        c_at = f"'created_at': '2024-03-09T16:24:10.920194'"
        u_at = f"'updated_at': '2024-03-09T16:24:10.920194'"
        name = f"'name': 'Gonder'"
        cl = f"'__class__': 'State'"
        out = f"{{'id': 'aaa', {c_at}, {u_at}, {name}, {cl}}}"

        self.assertTrue(isinstance(d, dict), "Expected: dictionary")
        self.assertEqual(str(d), out, "Expected to be Equal")

    def test_str(self):
        """
        test's the string representation of an object
        """

        oid = "7bee5af0-a962-4f35-b860-d7bd9300d974"
        self.state.id = oid
        self.state.created_at = datetime(2024, 3, 9, 17, 46, 27, 449165)
        self.state.updated_at = datetime(2024, 3, 9, 17, 46, 27, 449170)
        obj_str = str(self.state)

        cat = "'created_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449165)"
        uat = "'updated_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449170)"
        output = f"[State] ({oid}) {{'id': '{oid}', {cat}, {uat}}}"

        self.assertEqual(obj_str, output, "equal expected")

    def test_save(self):
        """
        tests if the modified model is saved to a file
        """
        self.state.name = "gojam"
        self.state.save()

        all_obj = models.storage.all()
        obj = all_obj[self.state.__class__.__name__ + '.' + str(self.state.id)]
        self.assertEqual(obj.name, self.state.name, "Expect: gojam")
