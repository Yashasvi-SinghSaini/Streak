import datetime
date_today = datetime.date.today()
def daychange(days_to_change): #THIS FUNCTION ADDS OR SUBSTRACTS GIVEN DAYS TO A DATE
    return date_today + datetime.timedelta(days_to_change)