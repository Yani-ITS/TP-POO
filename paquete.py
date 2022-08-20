class Paquete():
    def __init__(self, fechaDesde, cantidadDias, destino, cantTotalPlazas):
        self.fechaDesde= fechaDesde
        self.cantidadDias= cantidadDias
        self.destino= destino
        self.cantTotalPlazas= cantTotalPlazas
        self.cantPlazasDisponibles = self.cantTotalPlazas