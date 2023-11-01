import logging

logging.basicConfig(filename='calculadora.log', level=logging.INFO)

class Calculadora:
    #Clase para operaciones matematicas    

    def decorador_registro(method):
    # Registro de actividades en el LOG 
        def loggeo(*args, **kwargs):
            logger = logging.getLogger(method.__qualname__)
            logger.info(f"Argumentos: {args[1]},{args[2]} ")
            return method(*args, **kwargs)
        return loggeo
    
    @decorador_registro
    def sumar(self, num1, num2):
        #Suma de numeros
        resultado = num1 + num2
        return resultado
    
    @decorador_registro
    def restar(self, num1, num2):
        #Resta de numeros
        resultado = num1 - num2
        return resultado

    @decorador_registro
    def multiplicar(self, num1, num2):
        #Multiplicacion de numeros
        resultado = num1 * num2
        return resultado

    @decorador_registro
    def dividir(self, num1, num2):
        #Division de numeros
        try:
            resultado = num1 / num2
            return resultado
        except ZeroDivisionError:
            return "Error de division por cero"