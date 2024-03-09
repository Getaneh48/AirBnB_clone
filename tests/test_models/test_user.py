#!/usr/bin/python3
"""
a module that tests a base model class
"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
import models


class TestUser(unittest.TestCase):
    """
    a unittest class that tests each method
    """

    user = None

    def setUp(self):
        """
        setup resources
        """

        self.user = User()

    def test_init(self):
        """
        test for object creation and initialization
        """
        self.user.first_name = "bet"
        self.user.last_name = "smith"
        self.user.save()

        self.assertEqual(self.user.first_name, "bet", "Expected: bet")
        self.assertEqual(self.user.last_name, "smith", "Expected: smith")

    def test_init_kwargs(self):
        """
        test for object creation and initialization
        using keyword arguments
        """

        obj_dict = {
            "first_name": "alex",
            "last_name": "mulu",
            "email": "alm@mail.com"
        }

        obj = User(**obj_dict)
        self.assertEqual(obj.first_name, 'alex', "Expected: alex")
        self.assertEqual(obj.last_name, "mulu", "Expected: mulu")
        self.assertEqual(obj.email, "alm@mail.com", "Expected:")

    def test_is_sub_class_of(self):
        """
        test if the User model is a sub class of BaseModel
        """

        self.assertIsInstance(self.user, BaseModel)

    def test_to_dict(self):
        """
        test if the method returns the correct
        dictionary representation of an object
        """

        self.user.id = 'aaa'
        self.user.first_name = 'get'
        self.user.last_name = 'erk'
        self.user.created_at = datetime.strptime('2024-03-09T16:24:10.920194',
                                                 "%Y-%m-%dT%H:%M:%S.%f")
        self.user.updated_at = datetime.strptime('2024-03-09T16:24:10.920194',
                                                 "%Y-%m-%dT%H:%M:%S.%f")

        d = self.user.to_dict()
        c_at = f"'created_at': '2024-03-09T16:24:10.920194'"
        u_at = f"'updated_at': '2024-03-09T16:24:10.920194'"
        fn = f"'first_name': 'get'"
        ln = f"'last_name': 'erk'"
        cl = f"'__class__': 'User'"
        out = f"{{'id': 'aaa', {c_at}, {u_at}, {fn}, {ln}, {cl}}}"

        self.assertTrue(isinstance(d, dict), "Expected: dictionary")
        self.assertEqual(str(d), out, "Expected to be Equal")

    def test_str(self):
        """
        test's the string representation of an object
        """

        oid = "7bee5af0-a962-4f35-b860-d7bd9300d974"
        self.user.id = oid
        self.user.created_at = datetime(2024, 3, 9, 17, 46, 27, 449165)
        self.user.updated_at = datetime(2024, 3, 9, 17, 46, 27, 449170)
        obj_str = str(self.user)

        cat = "'created_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449165)"
        uat = "'updated_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449170)"
        output = f"[User] ({oid}) {{'id': '{oid}', {cat}, {uat}}}"

        self.assertEqual(obj_str, output, "equal expected")

    def test_save(self):
        """
        tests if the modified model is saved to a file
        """
        self.user.first_name = "alex"
        self.user.save()

        all_obj = models.storage.all()
        obj = all_obj[self.user.__class__.__name__ + '.' + str(self.user.id)]
        self.assertEqual(obj.first_name, self.user.first_name, "Expect: alex")
