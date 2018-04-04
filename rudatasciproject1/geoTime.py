import numpy as np
from datetime import datetime
from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()

def createLatitude(latlng):
    try:
        #print(latlng)
        # This removes paranthesis 
        latlngArray = latlng.strip("(").strip(")").split(",")
        lat,lon = np.round(np.float(latlngArray[0]),3),np.round(np.float(latlngArray[1]),3)
        #print(lat,lon)
        return lat
    except:
        return ""
    
def createLongitude(latlng):
    try:
        #print(latlng)
        # This removes paranthesis 
        latlngArray = latlng.strip("(").strip(")").split(",")
        lat,lon = np.round(np.float(latlngArray[0]),3),np.round(np.float(latlngArray[1]),3)
        #print(lat,lon)
        return lon
    except:
        return ""

def getZipCode(latlng):
    #print(latlng)
    #latlngStr = latlng.strip("(").strip(")")
    #target_url1 = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s&key=%s" % (latlngStr,apiKey)
    #geo_data = requests.get(target_url1).json()
    #print(json.dumps(geo_data['results'][0], sort_keys=True, indent=4))
    try:
        #print([item['long_name'] for item in geo_data['results'][0]['address_components'] if "postal_code" in item['types']][0])
        #return [item['long_name'] for item in geo_data['results'][0]['address_components'] if "postal_code" in item['types']][0]
        latlngArray = latlng.strip("(").strip(")").split(",")
        lat,lon = np.float(latlngArray[0]),np.float(latlngArray[1])
        return search.by_coordinate(lat,lon, radius=1)[0]['Zipcode']
    except:
        #print(geo_data)
        return ""
    
def getDateTime(date_string):
    #print(date_string)
    date_list = [date_string.split("/")[2],date_string.split("/")[0],date_string.split("/")[1]]
    date_list = [np.int(item) for item in date_list]
    return datetime(date_list[0],date_list[1],date_list[2])

#Create a method that cleans the data
def checkResults(iteminSeries):
    if (type(iteminSeries)==str) & (iteminSeries != np.nan):
        return "True"
    else:
        #print(iteminSeries)
        return "False"
