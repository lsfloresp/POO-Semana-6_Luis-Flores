from models.dispositivo import Dispositivo


class Televisor(Dispositivo):
    """
    Clase Televisor.
    Hereda de la clase base Dispositivo.
    """

    def __init__(self, marca: str, pulgadas: int):
        # Llamada al constructor de la clase base (herencia)
        super().__init__(marca)

        # Atributo propio del Televisor
        self.pulgadas = pulgadas

    def estado(self) -> str:
        """
        Método sobrescrito.
        Aplica polimorfismo: mismo método, diferente comportamiento.
        """
        if self._encendido:
            return f"Televisor {self.marca} de {self.pulgadas} pulgadas encendido"
        else:
            return f"Televisor {self.marca} de {self.pulgadas} pulgadas apagado"
