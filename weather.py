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

    """Converts and ISO formatted date into a human readable format.

        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #convert ISO string to human readable
    date_obj = datetime.fromisoformat(iso_string)
    human_readable_date = date_obj.strftime("%A %d %B %Y")
    return human_readable_date

    #pass


def convert_f_to_c(temp_in_farenheit):

    """ Converts a temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """   

    f=float(temp_in_farenheit)
    c= round((f - 32) * (5 / 9),1)
    return c
    #print(round((f - 32) * 5 / 9,1))

    #pass

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

    total_sum = 0
    for number in weather_data:
        total_sum += float(number)
    result = len(weather_data)
    calculate_mean = total_sum/result
    return float(calculate_mean)

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    #pass
#import csv ( done at top)


    
    #open file
    with open(csv_file, mode='r',encoding='utf-8') as file:
        #read file reader
        reader=csv.reader(file)
        #move to the next line/row in the csv i/e skip the header
        next(reader)

     
        # create an empty list (best to do inside this environment)
        data=[]
        #loop through row 2 to the end of the file
        for row in reader:
        #check for empty row if not row means there's nothing in the row
        #need entire row
            if not (row):
                continue
            data.append([row[0], int(row[1]), int(row[2])])    
                
        return data   

def find_max(weather_data):

    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    max_value=-200
    if not weather_data:
        return ()
    
    for i in range(len(weather_data)):
        Value=float(weather_data[i])
        #print(i)
        if Value>=max_value:
            max_value = Value
            max_position=i
            # print(max_value)

    #print(max_value, max_position )
    return (max_value, max_position)

    pass

#find_max([10.4, 14.5, 12.9, 8.9, 10.5, 11.7,14.5])

def find_min(weather_data):


    """Calculates the minimun value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimun value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    min_value=None
    min_position=0
    if not weather_data:
        #returning tupples as find min and max you dont want to be flexible
        return ()
    
    for i in range(len(weather_data)):
        value=float(weather_data[i])
        #print(i)
        if min_value == None or value<=min_value:
            min_value = value
            min_position=i
            # print(max_value)

    #print(max_value, max_position )
    return (min_value, min_position)

    pass

 

#find_max([10.4, 14.5, 12.9, 8.9, 10.5, 11.7,14.5])


def generate_summary(weather_data):

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #pass
    
#looping through weather_data
#define what kind of information is useful to sum
#for each sum create an append

    summaries=""
    minimum=[]
    maximum=[]

    for day in weather_data:

        #convert date/find min and find max
        date=convert_date(day[0])
        minimum.append(day[1])
        maximum.append(day[2])
        
        #count No of days
    No_days=len(weather_data)
    #find a min and max temp value on the list (minimum and maximum)    
    ovearall_minimum = find_min(minimum)
    ovearall_maximum = find_max(maximum)
    min_temp_date = weather_data[ovearall_minimum[1]][0]
    max_temp_date = weather_data[ovearall_maximum[1]][0]
    #convert min and max temp to C
    Convert_min = convert_f_to_c(ovearall_minimum[0])
    Convert_max = convert_f_to_c(ovearall_maximum[0])
    
    average_maximum = convert_f_to_c (calculate_mean (maximum))
    average_minimum = convert_f_to_c(calculate_mean(minimum))
        
        #return a string with summary info.
    summaries =(
                f"{No_days} Day Overview\n" 
                f"  The lowest temperature will be {format_temperature(Convert_min)}, and will occur on {convert_date(min_temp_date)}.\n"
                f"  The highest temperature will be {format_temperature(Convert_max)}, and will occur on {convert_date(max_temp_date)}.\n"
                f"  The average low this week is {format_temperature(average_minimum)}.\n"
                f"  The average high this week is {format_temperature(average_maximum)}.\n"
    ) 

    return summaries
    
def generate_daily_summary(weather_data):

    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #pass

    summaries=""

    for daily_data in weather_data:

        #convert date/find min and find max
        date=convert_date(daily_data[0])
        minimum=convert_f_to_c(daily_data[1])
        maximum=convert_f_to_c(daily_data[2])
        #return a string with summary info.
        summaries +=(
                    f"---- {date} ----\n" 
                    f"  Minimum Temperature: {format_temperature(minimum)}\n"
                    f"  Maximum Temperature: {format_temperature(maximum)}\n\n"
        ) 

    return summaries   
