import requests
import sys
import os
import dotenv 

def main():
    print("This program will retreive the weather data for a selected location between two years")
    print("Please input a city location:")
    location = input()

    print("Please input the first year in the format YYYY")
    start_date = input()
    print("Please input the second year in the format YYYY")
    end_date = input()

    if len(start_date) < 4 or len(start_date) > 4 and len(end_date) < 4 or len(end_date) > 4:
        print("Dates must be integers in the format YYYY")
        print("*****")
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif int(start_date) - int(end_date) >= 1:
        print("Please input two different dates, the first being the earlier date")
        print("*****")
        os.execl(sys.executable, sys.executable, *sys.argv)
    
    endpoint = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&aggregateHours=24&startDateTime={start_date}-01-01T00:00:00&endDateTime={end_date}-01-01T00:00:00&unitGroup=metric&contentType=json&dayStartTime=0:0:00&dayEndTime=0:0:00&location={location}&key={os.getenv('API_KEY')}"
    response  = requests.get(endpoint)

    
if __name__ == "__main__":
    main()
    