class Agencia:
    def __init__(self, nombre, direccion):
        self.nombre= nombre
        self.direccion= direccion
        self.colPaquetes= []
        self.colVentas= []
        
    def agregarPaquete(self, unPaquete):
        self.colPaquetes.append(unPaquete)
    
    