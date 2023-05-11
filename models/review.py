#!/usr/bin/python3
"""a file that defines a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from base model"""

    place_id = ""
    user_id = ""
    text = ""
