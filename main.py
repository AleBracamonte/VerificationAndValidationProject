import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def verificar_lados(lado1, lado2, lado3):
    return lado1 > 0 and lado2 > 0 and lado3 > 0

def calcular_tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

def graficar_triangulo(lado1, lado2, lado3):
    fig, ax = plt.subplots()
    ax.plot([0, lado1, lado2, 0], [0, 0, lado3, 0], 'ro-')
    ax.set_xlim(0, max(lado1, lado2) + 1)
    ax.set_ylim(0, lado3 + 1)
    return fig

def on_calcular():
    lado1 = entrada_lado1.get()
    lado2 = entrada_lado2.get()
    lado3 = entrada_lado3.get()

    if es_entero(lado1) and es_entero(lado2) and es_entero(lado3):
        lado1, lado2, lado3 = int(lado1), int(lado2), int(lado3)

        if verificar_lados(lado1, lado2, lado3):
            tipo_triangulo = calcular_tipo_triangulo(lado1, lado2, lado3)
            resultado.set(f'Tipo de triángulo: {tipo_triangulo}')

            # Graficar el triángulo en la interfaz gráfica
            fig = graficar_triangulo(lado1, lado2, lado3)
            canvas = FigureCanvasTkAgg(fig, master=ventana)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=4, column=0, columnspan=3)

        else:
            resultado.set('Los lados deben ser mayores a 0.')
    else:
        resultado.set('Ingrese valores enteros válidos.')

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title('Tipo de Triángulo')

etiqueta_lado1 = ttk.Label(ventana, text='Lado 1:')
etiqueta_lado1.grid(row=0, column=0)
entrada_lado1 = ttk.Entry(ventana)
entrada_lado1.grid(row=0, column=1)

etiqueta_lado2 = ttk.Label(ventana, text='Lado 2:')
etiqueta_lado2.grid(row=1, column=0)
entrada_lado2 = ttk.Entry(ventana)
entrada_lado2.grid(row=1, column=1)

etiqueta_lado3 = ttk.Label(ventana, text='Lado 3:')
etiqueta_lado3.grid(row=2, column=0)
entrada_lado3 = ttk.Entry(ventana)
entrada_lado3.grid(row=2, column=1)

boton_calcular = ttk.Button(ventana, text='Calcular', command=on_calcular)
boton_calcular.grid(row=3, column=0, columnspan=2)

resultado = tk.StringVar()
etiqueta_resultado = ttk.Label(ventana, textvariable=resultado)
etiqueta_resultado.grid(row=3, column=2)

ventana.mainloop()
