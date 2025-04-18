def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))   
    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}\n")
    
    print("Para la siguiente ecuación:")
    print(f"\tY = {A}X + {B}\n")
    
    print("Dados los siguientes puntos" )
    Y1 = A * X1 + B
    Y2 = A * X2 + B 
    print(f"\t P1 ({X1}, {A * X1 +B})")
    print(f"\t P2 ({X2}, {A * X2 +B})")
    
    dist = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5
    print(f"\n La distancia entre ellos es: {dist}")
