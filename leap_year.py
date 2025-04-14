def leap_year():
    year = int(input ("Ingrese un año: "))
    if(year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)):
		print(f"el año {year} es bisiesto")
    else:
		print(f"El año {yeat} no es bisiesto")
