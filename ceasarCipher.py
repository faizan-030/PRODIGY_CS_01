import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def encrypt_button_click():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
        encrypted_text = caesar_encrypt(text, shift)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer.")

def decrypt_button_click():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
        decrypted_text = caesar_decrypt(text, shift)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer.")

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher Encryptor/Decryptor")

# Create widgets
label_text = tk.Label(window, text="Enter text:")
label_text.grid(row=0, column=0, padx=10, pady=10)

entry_text = tk.Text(window, height=5, width=50)
entry_text.grid(row=0, column=1, padx=10, pady=10)

label_shift = tk.Label(window, text="Enter shift (integer):")
label_shift.grid(row=1, column=0, padx=10, pady=10)

entry_shift = tk.Entry(window)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_button_click)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_button_click)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

text_output = tk.Text(window, height=5, width=50)
text_output.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the main loop
window.mainloop()

