# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:59:33 2024

@author: USUARIO
"""

import tkinter as tk
from programa import Tienda, Videojuego, Cliente

class Ventana:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry('600x600')
        self.ventana.title('TIENDA DE JUEGOS')

        botonregistrarcliente = tk.Button(self.ventana, text='REGISTRAR CLIENTE', padx=10, pady=10, command=self.ventanaregistarcliente)
        botonregistrarcliente.pack()

        botonbuscarcliente = tk.Button(self.ventana, text='BUSCAR CLIENTE', padx=10, pady=10, command=self.ventanabuscarcliente)
        botonbuscarcliente.pack()

        botonbuscarjuegopornombre = tk.Button(self.ventana, text='BUSCAR JUEGO POR NOMBRE', padx=10, pady=10, command=self.ventanabuscarjuegopornombre)
        botonbuscarjuegopornombre.pack()

        botonbuscarjuegoporcodigo = tk.Button(self.ventana, text='BUSCAR JUEGO POR CODIGO', padx=10, pady=10, command=self.ventanabuscarjuegoporcodigo)
        botonbuscarjuegoporcodigo.pack()

        botonregistarjuego = tk.Button(self.ventana, text='REGISTRAR JUEGO', padx=10, pady=10, command=self.ventanaregistrarjuego)
        botonregistarjuego.pack()

        botondevolvervideojuego = tk.Button(self.ventana, text='DEVOLVER VIDEOJUEGO', padx=10, pady=10)
        botondevolvervideojuego.pack()

        botoncomprarjuegoalcliente = tk.Button(self.ventana, text='COMPRAR JUEGO AL CLIENTE', padx=10, pady=10, command=self.ventanacomprarjuegoalcliente)
        botoncomprarjuegoalcliente.pack()

        botonvender = tk.Button(self.ventana, text='VENDER', padx=10, pady=10, command=self.vender)
        botonvender.pack()

        botonalquilar = tk.Button(self.ventana, text='ALQUILAR', padx=10, pady=10, command=self.alquilar)
        botonalquilar.pack()

        self.ventana.mainloop()

    def ventanaregistarcliente(self):
        Ventana1(self)

    def ventanabuscarcliente(self):
        Ventana2(self)

    def ventanabuscarjuegopornombre(self):
        Ventana3(self)

    def ventanabuscarjuegoporcodigo(self):
        Ventana4(self)

    def ventanaregistrarjuego(self):
        Ventana5(self)

    def ventanacomprarjuegoalcliente(self):
        Ventana6(self)

    def vender(self):
        Ventana7(self)

    def alquilar(self):
        Ventana8(self)


class Ventana1:

    def __init__(self, parent):
        self.parent = parent
        self.ventanaregistarcliente = tk.Toplevel()
        self.ventanaregistarcliente.geometry('600x400')
        self.ventanaregistarcliente.title('REGISTRAR USUARIO')

        tk.Label(self.ventanaregistarcliente, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        self.cedula_entry = tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER)
        self.cedula_entry.pack()

        tk.Label(self.ventanaregistarcliente, text='INGRESE EL NOMBRE DEL USUARIO', justify=tk.CENTER).pack()
        self.nombre_entry = tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER)
        self.nombre_entry.pack()

        tk.Label(self.ventanaregistarcliente, text='INGRESE LA DIRECCIÓN DEL USUARIO', justify=tk.CENTER).pack()
        self.direccion_entry = tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER)
        self.direccion_entry.pack()

        tk.Label(self.ventanaregistarcliente, text='INGRESE EL TELEFONO DEL USUARIO', justify=tk.CENTER).pack()
        self.telefono_entry = tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER)
        self.telefono_entry.pack()

        tk.Label(self.ventanaregistarcliente, text='POR FAVOR INICIALICE LAS COMPRAS DEL USUARIO EN 0', justify=tk.CENTER).pack()
        self.compras_entry = tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER)
        self.compras_entry.pack()

        tk.Label(self.ventanaregistarcliente, text='POR FAVOR INICIALICE EL ESTADO DEL USUARIO EN 0', justify=tk.CENTER).pack()
        self.estado_entry = tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER)
        self.estado_entry.pack()

        self.registro1 = tk.Button(self.ventanaregistarcliente, text='GUARDAR', padx=10, pady=10, command=self.volverventana)
        self.registro1.pack()

    def volverventana(self):
        self.ventanaregistarcliente.destroy()


class Ventana2:

    def __init__(self, parent):
        self.parent = parent
        self.ventanabuscarcliente = tk.Toplevel()
        self.ventanabuscarcliente.geometry('600x200')
        self.ventanabuscarcliente.title('BUSCAR CLIENTE')

        tk.Label(self.ventanabuscarcliente, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        self.cedula_entry = tk.Entry(self.ventanabuscarcliente, justify=tk.CENTER)
        self.cedula_entry.pack()

        self.buscar = tk.Button(self.ventanabuscarcliente, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.ventanabuscarcliente, text='VOLVER AL INICIO', padx=10, pady=10, command=self.volverventana)
        self.volver.pack()

    def volverventana(self):
        self.ventanabuscarcliente.destroy()


class Ventana3:

    def __init__(self, parent):
        self.parent = parent
        self.ventanabuscarjuegopornombre = tk.Toplevel()
        self.ventanabuscarjuegopornombre.geometry('600x200')
        self.ventanabuscarjuegopornombre.title('BUSCAR JUEGO POR NOMBRE')

        tk.Label(self.ventanabuscarjuegopornombre, text='INGRESE EL NOMBRE DEL JUEGO', justify=tk.CENTER).pack()
        self.nombre_juego_entry = tk.Entry(self.ventanabuscarjuegopornombre, justify=tk.CENTER)
        self.nombre_juego_entry.pack()

        self.buscar = tk.Button(self.ventanabuscarjuegopornombre, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.ventanabuscarjuegopornombre, text='VOLVER AL INICIO', padx=10, pady=10, command=self.volverventana)
        self.volver.pack()

    def volverventana(self):
        self.ventanabuscarjuegopornombre.destroy()


class Ventana4:

    def __init__(self, parent):
        self.parent = parent
        self.ventanabuscarjuegoporcodigo = tk.Toplevel()
        self.ventanabuscarjuegoporcodigo.geometry('600x200')
        self.ventanabuscarjuegoporcodigo.title('BUSCAR JUEGO POR CODIGO')

        tk.Label(self.ventanabuscarjuegoporcodigo, text='INGRESE EL CODIGO DEL JUEGO', justify=tk.CENTER).pack()
        self.codigo_juego_entry = tk.Entry(self.ventanabuscarjuegoporcodigo, justify=tk.CENTER)
        self.codigo_juego_entry.pack()

        self.buscar = tk.Button(self.ventanabuscarjuegoporcodigo, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.ventanabuscarjuegoporcodigo, text='VOLVER AL INICIO', padx=10, pady=10, command=self.volverventana)
        self.volver.pack()

    def volverventana(self):
        self.ventanabuscarjuegoporcodigo.destroy()


class Ventana5:

    def __init__(self, parent):
        self.parent = parent
        self.ventanaregistrarjuego = tk.Toplevel()
        self.ventanaregistrarjuego.geometry('600x400')
        self.ventanaregistrarjuego.title('REGISTRAR JUEGO')

        tk.Label(self.ventanaregistrarjuego, text='INGRESE EL NOMBRE DEL JUEGO', justify=tk.CENTER).pack()
        self.nombre_juego_entry = tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER)
        self.nombre_juego_entry.pack()

        tk.Label(self.ventanaregistrarjuego, text='INGRESE EL CODIGO DEL JUEGO', justify=tk.CENTER).pack()
        self.codigo_juego_entry = tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER)
        self.codigo_juego_entry.pack()

        tk.Label(self.ventanaregistrarjuego, text='INGRESE EL PRECIO DE ALQUILER', justify=tk.CENTER).pack()
        self.precio_alquiler_entry = tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER)
        self.precio_alquiler_entry.pack()

        tk.Label(self.ventanaregistrarjuego, text='INGRESE EL PRECIO DE VENTA', justify=tk.CENTER).pack()
        self.precio_venta_entry = tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER)
        self.precio_venta_entry.pack()

        tk.Label(self.ventanaregistrarjuego, text='INGRESE LA CANTIDAD DE UNIDADES DISPONIBLES', justify=tk.CENTER).pack()
        self.unidades_entry = tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER)
        self.unidades_entry.pack()

        self.registro1 = tk.Button(self.ventanaregistrarjuego, text='GUARDAR', padx=10, pady=10, command=self.volverventana)
        self.registro1.pack()

    def volverventana(self):
        self.ventanaregistrarjuego.destroy()


class Ventana6:

    def __init__(self, parent):
        self.parent = parent
        self.ventanacomprarjuegoalcliente = tk.Toplevel()
        self.ventanacomprarjuegoalcliente.geometry('600x200')
        self.ventanacomprarjuegoalcliente.title('COMPRAR JUEGO AL CLIENTE')

        tk.Label(self.ventanacomprarjuegoalcliente, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        self.cedula_entry = tk.Entry(self.ventanacomprarjuegoalcliente, justify=tk.CENTER)
        self.cedula_entry.pack()

        self.buscar = tk.Button(self.ventanacomprarjuegoalcliente, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.ventanacomprarjuegoalcliente, text='VOLVER AL INICIO', padx=10, pady=10, command=self.volverventana)
        self.volver.pack()

    def volverventana(self):
        self.ventanacomprarjuegoalcliente.destroy()


class Ventana7:

    def __init__(self, parent):
        self.parent = parent
        self.vender = tk.Toplevel()
        self.vender.geometry('600x200')
        self.vender.title('VENDER')

        tk.Label(self.vender, text='INGRESE EL CODIGO DEL JUEGO', justify=tk.CENTER).pack()
        self.codigo_juego_entry = tk.Entry(self.vender, justify=tk.CENTER)
        self.codigo_juego_entry.pack()

        tk.Label(self.vender, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        self.cedula_entry = tk.Entry(self.vender, justify=tk.CENTER)
        self.cedula_entry.pack()

        self.buscar = tk.Button(self.vender, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.vender, text='VOLVER AL INICIO', padx=10, pady=10, command=self.volverventana)
        self.volver.pack()

    def volverventana(self):
        self.vender.destroy()


class Ventana8:

    def __init__(self, parent):
        self.parent = parent
        self.alquilar = tk.Toplevel()
        self.alquilar.geometry('600x200')
        self.alquilar.title('ALQUILAR')

        tk.Label(self.alquilar, text='INGRESE EL NOMBRE DEL JUEGO', justify=tk.CENTER).pack()
        self.nombre_juego_entry = tk.Entry(self.alquilar, justify=tk.CENTER)
        self.nombre_juego_entry.pack()

        tk.Label(self.alquilar, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        self.cedula_entry = tk.Entry(self.alquilar, justify=tk.CENTER)
        self.cedula_entry.pack()

        self.buscar = tk.Button(self.alquilar, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.alquilar, text='VOLVER AL INICIO', padx=10, pady=10, command=self.volverventana)
        self.volver.pack()

    def volverventana(self):
        self.alquilar.destroy()


if __name__ == "__main__":
    Ventana()
