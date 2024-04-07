import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Hello! Let\'s explore some US bikeshare data!')
# get user input for city (chicago, new york city, washington).
city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
# if input invalid, give the user another chance
while city not in CITY_DATA.keys():
    city = input('City not found. Please re-enter the city you wish to explore: Chicago, New York City, or Washington.\n').lower()

# load data file into a dataframe and add columns required for filtering
df = pd.read_csv(CITY_DATA[city])
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name
month_names = ['January', 'February', 'March', 'April', 'May', 'June']

# get user input for variable to filter by
filt = input('Would you like to filter by month, day, or neither?\n').lower()
# if input invalid, give the user another chance
while filt not in ('month', 'day', 'neither'):
    filt = input('Filter option not found. Please re-enter the option you wish to filter by: month, day, or neither.\n').lower()
# in the case of filtering by month, get user input for which month
if filt == 'month':
    month = input('Which month? Input 1 for January, 2 for February, etc, up to 6 for June.\n')
    # if input invalid, give the user another chance to input
    while int(month) not in range(1, 7):
        month = input('Month not found. Please re-enter the month you wish to explore. Input 1 for January, 2 for February, etc, up to 6 for June.\n')
    # filter data by chosen month
    df = df[df['month'] == int(month)]
# in the case of filtering by weekday, get user input for which day
elif filt == 'day':
    day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
    # if input invalid, give the user another chance to input
    while day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        day = input('Day not found. Please re-enter the day you wish to explore.\n').title()
    # filter data by chosen day
    df = df[df['day_of_week'] == day]

print('-'*40)
    
# provide a summary of user selection
print(f'You have selected to view statistics for {city.title()}.\n')
if filt == 'month':
    print(f'You have selected to filter by {filt}. Now showing results for the month of {month_names[int(month)-1]}.\n')
elif filt == 'day':
    print(f'You hvae selected to filter by {filt}. Now showing results for {day.title()}s.\n')
else:
    print('Now showing results for all days and months.\n')

# compute popular times of travel statistics
popular_month = df['month'].mode()[0]
popular_day = df['day_of_week'].mode()[0]
df['hour'] = df['Start Time'].dt.hour
popular_hour = df['hour'].mode()[0]
print(f'Popular Times of Travel\n\
    - The most common month to travel is {month_names[int(popular_month)-1]}.\n\
    - The most common day of the week to travel is {popular_day}.\n\
    - The most common hour of the day to travel is hour {popular_hour}.\n')

# compute popular stations and trip statistics
popular_start = df['Start Station'].mode()[0]
popular_end = df['End Station'].mode()[0]
df['start_end'] = df['Start Station'] + ' to ' + df['End Station']
popular_trip = df['start_end'].mode()[0]
print(f'Popular Stations and Trip\n\
    - The most common station to travel from is {popular_start}.\n\
    - The most common station to travel to is {popular_end}.\n\
    - The most common trip to complete is {popular_trip}.\n')

# compute trip duration statistics
total = 0
for duration in df['Trip Duration']: 
    total += duration
total_travel = total
average_travel = total / len(df['Trip Duration'])
print(f'Trip Duration\n\
    - The total travel time is {total_travel}.\n\
    - The average travel time is {average_travel}.\n')

# compute user info statistics
subscriber_count = (df['User Type'] == 'Subscriber').sum()
customer_count = (df['User Type'] == 'Customer').sum()
print(f'User Information\n\
    - The count for subscribers is {subscriber_count} and the count for customers is {customer_count}.')
### if viewing Washington data, gender and birth year statistics not available
if city == 'washington':
    print('    - The count by gender is not available for this dataset.\n\
    - Birth year statistics are not available for this dataset.\n')
### if viewing Chicago or New York City data, gender and birth year statistics are available
else:
    female_count = (df['Gender'] == 'Female').sum()
    male_count = (df['Gender'] == 'Male').sum()
    earliest_birth = int(df['Birth Year'].min())
    recent_birth = int(df['Birth Year'].max())
    popular_birth = int(df['Birth Year'].mode()[0])
    print(f'    - The count for females is {female_count} and the count for males is {male_count}.\n\
    - The earliest year of birth is {earliest_birth}, the most recent is {recent_birth}, and the most common is {popular_birth}.\n')

# disply raw data for user in 5-row increments
def snapshot(df):
    """
    Displays the data in 5-row increments, checking each time if the user wishes to see more.
    Args:
        df - raw data 
    Returns:
        df - 5-row snapshot of raw data
    """
    step = 0
    # initial user input
    while True:
        display = input('Would you like to see a snapshot of the raw data? Input yes or no.\n').lower()
        # if input invalid, give the user another chance to input
        if display not in ('yes', 'no'):
            print('Invalid option chosen.')
            continue
        # loop through displaying the data in 5-row increments
        elif display == 'yes':
            while True:
                raw_data = df.iloc[step:step+5, : ]
                step += 5
                # print data, ensuring all columns are displayed
                pd.set_option('display.max_columns', 13)
                print(raw_data)
                display = input('Would you like to see more rows of the raw data? Input yes or no.\n').lower()
                # if input invalid, give the user another chance to input
                if display not in ('yes', 'no'):
                    print('Invalid option chosen.')
                    continue
                elif display == 'no':
                    break
        break
snapshot(df)