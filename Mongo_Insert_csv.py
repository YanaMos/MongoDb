import csv
import json
import pandas as pd
import getopt, pprint
import pymongo
import os
from pymongo import MongoClient


def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27311)
    mng_db = mng_client['London_postcodes']
    collection_name = 'London_postcodes'
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)


if __name__ == "__main__":
  filepath = 'London_postcodes.csv'
  import_content(filepath)


print('insert done')


# how to run docker
# docker-compose -f docker-compose.1.yml -f docker-compose.2.yml  -f docker-compose.cnf.yml -f docker-compose.shard.yml up