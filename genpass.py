import string
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def validar_longitud(longi, tipos_seleccionados):
    if longi < tipos_seleccionados:
        raise ValueError(f"La longitud debe ser al menos {tipos_seleccionados} para incluir todos los tipos de caracteres seleccionados.")
    if longi > 10000:
        raise ValueError(f"La longitud debe ser de menos de 10000 caracteres para evitar sobrecargar de Hardware.")

def construir_conjunto_caracteres():
    caracteres = ""
    if var_lower.get():
        caracteres += string.ascii_lowercase
    if var_upper.get():
        caracteres += string.ascii_uppercase
    if var_digits.get():
        caracteres += string.digits
    if var_special.get():
        caracteres += string.punctuation
    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")
    return caracteres

def generar_contraseña():
    try:
        longi = int(entry_longitud.get())
        tipos_seleccionados = sum([var_lower.get(), var_upper.get(), var_digits.get(), var_special.get()])
        validar_longitud(longi, tipos_seleccionados)
        
        caracteres = construir_conjunto_caracteres()
        
        # Generar la contraseña
        contraseña = []
        if var_lower.get():
            contraseña.append(random.choice(string.ascii_lowercase))
        if var_upper.get():
            contraseña.append(random.choice(string.ascii_uppercase))
        if var_digits.get():
            contraseña.append(random.choice(string.digits))
        if var_special.get():
            contraseña.append(random.choice(string.punctuation))
        
        # Completar la contraseña con caracteres aleatorios
        contraseña += [random.choice(caracteres) for _ in range(longi - len(contraseña))]
        random.shuffle(contraseña)
        contraseña = "".join(contraseña)
        
        # Mostrar la contraseña en el Entry
        entry_contraseña.config(state=tk.NORMAL)
        entry_contraseña.delete(0, tk.END)
        entry_contraseña.insert(0, contraseña)
        entry_contraseña.config(state='readonly')

        # Copiar automáticamente si la opción está habilitada
        if var_autocopy.get():
            copiar_contraseña()
        
        messagebox.showinfo("Contraseña Generada", "Contraseña generada y copiada al portapapeles." if var_autocopy.get() else "Contraseña generada.")
    except ValueError as ve:
        messagebox.showerror("Error", f"Entrada inválida: {ve}")

def copiar_contraseña():
    contraseña = entry_contraseña.get()
    if contraseña:
        root.clipboard_clear()
        root.clipboard_append(contraseña)
        messagebox.showinfo("Copiar Contraseña", "Contraseña copiada al portapapeles.")
    else:
        messagebox.showwarning("Copiar Contraseña", "No hay contraseña para copiar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")

# Variables de los checkboxes
var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)
var_autocopy = tk.BooleanVar(value=False)  # Predeterminadamente desactivado

# Crear y colocar los widgets
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(main_frame, text="Ingrese la longitud de la contraseña:").grid(row=0, column=0, columnspan=2, pady=10)
entry_longitud = ttk.Entry(main_frame)
entry_longitud.grid(row=1, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

options_frame = ttk.LabelFrame(main_frame, text="Opciones de caracteres", padding="10")
options_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

ttk.Checkbutton(options_frame, text="Incluir letras minúsculas", variable=var_lower).grid(row=0, column=0, sticky=tk.W)
ttk.Checkbutton(options_frame, text="Incluir letras mayúsculas", variable=var_upper).grid(row=1, column=0, sticky=tk.W)
ttk.Checkbutton(options_frame, text="Incluir números", variable=var_digits).grid(row=2, column=0, sticky=tk.W)
ttk.Checkbutton(options_frame, text="Incluir caracteres especiales", variable=var_special).grid(row=3, column=0, sticky=tk.W)

# Opción de copiar automáticamente, separada del grupo de opciones de caracteres
ttk.Checkbutton(main_frame, text="Copiar automáticamente", variable=var_autocopy).grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.W)

ttk.Button(main_frame, text="Generar Contraseña", command=generar_contraseña).grid(row=4, column=0, columnspan=2, pady=20)

ttk.Label(main_frame, text="Contraseña Generada:").grid(row=5, column=0, pady=10, sticky=tk.W)
entry_contraseña = ttk.Entry(main_frame, width=50, state='readonly')
entry_contraseña.grid(row=6, column=0, pady=10, sticky=(tk.W, tk.E))

ttk.Button(main_frame, text="Copiar Contraseña", command=copiar_contraseña).grid(row=6, column=1, pady=10, padx=5, sticky=tk.W)

# Ajustar las columnas para que se expandan
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Iniciar el bucle principal de la interfaz
root.mainloop()
