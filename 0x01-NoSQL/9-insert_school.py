#!/usr/bin/env python3
"""  inserts a new doc in a collection based on kwargs """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ the main function """
    return mongo_collection.insert_one(kwargs).inserted_id
