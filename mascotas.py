#====================
#     LIBRERIAS
#====================

import os
import time
import sqlite3
from colorama import init, Fore, Back, Style
init()


#====================
#====================




#====================
# VARIABLES GLOBALES
#====================
banner = Fore.YELLOW + """

███╗   ███╗ █████╗ ███████╗ ██████╗ ██████╗ ████████╗ █████╗ ███████╗
████╗ ████║██╔══██╗██╔════╝██╔════╝██╔═══██╗╚══██╔══╝██╔══██╗██╔════╝
██╔████╔██║███████║███████╗██║     ██║   ██║   ██║   ███████║███████╗
██║╚██╔╝██║██╔══██║╚════██║██║     ██║   ██║   ██║   ██╔══██║╚════██║
██║ ╚═╝ ██║██║  ██║███████║╚██████╗╚██████╔╝   ██║   ██║  ██║███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝                                                                                                                                   
"""
#====================
#====================






#====================
#     FUNCIONES
#====================

def limpiar():
    time.sleep(0.3)
    os.system("cls")



def opcion_no_reconocida():
    print(f"""
                {Fore.RED}No se ha reconocido su opcion!
          
                {Fore.CYAN}(1): {Fore.WHITE}Si desea salir del programa.
                {Fore.CYAN}(2): {Fore.WHITE}Si desea regresar al menu.
          """)
    opcion = int(input(f"{Fore.CYAN}>>> "))
    
    
    if opcion == 1:
        print(f"{Fore.RED}Saliendo del programa...")
        limpiar()
    elif opcion == 2:
        limpiar()
        menu()
    else:
        opcion_no_reconocida()




def menu():
    print(banner)
    print(f"""
                       {Fore.LIGHTYELLOW_EX} Menu de Opciones:
                       
                {Fore.CYAN}(1): {Fore.WHITE}Registrar mascota nueva.
                {Fore.CYAN}(2): {Fore.WHITE}Mostrar la lista de mascotas registradas.
                {Fore.CYAN}(3): {Fore.WHITE}Adoptar una mascota por nombre.
                    
                {Fore.CYAN}(4): {Fore.RED}Salir del Programa.
          """)
    opcion = int(input(f"{Fore.CYAN}>>> "))
    
    if opcion == 1:
        limpiar()
        registrar_mascota()
    elif opcion == 2:
        limpiar()
        mascotas()
    elif opcion == 3:
        limpiar()
        adoptar()
    elif opcion == 4:
        print(f"{Fore.RED}Saliendo del programa...")
        limpiar()
    else:
        opcion_no_reconocida()
        
      
             
