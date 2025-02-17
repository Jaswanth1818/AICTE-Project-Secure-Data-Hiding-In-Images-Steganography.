from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from PIL import Image
import stepic

def encrypt_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    secret_message = message_entry.get().strip()
    password = password_entry.get().strip()

    if not secret_message or not password:
        messagebox.showerror("Error", "Please enter both secret message and password!")
        return
    
    try:
        img = Image.open(file_path)
        encoded_message = f"{password}||{secret_message}"  # Use a unique delimiter
        encoded_image = stepic.encode(img, encoded_message.encode('utf-8'))

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            encoded_image.save(save_path)
            messagebox.showinfo("Success", "Message encrypted and saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

# GUI Setup
root = Tk()
root.title("Steganography - Encrypt")
root.geometry("400x250")

Label(root, text="Enter Secret Message:").pack(pady=5)
message_entry = Entry(root, width=40)
message_entry.pack(pady=5)

Label(root, text="Enter Passcode:").pack(pady=5)
password_entry = Entry(root, width=40, show="*")
password_entry.pack(pady=5)

Button(root, text="Select Image & Encrypt", command=encrypt_message).pack(pady=10)

root.mainloop()
