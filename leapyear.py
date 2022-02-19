def leap_year(year):
    year_string = str(year)
    if year_string[-2:] == '00':
        century_year = int(year_string)
        if century_year % 400 == 0:
            return 'leap year!'
        else :
            return 'Not leap year'
    else:
        not_century = int(year_string)
        if not_century % 4 == 0:
            return 'leap year!'
        else:
            return 'Not leap year'


        


# year_string = str(1100)
# print(year_string[-2:])
print(leap_year(2010))
