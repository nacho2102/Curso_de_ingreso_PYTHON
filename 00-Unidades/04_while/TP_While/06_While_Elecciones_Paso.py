import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        candidato_mas_votado = ("", 0)
        candidato_menos_votado = ("", 0)
        promedio_edad = 0
        acumulador = 0
        total_votos = 0
        while True:
            nombre = prompt("Elecciones PASO", "Ingrese el nombre del candito")
            if nombre == None:
                break
            while nombre.isdigit():
                nombre = prompt("ERROR", "El nombre no puede contener numeros, porfavor reingrese el nombre")
                if not (nombre.isdigit):
                    break
                else:
                    continue
            edad = prompt("Elecciones PASO", "Ingrese la edad del candidato")
            if edad == None:
                break
            edad = int(edad)
            while (edad <= 25):
                edad = prompt("ERROR", "La edad no puede ser menor o igual a 25, porfavor reingrese la edad")
                edad = int(edad)
                if (edad > 25) or None:
                    break
                else:
                    continue
            votos = prompt("Elecciones Paso", "Ingrese los votos del candidato")
            if votos == None:
                break
            elif votos.isalpha():
                while votos.isalpha():
                    votos = prompt("ERROR", "Reingrese los votos del candidato")
                    if votos == None or not (votos.isalpha()):
                        break
                    else:
                        continue
            votos = int(votos)
            if votos < 0:
                while votos < 0:
                    votos = prompt("ERROR", "Reingrese los votos del candidato")
                    votos = int(votos)
                    if votos == None or votos >= 0:
                        break
                    else:
                        continue
            if (acumulador == 0):
                candidato_mas_votado = (nombre, votos)
                candidato_menos_votado = (nombre, votos)
            else:
                if votos > candidato_mas_votado[1]:
                    candidato_mas_votado = (nombre, votos)
                elif votos < candidato_menos_votado[1]:
                    candidato_menos_votado = (nombre, votos)
            promedio_edad += edad
            total_votos += votos
            acumulador += 1
        promedio_edad = promedio_edad / acumulador
        mensaje = (f"Candidato mas votado: {candidato_mas_votado[0]}.\nCandidato menos votado: {candidato_menos_votado[0]} con {candidato_menos_votado[1]} votos.\nEl promedio de la edad de los candidatos es: {promedio_edad}. \nTotal de votos : {total_votos}")
        alert("ELECCIONES PASO", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
