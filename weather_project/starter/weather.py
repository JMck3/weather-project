import csv
from datetime import datetime
from types import DynamicClassAttribute

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    dt = datetime.strptime(iso_string,'%Y-%m-%dT%H:%M:%S%z')
    date = dt.strftime("%A %d %B %Y")
    return date
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

def convert_f_to_c(temp_in_farenheit):
    heat = ((float(temp_in_farenheit) - 32)/1.8,".1f") 
    return heat
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
 
def calculate_mean(weather_data):
    addition = 0
    for temp in weather_data:
        addition = (addition +  temp)
    print (addition/int(len(weather_data)))  

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    
def load_data_from_csv(csv_file):
    data = []
    with open("tests/data/example_one.csv") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if line != []:
                data.append(line)
    with open("tests/data/example_two.csv") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if line != []:
                data.append(line)
    with open("tests/data/example_two.csv") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if line != []:
                data.append(line)
# need to make int line.  

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

def find_min(weather_data):
    if weather_data != []:
        minimum_value = min(weather_data)
    position: None
    # else:
    #     ()
    for pos, elem in enumerate(weather_data):
            position = pos
            if minimum_value == (float(elem)):
                return(float(minimum_value), position)
        # else:
        #     ()

    # if weather_data != []:
    #         for count, temperature in enumerate(weather_data): #count = 0, tempature = first_elem
    #             minvalue = min(weather_data)
    #             # minpos = weather_data.index(min(weather_data))

    #             # minvalue = min(weather_data)
    #             # index = weather_data.index(minvalue)
    #             # return (minvalue, index)
    #             print (weather_data)           
                # print(count, temperature)
            # minimum_value = "X"
                # position = weather_data.index(min(minvalue))
        # weather_data = [1,2,3]
        # minvalue = min(weather_data)
        # minvalue = 1.5
        # [1,2,3].index(2) = 1
        # weather_data = [x,y,z] 
        # pos = weather_data.index(z)
            # position = weather_data.index(minvalue)
        # weather_data.index(min(weather_data))
        # return(minvalue, position)
    # else:
    #     return ()  

    # min_value = min((weather_data))
    # # position = weather_data.index(weather_data)
    # print (min_value)     




    #     ""Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """


def find_max(weather_data):
        if weather_data != []:
            minimum_value = max(weather_data)
        position: None
    # else:
    #     ()
        for pos, elem in enumerate(weather_data):
            position = pos
            if minimum_value == (float(elem)):
                return(float(minimum_value), position)
        # else:
        #     ()


    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """



def generate_daily_summary(weather_data):


    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

