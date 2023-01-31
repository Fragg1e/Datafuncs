from collections import Counter 
import random

def mean(data):
    """
    Returns the mean of the list data
    """
    Mean = sum(data) / len(data)

    return round(Mean, 1)

def grt(data, value):
    """
    Returns the mean of the list data for values greater than value
    """
    data = [i for i in data if i > value]
    Mean = mean(data)
    
    return round(Mean, 1)

def grtEqual(data, value):
    """
    Returns the mean of the list data for values greater or equal to value
    """
    
    data = [i for i in data if i >= value]
    Mean = mean(data)
    
    return round(Mean, 1)
    
def less(data, value):
    """
    Returns the mean of the list data for values less than value
    """
    
    data = [i for i in data if i < value]
    Mean = mean(data)
    
    return round(Mean, 1)
    

def lessEqual(data, value):
    """
    Returns the mean of the list data for values less or equal to value
    """
    data = [i for i in data if i <= value]
    Mean = mean(data)
    
    return round(Mean, 1)

def notEqual(data, value):
    """
    Returns the mean of the list data for values not equal to value
    """
    data = [i for i in data if i != value]
    Mean = mean(data)
    
    return round(Mean, 1)


def outlier(data, low, high):
    """
    Removes the outliers from list data
    """
    
    fix = [i for i in data if i >= low and i <= high]
    
    return fix
    
def imputate(data, low, high):
    """
    Replaces invalid values in the data with the mean of the filtered data.
    """

    data_copy = outlier(data, low, high)
    mean_val = mean(data_copy)
    
    for i in data:
        if i > high or i < low:
            data[data.index(i)] = round(mean_val, 1)  
     
    return data

def median(data):
    """
    Returns the median of the list data
    """
    data.sort()
    if len(data)% 2 == 0:
        median = (data[int(len(data)/2)-1] + data[int(len(data)/2)])/2
    else:
        median = (data[int(len(data)/2)])

    return median

def mode(data):
    """
    Returns the mode of the list data
    """
    frequency = Counter(data)
    mode = [k for k, v in frequency.items() if v == max(list(frequency.values()))]
    if len(mode) == len(data):
        return None
    else:
        return mode

def freq(data, value):
    """
    Returns the Amount of time that a value occurs in the list data
    """
    counter = 0

    for i in data:
        if i == value:
            counter += 1

    return counter 

def gen(length, low, high):
    """
    Generates a list of random integers between low and high, that is length long
    """
    data = []
    for i in range(length):
        data.append(random.randint(low, high))
    return data

def range(data):
    """
    Returns the range of the list
    """
    Min = min(data)
    Max = max(data)
    Range = Max - Min
    return Range

def replace(data, old, new):
    """
    Replaces every old value in the list with the new value
    """
    for i in data:
        if i == old:
            data[data.index(i)] = new
     
    return data

  
def all(data):
    """
    Returns everything the script knows about a list
    """
    Mean = mean(data)
    Mode = mode(data)
    Median = median(data)
    Max = max(data)
    Min = min(data)
    Freq = freq(data, Mode[0])
    Range = range(data)
    string = f"Mean: {Mean}\nMode: {Mode[0]}\nFrequency of {str(Mode)}: {Freq}\nMedian: {Median}\nMax: {Max}\nMin: {Min}\nRange: {Range}"
    return string


def help():
    print(".mean(data) - Returns the mean of the list data\n")
    print(".grt(data, high) - Returns the mean of the list data for values greater than value\n")
    print(".grtEqual(data, low) - Returns the mean of the list data for values greater or equal to value\n")
    print(".less(data, high) - Returns the mean of the list data for values less than value\n")
    print(".lessEqual(data, high) - Returns the mean of the list data for values less or equal to value\n")
    print(".notEqual(data, num) - Returns the mean of the list data for values not equal to value\n")
    print(".outlier(data, low, high) - Removes the outliers from the list data\n")
    print(".imputate(data, low, high) - Replaces invalid values in the data with the mean of the filtered list data.\n")
    print(".median(data) - Returns the median of the list data\n")
    print(".mode(data) - Returns the mode of the list data - if there is no repition will return 'None' -"
    "If there is equal repitition will return a list of equal values\n")
    print(".freq(data, value) - Returns the Amount of time that a value occurs in the list data\n")
    print(".gen(length, low, high) - Generates a list of random integers between low and high, that is length long\n")
    print(".range(data) - Returns the range of the list\n")
    print(".replace(data, old, new) - Replaces every old value in the list with the new value\n")
    print(".all(data) - Returns everything the script knows about a list\n")
    print(".help - Shows you this!\n")
