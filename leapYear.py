def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else: 
                return False
        else: 
            return True
    else: 
        return False

isLeapYear(2020)
isLeapYear(2000)
isLeapYear(1900)
isLeapYear(1500)
isLeapYear(1893)