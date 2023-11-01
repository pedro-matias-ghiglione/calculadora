from calculadora import Calculadora
from sistemaCalculadora import SistemaCalculadora

#Inicializacion de clases de la aplicacion
cal = Calculadora()
siscal = SistemaCalculadora()

#Inicializacion de variables de la aplicacion
salir = False
opcion = False
parametro1=False
parametro2=False

#Sistema
while (salir == False):
    opcion = siscal.menu_principal()
    if opcion != "verhistorial" and opcion != "salir":
        #Ingreso de datos para el calculo
        siscal.mensaje_ingreso_parametro()
        parametro1 = int(input())
        siscal.mensaje_ingreso_parametro()
        parametro2 = int(input())

    if opcion == "suma":
        siscal.mensaje_resultado_operacion(opcion,cal.sumar(parametro1,parametro2))

    if opcion == "resta":
        siscal.mensaje_resultado_operacion(opcion,cal.restar(parametro1,parametro2))

    if opcion == "multiplicacion":
        siscal.mensaje_resultado_operacion(opcion,cal.multiplicar(parametro1,parametro2))

    if opcion == "division":
        siscal.mensaje_resultado_operacion(opcion,cal.dividir(parametro1,parametro2))

    if opcion == "verhistorial":
        pass
    
    if opcion == "salir":
        salir = True
        siscal.mensaje_salida_sistema()