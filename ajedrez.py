import tkinter as tk
ventana = tk.Tk()
ventana.title("Ajedrez")

from tkinter import PhotoImage




#fichas blancas:
reyN = PhotoImage(file="img/torre-negra.png")
reinaN= PhotoImage(file="img/torre-negra.png")
#torreN= "♜"
torreN = PhotoImage(file="img/torre-negra.png")
alfilN=PhotoImage(file="img/torre-negra.png")
caballoN=PhotoImage(file="img/torre-negra.png")
peonN=PhotoImage(file="img/torre-negra.png")

#fichas negras:
reyB = PhotoImage(file="img/torre-negra.png")
reinaB= PhotoImage(file="img/torre-negra.png")
torreB= PhotoImage(file="img/torre-negra.png")
alfilB=PhotoImage(file="img/torre-negra.png")
caballoB=PhotoImage(file="img/torre-negra.png")
peonB=PhotoImage(file="img/torre-negra.png")

#tablero 8*8:
tablero = [[torreN,caballoN,alfilN,reinaN,reyN,alfilN,caballoN,torreN],[peonN,peonN,peonN,peonN,peonN,peonN,peonN,peonN],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],[peonB,peonB,peonB,peonB,peonB,peonB,peonB,peonB],[torreB,caballoB,alfilB,reinaB,reyB,alfilB,caballoB,torreB]]

#otras globales uliles:
contador=0
topeFila = 0
topeColum = 0
corte = True
ficha = ""
fichaElegida=""
filaFichaElegida = 0
columFichaElegida = 0
destildar = 0
desabilitar = "blanca"


#funciones de recorridos pocibles en el tablero:
def mostras_tablero(tablero):
    for fila in tablero:
        print(fila)

def Posicion_inicial(tablero):
    for fila in range(8):
      for colum in range(8):
        botones_tablero[fila][colum].config(image=tablero[fila][colum])



def mov_diagonal_arriba_derecha(tablero, fila, colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]
    while fila >= 1 and fila <= 7 and colum >= 0 and colum <= 6 and corte == True :
        fila = fila-1
        colum = colum +1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True


def mov_diagonal_arriba_derecha_corto(tablero, fila, colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]
    if fila >= 1 and fila <= 7 and colum >= 0 and colum <= 6 and corte == True :
        fila = fila-1
        colum = colum +1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True

def mov_diagonal_arriba_izquierda(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]
    while fila >= 1 and fila <= 7 and colum >= 1 and colum <= 7 and corte == True :
        fila = fila-1
        colum = colum -1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True


def mov_diagonal_arriba_izquierda_corto(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]
    if fila >= 1 and fila <= 7 and colum >= 1 and colum <= 7 and corte == True :
        fila = fila-1
        colum = colum -1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True


def mov_diagonal_abajo_derecha(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]
    while fila >= 0 and fila <= 6 and colum >= 0 and colum <= 6 and corte == True :
        fila = fila+1
        colum = colum +1
        corte = ataque_o_paso(tablero, fila, colum, ficha) 
    corte = True


def mov_diagonal_abajo_derecha_corto(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]
    if fila >= 0 and fila <= 6 and colum >= 0 and colum <= 6 and corte == True :
        fila = fila+1
        colum = colum +1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True

def mov_diagonal_abajo_izquierda(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]
    while fila >= 0 and fila <= 6 and colum >= 1 and colum <= 7 and corte == True :
        fila = fila+1
        colum = colum -1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True


def mov_diagonal_abajo_izquierda_corto(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]
    if fila >= 0 and fila <= 6 and colum >= 1 and colum <= 7 and corte == True :
        fila = fila+1
        colum = colum -1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True

def mov_hacia_atras(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]

    while fila >= 0 and fila <= 6 and colum >= 0 and colum <= 7 and corte == True :
        fila = fila+1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True

def mov_hacia_atras_corto(tablero,fila,colum): 
    global ficha
    global corte
    ficha = tablero[fila][colum]
    if fila >= 0 and fila <= 6 and colum >= 0 and colum <= 7 and corte == True :
        fila = fila+1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True


def mov_hacia_delante(tablero,fila,colum): ####
    global ficha
    global corte
    ficha = tablero[fila][colum]
    while fila >= 1 and fila <= 7 and colum >= 0 and colum <= 7 and corte == True:
        fila = fila-1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True

def mov_hacia_delante_corto(tablero,fila,colum):
    global ficha
    ficha = tablero[fila][colum]
    if fila >= 1 and fila <= 7 and colum >= 0 and colum <= 7:
        fila = fila-1
        ataque_o_paso(tablero, fila, colum, ficha) 



def mov_izquierda(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum]   
    while fila >= 0 and fila <= 7 and colum >= 1 and colum <= 7 and corte == True:
        colum=colum-1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True


