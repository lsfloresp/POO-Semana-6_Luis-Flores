from models.dispositivo import Dispositivo


class Radio(Dispositivo):
    """
    Clase Radio.
    Hereda de la clase base Dispositivo.
    """

    def __init__(self, marca: str, frecuencia: str):
        # Llamada al constructor de la clase base
        super().__init__(marca)

        # Atributo propio de la Radio
        self.frecuencia = frecuencia

    def estado(self) -> str:
        """
        Método sobrescrito.
        Demuestra polimorfismo.
        """
        if self._encendido:
            return f"Radio {self.marca} en frecuencia {self.frecuencia} encendida"
        else:
            return f"Radio {self.marca} en frecuencia {self.frecuencia} apagada"
