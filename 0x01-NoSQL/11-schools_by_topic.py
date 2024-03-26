#!/usr/bin/env python3
"""  returns the list of school that has a specific topic """

import pymongo


def schools_by_topic(mongo_collection, topic):
    """ the main function """
    return mongo_collection.find({"topics": topic})
