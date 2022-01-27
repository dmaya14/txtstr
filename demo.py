from txtstr import txtstr
import os

#Crear una variable para usarlo como identificador
txtstr = txtstr


print("Elige las opciones")
print("1-  Crear txt")
print("2-  Leer txt")
print("1-  Transcribir txt")
option = int(input("-> "))

if option == 1:
    os.system("cls")
    text = str(input("Escribe tu texto -> "))
    name = str(input("Escribe el nombre del archivo -> "))
    txtstr.write(txtstr,text,name)
    os.system("cls")
    print("listo")

if option == 2:
    os.system("cls")
    rute = str(input("Escribe tu ruta -> "))
    txtstr.read(txtstr,rute)
    os.system("cls")
    print("listo")

if option == 3:
    os.system("cls")
    rute = str(input("Escribe tu ruta -> "))
    name = str(input("Escribe el nuevo nombre -> "))
    txtstr.transcript(txtstr,rute,name)
    os.system("cls")
    print("listo")









