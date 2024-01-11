import ui.menus as m
import os

if __name__ == '__main__':
    isActive = True
    while isActive:
        os.system('cls')
        m.menuPrincipal()
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
                os.system('cls')
                print ('Gracias por utilizar nuestro sistema......Vuelva Pronto!')
                os.system('pause')
                isActive = False
            else:
                print('Dato no valido')
                os.system('pause')