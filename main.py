import ui.titles as t
import ui.menus as m
import os

opciones = ['Administrador de Generos','Administrador de Actores', 'Administrador de Formatos', 'Gestor de Informes','Gestor de Peliculas','Salir']

if __name__ == '__main__':
    isActive = True
    while isActive:
        os.system('cls')
        t.headerPrincipal()
        for i, item in enumerate(opciones):
            print(f'{i+1}. {item}')
        try:
            opMenu = int(input(': '))
        except ValueError:
            print('Dato no valido')
            os.system('pause')
        else:
            if opMenu == 1:
                m.menuAdminGeneros()
            elif opMenu == 2:
                m.menuAdminActores()
            elif opMenu == 3:
                m.menuAdminFormatos()
            elif opMenu == 4:
                m.menuGestorInformes()
            elif opMenu == 5:
                m.menuGestorPeliculas()
            elif opMenu == 6:
                print ('Gracias por utilizar nuestro sistema......Vuelva Pronto!')
                os.system('pause')
                isActive = False
            else:
                print('Dato no valido')
                os.system('pause')
