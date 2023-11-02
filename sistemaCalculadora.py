"""Este modulo contiene las clases para utilizar y navegar por el programa"""


class SistemaCalculadora:
    """Sistema principal"""

    def menu_principal(self):
        """Funcion para mostrar y elegir aopcion del Menu principal"""
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
                if resp not in ("+", "-", "*", "/", "1", "2"):
                    # opcion ingresada NO valida
                    print("Error en la opcion ingresada")
                    resp = False
            except ValueError:
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
        """Mensaje de salida del sistema"""
        print("Gracias por utilizar la calculadora...")

    def mensaje_error_parametros(self):
        """Mensaje de error al ingresar parametros"""
        print("Parametros incorrectos...")

    def mensaje_ingreso_parametro(self):
        """Mensaje de salida del sistema"""
        print("Ingrese un numero:")

    def mensaje_resultado_operacion(self, operacion, resultado):
        """Mensaje de muestra del resultado en pantalla"""
        print(f"El resultado de {operacion} es: {resultado}")

    def muestra_historial(self, historial):
        """Mensaje de muestra del historial en pantalla"""
        for linea in historial:
            # Mostrar en pantalla el contenido del log
            print(linea, end='')

    def mensaje_salida_sistema(self):
        """Funcion para mostrar y elegir apcion del Menu principal"""
        print("Desea salir del sistema? si/no")
        # valida el ingreso de la opcion
        opcion = None
        salir = False
        while opcion is None:
            try:
                # Ingreso de opcion
                opcion = input("Ingrese opcion: ")
                # valida datos
                if opcion not in ["si", "no"]:
                    print("Solo puede ingresar si o no")
                    opcion = None
                else:
                    # Opcion validada. Por defecto esta en 'no', solo cambia si la opcion en 'si'
                    if opcion == "si":
                        salir = True
            except ValueError:
                print("Solo puede ingresar si o no")
                opcion = None
        return salir
