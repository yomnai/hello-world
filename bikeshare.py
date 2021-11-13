import time
import pandas as pd
import numpy as np

CITY_DATA = { 'c': 'chicago.csv',
              'n': 'new_york_city.csv',
              'w': 'washington.csv' }

def display_data(df):
    ask_user = input('would you like to see 5 rows of the raw data. type yes or no:').lower()
    row = 0
    while ask_user != 'no': 
        print(df.iloc[row:row+ 5])
        row += 5
        ask_user = input("Do you wish to continue?: ").lower()


def get_filters():
    monthes = ["all", "january", "february", "march", "april", "may", "june"]
    days = ["all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower() not in CITY_DATA.keys():
        city = input('please select a city to view its available data, type:\n (c) for Chicago\n or (n) for New York City\n or (w) for Washington\n:')

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month.lower() not in monthes:
        month = input('\n\n in order to filter the data by a specific month, please select a month or select all if a filter is not needed, type the month name as:\n (jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec)\n or all\n:')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day.lower() not in days:
        day = input('\n\n in order to filter the data by a specific day, please select a day or select all if a filter is not needed, type the day name as:\n (saturday, sunday, monday, tuesday, wednesday, thursday, friday)\n or all\n:')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    city = city.lower()
    month = month.lower().capitalize()
    day = day.lower().capitalize()
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['date_obj'] =  pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    if day != 'All':
        df = df[df['date_obj'].dt.day_name()==day]
    if month != 'All':
        df = df[df['date_obj'].dt.month_name()==month]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if len(df['date_obj'].dt.month_name().value_counts()) == 1:
        print("Working with only 1 month \n")
    else:
        print("Most Common Month is :")
        print(df['date_obj'].dt.month_name().value_counts().keys()[0])

    # display the most common day of week
    if len(df['date_obj'].dt.day_name().value_counts()) == 1:
        print("Working with only 1 day \n")
    else:    
        print("\n Most Common day is :")
        print(df['date_obj'].dt.day_name().value_counts().keys()[0])


    # display the most common start hour
        print("\n Most common Hour is :")
        print(df['date_obj'].dt.hour.value_counts().keys()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("the most commonly used start station is :")
    print(df["Start Station"].mode()[0])
    
    print("the most commonly used end station is :")
    print(df["End Station"].mode()[0])
    
    df["Route"] = df["Start Station"] + "-" + df["End Station"]
    print("the most frequent combination of start and end stations is:")
    print(df["Route"].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("the total of travel time is:")
    print(df["Trip Duration"].sum())
          
    print("the mean of travel time is:")
    print(df["Trip Duration"].mean())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
def user_stats(df):
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("counts of user types:")
    print(df["User Type"].value_counts())
    
    if 'Gender'  in df.columns and "Birth Year" in df.columns:
        gender_count = df['Gender'].value_counts().to_frame()
        print("counts of gender:", gender_count)
   
          
    print("Earliest year of birth is:")
    print(df["Birth Year"].min())
          
    print("Most recent year of birth is:")
    print(df["Birth Year"].max())
          
    print("Most common year of birth is:")
    print(df["Birth Year"].mode()[0])
    
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
       
      
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
     
       break


if __nam__ == "__main__":
	main()
