from datetime import datetime

def days_substraction(date1, date2):
    format_date1 = datetime.strptime(date1, '%Y-%m-%d')
    format_date2 = datetime.strptime(date2, '%Y-%m-%d')

    substraction = format_date1 - format_date2

    if substraction.days < 0:
        print(abs(substraction.days))
    else:
        return substraction.days