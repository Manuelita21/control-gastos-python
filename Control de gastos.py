import sqlite3
from tkinter import *

def crear_db():
    conn = sqlite3.connect('gastos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT NOT NULL,
        cantidad REAL NOT NULL,
        fecha TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def insertar_gasto():
    conn = sqlite3.connect('gastos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO gastos (categoria, cantidad, fecha) VALUES (?, ?, ?)",
                   (entrada_categoria.get(), entrada_cantidad.get(), entrada_fecha.get()))
    conn.commit()
    conn.close()
    entrada_categoria.delete(0, END)
    entrada_cantidad.delete(0, END)
    entrada_fecha.delete(0, END)


app = Tk()
app.title("Control de gastos")
app.geometry("300x200")

Label(app, text="Categoría:").pack()
entrada_categoria = Entry(app)
entrada_categoria.pack()

Label(app, text="Cantidad:").pack()
entrada_cantidad = Entry(app)
entrada_cantidad.pack()

Label(app, text="Fecha (YYYY-MM-DD):").pack()
entrada_fecha = Entry(app)
entrada_fecha.pack()

def mostrar_gastos():
    conn = sqlite3.connect('gastos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gastos")
    registros = cursor.fetchall()
    conn.close()

    ventana = Toplevel(app)
    ventana.title("Gastos registrados")

    for gasto in registros:
        texto = f"ID: {gasto[0]} | Categoría: {gasto[1]} | Cantidad: {gasto[2]} | Fecha: {gasto[3]}"
        Label(ventana, text=texto).pack()

Button(app, text="Agregar gasto", command=insertar_gasto).pack()
Button(app, text="Mostrar gastos", command=mostrar_gastos).pack()


crear_db()
app.mainloop()



