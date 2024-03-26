#!/usr/bin/env python3
"""  changes all topics of a school doc based on name """

import pymongo


def update_topics(mongo_collection, name, topics):
    """ the main function """
    mongo_collection.update_many({"name": name}, {'$set' : {"topics": topics}})
    