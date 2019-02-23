#!/usr/bin/python3

from vinylcut import db

try:
    db.drop_all()
except:
    pass
db.create_all()