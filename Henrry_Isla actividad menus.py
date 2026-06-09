deuda = 100000
repeticion = True

while repeticion:
    print("\n--- MENÚ ---")
    print("1. Pago tarjeta de crédito")
    print("2. Simulación de compras")
    print("3. Salir")
    
    try:
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            pago = float(input("Ingrese el monto a pagar: "))
            if pago < 0:
                print("Error. El monto debe ser mayor o igual a 0.")
            elif pago > deuda:
                print("Error. El pago no puede ser mayor a la deuda.")
            else:
                deuda -= pago
                print(f"Pago exitoso. La deuda actual es de: ${deuda}") 
                
        elif opcion == 2:
            cant_compra = int(input("Ingresa la cantidad de compras a simular: "))
            if cant_compra <= 0:
                print("Error. La cantidad de compras debe ser mayor a 0.")
            else:
                total_compras = 0 
                
                for i in range(cant_compra):
                   
                    valor = float(input(f"Ingresa el valor de la compra nro {i + 1}: "))
                    total_compras += valor 
                 
                deuda_simulada = deuda + total_compras
                print(f"Simulación registrada. La deuda si las compras se realizan sería de: ${deuda_simulada}")
                
                
        elif opcion == 3:
            print("Saliendo del sistema...")
            repeticion = False 
            
        else:
            print("Opción inválida. Por favor ingresa 1, 2 o 3.")
            
    except ValueError:
        print("Error. Ingresa un valor numérico válido.")