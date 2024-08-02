convert_from = input('Enter unit of measurement to convert from (feet,inches,yards): ' )

convert_to = input('Enter unit of measurement to convert to (feet,inches,yards): ' )



if convert_from.lower() in ['inches', 'inch', 'INCH', 'in', 'IN', 'i']:
    number_of_inches = int(input('Enter the number of inches to convert: '))
    if convert_to.lower() in ['feet', 'ft', 'FEET', 'f']:
         print('Result:','Inches: ', number_of_inches,'feet: ' ,round(number_of_inches/12,2))
    elif convert_to.lower() in ['yards', 'yard', 'yd', 'yrd', 'y']:
        print( 'Result:','inches: ', number_of_inches, 'yards: ', round(number_of_inches/36,2) )
    elif convert_from.lower() in ['inches', 'inch', 'INCH', 'in', 'IN', 'i']:
        print('Result:','Inches: ', number_of_inches,'Inches: ' ,number_of_inches)
    else:
        print('Please input the right measurement')
elif convert_from.lower() in ['feet', 'ft', 'FEET', 'f']:
    number_of_feet = int(input('Enter the number of feet to convert: '))
    if convert_to.lower() in ['inches', 'inch', 'INCH', 'in', 'IN', 'i']:
         print('Result:', 'Feet: ', number_of_feet, 'inches: ', number_of_feet*12)
    elif convert_to.lower() in ['yards', 'yard', 'yd', 'yrd', 'y']:
        print('Result:', 'feet: ', number_of_feet, 'yards: ', round(number_of_feet/3,2) )
    elif convert_from.lower() in ['feet', 'ft', 'FEET', 'f']:
        print('Result:','feet: ', number_of_feet,'feet: ', number_of_feet)
    else:
        print('Please input the right measurement')
elif convert_from.lower() in ['yards', 'yard', 'yd', 'yrd', 'y']:
    number_of_yards = int(input('Enter the number of feet to convert: '))
    if convert_to.lower() in ['inches', 'inch', 'INCH', 'in', 'IN', 'i']:
         print('Result:', 'yards: ', number_of_yards, 'inches: ', number_of_yards*36)
    elif convert_to.lower() in ['feet', 'ft', 'FEET', 'f']:
        print('Result:', 'yards: ', number_of_yards, 'feet: ', number_of_yards*3)
    elif convert_from.lower() in ['yards', 'yard', 'yd', 'yrd', 'y']:
        print('Result:', 'yards: ', number_of_yards, 'yards: ', number_of_yards)
    else:
        print('Please input the right measurement')


else:
    print('please input either inches or feet or yards')