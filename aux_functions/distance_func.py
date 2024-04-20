import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2

# Calcula la distancia euclidiana entre todas las ubicaciones
def euclidan_dist(coord):
    euclidian_distances = []
    for c in coord:
        this_row = [np.linalg.norm(np.array(c) - np.array(x)) for x in coord]
        euclidian_distances.append(this_row)

    # Crea un DataFrame con las distancias
    df_distance_matrix = pd.DataFrame(euclidian_distances)
    return df_distance_matrix

def distancia_entre_puntos(lat1, lon1, lat2, lon2):
        # Convertir grados a radianes
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        # Radio de la Tierra en kilómetros
        radio_tierra = 6371.0

        # Diferencia de latitud y longitud
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Fórmula de Haversine
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Distancia en kilómetros
        distancia = radio_tierra * c

        return distancia

def haversine_distance(coord):
    # Función auxiliar para calcular la distancia entre dos puntos
    

    # Crear matriz de distancias
    num_puntos = len(coord)
    matriz_distancias = np.zeros((num_puntos, num_puntos))

    # Calcular las distancias entre cada par de puntos
    for i in range(num_puntos):
        for j in range(num_puntos):
            lat1, lon1 = coord[i]
            lat2, lon2 = coord[j]
            distancia = distancia_entre_puntos(lat1, lon1, lat2, lon2)
            matriz_distancias[i][j] = distancia

    # Crear DataFrame de la matriz de distancias
    df_distance_matrix = pd.DataFrame(matriz_distancias) #, columns=range(0, num_puntos), index=range(0, num_puntos))

    return df_distance_matrix