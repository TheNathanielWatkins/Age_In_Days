# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

import time

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

special_message = " "

def isLeapYear(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    else:
        return True

def calc_1st_year(y1,m1,d1):
    first_days = 0
    if m1 <= 2:
        if isLeapYear(y1) is True:
            first_days +=1
    first_days = first_days + sum(daysOfMonths[m1-1:]) - d1
    return first_days

def calc_this_year(y2,m2,d2):
    current_days = 0
    if m2 > 2:
        if isLeapYear(y2) is True:
            current_days += 1
    current_days = current_days + sum(daysOfMonths[0:m2-1]) + d2
    return current_days

def calc_whole_years(y1, y2):
    year_days = 0
    if (y2) > (y1 + 1):
        for i in range(y1+1,y2):
            if isLeapYear(i) is True:
                year_days += 366
            else:
                year_days += 365
    else:
        year_days = 0
    return year_days

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    if (y1 <= 0) or (m1 <= 0) or (d1 <= 0) or (y2 <= 0) or (m2 <= 0) or (d2 <= 0):
        if y1 <= 0:
            return "Hey!  What's the big idea?!  You should know that's not how dates are formatted.  Check the birthYEAR and try again."
        if m1 <= 0:
            return "Hey!  What's the big idea?!  You should know that's not how dates are formatted.  Check the birthMONTH and try again."
        if d1 <= 0:
            return "Hey!  What's the big idea?!  You should know that's not how dates are formatted.  Check the birthDAY and try again."
        if y2 <= 0:
            return "Hey!  What's the big idea?!  You should know that's not how dates are formatted.  Check the current YEAR and try again."
        if m2 <= 0:
            return "Hey!  What's the big idea?!  You should know that's not how dates are formatted.  Check the current MONTH and try again."
        if d2 <= 0:
            return "Hey!  What's the big idea?!  You should know that's not how dates are formatted.  Check the current DAY and try again."
    if (daysOfMonths[m1-1] < d1) and not (isLeapYear(y1) is True and m1 == 2 and d1 == 29):
        if isLeapYear(y1) is True and m1 == 2 and d1 > 29:
            return "Sorry, there seems to be an issue with the day that you entered. Birthday could not possibly be {0} since {1}/{2} only has 29 days in it.".format(d1,m1,y1)
        return "Sorry, there seems to be an issue with the day that you entered. Birthday could not possibly be {0} since {1}/{2} only has {3} days in it.".format(d1,m1,y1,daysOfMonths[m1-1])
    if (daysOfMonths[m2-1] < d2) and not (isLeapYear(y2) is True and m2 == 2 and d2 == 29):
        if isLeapYear(y2) is True and m2 == 2 and d2 > 29:
            return "Sorry, there seems to be an issue with the day that you entered. Current day could not possibly be {0} since {1}/{2} only has 29 days in it.".format(d2,m2,y2)
        return "Sorry, there seems to be an issue with the day that you entered. Current day could not possibly be {0} since {1}/{2} only has {3} days in it.".format(d2,m2,y2,daysOfMonths[m2-1])
    if (y1 == y2) and (m1 == m2) and (d1 == d2):
        special_message = "Thank your mother because you were just born today!"
        return 0
    if (m1 == m2) and (d1 == d2):
        special_message = "Happy Birthday!! You're now {0} years old!".format(y2-y1)
    if y1 > y2:
        return "Sorry, there seems to be an issue with the years that you entered. Birthyear cannot be after the current year. ...unless you're some kind of Time Lord."
    if y1 == y2:
        if m1 == m2:
            return d2 - d1
        if m1 + 1 == m2:
            if m1 == 2 and isLeapYear(y1) is True:
                return (29 - d1) + d2 #since Feb has 29 days in a leap year
            else:
                return (daysOfMonths[m1-1] - d1) + d2
        if m1 > m2:
            return "Sorry, there seems to be an issue with the months (or years) that you entered. Birthmonth cannot be after the current month. Unless... You'd tell me if you were a time traveler, right?"
        else:
            if isLeapYear(y1) is True:
                if m1 <= 2 and m2 >2:
                    days += 1
            return days + sum(daysOfMonths[m1:m2-1]) + d2 + (daysOfMonths[m1-1] - d1)
    if y2 == y1 + 1:
        return calc_1st_year(y1,m1,d1) + calc_this_year(y2,m2,d2)
    if y2 > y1 + 1:
        return calc_1st_year(y1,m1,d1) + calc_whole_years(y1,y2) + calc_this_year(y2,m2,d2)
    else:
        return "Congratulations! You win. You've found some inputs that I didn't plan for (and somehow they didn't cause an error). Let me know how you did it. K THX BYE"

print "Ready to find out how many day's you've been alive?  Please input your birthdate then the current date in this format: YYYY,MM,DD"

while True:
	try:
		y1 = int(input("Enter Birth Year > "))
		if y1 > 0:
		    break
	except:
		print("The year needs to be a positive whole number")
while True:
	try:
		m1 = int(input("Enter Birth Month > "))
		if (m1 >= 1) and (m1 <= 12):
		    break
	except:
		print("The month needs to be a whole number between 1 and 12")
while True:
    try:
        d1 = int(input("Enter Birth Day > "))
        if (d1 >= 1) and (d1 <= 31):
            break
    except:
		print("The day needs to be a whole number between 1 and 31")

print "Today's date (formatted YYYY,MM,DD) is " + (time.strftime("%Y,%m,%d"))
toggle = True
answer = " "
while toggle:
    answer = input("Would you like to auto-input today's date? [Y/N] If no, you'll be prompted to enter the current date. > ")
    # answer = answer.lower()
    # print answer
    if (answer.lower() == "y") or (answer.lower() == "yes") or (answer.lower() == "yeah") or (answer.lower() == "sure") or (answer.lower() == "affirmative") or (answer.lower() == "yup") or (answer.lower() == "okay") or (answer.lower() == "ok"):
        y2 = time.strftime("%Y")
        m2 = time.strftime("%m")
        d2 = time.strftime("%d")
        toggle = False
    elif (answer.lower() == "n") or (answer.lower() == "no") or (answer.lower() == "nah") or (answer.lower() == "nope") or (answer.lower() == "negative") or (answer.lower() == "nix"):
        while True:
            try:
                y2 = int(input("Enter Current Year > "))
                if y2 > 0:
                    break
            except:
        		print("The year needs to be a positive whole number")
        while True:
        	try:
        		m2 = int(input("Enter Current Month > "))
        		if (m2 >= 1) and (m1 <= 12):
        		    break
        	except:
        		print("The month needs to be a whole number between 1 and 12")
        while True:
            try:
                d2 = int(input("Enter Current Day > "))
                if (d2 >= 1) and (d1 <=31):
                    break
            except:
        		print("The day needs to be a whole number between 1 and 31")
        toggle = False
    else:
        print 'Your response was not recognized as a "Yes" or "no", please try again.'

daysBetweenDates(y1,m1,d1,y2,m2,d2)
print special_message
print "Congratulations! You've now been alive for a whoping {0} days!".format(daysBetweenDates(y1,m1,d1,y2,m2,d2))
