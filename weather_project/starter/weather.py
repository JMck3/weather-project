import csv
from datetime import datetime
from types import DynamicClassAttribute

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # """Takes a temperature and returns it in string format with the degrees
    #     and celcius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celcius."
    # """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    # dt = datetime.strptime(iso_string,'%Y-%m-%dT%H:%M:%S%z')
    # date = dt.strftime("%A %d %B %Y")
    # return date
    date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    new_date = date.strftime("%A %d %B %Y")
    return new_date

    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """

def convert_f_to_c(temp_in_farenheit):
    heat = (float(temp_in_farenheit) - 32)/1.8
    return (round(heat,1))
    

    # """Converts an temperature from farenheit to celcius.

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
 
def calculate_mean(weather_data):
    addition = 0
    for temp in weather_data:
        addition = (addition +  float(temp))
    return (addition/(len(weather_data)))  

    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    
def load_data_from_csv(csv_file):
    data = []
    with open(csv_file, mode="r", encoding = "utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if len(line) != 0:
                data.append([line[0], int(line[1]), int(line[2])])
    return (data) 

    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """

def find_min(weather_data):
    if len(weather_data) == 0:
        return()
    minimum = float(weather_data [0])
    min_position = 0
    for index, num in enumerate(weather_data):
        if float(num) <= minimum:
            minimum = float(num)
            min_position = index
    return (minimum, min_position)
 
    #     Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """


def find_max(weather_data):
    if len(weather_data) == 0:
        return()
    maximum = float(weather_data [0])
    max_position = 0
    for index, num in enumerate(weather_data):
        if float(num) >= maximum:
            maximum = float(num)
            max_position = index
    return (maximum, max_position)


    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """


def generate_summary(weather_data):
    count = 0
    all_min = []
    all_max = []
    for row in weather_data:
        if len(row) != 0:
            count += 1
            all_min.append(row[1])
            all_max.append(row[2])
    minimum, min_position = find_min(all_min)
    minimum_c = convert_f_to_c(minimum)
    min_temp = format_temperature(minimum_c)
    min_date = convert_date(weather_data[min_position][0])  
    maximum, max_position = find_max(all_max)
    maximum_c = convert_f_to_c(maximum)
    max_temp = format_temperature(maximum_c)
    max_date = convert_date(weather_data[max_position][0])
    av_low = calculate_mean(all_min)
    av_low_c = convert_f_to_c(av_low)
    av_high = calculate_mean(all_max)
    av_high_c = convert_f_to_c(av_high)
    summary = ""
    summary += f"{count} Day Overview\n"
    summary += f"  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n"
    summary += f"  The highest temperature will be {max_temp}, and will occur on {max_date}.\n"
    summary += f"  The average low this week is {format_temperature(av_low_c)}.\n"
    summary += f"  The average high this week is {format_temperature(av_high_c)}.\n"
    return summary

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """



def generate_daily_summary(weather_data):
    summary = ""
    for rows in weather_data:
        if len(rows) != 0:
            summary += f"---- {convert_date(rows[0])} ----\n"
            summary += f"  Minimum Temperature: {format_temperature(convert_f_to_c(int(rows[1])))}\n"
            summary += f"  Maximum Temperature: {format_temperature(convert_f_to_c(int(rows[2])))}\n"
            summary += f"\n"
    return summary


    # """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """

