def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente de la ecuación de la recta es: {A}")
    print(f"El coeficiente de la ecuación de la recta es: {B}")
    print(f"El coeficiente de la ecuación de la recta es: {X1}")
    print(f"El coeficiente de la ecuación de la recta es: {X2}")
    print("Para la siguiente ecuacion:")
    print(f"\tY = {A}X + {B}\n")
    print("Dados los siguientes puntos" )
    Y1 = A * X1 +B
    Y2 = A * X2 +B
    dist = ((X2 - X1)**2 + (Y2-Y1)**2)**0.5 
    print(f"\t P1 ({X1}, {A * X1 +B})")
    print(f"\t P2 ({X2}, {A * X2 +B})")
    
    print(f"\t La distancia entre ellos es: {dist}")
