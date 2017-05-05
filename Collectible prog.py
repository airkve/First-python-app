#Richard collectibles
import sys, os

mainmenu = {
    "1": "Cartas",
    "2": "Figuras",
    "3": "Salir"
}

cardmenu = {
    "1": "Ver libreria",
    "2": "Buscar una carta",
    "3": "Cargar una carta",
    "4": "Regresar",
    "5": "Salir"
}

figsmenu = {
    "1": "Ver libreria",
    "2": "Buscar una figura",
    "3": "Cargar una figura",
    "4": "Regresar",
    "5": "Salir"
}

cartas = {}
figuras = {}
mainmenu_choice = 0
cardmenu_choice = 0
figsmenu_choice = 0
card_buffer = []
figs_buffer = []
os.system('cls')

while True:
    '''Menu principal.'''
    menu_x1 = mainmenu.keys()
    menu_x1.sort()
    for key in menu_x1:
        print key, mainmenu[key]
    mainmenu_choice = input("Seleccione: ")
    '''Submenu de cartas.'''
    if mainmenu_choice == 1:
        menu_x2 = cardmenu.keys()
        menu_x2.sort()
        for key1 in menu_x2:
            print key1, cardmenu[key1]
        cardmenu_choice = input("Seleccione: ")
        '''Libreria de Cartas.'''
        if cardmenu_choice == 1:
            for opt1 in cartas.keys():
                print opt1, ":", cartas[opt1]
        '''Busqueda de carta.'''
        elif cardmenu_choice == 2:
            busqueda = input("Introduce el nombre de la carta: ")
            busqueda.capitalize()
            with open("mtg-data.txt", "r") as mtgdb:
            for seekdb in mtgdb:
                if busqueda in seekdb:
                    print seekdb.readline()
                else:
                    print "Carta invalida o no existe"        
        '''Carga de carta.'''
        elif cardmenu_choice == 3:
            print "LLene los datos:"
            cardname = input("Nombre de la carta: ")
            cardcost = input("Costo de la carta: ")
            carddesc = input("Descripcion de la carta: ")
    ''' Submenu de figuras.'''
    elif mainmenu_choice == 2:
        menu_x3 = figsmenu.keys()
        menu_x3.sort()
        for key2 in menu_x3:
            print key2, figsmenu[key2]
        figsmenu_choice = input("Seleccione: ")
        pass
    else:
        break
