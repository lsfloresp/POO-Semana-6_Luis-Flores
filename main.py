from models.televisor import Televisor
from models.radio import Radio
from service.control_service import ControlService


def main():
    """
    Función principal del programa.
    Aquí se crean las instancias y se demuestra su funcionamiento.
    """

    # Creación de objetos (instancias)
    televisor = Televisor("Samsung", 55)
    radio = Radio("Sony", "FM")

    # Creación del servicio
    control = ControlService()

    # Encender los dispositivos
    televisor.encender()
    radio.encender()

    # Mostrar el estado usando polimorfismo
    control.mostrar_estado(televisor)
    control.mostrar_estado(radio)


# Punto de arranque del programa
if __name__ == "__main__":
    main()
