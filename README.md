>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date Created
7-Apr-2024

### Bikeshare Analysis

### Description
The Bikeshare Analysis project ingests csv files (_see 'Files Used' section_) to compute the various **statistics** from bikeshare data.

This is an **interactive experience** for the user, allowing the user to filter by:
* city (_Chicago_, _New York City_, _Washington_)
* time frequency (_month_, _day_, _neither_)
* time period (_January_ to _June_ if month is chosen, day of week if day is chosen)

The following statistics are computed with the chosen filtered data:
1. Popular times of travel
2. Popular stations and trip
3. Trip duration
4. User information

Lastly, the user is asked if they would like to see a **snapshot** of the raw data. This shows the data in **5-row incrememnts** as long as the user continues to request it.

### Files Used
* chicago.csv
* new_york_city.csv
* washington.csv
    * NOTE: fields _Gender_ and _Birth Year_ are not available in washington.csv, so some user information cannot be calculated.


