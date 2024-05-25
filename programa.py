# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:34:07 2024

@author: USUARIO
"""

from dataclasses import dataclass

@dataclass
class Cliente:
    cedula: int
    nombre: str
    direccion: str
    telefono: int
    compras: int
    estado: int

@dataclass
class Videojuego:
    nombre_juego: str
    codigo_juego: int
    precio_alquiler: int
    precio_venta: int
    cantidad: int

class Tienda:

    def __init__(self):
        self.listaclientes: dict[int, Cliente] = dict()
        self.catalogo: dict[int, Videojuego] = dict()

    def registrar_cliente(self, cedula: int, nombre: str, direccion: str, telefono: int, compras: int, estado: int):
        if self.buscar_cliente(cedula) is None:
            cliente = Cliente(cedula, nombre, direccion, telefono, compras, estado)
            self.listaclientes[cedula] = cliente

    def buscar_cliente(self, cedula: int):
        return self.listaclientes.get(cedula, None)

    def registrar_juego(self, nombre_juego: str, codigo_juego: int, precio_alquiler: int, precio_venta: int, cantidad: int):
        if self.buscar_juego_por_codigo(codigo_juego) is None:
            juego = Videojuego(nombre_juego, codigo_juego, precio_alquiler, precio_venta, cantidad)
            self.catalogo[codigo_juego] = juego

    def buscar_juego_por_nombre(self, nombre_juego: str):
        for juego in self.catalogo.values():
            if juego.nombre_juego == nombre_juego:
                return juego
        return None

    def buscar_juego_por_codigo(self, codigo_juego: int):
        return self.catalogo.get(codigo_juego, None)

    def vender(self, codigo_juego: int, cedula: int):
        juego = self.buscar_juego_por_codigo(codigo_juego)
        cliente = self.buscar_cliente(cedula)
        if juego and cliente and juego.cantidad > 0:
            juego.cantidad -= 1
            cliente.compras += 1

    def alquilar(self, nombre_juego: str, cedula: int):
        juego = self.buscar_juego_por_nombre(nombre_juego)
        cliente = self.buscar_cliente(cedula)
        if juego and cliente and juego.cantidad > 0:
            cliente.estado = 1
            juego.cantidad -= 1

    def devolver_videojuego(self, cedula: int):
        cliente = self.buscar_cliente(cedula)
        if cliente and cliente.estado == 1:
            cliente.estado = 0
            # Asumimos que la devolución siempre incrementa la cantidad del primer juego alquilado
            for juego in self.catalogo.values():
                juego.cantidad += 1
                break
        else:
            print("NO TIENES JUEGOS ALQUILADOS")

    def comprar_juego_al_cliente(self, cedula: int):
        cliente = self.buscar_cliente(cedula)
        if cliente:
            # Asumimos que la compra siempre decrementa la cantidad del primer juego del catálogo
            for juego in self.catalogo.values():
                if juego.cantidad > 0:
                    juego.cantidad -= 1
                    cliente.compras += 1
                    break
        else:
            print("El cliente no está registrado")
