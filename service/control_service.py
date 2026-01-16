class ControlService:
    """
    Servicio encargado de manejar la lógica del sistema.
    No depende de un tipo específico de dispositivo.
    """

    def mostrar_estado(self, dispositivo):
        """
        Recibe cualquier objeto que herede de Dispositivo.
        Aquí se demuestra el polimorfismo.
        """
        print(dispositivo.estado())
