import math

option = 0 # OPCION DEL EJERCICIO
exit = 2   # 1 (SALIR) - 2 (REPETIR MENU)

pi = math.pi

msj_menu = '''           
    ---------- MENU ----------

1. Saludo personalizado
2. Producto de dos números
3. Perímetro y área de un rectángulo
4. Perímetro y área de un círculo
5. Volumen de una esfera
6. Operaciones aritméticas de dos números
7. Factorial de un número
8. Convertidor de dinero
9. Cálculo de Índice de Masa Corporal (IMC)
10.Convertidor de temperatura

Ingrese un número para acceder a un ejercicio: '''

msj_question = '''
Desea salir?
1. Si (Finalizar programa)
2. No (Volver al Menú)

Opción: '''

while exit == 2:
    option = int(input(msj_menu))
    
    if option == 1:
        print("\nSALUDO PERSONALIZADO\n")
        name = input("¿Cúal es tu nombre? ")
        print(f"Hola, {name}!")
        
    elif option == 2:
        print("\nPRODUCTO DE DOS NÚMEROS\n")
        num1 = float(input("Ingresa un numero: "))
        num2 = float(input("Ingresa otro numero: "))
        #mult = num1 * num2
        print(f"\nEl producto total es: {num1 * num2}")
        
    elif option == 3:
        print("\nPERÍMETRO Y ÁREA DE UN RECTÁNGULO\n")
        base = float(input("Ingrese el valor de la base: "))
        altura = float(input("Ingrese el valor de la altura: "))

        perimetro_rec = (base * 2) + (altura * 2)
        area_rec = base * altura

        print(f"\nEl perímetro del rectángulo es {perimetro_rec}")
        print(f"El área del rectángulo es {area_rec}")
        # print(f'''
        # El perímetro del rectángulo es {perimetro}
        # El área del rectangulo es {area}''')
        
    elif option == 4:
        print ("\nPERÍMETRO Y ÁREA DE UN CÍRCULO")
        radio_cir = float (input("Ingrese el radio del círculo: "))
        area_cir = pi * (radio_cir ** 2)
        perimetro_cir = 2 * pi * radio_cir

        print(f"\nEl perímetro del círculo es {perimetro_cir}")
        print(f"El área del círculo es {area_cir}")
        
    elif option == 5:
        print("\nVOLUMEN DE UNA ESFERA\n")
        radio_esf = float(input("Ingrese el valor del radio de la esfera en cms: "))
        volumen = (4/3) * pi * (radio_esf ** 3)
        
        print(f"El volumen de la esfera es {volumen}")
        
    elif option == 6:
        print("\nOPERACIONES ARITMÉTICAS DE DOS NÚMEROS\n")
        valor1 = float(input("Ingresa un numero: "))
        valor2 = float(input("Ingresa otro numero: "))
        
        print(f"\nLa suma es {valor1 + valor2}")
        print(f"La resta es {valor1 - valor2}")
        print(f"La división es {valor1 / valor2}")
        print(f"La multiplicación es {valor1 * valor2}")
        
    elif option == 7:
        print("\nFACTORIAL DE UN NÚMERO\n")
        num = int(input("Ingrese un numero: "))
        fact = 1
        while num != 0:
            fact *= num
            num -= 1
            
        print(f"El factorial es {fact}")
        
    elif option == 8:
        print("\nCONVERTIDOR DE DINERO\n")
        pesos_col = float(input("Ingrese la cifra en pesos colombianos: "))
        dolar = pesos_col / 4396.84
        euro = pesos_col / 4413.11
        bit = pesos_col / 93140523.69

        print("\nLa cifra ingresada es igual a: \nUS$ "
            ,dolar, " en Dolares\n  € "
            ,euro, " en Euros\n  ฿ "
            ,bit, "en Bitcoins")
        
    elif option == 9:
        print("\nCÁLCULO DE ÍNDICE DE MASA CORPORAL (IMC)\n")
        peso = float(input("Ingrese su peso en Kg: "))
        est = float(input("Ingrese su estatura en Mts: "))
        imc = peso / (est ** 2)

        print(f"\nSu Índice de Masa Corporal es {imc}")
        
    elif option == 10:
        print("\nCONVERTIDOR DE TEMPERATURA\n")
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahren = (celsius * (9/5) + 32)
        kelvin = celsius + 273.15

        print("\nLa temperatura ingresada equivale a: \n"
            ,fahren, " en Fahrenheit\n"
            ,kelvin, " en Kelvin")
    
    while exit != 1 or exit != 2:
        exit = int(input(msj_question))
        
        if exit == 1:
            print('---------- BYE BYE :) ----------')
            break
        if exit == 2:
            break
        else:
            print('Opción inválida. Intente nuevamente...')
            continue
    





