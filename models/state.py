#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """state of the user"""


    name = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)