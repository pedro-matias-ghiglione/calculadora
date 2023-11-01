class SistemaCalculadora:

    def menu_principal(self):
        #Funcion para mostrar y elegir aopcion del Menu principal
        print("--------MENU--------")
        print("Elige una opcion:")
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicacion")
        print("4) Division")
        print("5) Ver el historial")
        print("6) Salir")
        
        #valida el ingreso de la opcion
        resp = False
        while resp ==  False:    
            try:
                resp = int(input())
                if resp < 1 or resp > 6:
                    resp = False
            except:
                print("Error en la opcion ingresada")
                resp = False

        if(resp == 1):
            resp = "suma"
        if(resp == 2):
            resp = "resta"
        if(resp == 3):
            resp = "multiplicacion"
        if(resp == 4):
            resp = "division"
        if(resp == 5):
            resp = "verhistorial"
        if(resp == 6):
            resp = "salir"
        return resp
    
    def mensaje_salida_sistema(self):
        #Mensaje de salida del sistema
        print("Gracias por utilizar la calculadora...")
    
    def mensaje_ingreso_parametro(self):
        #Mensaje de salida del sistema
        print("Ingrese un numero:")  

    def mensaje_resultado_operacion(self, operacion, resultado):
        #Mensaje de muestra del resultado en pantalla
        print(f"El resultado de {operacion} es: {resultado}")    
