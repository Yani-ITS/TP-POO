from paquete import Paquete
from destino import Destino
from ventas import Ventas

class VentaAgencia:
    def __init__(self, fecha, paquete, cantPersona, cliente):
        super.__init__(fecha, paquete, cantPersona, cliente)
        
    def darImporteVenta(cantPersona:Ventas, valorxdia:Destino, cantidadDias:Paquete):
        importe= cantPersona * valorxdia * cantidadDias
        return importe
    