def registrar_mascota():
    nombre = input(f"{Fore.CYAN}Escriba {Fore.WHITE}el nombre de la mascota: {Fore.YELLOW}") 
    try:  
        edad = int(input(f"{Fore.CYAN}Escriba {Fore.WHITE}la edad de la mascota en años: {Fore.YELLOW}"))
    except Exception as e:
        print(" ")
        print(f"{Fore.WHITE}>>> {Fore.RED}Solo puede escribir un numero {Fore.YELLOW}entero{Fore.RED}, que represtara sus años.")
        print(f"{Fore.WHITE}>>> {Fore.CYAN}Razon del error: {Fore.RED}{e}")
        print(" ")
        input(f"{Fore.CYAN}Presione {Fore.YELLOW}ENTER {Fore.CYAN}si desea volver al menu.")
        limpiar()
        menu()  
    tipo = input(f"{Fore.CYAN}Escriba {Fore.WHITE}el tipo de animal que es: {Fore.YELLOW}")
    
    
    
    conn = sqlite3.connect("mascotas.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Mascotas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        tipo TEXT NOT NULL
    );
                   """)
    cursor.execute("INSERT INTO Mascotas (nombre, edad, tipo) VALUES (?, ?, ?)", (nombre, edad, tipo))
    conn.commit()
    conn.close()
    
    
    
    mascota_registrada = Mascota(nombre, edad, tipo)
    print(f"{Fore.GREEN}La mascota se ha registrado con exito!")
    print(f"{Fore.YELLOW}{mascota_registrada}")
    print(" ")
    input(f"{Fore.CYAN}Presione {Fore.YELLOW}ENTER {Fore.CYAN}si desea volver al menu.")
    limpiar()
    menu()




def mascotas():
    conn = sqlite3.connect("mascotas.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Mascotas")
    todas_las_mascotas = cursor.fetchall()
    cantidad = len(todas_las_mascotas)
    
    if not todas_las_mascotas:
        print(f"{Fore.RED}No hay mascotas registradas.")
        input(f"{Fore.CYAN}Presione {Fore.YELLOW}ENTER {Fore.CYAN}si desea volver al menu.")
        limpiar()
        menu()

    else:
        for mascota in todas_las_mascotas:
            id, nombre, edad, tipo = mascota
            print(f"{Fore.CYAN}ID: {Fore.WHITE}{id}, {Fore.CYAN}Nombre: {Fore.WHITE}{nombre}, {Fore.CYAN}Edad: {Fore.WHITE}{edad}, {Fore.YELLOW}Tipo: {Fore.YELLOW}{tipo}")
        print(" ")
        print(f"{Fore.WHITE}>>> {Fore.CYAN}En total tenemos {Fore.MAGENTA}{cantidad} {Fore.CYAN}mascota(s) registrada(s)!")
        input(f"{Fore.CYAN}Presione {Fore.YELLOW}ENTER {Fore.CYAN}si desea volver al menu.")
        limpiar()
        menu()

    conn.close()




def adoptar():
    conn = sqlite3.connect("mascotas.db")
    cursor = conn.cursor()
    
    nombre_buscado = input(f"{Fore.CYAN}Escriba {Fore.WHITE}el nombre de la mascota que quiere adoptar: {Fore.YELLOW}")
    
    cursor.execute("SELECT * FROM Mascotas WHERE nombre = ?", (nombre_buscado,))
    mascota = cursor.fetchone()
    
    
    if mascota:
        id, nombre, edad, tipo = mascota
        print(f"{Fore.WHITE}>>> {Fore.GREEN}Mascota encontrada: {Fore.CYAN}ID: {Fore.WHITE}{id}, {Fore.CYAN}Nombre: {Fore.WHITE}{nombre}, {Fore.CYAN}Edad: {Fore.WHITE}{edad}, {Fore.YELLOW}Tipo: {Fore.YELLOW}{tipo}")
        print(" ")
        eleccion = input(f"{Fore.GREEN}Desea adoptar a {Fore.WHITE}{nombre_buscado}{Fore.GREEN}? {Fore.YELLOW}Si/No: {Fore.GREEN}").lower()
        
        if eleccion == "si":
            print(f"{Fore.YELLOW}Gracias por adoptar a {Fore.WHITE}{nombre_buscado}{Fore.YELLOW}!, {Fore.CYAN}sabemos que ambos seran muy felices :)")
            cursor.execute("DELETE FROM Mascotas WHERE LOWER(nombre) = LOWER(?)", (nombre_buscado,))
            print(" ")
            input(f"{Fore.CYAN}Presione {Fore.YELLOW}ENTER {Fore.CYAN}si desea volver al menu.")
            limpiar()
            menu()
        else:
            print(f"{Fore.YELLOW}Entendemos que no quiera adoptar a {Fore.WHITE}{nombre_buscado}{Fore.YELLOW}, {Fore.CYAN}no se preocupe :)")
            input(f"{Fore.CYAN}Presione {Fore.YELLOW}ENTER {Fore.CYAN}si desea volver al menu.")
            limpiar()
            menu()
            
    else    :
        print(" ")
        print(f"{Fore.RED}No se encontró ninguna mascota llamada '{nombre_buscado}'.")
        input(f"{Fore.CYAN}Presione {Fore.YELLOW}ENTER {Fore.CYAN}si desea volver al menu.")
        limpiar()
        menu()


    conn.commit()
    conn.close()
#====================
#====================




#====================
#      CLASES
#====================

class Mascota:
    
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        
    def __str__(self):
        return f"{self.tipo} llamado {self.nombre}, {self.edad} años"

#====================
#====================




#====================
#  CONTENIDO GLOBAL
#====================
menu()
#====================
#====================
