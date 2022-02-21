import pandas
import datetime as dt
import smtplib
import random

# -------------------- Get Today's dates ----------------------- #
currentDay = dt.datetime.now().day
currentMonth = dt.datetime.now().month
currentYear = dt.datetime.now().year


# -------------------- Get dates from database ----------------------- #

# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict(orient='records')

print(data_dict)

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




