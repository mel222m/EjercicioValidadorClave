from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneCaracterEspecialError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTienePalabraSecretaError, 

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada
    
    def _validar_longuitud(self, clave: str) -> bool:
        return len(clave) >= self._longitud_esperada

    def _contiene_mayuscula(self, clave: str)-> bool:
        for letra in clave:
            if letra.isupper():
                return True
            
        return False 

    def _contiene_minuscula(self, clave: str)-> bool:
        for letra in clave:
            if letra.islower():
                return True
            
        return False 
    
    def _contiene_numero(self, clave: str)-> bool:
        for letra in clave:
            if letra.isdigit():
                return True
            
        return False 
    
    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        ...

class ReglaValidacionGanimedes(ReglaValidacion):
    def _init_(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        for letra in clave:
            if letra in "_@$%":
                return True 
        
        return False 
    
    def es_valida(self, clave: str) -> bool:
        if not self._validar_longuitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longuitd de mas de 8 caracteres")

        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave debe tener al menos una letra en mayuscula")

        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave debe tener al manos una letra en minuscula")

        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave debe tener al menos un caracter especial como @_#%")

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe tener al menos un numero")

        return True
    
    class ReglaValidacionCalisto(ReglaValidacion):
        def _init_(self):
            super().__init__(longitud_esperada=6)

        def contiene_calisto(self, clave: str) -> bool:
            clave_tempo: str = clave.lower()
            palabra: str = "calisto" 
            clave_tempo.find()
            indice_calisto: int = 0 
            while (indice_caliso + len(palabra)) <= len(clave):
                indice_caliso = clave_tempo.find(palabra, indice_calisto)

                if indice_calisto >= 0:
                    pi = indice_caliso
                    pf = indice_caliso
                    palabra_original = clave[pi:pf]

                    contador_mayusculas = 0 
                    for letra in palabra_original:
                        if letra.isupper():
                            contador_mayusculas += 1 

                    if 2 <= contador_mayusculas < len(palabra):
                        return True 
                    
                    else:
                        indice_caliso += len(palabra)
                
                else:
                    return False 
            
            return False 



        def es_valida(self, clave: str) -> bool:
            if not self._validar_longuitud(clave):
                raise NoCumpleLongitudMinimaError("La clave debe tener al menos 6 caracteres")

            if not self._contiene_numero(clave):
                raise NoTieneNumeroError("La clave debe tener al menos un numero")

            if not self.contiene_calisto(clave):
                raise NoTienePalabraSecretaError("")        
            
            return True 
        
class Validador():
    pass
