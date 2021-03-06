"""A vaccination calculator."""

__author__ = "730320065"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population = int (input ("Population: "))
doses_administered = int (input ("Doses administered: "))
doses_per_day = int (input ("Doses per day: "))
target_percent_vaccinated = int (input ("Target percent vaccinated: "))
days_until_completion = int ((((population * (target_percent_vaccinated / 100)) - (doses_administered / 2)) / (doses_per_day / 2)))

today: datetime = datetime.today()
completed: datetime = today + timedelta(days_until_completion)


print("We will reach " + str(target_percent_vaccinated) + "%" + " vaccinated in " + str(days_until_completion) + " days, which falls on " + str(completed.strftime("%B %d, %Y")) + ".") 