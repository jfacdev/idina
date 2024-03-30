#!/usr/bin/python3


def main():

    class Obj():
        def __init__(self, nombre, accion):

            self.nombre = nombre
            self.accion = accion

        def jugador(self):
            print(self.nombre + " -> " + self.accion)



    eleccion = Obj("Manzana", "comer")

    eleccion.jugador()
main()
