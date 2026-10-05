# -*- coding: utf-8 -*-
"""
Registro para Farmacia (Tkinter)
--------------------------------
Aplicación de escritorio para registrar medicamentos.
Incluye: Tk, Frame, Toplevel (ventana emergente), Label, Button,
Entry, Text, Checkbutton, Radiobutton, Combobox y Treeview.
Tema: rosado suave (tonos pastel, nada estridente).
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------------------------
# Paleta de color rosado suave
# ---------------------------------------------------------------------------
COLOR_FONDO = "#FBEEEF"    # rosado muy claro
COLOR_PANEL = "#F6DEE3"    # rosado pastel
COLOR_ACENTO = "#D9A5B3"   # rosado medio
COLOR_BOTON = "#E4B7C2"    # rosado suave
COLOR_BOTON_HOVER = "#D9A0B0"
COLOR_TEXTO = "#6B4B57"    # guinda suave
COLOR_BLANCO = "#FFF9FA"


# ---------------------------------------------------------------------------
# Toplevel: ventana emergente (equivalente al QDialog)
# ---------------------------------------------------------------------------
class DialogoProveedor(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registrar proveedor")
        self.configure(bg=COLOR_FONDO)
        self.resizable(False, False)
        self.result = None

        tk.Label(self, text="Datos del proveedor",
                 bg=COLOR_PANEL, fg=COLOR_TEXTO,
                 font=("Arial", 13, "bold"), padx=10, pady=8).grid(
            row=0, column=0, columnspan=2, sticky="we", padx=15, pady=(15, 10))

        tk.Label(self, text="Nombre:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=1, column=0, sticky="e", padx=10, pady=4)
        self.txt_nombre = tk.Entry(self, width=32, bg=COLOR_BLANCO, fg=COLOR_TEXTO, relief="solid", bd=1)
        self.txt_nombre.grid(row=1, column=1, padx=10, pady=4)

        tk.Label(self, text="Teléfono:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=2, column=0, sticky="e", padx=10, pady=4)
        self.txt_telefono = tk.Entry(self, width=32, bg=COLOR_BLANCO, fg=COLOR_TEXTO, relief="solid", bd=1)
        self.txt_telefono.grid(row=2, column=1, padx=10, pady=4)

        tk.Label(self, text="Correo:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=3, column=0, sticky="e", padx=10, pady=4)
        self.txt_correo = tk.Entry(self, width=32, bg=COLOR_BLANCO, fg=COLOR_TEXTO, relief="solid", bd=1)
        self.txt_correo.grid(row=3, column=1, padx=10, pady=4)

        tk.Label(self, text="Tipo:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=4, column=0, sticky="e", padx=10, pady=4)
        self.cmb_tipo = ttk.Combobox(self, values=["Mayorista", "Minorista", "Laboratorio"],
                                     state="readonly", width=29)
        self.cmb_tipo.set("Mayorista")
        self.cmb_tipo.grid(row=4, column=1, padx=10, pady=4)

        tk.Label(self, text="Origen:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=5, column=0, sticky="e", padx=10, pady=4)
        self.origen = tk.StringVar(value="Nacional")
        tk.Radiobutton(self, text="Nacional", variable=self.origen, value="Nacional",
                       bg=COLOR_FONDO, fg=COLOR_TEXTO, activebackground=COLOR_FONDO).grid(row=5, column=1, sticky="w")
        tk.Radiobutton(self, text="Internacional", variable=self.origen, value="Internacional",
                       bg=COLOR_FONDO, fg=COLOR_TEXTO, activebackground=COLOR_FONDO).grid(row=6, column=1, sticky="w")

        self.autorizado = tk.BooleanVar(value=True)
        tk.Checkbutton(self, text="Es distribuidor autorizado", variable=self.autorizado,
                       bg=COLOR_FONDO, fg=COLOR_TEXTO, activebackground=COLOR_FONDO).grid(row=7, column=1, sticky="w", pady=4)

        tk.Label(self, text="Notas:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=8, column=0, sticky="ne", padx=10, pady=4)
        self.txt_notas = tk.Text(self, width=32, height=4, bg=COLOR_BLANCO, fg=COLOR_TEXTO,
                                 relief="solid", bd=1)
        self.txt_notas.grid(row=8, column=1, padx=10, pady=4)

        fila = tk.Frame(self, bg=COLOR_FONDO)
        fila.grid(row=9, column=0, columnspan=2, pady=(10, 15))
        tk.Button(fila, text="Cancelar", bg=COLOR_BOTON, fg=COLOR_TEXTO, relief="flat",
                  width=12, command=self.destroy).pack(side="left", padx=5)
        tk.Button(fila, text="Guardar", bg=COLOR_BOTON, fg=COLOR_TEXTO, relief="flat",
                  width=12, command=self.guardar).pack(side="left", padx=5)

        self.grab_set()
        self.transient(parent)

    def guardar(self):
        self.result = {
            "nombre": self.txt_nombre.get().strip(),
            "telefono": self.txt_telefono.get().strip(),
            "correo": self.txt_correo.get().strip(),
            "tipo": self.cmb_tipo.get(),
            "origen": self.origen.get(),
            "autorizado": self.autorizado.get(),
            "notas": self.txt_notas.get("1.0", "end").strip(),
        }
        self.destroy()


# ---------------------------------------------------------------------------
# Ventana principal
# ---------------------------------------------------------------------------
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Farmacia - Registro de Medicamentos")
        self.geometry("900x620")
        self.configure(bg=COLOR_FONDO)

        # Estilo de ttk para Combobox y Treeview
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("Treeview", background=COLOR_BLANCO, foreground=COLOR_TEXTO,
                         fieldbackground=COLOR_BLANCO, rowheight=24)
        estilo.configure("Treeview.Heading", background=COLOR_BOTON, foreground=COLOR_TEXTO,
                         font=("Arial", 10, "bold"))
        estilo.map("Treeview", background=[("selected", COLOR_ACENTO)])

        tk.Label(self, text="Registro de Medicamentos", bg=COLOR_PANEL, fg=COLOR_TEXTO,
                 font=("Arial", 16, "bold"), padx=10, pady=10).pack(fill="x", padx=10, pady=10)

        # ---------------- Pie de página ----------------
        tk.Label(self, text="Creado por Jhudith Romero - 2026",
                 bg=COLOR_PANEL, fg=COLOR_TEXTO,
                 font=("Arial", 10, "italic"), padx=10, pady=6).pack(
            side="bottom", fill="x", padx=10, pady=(5, 10))

        # ---------------- Panel del formulario ----------------
        panel = tk.Frame(self, bg=COLOR_PANEL, padx=10, pady=10)
        panel.pack(side="left", fill="y", padx=10, pady=5)

        tk.Label(panel, text="Nombre:", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(row=0, column=0, sticky="e", pady=4)
        self.txt_nombre = tk.Entry(panel, width=28, bg=COLOR_BLANCO, fg=COLOR_TEXTO, relief="solid", bd=1)
        self.txt_nombre.grid(row=0, column=1, pady=4)

        tk.Label(panel, text="Dosis:", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(row=1, column=0, sticky="e", pady=4)
        self.txt_dosis = tk.Entry(panel, width=28, bg=COLOR_BLANCO, fg=COLOR_TEXTO, relief="solid", bd=1)
        self.txt_dosis.grid(row=1, column=1, pady=4)

        tk.Label(panel, text="Precio:", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(row=2, column=0, sticky="e", pady=4)
        self.txt_precio = tk.Entry(panel, width=28, bg=COLOR_BLANCO, fg=COLOR_TEXTO, relief="solid", bd=1)
        self.txt_precio.grid(row=2, column=1, pady=4)

        tk.Label(panel, text="Categoría:", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(row=3, column=0, sticky="e", pady=4)
        self.cmb_categoria = ttk.Combobox(panel, values=[
            "Analgésico", "Antibiótico", "Antihistamínico",
            "Antiinflamatorio", "Vitaminas", "Otro",
        ], state="readonly", width=25)
        self.cmb_categoria.set("Analgésico")
        self.cmb_categoria.grid(row=3, column=1, pady=4)

        tk.Label(panel, text="Presentación:", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(row=4, column=0, sticky="e", pady=4)
        self.cmb_presentacion = ttk.Combobox(panel, values=[
            "Tabletas", "Jarabe", "Cápsula", "Inyección", "Crema",
        ], state="readonly", width=25)
        self.cmb_presentacion.set("Tabletas")
        self.cmb_presentacion.grid(row=4, column=1, pady=4)

        self.req_receta = tk.BooleanVar(value=False)
        tk.Checkbutton(panel, text="Requiere receta médica", variable=self.req_receta,
                       bg=COLOR_PANEL, fg=COLOR_TEXTO, activebackground=COLOR_PANEL).grid(row=5, column=0, columnspan=2, sticky="w", pady=2)

        self.en_stock = tk.BooleanVar(value=True)
        tk.Checkbutton(panel, text="Disponible en stock", variable=self.en_stock,
                       bg=COLOR_PANEL, fg=COLOR_TEXTO, activebackground=COLOR_PANEL).grid(row=6, column=0, columnspan=2, sticky="w", pady=2)

        self.via = tk.StringVar(value="Oral")
        tk.Radiobutton(panel, text="Vía oral", variable=self.via, value="Oral",
                       bg=COLOR_PANEL, fg=COLOR_TEXTO, activebackground=COLOR_PANEL).grid(row=7, column=0, sticky="w")
        tk.Radiobutton(panel, text="Inyectable", variable=self.via, value="Inyectable",
                       bg=COLOR_PANEL, fg=COLOR_TEXTO, activebackground=COLOR_PANEL).grid(row=7, column=1, sticky="w")
        tk.Radiobutton(panel, text="Tópica", variable=self.via, value="Tópica",
                       bg=COLOR_PANEL, fg=COLOR_TEXTO, activebackground=COLOR_PANEL).grid(row=8, column=0, sticky="w")

        tk.Label(panel, text="Observaciones:", bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(row=9, column=0, sticky="nw", pady=4)
        self.txt_obs = tk.Text(panel, width=28, height=4, bg=COLOR_BLANCO, fg=COLOR_TEXTO,
                               relief="solid", bd=1)
        self.txt_obs.grid(row=10, column=0, columnspan=2, pady=4)

        fila_btn = tk.Frame(panel, bg=COLOR_PANEL)
        fila_btn.grid(row=11, column=0, columnspan=2, pady=6)
        tk.Button(fila_btn, text="Agregar registro", bg=COLOR_BOTON, fg=COLOR_TEXTO, relief="flat",
                  width=16, command=self.agregar_registro).pack(side="left", padx=4)
        tk.Button(fila_btn, text="Limpiar", bg=COLOR_BOTON, fg=COLOR_TEXTO, relief="flat",
                  width=10, command=self.limpiar_formulario).pack(side="left", padx=4)

        # ---------------- Tabla de registros ----------------
        derecha = tk.Frame(self, bg=COLOR_FONDO)
        derecha.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        tk.Label(derecha, text="Medicamentos registrados:", bg=COLOR_FONDO, fg=COLOR_TEXTO,
                 font=("Arial", 11, "bold")).pack(anchor="w")

        columnas = ("Nombre", "Dosis", "Categoría", "Presentación", "Precio", "Receta")
        self.tabla = ttk.Treeview(derecha, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=110, anchor="center")
        self.tabla.pack(fill="both", expand=True, pady=5)

        tk.Label(derecha, text="Historial:", bg=COLOR_FONDO, fg=COLOR_TEXTO,
                 font=("Arial", 11, "bold")).pack(anchor="w")
        self.txt_registro = tk.Text(derecha, height=6, state="disabled",
                                    bg=COLOR_BLANCO, fg=COLOR_TEXTO, relief="solid", bd=1)
        self.txt_registro.pack(fill="x", pady=5)

        # ---------------- Botones laterales ----------------
        laterales = tk.Frame(self, bg=COLOR_FONDO)
        laterales.pack(side="left", fill="y", padx=10, pady=5)
        tk.Button(laterales, text="Registrar proveedor", bg=COLOR_BOTON, fg=COLOR_TEXTO,
                  relief="flat", width=18, command=self.abrir_dialogo_proveedor).pack(pady=6)
        tk.Button(laterales, text="Mostrar resumen", bg=COLOR_BOTON, fg=COLOR_TEXTO,
                  relief="flat", width=18, command=self.mostrar_resumen).pack(pady=6)


    # ------------------------- Métodos -------------------------
    def agregar_registro(self):
        nombre = self.txt_nombre.get().strip()
        dosis = self.txt_dosis.get().strip()
        precio = self.txt_precio.get().strip()

        if not nombre or not dosis or not precio:
            messagebox.showwarning("Datos incompletos", "Completa nombre, dosis y precio.")
            return

        receta = "Sí" if self.req_receta.get() else "No"

        self.tabla.insert("", "end", values=(
            nombre, dosis, self.cmb_categoria.get(),
            self.cmb_presentacion.get(), precio, receta,
        ))

        self.txt_registro.configure(state="normal")
        self.txt_registro.insert("end",
            f"• {nombre} ({dosis}) - {self.cmb_categoria.get()}, "
            f"{self.cmb_presentacion.get()}, vía {self.via.get()}, ${precio}, "
            f"receta: {receta}, stock: {'Sí' if self.en_stock.get() else 'No'}\n"
        )
        obs = self.txt_obs.get("1.0", "end").strip()
        if obs:
            self.txt_registro.insert("end", f"  Obs: {obs}\n")
        self.txt_registro.configure(state="disabled")

        self.limpiar_formulario()

    def limpiar_formulario(self):
        self.txt_nombre.delete(0, "end")
        self.txt_dosis.delete(0, "end")
        self.txt_precio.delete(0, "end")
        self.txt_obs.delete("1.0", "end")
        self.req_receta.set(False)
        self.en_stock.set(True)
        self.via.set("Oral")
        self.cmb_categoria.set("Analgésico")
        self.cmb_presentacion.set("Tabletas")

    def abrir_dialogo_proveedor(self):
        dialogo = DialogoProveedor(self)
        self.wait_window(dialogo)
        if dialogo.result and dialogo.result["nombre"]:
            d = dialogo.result
            self.txt_registro.configure(state="normal")
            self.txt_registro.insert("end",
                f"• Proveedor: {d['nombre']} ({d['tipo']}, {d['origen']}) - {d['telefono']}\n")
            self.txt_registro.configure(state="disabled")

    def mostrar_resumen(self):
        total = len(self.tabla.get_children())
        messagebox.showinfo("Resumen",
                            f"Hay {total} medicamento(s) registrado(s) en la farmacia.")


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
