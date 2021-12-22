import pandas as pd
from scipy import spatial
import numpy as np
from scipy.spatial import KDTree

# will fetch radar scan that coincides with specific time and location
def fetch_image(self, coordinates, time):
    pass

# returns dictionary of station abbreviations and cartesian coordinates
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

# returns cartesian coordinates of stations in a numpy array for use in nn search
def station_array():
    stations = pd.read_csv('stations_csv.csv', encoding='unicode_escape')
    stations = stations[['ICAO', 'X\'', 'Y\'']]
    stations_array = stations[['X\'', 'Y\'']].to_numpy()

    return stations_array

# find nearest station for given input coordinates using binary search
def localize(x, y):
    x_input, y_input = x, y
    array = station_array()
    Tree = KDTree(array)

    #find distance and index of nearest station
    nn_result = Tree.query([x, y], k=1)

    return nn_result
            
if __name__ == "__main__":
    result = localize(34.67, 21.987)
    print(f'Distance to Nearast radar (Coordinate Units): {result[0]}\nIndex (Check Station List): {result[1]}')

        
        

