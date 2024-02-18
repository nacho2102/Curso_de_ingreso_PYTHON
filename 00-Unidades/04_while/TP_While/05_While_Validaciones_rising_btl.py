import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.txt_tipo = customtkinter.CTkEntry(master=self)
        self.txt_tipo.grid(row=2, column=1, padx=20, pady=10)
        

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = prompt("Risin BTL", "Ingrese su apellido")
        edad_str = prompt("Rising BTL", "Ingrese su edad")
        edad = int(edad_str)
        tipo = prompt("Rising BTL", "Ingrese su estado civil")
        legajo_str = prompt("Rising BTL", "Ingrese su numero de legajo")
        legajo = int(legajo_str)
        while apellido.isdigit():
            apellido = prompt("ERROR", "Apellido invalido, reingrese su apellido")
            if apellido is None:
                break
            else:
                continue
        while edad_str.isalpha() or (edad < 18 or edad > 90):
            edad_str = prompt("ERROR", "Edad invalida, reingrese su edad")
            edad = int(edad_str)
            if edad_str is None:
                break
            else:
                continue
        while not (tipo == "Soltero" or tipo == "Soltera" or tipo == "Casado" or tipo == "Casada" or tipo == "Divorciado"
                    or tipo == "Divorciada" or tipo == "Viudo" or tipo == "Viuda"):
            tipo = prompt("ERROR", "Estado civil invalido, reingrese su estado civil")
            if tipo is None:
                break
            else:
                continue
        while legajo_str.isalpha() or (legajo < 1000 or legajo > 9999):
            legajo_str = prompt("ERROR", "N° de legajo invalido, reingrese su N° de legajo")
            legajo = int(legajo_str)
            if legajo_str is None:
                break
            else:
                continue
        self.txt_apellido.delete(0, tkinter.END)
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, tkinter.END)
        self.txt_edad.insert(0, edad_str)
        self.txt_tipo.delete(0, tkinter.END)
        self.txt_tipo.insert(0, tipo)
        self.txt_legajo.delete(0, tkinter.END)
        self.txt_legajo.insert(0, legajo_str)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
