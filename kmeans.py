import numpy as np 
import pandas as pd

def euclidean_distance(p1, p2):
    #check if somehow the sum is negative? I do not think that is even possible but just check
    
    #check that both lists are not empty 
    if(len(p1) == 0 or len(p2) == 0):
        raise ValueError("Input list(s) cannot be empty.")
    #check that both lists have the same amount of entries 
    elif(len(p1) != len(p2)):
        raise ValueError("Input lists must be the same length.")

    for i in range(0, len(p1)):
        if p1[i] == str or p2[i] == str:
            raise TypeError("Input list(s) cannot contain strings.")
            #referenced: https://www.geeksforgeeks.org/python/python-isinstance-method/ on March 12, 2026

    difference = []

    for i in range(0, len(p1)):
        diff = p1[i] - p2[i]
        diff_square = diff**2
        difference.append(diff_square)
        
    euc_sum = np.sum(difference)
    euc_distance = np.sqrt(euc_sum)
    
    return euc_distance

def find_closest_centroid(point, centroids):
    #return the index of the closest centroid to the point
    #the centroid can have x, y, ..., z dimensions and so can the point
    distances = []
    diff = []
    if(len(point) == 0 and len(centroids) == 0):
        raise ValueError("Input lists cannot be empty.")
    elif(point[0:len(point)] == str or centroids[0:len(centroids)] == str):
        raise TypeError("Input list(s) cannot contain strings.")
    if len(point) == 1: #one dimension
        for i in range(0, len(centroids)):
            diff = point[0] - centroids[i]
            diff_square = diff**2
            distances.append(diff_square)
    else: #more than one dimension
        for i in range(0, len(centroids)):
            if(len(point) != len(centroids[i])):
                raise ValueError("Input lists must be of the same length.")
            else:
                for j in range(0, len(centroids[i])):                    
                    diff = point[j] - centroids[i][j]
                    diff_square = diff**2
                    euc_sum = np.sum(diff_square)
                    euc_sqrt = np.sqrt(euc_sum)
            distances.append(euc_sqrt)

    closest = distances.index(np.min(distances)) 
    #if there are two or more minimums this defaults to taking the one with the smallest index 
    
    #referenced on March 12, 2026 for the index and min function: 
        #https://www.geeksforgeeks.org/python/python-list-index/
        #https://www.geeksforgeeks.org/python/find-the-maximum-and-minimum-element-in-a-numpy-array/
    
    #need to return the index of closest centroid
    return(closest)


def update_centroids(data, labels, k):
    #We will need Sum and Count to compute the Average. 
    
    Sum_Data = []
    Count_Data = []
    
    #Now will initialize the Sum and Count
    for i in range(k):
        Sum_Data.append([0,0])
        Count_Data.append(0)
    
    #Now will go over each of the data points where will indicate the cluster where data point actually belongs
    
    for i in range(len(data)):
        Cluster = labels[i]
        Point = data[i]
        
        #Now will do sum
        Sum_Data[Cluster][0] += Point[0]
        Sum_Data[Cluster][1] += Point[1]
    
        #Since did the sum now we will increase the count too
        Count_Data[Cluster] += 1
    
    #Now since our for loop is already doing sum and increasing the count for each of the data pair, we can count the centroid by dividing sum with count.
    Centroid = []
    for j in range (k):
        DataX_Avg = Sum_Data[j][0] / Count_Data[j]
        DataY_Avg = Sum_Data[j][1] / Count_Data[j]
        Centroid.append([DataX_Avg, DataY_Avg])
    return Centroid

def has_converged(old, new, tol):
    #To go over each centroid one by one we will do for loop
    
    for i in range(len(old)):
        Centroid_Old = old[i]
        Centroid_New = new[i]
        
        #Since now we will have to see the actual distance between the old and new centroid adnd since Aysha has created Euclidean function we will use it
        Distance = euclidean_distance(Centroid_Old, Centroid_New)
        
        #Now since we have a distance, we will compare it with tolerance level to see is it converged yet or not.
        if Distance > tol:
            return False
    return True

def fit(data, k):
    # Isaac to implement
    pass