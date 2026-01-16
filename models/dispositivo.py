class Dispositivo:
    """
    Clase base Dispositivo.
    Representa un dispositivo electrónico genérico.
    Aplica encapsulación y sirve como base para herencia.
    """

    def __init__(self, marca: str):
        # Atributo público: puede ser accedido por clases hijas
        self.marca = marca

        # Atributo protegido (encapsulación)
        # El guion bajo indica que no debe accederse directamente
        self._encendido = False

    def encender(self):
        """
        Método para encender el dispositivo
        """
        self._encendido = True

    def apagar(self):
        """
        Método para apagar el dispositivo
        """
        self._encendido = False

    def estado(self) -> str:
        """
        Método que será sobrescrito por las clases hijas.
        Aquí se aplica el concepto de polimorfismo.
        """
        if self._encendido:
            return "Dispositivo encendido"
        else:
            return "Dispositivo apagado"
