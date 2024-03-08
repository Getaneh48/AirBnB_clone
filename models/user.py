#!/usr/bin/python3
"""
a module that defines a user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A user class
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
