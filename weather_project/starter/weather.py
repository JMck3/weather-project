import csv
from datetime import datetime

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
        #temp = 49
        #temp = 57
        #addition variable does not exist
        addition = (addition +  temp)
    print (addition/int(len(weather_data)))  

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    
def load_data_from_csv(csv_file):
    def load_data_from_csv(csv_file):
        data = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if line != []:
                data.append(line [1])
    print(data)
    return data
# need to make int line.  
    # print (csv_file)
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

def find_min(weather_data):
    # low: weather_data.index(min(weather_data))
    min_value = min(weather_data)
    if weather_data.count(min_value) > 1:
        return [i for i, x in enumerate(weather_data) if x == min(weather_data)]
    else:
        position = weather_data.index(min(weather_data))
        return (f"({min_value}, {position})"),".1f"


    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
