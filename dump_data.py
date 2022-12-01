import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

file_path_name="/config/workspace/aps_failure_training_set1.csv"
database_name="aps"
collection_name="sensor"

if __name__=="__main__":
    df=pd.read_csv(file_path_name)
    print(f"row and column :{df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())

    client[database_name][collection_name].insert_many(json_record)

    print(json_record[0])

