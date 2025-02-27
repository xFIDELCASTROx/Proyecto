hola este es mi proyecto para la univeridad espero que les guste 

print("bienvenido al sistema de venta de boletos de Laser Airlines")
print("por favor, seleccione una opción del menú: ")	

total_boletos_vendidos = 0
ingresos_primera = 0
ingresos_segunda = 0
ingresos_tercera = 0
ingresos_nacional = 0
ingresos_internacional = 0
servicios_adicionales = 0
precio_adicional_total = 0


while True:
    print("1. compra de boletos")
    print("2. ver sistema")
    print("3. salir")
    opcion = input("selecione una opción: ")
    if opcion == "1":
        num_boletos = int(input("número de boletos a vender: "))
        i = 0
        while i < num_boletos:
            nombre = input("nombre del pasajero: ")
            cedula_tipo = input("cédula de identidad (V - E): ")
            cedula_numero = input("número de cédula: ")
            edad = int(input("edad del pasajero: "))

            if edad < 18:
                print("solo se venden boletos a pasajeros mayores de 18 años.")
                continue

            print("seleccione la clase de boleto: ")
            print("1. primera clase")
            print("2. segunda clase")
            print("3. tercera clase")
            clase = input("clase: ")

            if clase == "3" and edad >= 60:
                print("los boletos de tercera clase no están disponibles para pasajeros mayores de 60 años.")
                continue

            tipo_boleto = input("tipo de boleto (N para nacional, I para internacional): ")
            origen = input("origen: ")
            destino = input("destino: ")
            ruta = origen + " - " + destino
            ida_y_vuelta = input("desea ida y vuelta? (S/N): ")

            adicional = input("requiere servicios adicionales? (S/N): ")
            precio = 100
            if adicional == "S":

                servicios_adicionales += 1
                precio_adicional = 0
                print("servicios adicionales:")
                print("1. comida - $10")
                print("2. bebida - $5")
                print("3. entretenimiento - $20")
                print("4. ninguno")
                while True:
                    servicio = input("seleccione un servicio adicional: ")
                    if servicio == "1":
                        precio_adicional = 10
                        break
                    elif servicio == "2":
                        precio_adicional = 5
                        break
                    elif servicio == "3":
                        precio_adicional = 20
                        break
                    elif servicio == "4":
                        break
                    else:
                        print("opción inválida. intente de nuevo.")
                precio_adicional_total += precio_adicional
                precio += precio_adicional

            if clase == "1":
                precio += 100
                ingresos_primera += precio
            elif clase == "2":
                precio += 70
                ingresos_segunda += precio
            elif clase == "3": 
                ingresos_tercera += precio
            if tipo_boleto == "N":
                ingresos_nacional += precio
            elif tipo_boleto == "I":
                ingresos_internacional += precio
            if edad < 12 or edad >= 50:
                precio *= 0.9

            total_boletos_vendidos += 1
            print(f"total a pagar por el boleto: ${precio:.2f}")
            pago = float(input("ingrese el monto de pago: "))
            if pago >= precio:
                print(f"vuelto: ${pago - precio:.2f}")
            else:
                print("monto insuficiente. no se puede completar la compra.")
                continue  

            i += 1

    elif opcion == "2":
        print("reporte del sistema:")
        print(f"total de boletos vendidos: {total_boletos_vendidos}")
        print(f"ingresos por primera clase: ${ingresos_primera}")
        print(f"ingresos por segunda clase: ${ingresos_segunda}")
        print(f"ingresos por tercera clase: ${ingresos_tercera}")
        print(f"ingresos por boletos nacionales: ${ingresos_nacional}")
        print(f"ingresos por boletos internacionales: ${ingresos_internacional}")
        print(f"número de servicios adicionales solicitados: {servicios_adicionales}")

    elif opcion == "3":
        break

    else:
        print("oción incorrecta. Intente nuevamente.")

