def leapYear(input_data):
    if (input_data % 4 == 0):
        if(input_data % 100 == 0):
            if(input_data % 400 == 0):
                return "This is a leap year!"
            else:
                return "This is not a leap year!"
        else:
            return "This is a leap year!"
    else:
        return "This is not a leap year!"