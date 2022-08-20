from ventas import Ventas
from destino import Destino
from paquete import Paquete

class VentaOnLine:
    def __init__(self, fecha,paquete, cantPersona, cliente, porcDescuento):
        super.__init__(fecha,paquete, cantPersona, cliente)
        self.porcDescuento= porcDescuento
        
    def darImporteVenta(self, cantPersona:Ventas, valorxdia:Destino, cantidadDias:Paquete):
        importe= cantPersona * valorxdia * cantidadDias * self.porcDescuento
        