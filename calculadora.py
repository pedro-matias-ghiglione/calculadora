"""
      Este modulo contiene las operaciones matematicas para realizar. Tambien 
      muestra el historial.
"""
import logging


class Calculadora:
    """Clase para operaciones matematicas"""
    # Constructor
    def __init__(self):
        self.archivolog = "calculadora.log"
        logging.basicConfig(filename=self.archivolog, level=logging.INFO)

    # Decoradores
    def decorador_log(method):
        """Registro de actividades en el LOG"""
        def loggeo(*args, **kwargs):
            # Primero genera el resultado de la opracion
            resultado = method(*args, **kwargs)
            # Guarda en log los parametros y el resultado
            logger = logging.getLogger()
            logger.info(f"La {method.__name__} de {args[1]}y {args[2]} es igual a {resultado}")
            return resultado
        return loggeo

    # Metodos
    @decorador_log
    def suma(self, num1, num2):
        """Suma de dos numeros"""
        try:
            resultado = num1 + num2
            return resultado
        except ValueError:
            return "Error al sumar"

    @decorador_log
    def resta(self, num1, num2):
        """Resta de dos numeros"""
        try:
            resultado = num1 - num2
            return resultado
        except ValueError:
            return "Error al restar"

    @decorador_log
    def multiplicacion(self, num1, num2):
        """Multiplicacion de dos numeros"""
        try:
            resultado = num1 * num2
            return resultado
        except ValueError:
            return "Error al multiplicar"

    @decorador_log
    def division(self, num1, num2):
        """Division de dos numeros"""
        try:
            resultado = num1 / num2
            return resultado
        except ZeroDivisionError:
            return "Error de division por cero"
        except ValueError:
            return "Error al dividir"

    def verhistorial(self):
        """Muestra el archivo log en pantalla"""
        with open(self.archivolog, 'r',encoding="utf-8") as archivolog:
            lineas = archivolog.readlines()
        return lineas
