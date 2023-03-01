import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
DATABASE_NAME = "air_pressure_system"

# Collection  Name
COLLECTION_NAME ="Sensor"
DATA_FILE_PATH ="/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__" :
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows And Column : {df.shape}")

    #Convert DataFrame To json so that we dump it in into Mongo Db
    # and We have to remove index
    df.reset_index(drop = True,inplace = True)
    # below we transposing dataframe
    json_record =list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converteed json record to mongo DB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
