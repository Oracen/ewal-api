# -*- coding: utf-8 -*-
"""
Random user endpoint.

Using Mimesis example for this: https://bit.ly/37KUAlo

"""

# _ = Field("en")
random_users = {
    "id": "",
    "name": "bob",
    "surname": "Dole",
    "email": "no@abc.com",
    "age": 12,
    "username": "mad",
    "occupation": "lad",
    "address": {
        "street": "22 Wallaby Way",
        "city": "Sydney",
        "zipcode": "2000",
    },
}


def passwd(length: int = 8, hash: bool = False) -> str:
    """
    Helper function to generate a random password.
    """
    return ""


def emojis() -> str:
    """
    Helper function to create random a emoji.
    """
    return ""
