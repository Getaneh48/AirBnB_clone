#!/usr/bin/python3
"""
a module that tests a base model class
"""
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
import models


class TestReview(unittest.TestCase):
    """
    a unittest class that tests each method
    """

    review = None

    def setUp(self):
        """
        setup resources
        """

        self.review = Review()

    def test_init(self):
        """
        test for object creation and initialization
        """

        objs = models.storage.all()
        obj_key = f"{self.review.__class__.__name__}.{self.review.id}"
        self.assertTrue(obj_key in objs.keys(), "Expected: True")

    def test_init_kwargs(self):
        """
        test for object creation and initialization
        using keyword arguments
        """
        self.review.place_id = 'bbb'
        self.review.user_id = 'aaa'
        self.review.text = 'i am very happy'

        obj = Review(**self.review.to_dict())
        objs = models.storage.all()
        t_obj = objs[f"{self.review.__class__.__name__}.{self.review.id}"]

        self.assertEqual(self.review.id, t_obj.id, "expected to be equal")
        self.assertEqual(self.review.place_id, 'bbb', "Expected: bbb")
        self.assertEqual(self.review.user_id, 'aaa', "Expected: aaa")
        self.assertEqual(self.review.text, 'i am very happy',
                         "Expected: i am very happy")

    def test_is_sub_class_of(self):
        """
        test if the model is a sub class of BaseModel
        """

        self.assertIsInstance(self.review, BaseModel)

    def test_to_dict(self):
        """
        test if the method returns the correct
        dictionary representation of an object
        """

        self.review.id = 'ddd'
        self.review.place_id = 'bbb'
        self.review.user_id = 'aaa'
        self.review.text = 'test'
        self.review.created_at = datetime.strptime(
                                                  '2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")
        self.review.updated_at = datetime.strptime(
                                                  '2024-03-09T16:24:10.920194',
                                                  "%Y-%m-%dT%H:%M:%S.%f")

        d = self.review.to_dict()
        c_at = f"'created_at': '2024-03-09T16:24:10.920194'"
        u_at = f"'updated_at': '2024-03-09T16:24:10.920194'"
        p_id = f"'place_id': 'bbb'"
        u_id = f"'user_id': 'aaa'"
        text = f"'text': 'test'"
        cl = f"'__class__': 'Review'"
        out = f"{{'id': 'ddd', {c_at}, {u_at}, {p_id}, {u_id}, {text}, {cl}}}"

        self.assertTrue(isinstance(d, dict), "Expected: dictionary")
        self.assertEqual(str(d), out, "Expected to be Equal")

    def test_str(self):
        """
        test's the string representation of an object
        """

        oid = "7bee5af0-a962-4f35-b860-d7bd9300d955"
        self.review.id = oid
        self.review.created_at = datetime(2024, 3, 9, 17, 46, 27, 449165)
        self.review.updated_at = datetime(2024, 3, 9, 17, 46, 27, 449170)
        obj_str = str(self.review)

        cat = "'created_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449165)"
        uat = "'updated_at': datetime.datetime(2024, 3, 9, 17, 46, 27, 449170)"
        output = f"[Review] ({oid}) {{'id': '{oid}', {cat}, {uat}}}"

        self.assertEqual(obj_str, output, "equal expected")

    def test_save(self):
        """
        tests if the modified model is saved to a file
        """
        self.review.text = "i am excited"
        self.review.save()

        all_obj = models.storage.all()
        obj = all_obj[self.review.__class__.__name__ + '.' +
                      str(self.review.id)]
        self.assertEqual(obj.text, self.review.text, "Expect: i am excited")
