import pandas as pd
import math

# fetches image most matching given spatio-temporal definition (time and location)
def fetch_image(self, coordinates, time):
    pass

# returns dictionary of station abrevs as keys and x, y coordinate values in di-entry list as values
def station_coordinates():
    stations = pd.read_csv('stations_csv.csv', encoding='unicode_escape')
    stations = stations[['ICAO', 'X\'', 'Y\'']]
    stations_dict = {}
    for index, row in stations.iterrows():
        coords_list = []
        station = row[0]
        x = row[1]
        y = row[2]
        coords_list.append(x)
        coords_list.append(y)
        stations_dict[station] = coords_list

    return stations_dict

# find nearest station for given input coordinates
def localize(x, y):
    x_input, y_input = x, y
    station_coords = station_coordinates()
    distance = 0
    for item in station_coords:
        x_cand = float(station_coords.get(item)[0])
        y_cand = float(station_coords.get(item)[1])

        distance = math.sqrt(((x_input-x_cand)**2)+((y_input-y_cand)**2))
        print(distance)

            
if __name__ == "__main__":
    localize(34.67, 21.987)





    '''
    get radar slices constrained by:
        1. number of images symmetric on target time and place (time and station)
        2. time interval between consecutive images    
    
    '''
        
        

