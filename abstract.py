from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada
    
    @abstractmethod
    def es_valida(self, clave):
        pass 
    
    def _validar_longuitud(self):
        pass 

    def _contiene_mayuscula(self, clave:str):
        return clave.isupper() 

    def _contiene_minuscula(self):
        pass 

    def _contiene_numero(self):
        pass 
