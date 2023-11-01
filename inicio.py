from calculadoraculadora import Calculadora
from sistemaCalculadora import SistemaCalculadora

#Inicializacion de clases de la aplicacion
calculadora = Calculadora()
sistemaCentral = SistemaCalculadora()

#Inicializacion de variables de la aplicacion
salir = False
opcion = False
parametro1=False
parametro2=False

#Bucle de sistema
while (salir == False):
    opcion = sistemaCentral.menu_principal()
    if opcion != "verhistorial" and opcion != "salir":
        #Ingreso de datos para el calculo
        sistemaCentral.mensaje_ingreso_parametro()
        parametro1 = int(input())
        sistemaCentral.mensaje_ingreso_parametro()
        parametro2 = int(input())

    if opcion == "suma":
        sistemaCentral.mensaje_resultado_operacion(opcion,calculadora.sumar(parametro1,parametro2))

    if opcion == "resta":
        sistemaCentral.mensaje_resultado_operacion(opcion,calculadora.restar(parametro1,parametro2))

    if opcion == "multiplicacion":
        sistemaCentral.mensaje_resultado_operacion(opcion,calculadora.multiplicar(parametro1,parametro2))

    if opcion == "division":
        sistemaCentral.mensaje_resultado_operacion(opcion,calculadora.dividir(parametro1,parametro2))

    if opcion == "verhistorial":
        pass
    
    if opcion == "salir":
        salir = True
        sistemaCentral.mensaje_salida_sistema()