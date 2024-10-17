from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada
    
    @abstractmethod
    def es_valida(self, clave: str)-> bool:
        pass 
    
    def _validar_longuitud(self, clave: str) -> bool:
        return len(clave) >= self._longitud_esperada

    def _contiene_mayuscula(self, clave: str)-> bool:
        return any(letra.isupper() for letra in clave)

    def _contiene_minuscula(self, clave: str)-> bool:
        return any(letra.islower() for letra in clave)

    def _contiene_numero(self, clave: str)-> bool:
        return any(letra.isdigit() for letra in clave)

class ReglaValidacionGanimedes:
    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = '@_#$%'
        return any(c in caracteres_especiales for c in clave)
    
class ReglaValidacionCalisto:
    def contiene_calisto(self, clave: str) -> bool:
        