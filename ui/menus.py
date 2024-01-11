import ui.titles as t
import funciones.generos as g
import funciones.actores as a 
import funciones.peliculas as p 
import funciones.formatos as f 
import funciones.informes as fi
import os
def menuPrincipal():
    t.headerPrincipal()
    opciones = ['Administrador de Generos','Administrador de Actores', 'Administrador de Formatos', 'Gestor de Informes','Gestor de Peliculas','Salir']
    for i, item in enumerate(opciones):
        print(f'{i+1}. {item}')
        
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
                g.crearGenero()
            elif opMenu == 2:
                g.listarGenero()
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
                a.crearActor()
            elif opMenu == 2:
                a.listarActor()
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
                f.crearFormato()
            elif opMenu == 2:
                f.listarFormato()
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
                fi.listGenero()
            elif opMenu == 2:
                fi.listSS()
            elif opMenu == 3:
                fi.buscarPelicula()
            elif opMenu == 4:
                isActiveInf = False
            else:
                print('Dato no valido')
                os.system('pause')

def menuGestorPeliculas():
    p.cf.checkFile(p.peliculas)
    opciones = ['Agregar Pelicula', 'Editar Pelicula', 'Eliminar Pelicula', 'Eliminar Actor', 'Buscar Pelicula', 'Listar todas las Peliculas', 'Ir Menu principal']
    isActivePel = True
    while isActivePel:
        os.system('cls')
        t.headerGestorPeliculas()
        for i, item in enumerate(opciones):
            print(f'{i+1}. {item}')
        try:
            opMenu = int(input(': '))
        except ValueError:
            print('Dato no valido')
            os.system('pause')
        else:
            if opMenu == 1:
                p.agregarPelicula()
            elif opMenu == 2:
                p.editarPelicula()
            elif opMenu == 3:
                p.eliminarPelicula()
            elif opMenu == 4:
                p.eliminarActor()
            elif opMenu == 5:
                p.buscarPelicula()
            elif opMenu == 6:
                p.listarPeliculas()
            elif opMenu == 7:
                isActivePel = False
            else:
                print('Dato no valido')
                os.system('pause') 