import tkinter as tk
from tkinter import messagebox, simpledialog
import math
import matplotlib.pyplot as plt

class TablaFrecuencias:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de Frecuencias")
        self.root.geometry("600x400")
        self.root.configure(bg="#f4f6f7")
        self.root.state("zoomed")  # O usa self.root.attributes("-fullscreen", True)
        

        # ---- Entrada de datos iniciales ----
        frame_input = tk.Frame(root, bg="#d6eaf8", pady=10, padx=10, relief="groove", bd=2)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Límite Inferior (Li)", bg="#d6eaf8").grid(row=0, column=0, padx=5)
        self.li_entry = tk.Entry(frame_input, width=10)
        self.li_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame_input, text="Límite Superior (Ls)", bg="#d6eaf8").grid(row=0, column=2, padx=5)
        self.ls_entry = tk.Entry(frame_input, width=10)
        self.ls_entry.grid(row=0, column=3, padx=5)

        tk.Label(frame_input, text="Amplitud", bg="#d6eaf8").grid(row=0, column=4, padx=5)
        self.amp_entry = tk.Entry(frame_input, width=10)
        self.amp_entry.grid(row=0, column=5, padx=5)

        tk.Button(frame_input, text="Generar Intervalos", command=self.generar_intervalos, bg="#5dade2", fg="white").grid(row=0, column=6, padx=10)

        # ---- Frame para la tabla ----
        self.table_frame = tk.Frame(root, bg="#f4f6f7")
        self.table_frame.pack(pady=10)

        tk.Button(root, text="Calcular FI", command=self.calcular_fi, bg="#27ae60", fg="white").pack(pady=5)

        # ---- Frame inferior con botones organizados ----
        frame_botones = tk.Frame(root, bg="#f4f6f7", pady=15)
        frame_botones.pack(side="bottom", fill="x")

        # Configurar 3 columnas centradas
        frame_botones.grid_columnconfigure(0, weight=1)
        frame_botones.grid_columnconfigure(1, weight=1)
        frame_botones.grid_columnconfigure(2, weight=1)



        # Columna izquierda → Medidas de posición
        frame_posicion = tk.LabelFrame(frame_botones, text="📊 Medidas de Posición y Proporción", 
                                       bg="#d6eaf8", padx=20, pady=10, font=("Arial", 10, "bold"))
        frame_posicion.grid(row=0, column=0, padx=50, pady=10, sticky="n")

        botones_pos = [
            ("Media", self.calcular_media, "#1abc9c"),
            ("Mediana", self.calcular_mediana, "#3498db"),
            ("Moda", self.calcular_moda, "#9b59b6"),
            ("Cuartiles", self.calcular_cuartil, "#e67e22"),
            ("Deciles", self.calcular_decil, "#16a085"),
            ("Percentiles", self.calcular_percentil, "#c0392b")
        ]

        for txt, cmd, color in botones_pos:
            tk.Button(frame_posicion, text=txt, width=18, command=cmd, bg=color, fg="white").pack(pady=4)

        # Columna derecha → Medidas de dispersión
        frame_dispersion = tk.LabelFrame(frame_botones, text="📉 Medidas de Dispersión", 
                                         bg="#d6eaf8", padx=20, pady=10, font=("Arial", 10, "bold"))
        frame_dispersion.grid(row=0, column=1, padx=50, pady=10, sticky="n")

        botones_disp = [
            ("Rango", self.calcular_rango, "#2ecc71"),
            ("Varianza", self.calcular_varianza, "#f39c12"),
            ("Desviación Estándar", self.calcular_desviacion, "#d35400"),
            ("Coef. de Variación", self.calcular_cv, "#8e44ad")
        ]

        for txt, cmd, color in botones_disp:
            tk.Button(frame_dispersion, text=txt, width=20, command=cmd, bg=color, fg="white").pack(pady=4)

        
        # ---- Frame para gráficos ----
        frame_graficos = tk.LabelFrame(frame_botones, text="📈 Gráficos", 
                                    bg="#d6eaf8", padx=20, pady=10, font=("Arial", 10, "bold"))
        frame_graficos.grid(row=0, column=2, padx=50, pady=10, sticky="n")

        botones_graf = [
            ("Histograma", self.mostrar_histograma, "#e74c3c"),
            ("Polígono de Frecuencias", self.mostrar_poligono, "#2980b9"),
            ("Ojiva", self.mostrar_ojiva, "#27ae60")
        ]

        for txt, cmd, color in botones_graf:
            tk.Button(frame_graficos, text=txt, width=20, command=cmd, bg=color, fg="white").pack(pady=4)


        # Cabecera
        self.headers = ["Li", "Ls", "fi", "Fi"]
        for col, header in enumerate(self.headers):
            label = tk.Label(self.table_frame, text=header, width=12, borderwidth=2, relief="ridge", bg="#2e86c1", fg="white")
            label.grid(row=0, column=col, padx=1, pady=1)

        self.filas = []

    def generar_intervalos(self):
        # Limpiar filas anteriores
        for fila in self.filas:
            for widget in fila:
                widget.destroy()
        self.filas.clear()

        try:
            li = int(self.li_entry.get())
            ls = int(self.ls_entry.get())
            amp = int(self.amp_entry.get())

            if li >= ls or amp <= 0:
                messagebox.showerror("Error", "Revisa los valores de Li, Ls y Amplitud.")
                return

            fila_idx = 1
            while li < ls:
                intervalo_ls = li + amp
                if intervalo_ls > ls:
                    intervalo_ls = ls

                li_label = tk.Label(self.table_frame, text=str(li), width=12, borderwidth=1, relief="solid", bg="#d5dbdb")
                li_label.grid(row=fila_idx, column=0, padx=1, pady=1)

                ls_label = tk.Label(self.table_frame, text=str(intervalo_ls), width=12, borderwidth=1, relief="solid", bg="#d5dbdb")
                ls_label.grid(row=fila_idx, column=1, padx=1, pady=1)

                fi_entry = tk.Entry(self.table_frame, width=12, borderwidth=1, relief="solid", bg="#f9e79f")
                fi_entry.grid(row=fila_idx, column=2, padx=1, pady=1)

                self.filas.append([li_label, ls_label, fi_entry])

                li = intervalo_ls
                fila_idx += 1

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def calcular_fi(self):
        try:
            acumulado = 0
            for fila in self.filas:
                fi_entry = fila[2]
                fi_val = int(fi_entry.get())
                acumulado += fi_val

                # Si aún no existe el campo Fi, lo crea
                if len(fila) == 3:  
                    fi_label = tk.Label(self.table_frame, text=str(acumulado), width=12, borderwidth=1, relief="solid", bg="#abebc6")
                    fi_label.grid(row=self.filas.index(fila)+1, column=3, padx=1, pady=1)
                    fila.append(fi_label)
                else:  # Si ya existe, lo actualiza
                    fila[3].config(text=str(acumulado))

        except ValueError:
            messagebox.showerror("Error", "Ingrese solo valores numéricos en fi.")

     # ---------------- Medidas de posición ----------------
    def calcular_media(self):
        try:
            datos = self.obtener_datos()
            N = sum(fi for _, fi in datos)
            if N == 0:
                messagebox.showerror("Error", "Las frecuencias no pueden sumar 0.")
                return
            media = sum(mc * fi for mc, fi in datos) / N
            messagebox.showinfo("Media", f"La media es: {media:.4f}")
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def calcular_mediana(self):
        try:
            N = sum(int(fila[2].get()) for fila in self.filas)
            pos = N / 2
            acumulado = 0

            for fila in self.filas:
                Li = int(fila[0].cget("text"))
                Ls = int(fila[1].cget("text"))
                fi = int(fila[2].get())
                acumulado += fi

                if acumulado >= pos:
                    F_prev = acumulado - fi
                    c = Ls - Li
                    mediana = Li + ((pos - F_prev) / fi) * c
                    messagebox.showinfo("Mediana", f"La Mediana es: {mediana:.2f}")
                    return
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def calcular_moda(self):
        try:
            max_fi = max(int(fila[2].get()) for fila in self.filas)
            for i, fila in enumerate(self.filas):
                fi = int(fila[2].get())
                if fi == max_fi:
                    Li = int(fila[0].cget("text"))
                    Ls = int(fila[1].cget("text"))
                    c = Ls - Li
                    f1 = fi
                    f0 = int(self.filas[i-1][2].get()) if i > 0 else 0
                    f2 = int(self.filas[i+1][2].get()) if i < len(self.filas)-1 else 0
                    moda = Li + ((f1 - f0) / ((2*f1 - f0 - f2))) * c
                    messagebox.showinfo("Moda", f"La Moda es: {moda:.2f}")
                    return
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def calcular_cuartil(self):
        try:
            k = simpledialog.askinteger("Cuartil", "Ingrese k (1-3):")
            if not (1 <= k <= 3):
                messagebox.showerror("Error", "k debe estar entre 1 y 3.")
                return

            N = sum(int(fila[2].get()) for fila in self.filas)
            pos = (k * N) / 4
            acumulado = 0

            for fila in self.filas:
                Li = int(fila[0].cget("text"))
                Ls = int(fila[1].cget("text"))
                fi = int(fila[2].get())
                acumulado += fi

                if acumulado >= pos:
                    F_prev = acumulado - fi
                    c = Ls - Li
                    Qk = Li + ((pos - F_prev) / fi) * c
                    messagebox.showinfo("Cuartil", f"Q{k} = {Qk:.2f}")
                    return
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def calcular_decil(self):
        try:
            k = simpledialog.askinteger("Decil", "Ingrese k (1-9):")
            if not (1 <= k <= 9):
                messagebox.showerror("Error", "k debe estar entre 1 y 9.")
                return

            N = sum(int(fila[2].get()) for fila in self.filas)
            pos = (k * N) / 10
            acumulado = 0

            for fila in self.filas:
                Li = int(fila[0].cget("text"))
                Ls = int(fila[1].cget("text"))
                fi = int(fila[2].get())
                acumulado += fi

                if acumulado >= pos:
                    F_prev = acumulado - fi
                    c = Ls - Li
                    Dk = Li + ((pos - F_prev) / fi) * c
                    messagebox.showinfo("Decil", f"D{k} = {Dk:.2f}")
                    return
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def calcular_percentil(self):
        try:
            k = simpledialog.askinteger("Percentil", "Ingrese k (1-99):")
            if not (1 <= k <= 99):
                messagebox.showerror("Error", "k debe estar entre 1 y 99.")
                return

            N = sum(int(fila[2].get()) for fila in self.filas)
            pos = (k * N) / 100
            acumulado = 0

            for fila in self.filas:
                Li = int(fila[0].cget("text"))
                Ls = int(fila[1].cget("text"))
                fi = int(fila[2].get())
                acumulado += fi

                if acumulado >= pos:
                    F_prev = acumulado - fi
                    c = Ls - Li
                    Pk = Li + ((pos - F_prev) / fi) * c
                    messagebox.showinfo("Percentil", f"P{k} = {Pk:.2f}")
                    return
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")


    # ---------------- Medidas de dispersión ----------------
    def obtener_datos(self):
        """ Devuelve lista de (marca de clase, fi) """
        datos = []
        for fila in self.filas:
            Li = int(fila[0].cget("text"))
            Ls = int(fila[1].cget("text"))
            fi = int(fila[2].get())
            marca = (Li + Ls) / 2
            datos.append((marca, fi))
        return datos

    def calcular_rango(self):
        try:
            datos = self.obtener_datos()
            marcas = [mc for mc, _ in datos]
            rango = max(marcas) - min(marcas)
            messagebox.showinfo("Rango", f"El rango es: {rango:.2f}")
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def calcular_varianza(self):
        try:
            datos = self.obtener_datos()
            N = sum(fi for _, fi in datos)
            media = sum(mc * fi for mc, fi in datos) / N
            varianza = sum(fi * ((mc - media) ** 2) for mc, fi in datos) / N
            messagebox.showinfo("Varianza", f"La varianza es: {varianza:.2f}")
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def calcular_desviacion(self):
        try:
            datos = self.obtener_datos()
            N = sum(fi for _, fi in datos)
            media = sum(mc * fi for mc, fi in datos) / N
            varianza = sum(fi * ((mc - media) ** 2) for mc, fi in datos) / N
            desviacion = math.sqrt(varianza)
            messagebox.showinfo("Desviación Estándar", f"La desviación estándar es: {desviacion:.2f}")
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def calcular_cv(self):
        try:
            datos = self.obtener_datos()
            N = sum(fi for _, fi in datos)
            media = sum(mc * fi for mc, fi in datos) / N
            varianza = sum(fi * ((mc - media) ** 2) for mc, fi in datos) / N
            desviacion = math.sqrt(varianza)
            cv = (desviacion / media) * 100
            messagebox.showinfo("Coeficiente de Variación", f"El CV es: {cv:.2f}%")
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")
    

        # ---------------- Métodos para gráficos ----------------
    def mostrar_histograma(self):
        try:
            datos = self.obtener_datos()
            marcas = [mc for mc, _ in datos]
            fi = [f for _, f in datos]
            plt.bar(marcas, fi, width=(marcas[1]-marcas[0])*0.9 if len(marcas)>1 else 1, color="#3498db", edgecolor="black")
            plt.xlabel("Marca de Clase")
            plt.ylabel("Frecuencia")
            plt.title("Histograma")
            plt.show()
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def mostrar_poligono(self):
        try:
            datos = self.obtener_datos()
            marcas = [mc for mc, _ in datos]
            fi = [f for _, f in datos]
            plt.plot(marcas, fi, marker='o', linestyle='-', color="#9b59b6")
            plt.xlabel("Marca de Clase")
            plt.ylabel("Frecuencia")
            plt.title("Polígono de Frecuencias")
            plt.grid(True)
            plt.show()
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

    def mostrar_ojiva(self):
        try:
            datos = self.obtener_datos()
            fi = [f for _, f in datos]
            Fi = []
            acumulado = 0
            for f in fi:
                acumulado += f
                Fi.append(acumulado)
            ls = [int(fila[1].cget("text")) for fila in self.filas]
            plt.plot(ls, Fi, marker='o', linestyle='-', color="#e67e22")
            plt.xlabel("Límite Superior")
            plt.ylabel("Frecuencia Acumulada (Fi)")
            plt.title("Ojiva")
            plt.grid(True)
            plt.show()
        except:
            messagebox.showerror("Error", "Complete correctamente la tabla fi.")

# ---- Ejecutar programa ----
if __name__ == "__main__":
    root = tk.Tk()
    app = TablaFrecuencias(root)
    root.mainloop()
