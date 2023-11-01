import logging

logging.basicConfig(filename='calculadora.log', level=logging.INFO)

class Calculadora:
    #Clase para operaciones matematicas    
    
    #Decoradores
    # Registro de actividades en el LOG 
    def decorador_log(method):
        def loggeo(*args, **kwargs):
            #Primero genera el resultado de la opracion
            resultado = method(*args, **kwargs)
            #Guarda en log los parametros y el resultado
            logger = logging.getLogger()
            logger.info(f"La {method.__name__} de {args[1]}y {args[2]} es igual a {resultado}")
            return resultado
        return loggeo
    
    #Metodos
    @decorador_log
    def suma(self, num1, num2):
        #Suma de numeros
        try:
            resultado = num1 + num2
            return resultado
        except:
            return "Error al sumar"
    
    @decorador_log
    def resta(self, num1, num2):
        #Resta de numeros
        try:
            resultado = num1 - num2
            return resultado
        except:
            return "Error al restar"

    @decorador_log
    def multiplicacion(self, num1, num2):
        #Multiplicacion de numeros
        try:
            resultado = num1 * num2
            return resultado
        except:
            return "Error al multiplicar"

    @decorador_log
    def division(self, num1, num2):
        #Division de numeros
        try:
            resultado = num1 / num2
            return resultado
        except ZeroDivisionError:
            return "Error de division por cero"
        except:
            return "Error al dividir"