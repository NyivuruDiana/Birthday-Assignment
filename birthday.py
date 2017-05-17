# A progam that request a one to input his/her date of birth,month of birth, and age then it computes the day he/she was born.
# Import the datetime module which avails the calender functions
import datetime
# Getting data from the client
Date_of_Birth=int(input("Input Your Date of Birth:\n "))
Month_of_Birth=int(input("Input Your Month of Birth:\n "))
Age=int(input("Input Your Age:\n "))
# Computing the current date and the total days one has lived
DateNow=datetime.datetime.now()
DaysPerYear=365
DaysLived=DaysPerYear*Age
DaysLived_in_Timedelta= datetime.timedelta(days=DaysLived)
# Calculating the year of birth in string format
Year_of_Birth=DateNow-DaysLived_in_Timedelta
# Converting the year of birth to integer data type
RealYear_of_Birth=int(Year_of_Birth.strftime("%Y"))
# Calculating the actual date of birth in calender format i.e. day/DD/MM/YY
ActualDate_of_Birth=datetime.date(RealYear_of_Birth,Month_of_Birth,Date_of_Birth)
# Printing the day on was born
print(ActualDate_of_Birth.strftime("%A"))