def mov_izquierda_corto(tablero,fila,colum):
    global ficha
    ficha = tablero[fila][colum] 
    if fila >= 0 and fila <= 7 and colum >= 1 and colum <= 7:
        colum=colum-1
        ataque_o_paso(tablero, fila, colum, ficha)

def mov_derecha(tablero,fila,colum):
    global ficha
    global corte
    ficha = tablero[fila][colum] 
    while fila >= 0 and fila <= 7 and colum >= 0 and colum <= 6 and corte == True:
        colum=colum+1
        corte = ataque_o_paso(tablero, fila, colum, ficha)
    corte = True

def mov_derecha_corto(tablero,fila,colum):
    global ficha
    ficha = tablero[fila][colum] 
    if fila >= 0 and fila <= 7 and colum >= 0 and colum <= 6:
        colum=colum+1
        ataque_o_paso(tablero, fila, colum, ficha)

def mov_caballo(tablero, fila, colum):
    if tablero[fila][colum] == caballoB or tablero[fila][colum] == caballoN:
        global ficha
        ficha = tablero[fila][colum] 
        f= fila-2
        c= colum+1
        if  f >= 0 and f <= 7 and c >= 0 and c <= 7:
             ataque_o_paso(tablero, f, c, ficha)
        f= fila-1
        c= colum+2
        if  f >= 0 and f <= 7 and c >= 0 and c <= 7:
            ataque_o_paso(tablero, f, c, ficha)
        f= fila+1
        c= colum+2
        if  f >= 0 and f <= 7 and c >= 0 and c <= 7:
            ataque_o_paso(tablero, f, c, ficha)
        f= fila+2
        c= colum+1
        if  f >= 0 and f <= 7 and c >= 0 and c <= 7:
            ataque_o_paso(tablero, f, c, ficha)
        f= fila+2
        c= colum-1
        if  f >= 0 and f <= 7 and c >= 0 and c <= 7:
            ataque_o_paso(tablero, f, c, ficha)
        f= fila+1
        c= colum-2
        if  f >= 0 and f <= 7 and c >= 0 and c <= 7:
            ataque_o_paso(tablero, f, c, ficha)
        f= fila-1
        c= colum-2
        if  f >= 0 and f <= 7 and c >= 0 and c <= 7:
            ataque_o_paso(tablero, f, c, ficha)
        f= fila-2
        c= colum-1
        if  f >= 0 and f <= 7 and c >= 0 and c <= 7:
            ataque_o_paso(tablero, f, c, ficha)




def paso_peon_Blanco(tablero,fila,colum):
    if tablero[fila][colum] == peonB:
        if fila >= 1 and fila <= 7 and colum >= 0 and colum <= 7:
            if fila == 6:
                fila = fila-1
                if tablero[fila][colum] == "" :
                    botones_tablero[fila][colum].config(bg="red")
                    fila = fila-1
                    botones_tablero[fila][colum].config(bg="red")
            else:
                fila = fila-1
                if tablero[fila][colum] == "" :
                    botones_tablero[fila][colum].config(bg="red")


def paso_peon_Negro(tablero,fila,colum): ### 
    if tablero[fila][colum] == peonN:
        if fila >= 0 and fila <= 6 and colum >= 0 and colum <= 7:
            if fila == 1:
                fila = fila+1
                if tablero[fila][colum] == "" :
                    botones_tablero[fila][colum].config(bg="red")
                    fila = fila+1
                    botones_tablero[fila][colum].config(bg="red")
            else:
                fila = fila+1
                if tablero[fila][colum] == "" :
                    botones_tablero[fila][colum].config(bg="red")


    


## SI ENCUENTRA A UN ENEMIGO:

def ataque_o_paso(tablero, fila, colum, ficha): ## aca solo defino el ataque del peon
        global corte
        corte = True
        if ficha == peonB or ficha == torreB or ficha == caballoB or ficha == alfilB or ficha == reinaB or ficha == reyB:
            if tablero[fila][colum] == peonN or tablero[fila][colum] == torreN or tablero[fila][colum] == caballoN or tablero[fila][colum] == alfilN or tablero[fila][colum] == reinaN or tablero[fila][colum] == reyN:
                botones_tablero[fila][colum].config(bg="red")
                return False
            elif tablero[fila][colum] == "" and ficha != peonB:
                botones_tablero[fila][colum].config(bg="red")
                return True
            else:
                return False
            
        elif ficha == peonN or ficha == torreN or ficha == caballoN or ficha == alfilN or ficha == reinaN or ficha == reyN:
            if tablero[fila][colum] == peonB or tablero[fila][colum] == torreB or tablero[fila][colum] == caballoB or tablero[fila][colum] == alfilB or tablero[fila][colum] == reinaB or tablero[fila][colum] == reyB:
                botones_tablero[fila][colum].config(bg="red")
                return False
            elif tablero[fila][colum] == "" and ficha != peonN:
                botones_tablero[fila][colum].config(bg="red")
                return True
            else:
                return False
            



    


