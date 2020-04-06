"""This script explores data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.  It is imports data on each city and computes descriptive statistics. It requests input from the user to select a city, a month, and a day.  Also, the month/day response can be 'all' for all months in the file and/or all days in a month or all months.  Statiscits are calculated based on these user inputs."""

from random import sample
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Please enter a city: Chicago, New York City, or Washington\n').lower()
            if city in CITY_DATA:
                break
            else:
                print(city, "is not a valid city")
        except ValueError:
            print("This is not a valid city")
        finally:
            print('\nInput for city attempted\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Please enter a month January through June, or All to process all months\n').lower()
            if month in MONTHS or month == "all":
                break
            else: 
                print(month, "is not a valid month")
        except ValueError:
            print("This is not a valid month")
        finally:
            print('\nInput for month attempted\n')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Please enter a day of the week Monday through Sunday, or All to process all months\n').lower()
            if day in DAYS or day == "all":
                break
            else: 
                print(day, "is not a valid day")
        except ValueError:
            print("This is not a valid day")
        finally:
            print('\nInput for day attempted\n')
            

    #print('-'*40)
    print(city, month, day)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0] - 1
    print("\nThe most popular month is {}.".format(MONTHS[popular_month]))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("\nThe most common day is {}.".format(popular_day))


    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print("\nThe most popular hour is {}.".format(popular_hour))


    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nThe most popular start station is {}.".format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nThe most popular end station is {}.".format(popular_end_station))    


    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = "Start Station: " + df['Start Station'] + "  End Station: " + df['End Station']
    print("\nThe most frequent combination of start station and end station trip is: \n{}.".format(start_end_station.mode()[0]))
                                     


    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nThe total travel time is {} seconds. ".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe mean travel time is {} seconds. ".format(mean_travel_time))

    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df.groupby('User Type').size()
    print("\nThe counts of the different user types:\n{}".format(user_types_count))

                          
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df.groupby('Gender').size()
        print("\nThe counts of each gender is:\n{}".format(gender_count))

    
    
    # TO DO: Display earliest, most recent, and most common year of birth
     # TO DO: Display counts of user types
    if 'Birth Year' in df.columns:
        earliest_bday = df['Birth Year'].min()
        print("\nThe earliest user birthday is: {}\n".format(earliest_bday))

        latest_bday = df['Birth Year'].max()
        print("\nThe latest user birthday is: {}\n".format(latest_bday))

        most_common_bday = df['Birth Year'].mode()[0]
        print("\nThe most common user birthday is: {}\n".format(most_common_bday))


    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)

    
def raw_data(df):
    """Displays raw data on bikeshare users."""

    print('\nCalculating Raw Data...\n')
    start_time = time.time()

    # TO DO: Prompt the user to display raw data
    while True:
        try:
            response = input('Please enter "Yes" if you would like to see 5 lines of raw data, or hit "enter" to continue:\n').lower()
            if response.lower() != 'yes':
                break 
            else:
                print(df.sample(5))
        except ValueError:
            print("This is not a valid response")
        finally:
            print('\nInput for raw data attempted\n')


    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
