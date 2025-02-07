import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ignacio Agustin
apellido: Herrera
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    G. El máximo valor. 
    H. El mínimo valor (incluyendo en que iteracion se encontro, solo la primera)

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        contador = 0
        while True:
            numero_str = prompt("Ingresar número", "Ingrese un número (presione Cancelar para finalizar):")
            if numero_str == None:
                break
            contador += 1
            while numero_str == "":
                numero_str = prompt("ERROR", "Ingrese un número valido (presione Cancelar para finalizar):")
            numero = float(numero_str)
            if numero > 0:
                suma_positivos += numero
                cantidad_positivos += 1
            elif numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
            else:
                cantidad_ceros += 1
            if contador == 1 or numero > maximo_valor:
                maximo_valor = numero
            if contador == 1 or numero < minimo_valor:
                minimo_valor = numero
                iteracion = contador 
        diferencia = cantidad_positivos - cantidad_negativos
        if diferencia < 0:
            diferencia *= -1
        if contador == 0:
            resultado = "No se han igresado datos"
        else:
            resultado = (
            f"A. Suma de negativos: {suma_negativos}\n"
            f"B. Suma de positivos: {suma_positivos}\n"
            f"C. Cantidad de números positivos: {cantidad_positivos}\n"
            f"D. Cantidad de números negativos: {cantidad_negativos}\n"
            f"E. Cantidad de ceros: {cantidad_ceros}\n"
            f"F. Diferencia entre positivos y negativos: {diferencia}\n"
            f"G. Valor maximo: {maximo_valor}\n"
            f"H. Valor minimo: {minimo_valor} en iteracion {iteracion}\n"
        )
        alert("Resultados", resultado)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
