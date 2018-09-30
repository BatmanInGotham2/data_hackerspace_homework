#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
from math import e

def histogram_times(filename):
    crashCount = [0] * 24
    with open(filename) as f:
        csvReader = csv.reader(f)
        planeData = list(csvReader)

    for i in range(0, len(planeData)):
        time = planeData[i][1]
        check = False
        hour = 0
        try:
            hour = int(time.split(":")[0])
            check = True
        except:
            check = False
        if check and hour <= 24:
            crashCount[hour] += 1
    print(crashCount)

def weigh_pokemons(filename, weight):
    pokes = []
    dict = None
    with open(filename, 'r') as f:
        dict = json.load(f)
    for x in dict["pokemon"]:
        check = False
        w = 0.0
        try:
            w = float(x["weight"].split(" ")[0])
            check = True
        except:
            check = False

        if check and w == weight:
            pokes.append(x["name"])
    print(pokes)
    return pokes

def single_type_candy_count(filename):
    dict = None
    candy = 0
    with open(filename, 'r') as f:
        dict = json.load(f)
    for x in dict["pokemon"]:
        if len(x["type"]) == 1:
            try:
                candy += int(x["candy_count"])
            except:
                candy += 0
    print(candy)
    return candy

def reflections_and_projections(points):
    print(points)
    for i in range(0,len(points[1])):
        points[1][i] = points[1][i]*-1 + 2
    #print(points)
    points = np.array(points)
    #print(points)
    points = np.transpose(points)
    #print(points[0][0])
    for i in range(0,len(points)):
        point = np.matmul([[0,-1],[1,0]],(points[i]))
        #print(point)
        points[i][0] = point[0]
        points[i][1] = point[1]

    for i in range(0,len(points)):
        point = np.matmul([[1,3],[3,9]],(points[i]))
        #print(point)
        points[i][0] = point[0]/10.0
        points[i][1] = point[1]/10.0

    print(points)
    return points;

def normalize(image):
    min = image[0][0]
    max = image[0][0]
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if image[i][j] > max:
                max = image[i][j]
            if image[i][j] < min:
                min = image[i][j]

    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            image[i][j] = (255/(max-min)) * (image[i][j] - min)

def sigmoid_normalize(image, a):
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            image[i][j] = (255)((1 + e**((-a**1)(image[i][j]-128)))**(-1))




#reflections_and_projections([[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8]])
#single_type_candy_count('pokedex.json')
#weigh_pokemons('pokedex.json', 6.9)
#histogram_times('airplane_crashes.csv')
