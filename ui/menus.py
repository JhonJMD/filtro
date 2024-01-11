import ui.titles as t
import funciones.generos as fg
import funciones.actores as fa 
import funciones.peliculas as fp 
import funciones.formatos as ff 
import funciones.informes as fi 
import os

def menuAdminGeneros():
    os.system('cls')
    t.headerAdminGeneros()
    opciones = ['Crear Genero', 'Listar Genero', 'Ir Menu principal']
    isActiveGen = True
    while isActiveGen:
        for i, item in enumerate(opciones):
            print(f'{i+1}. {item}')
        try:
            opMenu = int(input(': '))
        except ValueError:
            print('Dato no valido')
            os.system('pause')
        else:
            if opMenu == 1:
                crearGenero()
            elif opMenu == 2:
                listarGenero()
            elif opMenu == 3:
                isActiveGen = False
            else:
                print('Dato no valido')
                os.system('pause')

def menuAdminActores():
    os.system('cls')
    t.headerAdminActores()
    opciones = ['Crear Actor', 'Listar Actor', 'Ir Menu principal']
    isActiveAct = True
    while isActiveAct:
        for i, item in enumerate(opciones):
            print(f'{i+1}. {item}')
        try:
            opMenu = int(input(': '))
        except ValueError:
            print('Dato no valido')
            os.system('pause')
        else:
            if opMenu == 1:
                crearActor()
            elif opMenu == 2:
                listarActor()
            elif opMenu == 3:
                isActiveAct = False
            else:
                print('Dato no valido')
                os.system('pause')  

def menuAdminFormatos():
    os.system('cls')
    t.headerAdminFormatos()
    opciones = ['Crear Formato', 'Listar Formato', 'Ir Menu principal']
    isActiveForm = True
    while isActiveForm:
        for i, item in enumerate(opciones):
            print(f'{i+1}. {item}')
        try:
            opMenu = int(input(': '))
        except ValueError:
            print('Dato no valido')
            os.system('pause')
        else:
            if opMenu == 1:
                crearFormato()
            elif opMenu == 2:
                listarFormato()
            elif opMenu == 3:
                isActiveForm = False
            else:
                print('Dato no valido')
                os.system('pause')

def menuGestorInformes():
    os.system('cls')
    t.headerGestorInformes()
    opciones = ['Listar Peliculas de un genero especifico', 'Listar Peliculas donde el protagonista sea Silvestre Stallone', 'Buscar Pelicula y mostrar la sinopsis y los actores', 'Ir Menu principal']
    isActiveInf = True
    while isActiveInf:
        for i, item in enumerate(opciones):
            print(f'{i+1}. {item}')
        try:
            opMenu = int(input(': '))
        except ValueError:
            print('Dato no valido')
            os.system('pause')
        else:
            if opMenu == 1:
                listGenero()
            elif opMenu == 2:
                listSS()
            elif opMenu == 3:
                buscarPelicula()
            elif opMenu == 4:
                isActiveInf = False
            else:
                print('Dato no valido')
                os.system('pause')

def menuGestorPeliculas():
    os.system('cls')
    t.headerGestorPeliculas()
    opciones = ['Agregar Pelicula', 'Editar Pelicula', 'Eliminar Pelicula', 'Eliminar Actor', 'Buscar Pelicula', 'Listar todas las Peliculas', 'Ir Menu principal']
    isActivePel = True
    while isActivePel:
        for i, item in enumerate(opciones):
            print(f'{i+1}. {item}')
        try:
            opMenu = int(input(': '))
        except ValueError:
            print('Dato no valido')
            os.system('pause')
        else:
            if opMenu == 1:
                agregarPelicula()
            elif opMenu == 2:
                editarPelicula()
            elif opMenu == 3:
                eliminarPelicula()
            elif opMenu == 4:
                eliminarActor()
            elif opMenu == 5:
                buscarPelicula()
            elif opMenu == 6:
                listarPeliculas()
            elif opMenu == 7:
                isActivePel = False
            else:
                print('Dato no valido')
                os.system('pause') 