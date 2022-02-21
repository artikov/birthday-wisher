import pandas
import datetime as dt
import smtplib
import random
from private import *

my_email = MY_EMAIL
password = PASSWORD

# -------------------- Get Today's dates ----------------------- #
currentDay = dt.datetime.now().day
currentMonth = dt.datetime.now().month
currentYear = dt.datetime.now().year


# -------------------- Get dates from database ----------------------- #
data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict(orient='records')


# -------------------- Function to send email ----------------------- #


def send_email(letter_to_send):
    with smtplib.SMTP_SSL(host='smtp.gmail.com') as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=RECIPIENT,
            msg=f"Subject:Happy Birthday Dear!!!\n\n{letter_to_send}"
        )


# -------------------- Check if today someone's birthday ----------------------- #

for n in data_dict:
    if n['day'] == currentDay and n['month'] == currentMonth:
        age = currentYear - n['year']
        # if birthday, pick one letter and replace placeholders
        random_letter = f'letter_templates/letter_{random.randint(1, 3)}.txt'
        with open(f'{random_letter}') as letter_data:
            letter = letter_data.read()
            letter = letter.replace('[NAME]', f'{n["name"]}').replace('[AGE]', f'{age}')
            send_email(letter)



