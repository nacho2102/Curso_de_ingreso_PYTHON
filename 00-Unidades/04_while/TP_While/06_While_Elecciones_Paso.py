import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ignacio Agustin
apellido: Herrera
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
        promedio_edad = 0
        acumulador = 0
        total_votos = 0
        continuar = True
        while continuar:
            nombre = prompt("Elecciones PASO", "Ingrese el nombre del candito")
            if nombre == None:
                break
            while not (nombre.isalpha()):
                nombre = prompt("ERROR", "El nombre no puede contener numeros, porfavor reingrese el nombre")
                if nombre == None:
                    break
                else:
                    continue
            edad = prompt("Elecciones PASO", "Ingrese la edad del candidato")
            if edad == None:
                break
            while not (edad.isdigit() and int(edad) > 25):
                edad = prompt("ERROR", "La edad no puede ser menor o igual a 25, ni letras, porfavor reingrese la edad")
                if edad == None:
                    break
                else:
                    continue
            edad = int(edad)
            votos = prompt("Elecciones Paso", "Ingrese los votos del candidato")
            if votos == None:
                break
            while not (votos.isdigit() and int(votos) >= 0):
                votos = prompt("ERROR", "Reingrese los votos del candidato")
                if votos == None:
                    break
                else:
                    continue
            votos = int(votos)
            if acumulador == 0 or votos > mas_votado:
                candidato_mas_votado = nombre
                mas_votado = votos
            if acumulador == 0 or votos < menos_votos:
                candidato_menos_votado = nombre
                menos_votos = votos
            promedio_edad += edad
            total_votos += votos
            acumulador += 1
            continuar = question("PASO", "Desea seguir ingresando candidatos?")
        if acumulador == 0:
            mensaje = "No se ingresaron todos los datos minimos requeridos"
        else:
            promedio_edad = promedio_edad / acumulador
            mensaje = (
            f"Candidato mas votado: {candidato_mas_votado}.\n"
            f"Candidato menos votado: {candidato_menos_votado} con {menos_votos} votos.\n"
            f"El promedio de la edad de los candidatos es: {promedio_edad}.\n"
            f"Total de votos : {total_votos}"
        )
        alert("ELECCIONES PASO", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
