#!/usr/bin/python3
"""
a module that define a review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A review class
    """

    place_id = ''
    user_id = ''
    text = ''
