"""
    Programa principal
"""

from calculadora import Calculadora
from sistemaCalculadora import SistemaCalculadora

# Inicializacion de clases de la aplicacion
calculadora = Calculadora()
sistemaCentral = SistemaCalculadora()

# Inicializacion de variables de la aplicacion
salir = False
opcion = False
parametro1 = False
parametro2 = False

# Bucle de sistema
while salir is False:

    opcion = sistemaCentral.menu_principal()
    # Ingreso de datos para el calculo
    if opcion != "verhistorial" and opcion != "salir":
        sistemaCentral.mensaje_ingreso_parametro()
        try:
            parametro1 = int(input())
            sistemaCentral.mensaje_ingreso_parametro()
            parametro2 = int(input())
        except ValueError:
            sistemaCentral.mensaje_error_parametros()
            salir = False
            opcion = "error"
    try:
        if opcion == "suma":
            sistemaCentral.mensaje_resultado_operacion(opcion, calculadora.suma(parametro1, parametro2))
            # Pregunta si quiere salir del sistema
            salir = sistemaCentral.mensaje_salida_sistema()

        if opcion == "resta":
            sistemaCentral.mensaje_resultado_operacion(opcion, calculadora.resta(parametro1, parametro2))
            # Pregunta si quiere salir del sistema
            salir = sistemaCentral.mensaje_salida_sistema()

        if opcion == "multiplicacion":
            sistemaCentral.mensaje_resultado_operacion(opcion, calculadora.multiplicacion(parametro1, parametro2))
            # Pregunta si quiere salir del sistema
            salir = sistemaCentral.mensaje_salida_sistema()

        if opcion == "division":
            sistemaCentral.mensaje_resultado_operacion(opcion, calculadora.division(parametro1, parametro2))
            # Pregunta si quiere salir del sistema
            salir = sistemaCentral.mensaje_salida_sistema()

        if opcion == "verhistorial":
            sistemaCentral.muestra_historial(calculadora.verhistorial())
            # Pregunta si quiere salir del sistema
            salir = sistemaCentral.mensaje_salida_sistema()

        if opcion == "salir":
            # Vuelve a preguntar si quiere salir del sistema
            salir = sistemaCentral.mensaje_salida_sistema()
    except ValueError:
        salir = False

sistemaCentral.mensaje_cierre_sistema()
