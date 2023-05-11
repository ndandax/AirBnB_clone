#!/usr/bin/bash python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """state of the user"""


    name = ""