#funciones de movimiento:



def mov_peon_negro(tablero, fila, colum):
    if tablero[fila][colum] == peonN:
        paso_peon_Negro(tablero, fila, colum)
        mov_diagonal_abajo_derecha_corto(tablero, fila, colum)
        mov_diagonal_abajo_izquierda_corto(tablero, fila, colum)

def mov_peon_blanco(tablero, fila, colum):
    if tablero[fila][colum] == peonB:
        paso_peon_Blanco(tablero, fila, colum)
        mov_diagonal_arriba_derecha_corto(tablero, fila, colum)
        mov_diagonal_arriba_izquierda_corto(tablero, fila, colum)




def mov_reina(tablero, fila, colum):
    #global corte
    if tablero[fila][colum] == reinaB or tablero[fila][colum] == reinaN:
        mov_derecha(tablero, fila, colum)
        mov_diagonal_abajo_derecha(tablero, fila, colum)
        mov_hacia_atras(tablero, fila, colum)
        mov_diagonal_abajo_izquierda(tablero, fila, colum)
        mov_hacia_delante(tablero, fila, colum)
        mov_diagonal_arriba_izquierda(tablero, fila, colum)
        mov_izquierda(tablero, fila, colum)
        mov_diagonal_arriba_derecha(tablero, fila, colum)

def mov_rey(tablero, fila, colum):
    if tablero[fila][colum] == reyB or tablero[fila][colum] == reyN:
        mov_derecha_corto(tablero, fila, colum)
        mov_izquierda_corto(tablero, fila, colum)
        mov_hacia_atras_corto(tablero, fila, colum)
        mov_hacia_delante_corto(tablero, fila, colum)
        mov_diagonal_arriba_izquierda_corto(tablero, fila, colum)
        mov_diagonal_abajo_izquierda_corto(tablero, fila, colum)
        mov_diagonal_arriba_derecha_corto(tablero, fila, colum)
        mov_diagonal_abajo_derecha_corto(tablero, fila, colum)

def mov_alfil(tablero,fila, colum):
    if tablero[fila][colum] == alfilB or tablero[fila][colum] == alfilN:
        mov_diagonal_abajo_derecha(tablero, fila, colum)
        mov_diagonal_abajo_izquierda(tablero, fila, colum)
        mov_diagonal_arriba_derecha(tablero, fila, colum)
        mov_diagonal_arriba_izquierda(tablero, fila, colum)

def mov_torre(tablero,fila, colum):
    if tablero[fila][colum] == torreB or tablero[fila][colum] == torreN:  
        mov_hacia_atras(tablero, fila, colum)
        mov_hacia_delante(tablero, fila, colum)
        mov_izquierda(tablero, fila, colum)
        mov_derecha(tablero, fila, colum)





#destildar botones:
def destildar_botones(tablero):
    for fila in range(8):
      for colum in range(8):
        if fila % 2 == 0:
            if colum % 2 == 0:
                botones_tablero[fila][colum].config(bg="#F0E68C")
            else:
                botones_tablero[fila][colum].config(bg="#8B4513")
        else:
            if colum % 2 == 0:
                botones_tablero[fila][colum].config(bg="#8B4513")
            else:
                botones_tablero[fila][colum].config(bg="#F0E68C")           






#MOVIMIENTO DE TODAS LAS FICHAS JUNTAS:

def mov_fichas(tablero, fila, colum):
    global fichaElegida
    global filaFichaElegida
    global columFichaElegida

    global destildar
    

    boton = botones_tablero[fila][colum]

    if boton.cget("bg") != "red":
        filaFichaElegida= fila
        columFichaElegida= colum
        fichaElegida = tablero[fila][colum]
        

        mov_torre(tablero, fila, colum)
        mov_caballo(tablero, fila, colum)
        mov_alfil(tablero, fila, colum)
        mov_reina(tablero, fila, colum)
        mov_rey(tablero, fila, colum)
        mov_peon_blanco(tablero, fila, colum)
        mov_peon_negro(tablero, fila, colum)
        
    elif boton.cget("bg") == "red":
        tablero[filaFichaElegida][columFichaElegida] = ""
        tablero[fila][colum] = fichaElegida
        Posicion_inicial(tablero)
        destildar_botones(tablero)
        
        
    
    #truco que invente para destidar:
    destildar = 1 if destildar == 0 else 0
    if destildar == 0:
        destildar_botones(tablero)




#mostras_tablero(tablero)


#botones:

botones_tablero = [[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None]]
for fila in range(8):
    for colum in range(8):
        botones_tablero[fila][colum] = tk.Button(ventana, width=6, height=3, command=lambda fila=fila, colum=colum: mov_fichas(tablero,fila, colum)) #commando!
        botones_tablero[fila][colum].grid(row=fila,column=colum)


Posicion_inicial(tablero)
destildar_botones(tablero)
ventana.mainloop()





















