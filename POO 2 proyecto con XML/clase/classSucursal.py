from clase.classCategoria import Categoria
class Sucursal:
    def __init__(self, nombresucursal):
        self.nombresucursal = nombresucursal
        self.__categoria = {}

    #GETTERS
    def getcategoria(self):
        return self.__categoria
    #SETTERS
    def setcategoria(self, categoria):
        self.__categoria = categoria

    def mostrar_informacion(self):
        info = f"- {self.nombresucursal}"
        return info
    
    def get_categoria(self):
        return list (self.__categoria.values())
    
    def agregar_producto(self, nombre_categoria, producto):
        if nombre_categoria not in self._Sucursal__categoria:
            self._Sucursal__categoria[nombre_categoria] = Categoria(nombre_categoria)

        self._Sucursal__categoria[nombre_categoria]._Categoria__producto.append(producto)