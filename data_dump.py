import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILEPATH = "/config/workspace/aps_failure_training_set1.csv"

DATA_BASENAME = "aps"
COLLECTION_NAME= "sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILEPATH)
    print(f"Rows amd Columns :{df.shape}")

df.reset_index(drop=True ,inplace = True ) 
json_records = list(json.loads(df.T.to_json()).values())
print(json_records[0])
client [DATA_BASENAME][COLLECTION_NAME].insert_many(json_records
)
