class WeekDayError(Exception):
    pass

class Weeker:
    
    weeklist=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    def __init__(self, day):
        if day in Weeker.weeklist:
            self.__weekday = day
            self.__weeknum = Weeker.weeklist.index(day)
        else:
            raise WeekDayError

    def __str__(self):
        return Weeker.weeklist[self.__weeknum]

    def add_days(self, n):
        self.__weeknum+=n
        self.__weeknum%=7

    def subtract_days(self, n):
        self.__weeknum=(self.__weeknum+(7-n%7))%7

try:
    weekday = Weeker('Sun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")