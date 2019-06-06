import pandas as pd

import sys

import os

if __name__=='__main__':


# Script which groups yellow taxi data by yr_month, pickup location, dropoff location,
# day of week and pickup hour



  def process_data_yellow(file, adjustment):
      
      if adjustment:
      
        yellow = pd.read_csv(file, error_bad_lines=False, header=None, names=['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime','passenger_count', 
        'trip_distance', 'RatecodeID', 'store_and_fwd_flag','PULocationID', 'DOLocationID', 'payment_type', 'fare_amount', 'extra','mta_tax', 'tip_amount',
        'tolls_amount', 'improvement_surcharge','total_amount'])
        
        yellow.drop(0, inplace=True)
        
        numerics = ['passenger_count', 'trip_distance', 'fare_amount', 'extra','mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge','total_amount']
        
        for col in yellow.columns:
        
          if col in numerics:
    
            yellow[col] = pd.to_numeric(yellow[col], errors="coerce")
            
          else:
          
            yellow[col] = yellow[col].astype("str")
          
        yellow.dropna(inplace=True)
        
      else:

        yellow = pd.read_csv(file, error_bad_lines=False)
        
      
      yellow.dropna(inplace=True)
      
      yellow["tpep_pickup_datetime"] = pd.to_datetime(yellow["tpep_pickup_datetime"])
      
      yellow["tpep_dropoff_datetime"] = pd.to_datetime(yellow["tpep_dropoff_datetime"])
      
      

      yellow["yr_month"] = yellow.tpep_pickup_datetime.dt.strftime("%Y-%m")
    
      i = (yellow.tpep_pickup_datetime.dt.hour >= 5) & (yellow.tpep_pickup_datetime.dt.hour <=10)

      yellow = yellow.loc[i, :]
      
      yellow["date"] = yellow.tpep_pickup_datetime.dt.date
    
      yellow["hour"] = yellow.tpep_pickup_datetime.dt.hour

      yellow["trip_dur"] = (yellow.tpep_dropoff_datetime - yellow.tpep_pickup_datetime).apply(lambda td: td.seconds)
      
      

      yellow_ = yellow.groupby(["yr_month", "PULocationID", "DOLocationID","date", "hour"]).mean()

      yellow_["total_passengers"] = yellow.groupby(["yr_month", "PULocationID", "DOLocationID","date", "hour"]).sum()["passenger_count"]

      yellow_["ride_counts"] = yellow.groupby(["yr_month", "PULocationID", "DOLocationID", "date", "hour"]).count()["passenger_count"] 

      yellow_.reset_index(inplace=True)

      for col in yellow_.columns:

          if col not in ["PULocationID", "DOLocationID", "hour", "total_passengers", "yr_month", "ride_counts", "date"]:

              yellow_.rename(columns={col: col + "_mean"}, inplace=True)
              
      drops = [col for col in yellow_.columns if col not in ["trip_dur_mean", "yr_month", "hour", "total_passengers", "ride_counts", "PULocationID", "DOLocationID" ,"passenger_count_mean",
       "fare_amount_mean" ,  "tip_amount_mean",   "total_amount_mean", "date"]]
              
      yellow_.drop(drops, inplace=True, axis=1)
      
      print(file, "done")

      return yellow_

      
  for file in sys.argv[1:-1]:
  
    adj = sys.argv[-1].lower() == "true"
    
    name = file[:-4]
    
    file_processed = process_data_yellow(file, adj)
    
    
    
    file_processed.to_csv(name + "_processed_bydate.csv", index=False)
    
    os.system("mv " + name + "_processed_bydate.csv " + "bydate_yellow/")