import pandas as pd
from scipy import spatial
import numpy as np
from scipy.spatial import KDTree

# will fetch radar scan that coincides with specific time and location
def fetch_image(self, coordinates, time):
    pass

# returns dictionary of station abbreviations and cartesian coordinates
def get_stations():
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

# returns cartesian coordinates of stations in a numpy array for use in nn search
def get_station_array():
    stations = pd.read_csv('stations_csv.csv', encoding='unicode_escape')
    stations_array = stations[['ICAO', 'X\'', 'Y\'']].to_numpy()

    return stations_array

# find nearest station for given input coordinates using KDTree data structure
def localize(x, y):
    x_input, y_input = x, y
    array = get_station_array()
    coordinate_array = array[:, [1, 2]]
    Tree = KDTree(coordinate_array)

    #find distance and index of nearest station and return corresponding station
    nn_result = Tree.query([x_input, y_input], k=1)
    distance = nn_result[0]
    index = nn_result[1]
    nearest_coords = coordinate_array[index]
    nearest_station = array[index][0]
    
    return nearest_station
            
if __name__ == "__main__":
    nearest_stat = localize()
    print(nearest_stat)
    

    

    
    

        
        

