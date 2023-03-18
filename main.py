# import pymongo

# # Provide the mongodb localhost url to connect python to mongodb.
# client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# # Database Name
# dataBase = client["neurolabDB"]

# # Collection  Name
# collection = dataBase['Products']

# # Sample data
# d = {'companyName': 'iNeuron',
#      'product': 'Affordable AI',
#      'courseOffered': 'Machine Learning with Deployment'}

# # Insert above records in the collection
# rec = collection.insert_one(d)

# # Lets Verify all the record at once present in the record with all the fields
# all_record = collection.find()

# # Printing all records present in the collection
# for idx, record in enumerate(all_record):
#      print(f"{idx}: {record}")




from Sensor.logger import logging
from Sensor.exception import SensorException
from Sensor.utils import get_collection_as_dataframe
from Sensor.Entity.config_entity import DataIngestionConfig
from Sensor.Entity import config_entity
from Sensor.Components.data_ingestion import DataIngestion
from Sensor.Components.data_validation import DataValidation 
import sys, os
# def test_logger_and_exception():
#      try:
#           logging.info("Statring the test_logger_and_exception")
#           result = 3/0
#           print(result) 
#           logging.info("Stopping The test_logger_and_exception")
#      except Exception as e:
#           logging.debug("Stopping The test_logger_and_exception")
#           raise SensorException(e,sys)

if __name__ == "__main__":
     try:
          # test_logger_and_exception()
          #get_collection_as_dataframe(database_name="air_pressure_system",collection_name="Sensor")
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = DataIngestionConfig(training_pipeline_config = training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
          #print(data_ingestion.initiate_data_ingestion())
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

          data_validation_config = config_entity.DataValidationConfig(training_pipeline_config =training_pipeline_config)
          
          data_validation = DataValidation(data_validation_config = data_validation_config, 
                                        data_ingestion_artifact = data_ingestion_artifact) 

          data_validation_artifact = data_validation.initiate_data_validation()

     except Exception as e:
          print(e)
          
