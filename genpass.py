import string
import random
import tkinter as tk
from tkinter import messagebox

def generar_contraseña():
    try:
        longi = int(entry_longitud.get())
        if longi < 1:
            raise ValueError("La longitud debe ser al menos 1.")
        
        selected_char_types = sum([var_lower.get(), var_upper.get(), var_digits.get(), var_special.get()])
        if longi < selected_char_types:
            raise ValueError(f"La longitud debe ser al menos {selected_char_types} para incluir todos los tipos de caracteres seleccionados.")
        
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
        
        # Mezclar la contraseña para que los primeros caracteres no sigan siempre el mismo patrón
        random.shuffle(contraseña)
        
        # Convertir la lista en una cadena
        contraseña = "".join(contraseña)
        
        # Mostrar la contraseña en el Entry
        entry_contraseña.delete(0, tk.END)
        entry_contraseña.insert(0, contraseña)
        
        messagebox.showinfo("Contraseña Generada", f"Tu nueva contraseña es: {contraseña}")
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

# Crear y colocar los widgets
tk.Label(root, text="Ingrese la longitud de la contraseña:").pack(pady=10)
entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=5)

tk.Checkbutton(root, text="Incluir letras minúsculas", variable=var_lower).pack(anchor=tk.W, padx=20)
tk.Checkbutton(root, text="Incluir letras mayúsculas", variable=var_upper).pack(anchor=tk.W, padx=20)
tk.Checkbutton(root, text="Incluir números", variable=var_digits).pack(anchor=tk.W, padx=20)
tk.Checkbutton(root, text="Incluir caracteres especiales", variable=var_special).pack(anchor=tk.W, padx=20)

tk.Button(root, text="Generar Contraseña", command=generar_contraseña).pack(pady=20)

# Entry para mostrar la contraseña generada
entry_contraseña = tk.Entry(root, width=50)
entry_contraseña.pack(pady=10)

# Botón para copiar la contraseña
tk.Button(root, text="Copiar Contraseña", command=copiar_contraseña).pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()



