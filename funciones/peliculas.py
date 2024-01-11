import funciones.corefile as cf
import ui.titles as t
import json
import os

cf.MY_DATABASE = 'data/peliculas.json'
peliculas = {}
idsum = 0
def NewPelicula(peli):
    id = peli['id']
    peliculas[id] = peli
    cf.AddData(id, peli)


def valFilePelicula():
    if(cf.checkFile()):
        print('OK')
    else:
        cf.NewFile(peliculas)
def agregarPelicula():
    global idsum
    pelicula = {
        'id': '',
        'nombre':'',
        'duracion':'',
        'sinopsis': '',
        'generos':'',
        'actores':'',
        'formato': ''
    }
    for key, item in pelicula.items():
        if (key != 'id'):
            pelicula[key] = input(f'Ingrese {key.capitalize()} de la Pelicula: ')
        else:
            idsum += 1
            pelicula[key] = idsum
    NewPelicula(pelicula)
    print(f'Pelicula {pelicula['nombre']} agregada correctamente')
    os.system('pause')