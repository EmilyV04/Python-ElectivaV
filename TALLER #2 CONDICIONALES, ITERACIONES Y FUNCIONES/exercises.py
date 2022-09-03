option = 0 # OPCION DEL EJERCICIO
exit = 2   # 1 (SALIR) - 2 (REPETIR MENU)

msj_menu = '''           
    ---------- MENU ----------

1. Números pares
2. Números triangulares
3. Números triangulares (versión funciones)
4. Costo de llamadas
5. Convertidor de dinero
6. Organizar números

Ingrese un número para acceder a un ejercicio: '''

msj_question = '''
Desea salir?
1. Si (Finalizar programa)
2. No (Volver al Menú)

Opción: '''

while exit == 2:
    option = int(input(msj_menu))
    
    if option == 1:
        print("\nNÚMEROS PARES\n")
        
        def num_par(num1,num2):
            for i in range(num1, num2 + 1, 1):
                if i % 2 == 0:
                    print(i)

        a = 0
        while a == 0:
            try:       
                num1 = int(input("Ingrese un número: "))
                num2 = int(input("Ingrese otro número: "))
                num_par(num1, num2)
                a += 1
            except:
                print("Número inválido. Intente nuevamente...")
        
    elif option == 2:
        print("\nNÚMEROS TRIANGULARES\n")
        num = int(input("Ingrese un número: "))
        contador = 0

        for i in range(1, num + 1, 1):
            #print(i, " --> ", contador + i)
            print(f"{i} --> {contador + i}")
            contador += i
        
    elif option == 3:
        print("\nNÚMEROS TRIANGULARES (VERSIÓN FUNCIONES)\n")
        
        def num_triangular(n, a):
            for x in range(1, n + 1, 1):
                # print(x, " --> ", a + x)
                print(f"{x} --> {a + x}")
                a += x
   
        num = int(input("Ingrese un número: "))
        cont = 0
        num_triangular(num, cont)
        
    elif option == 4:
        print ("\nCOSTO DE LLAMADAS")
        
        def calculo_segundos(hr,min,seg):
            calseg = (hr * 3600) + (min * 60) + seg
            return calseg
        
        precio   = float(input("Ingrese la tarifa por segundo: "))
        llamadas = int(input("Ingrese el número de llamadas realizadas: "))

        for x in range(llamadas):
            print(f"\nLLAMADA {x + 1}")
            hr  = int(input("¿Cuántas horas? "))
            min = int(input("¿Cuántos minutos? "))
            seg = int(input("¿Cuántos segundos? "))
            calseg = calculo_segundos(hr,min,seg)
            costo  = calseg * precio
            print(f"Duración: {calseg} en segundos \nCosto: {costo}")
        
    elif option == 5:
        print("\nCONVERTIDOR DE DINERO\n")
        
        def convertidor(n):
            dolar = n / 4396.84
            euro = n / 4413.11
            bit = n / 93140523.69
            
            print("\nLa cifra ingresada es igual a: \nUS$ "
            ,dolar, " en Dolares\n  € "
            ,euro, " en Euros\n  ฿ "
            ,bit, "en Bitcoins")

        pesos_col = float(input("Ingrese la cifra en pesos colombianos: "))
        convertidor(pesos_col)             
        
    elif option == 6:
        print("\nORGANIZAR NÚMEROS\n")
        
        def organizar(a, b, c):
            if a < b and b < c :
                print("Orden :",a," - ",b," - ",c)
            elif b < a and a < c :
                print("Orden :",b," - ",a," - ",c)
            elif a < c and c < b :
                print("Orden :",a," - ",c," - ",b)
            elif c < a and a < b :
                print("Orden :",c," - ",a," - ",b)
            elif b < c and c < a :
                print("Orden :",b," - ",c," - ",a)
            elif c < b and b < a :
                print("Orden :",c," - ",b," - ",a)
            
        a = 0
        while a == 0:
            try:       
                num1 = int(input("Ingrese el primer número: "))
                num2 = int(input("Ingrese el segundo número: "))
                num3 = int(input("Ingrese el tercer número: "))
                organizar(num1, num2, num3)
                a += 1
            except:
                print("Número inválido. Intente nuevamente...")
    
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
    





