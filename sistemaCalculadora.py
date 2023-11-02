class SistemaCalculadora:

    def menu_principal(self):
        # Funcion para mostrar y elegir aopcion del Menu principal
        print("--------MENU--------")
        print("Elige una opcion:")
        print("+) Suma")
        print("-) Resta")
        print("*) Multiplicacion")
        print("/) Division")
        print("1) Ver el historial")
        print("2) Salir")
        
        # valida el ingreso de la opcion
        resp = False
        while resp is False:
            try:
                resp = input("Ingrese opcion: ")
                # Verifica opcion ingresada
                if resp != "+" and resp != "-" and resp != "*" and resp != "/" and resp != "1" and resp != "2":
                    # opcion ingresada NO valida
                    resp = False
            except Exception:
                print("Error en la opcion ingresada")
                resp = False
        # Transforma la opcion en algo mas amigable
        if (resp == "+"):
            resp = "suma"
        if (resp == "-"):
            resp = "resta"
        if (resp == "*"):
            resp = "multiplicacion"
        if (resp == "/"):
            resp = "division"
        if (resp == "1"):
            resp = "verhistorial"
        if (resp == "2"):
            resp = "salir"
        return resp

    def mensaje_cierre_sistema(self):
        # Mensaje de salida del sistema
        print("Gracias por utilizar la calculadora...")

    def mensaje_ingreso_parametro(self):
        # Mensaje de salida del sistema
        print("Ingrese un numero:")

    def mensaje_resultado_operacion(self, operacion, resultado):
        # Mensaje de muestra del resultado en pantalla
        print(f"El resultado de {operacion} es: {resultado}")    

    def mensaje_salida_sistema(self):
        # Funcion para mostrar y elegir aopcion del Menu principal
        print("Desea salir del sistema? si/no")
        # valida el ingreso de la opcion
        opcion = None
        salir = False
        while opcion is None:
            try:
                # Ingreso de opcion
                opcion = input("Ingrese opcion: ")
                # valida datos
                if opcion != "si" and opcion != "no":
                    print("Solo puede ingresar si o no")
                    opcion = None
                else:
                    # Opcion validada. Por defecto esta en 'no', solo cambia si si la opcion en 'si'
                    if opcion == "si":
                        salir = True
            except Exception:
                print("Solo puede ingresar si o no")
                opcion = None
        return salir
