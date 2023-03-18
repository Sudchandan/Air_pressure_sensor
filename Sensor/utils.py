import pandas as pd
from Sensor.logger import logging
from Sensor.exception import SensorException
from Sensor.config import mongo_client
import os,sys
import yaml
def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)

        
def write_yaml_file(file_path,data:dict):
        try:
            file_dir = os.path.dirname(file_path)
            os.makedirs(file_dir,exists_ok = True)
            with open(file_path,"w") as file_writer:
                yaml.dump(data,file_writer)

        
        except Exception as e:
            raise SensorException(e, sys)