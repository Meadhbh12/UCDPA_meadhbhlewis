import requests
import sys
import os
import json 
import pandas as pd

def main():
    print("This program will retreive 6 months of weather data for a selected location")
    print("Please input a city location:")
    location = input()

    print("Please input the year in the format YYYY (2020 and below)")
    start_year = input()
    print("Please input the month in the format MM")
    start_month = input()


    if len(start_year) < 4 or len(start_year) > 4 or int(start_year) > int(2020):
        print("Dates must be integers in the format YYYY")
        print("*****")
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif len(start_month) < 2 or len(start_month) > 2 or type(start_month) is not str:
        print("Dates must be letters in the format MM")
        print("*****")
        os.execl(sys.executable, sys.executable, *sys.argv)
    
    end_month = int(start_month) + 6
    end_year = int(start_year) 

    if end_month > 12:
        end_year = int(start_year) + 1
        end_month = end_month - 12
    
    endpoint = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&aggregateHours=24&startDateTime={start_year}-{start_month}-01T00:00:00&endDateTime={end_year}-{end_month}-01T00:00:00&unitGroup=metric&contentType=json&dayStartTime=0:0:00&dayEndTime=0:0:00&location={location}&key=PJ8XNJNRDLVHCD7WUVH9BCRL9"
    response  = requests.get(endpoint).json()
    
    if 'errorCode' not in response.keys():
        # need file 
        with open('json_response.json', 'w') as f:
            json.dump(response, f)

    df = pd.read_json(f"{os.getcwd()}/json_response.json")
    data_csv = df.to_csv('./output.csv')

if __name__ == "__main__":
    main()
    