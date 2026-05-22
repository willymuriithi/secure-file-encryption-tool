import threading
import os
import tkinter as tk
from tkinter import filedialog, messagebox

from encrypt import encrypt_file
from decrypt import decrypt_file


class EncryptionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure File Encryption Tool")
        self.geometry("520x200")
        self.resizable(False, False)

        self.file_path = None
        self.key_path = tk.StringVar(value="secret.key")
        self.mode = tk.StringVar(value="key")  # or 'password'
        self.password_var = tk.StringVar()

        self._build_widgets()

    def _build_widgets(self):
        frm = tk.Frame(self, padx=12, pady=12)
        frm.pack(fill=tk.BOTH, expand=True)

        # Allow the middle columns to expand so labels/entries can grow
        frm.grid_columnconfigure(1, weight=1)
        frm.grid_columnconfigure(2, weight=0)
        frm.grid_columnconfigure(3, weight=0)

        label_font = ("Segoe UI", 10)
        btn_font = ("Segoe UI", 10, "bold")

        tk.Label(frm, text="Selected file:", font=label_font).grid(row=0, column=0, sticky="w")
        self.file_label = tk.Label(frm, text="(none)", anchor="w", width=40, relief=tk.SUNKEN, font=label_font, wraplength=360)
        self.file_label.grid(row=0, column=1, columnspan=3, sticky="we", padx=(6, 0))

        tk.Button(frm, text="Browse...", command=self.browse_file, bg="#B7BBBE", fg="white", activebackground="#515356", font=btn_font, bd=1, relief=tk.RAISED).grid(row=0, column=4, padx=6)

        # Key file entry (visible when mode == 'key')
        tk.Label(frm, text="Key file:", font=label_font).grid(row=1, column=0, sticky="w", pady=(8, 0))
        self.key_entry = tk.Entry(frm, textvariable=self.key_path, font=label_font)
        self.key_entry.grid(row=1, column=1, columnspan=3, sticky="we", padx=(6, 0), pady=(8, 0))
        self.key_browse_btn = tk.Button(frm, text="Browse Key...", command=self.browse_key, bg="#1976D2", fg="white", activebackground="#115293", font=btn_font, bd=1, relief=tk.RAISED)
        self.key_browse_btn.grid(row=1, column=4, padx=6, pady=(8, 0))

        # Password entry (visible when mode == 'password')
        self.pw_label = tk.Label(frm, text="Password:", font=label_font)
        self.pw_entry = tk.Entry(frm, textvariable=self.password_var, font=label_font, show="*")

        # Mode selector
        tk.Label(frm, text="Mode:", font=label_font).grid(row=2, column=0, sticky="w", pady=(12, 0))
        tk.Radiobutton(frm, text="Key file", variable=self.mode, value="key", command=self._on_mode_change, font=label_font).grid(row=2, column=1, sticky="w", pady=(12, 0))
        tk.Radiobutton(frm, text="Password", variable=self.mode, value="password", command=self._on_mode_change, font=label_font).grid(row=2, column=2, sticky="w", pady=(12, 0))

        self.encrypt_btn = tk.Button(frm, text="Encrypt", width=14, command=lambda: self._run_in_thread(self.encrypt), font=btn_font, bg="#2E7D32", fg="white")
        self.encrypt_btn.grid(row=3, column=1, pady=(16, 0))

        self.decrypt_btn = tk.Button(frm, text="Decrypt", width=14, command=lambda: self._run_in_thread(self.decrypt), font=btn_font, bg="#C62828", fg="white")
        self.decrypt_btn.grid(row=3, column=2, pady=(16, 0))

        self.status_label = tk.Label(frm, text="Ready", anchor="w", font=label_font)
        self.status_label.grid(row=4, column=0, columnspan=5, sticky="we", pady=(14, 0))

        # initialize mode UI
        self._on_mode_change()

    def browse_file(self):
        path = filedialog.askopenfilename(title="Select file")
        if path:
            self.file_path = path
            self.file_label.config(text=path)

    def browse_key(self):
        path = filedialog.askopenfilename(title="Select key file", filetypes=[("Key files", "*.key"), ("All files", "*")])
        if path:
            self.key_path.set(path)

    def _on_mode_change(self):
        mode = self.mode.get()
        if mode == "password":
            # hide key widgets
            self.key_entry.grid_remove()
            self.key_browse_btn.grid_remove()
            # show password widgets in the same area
            self.pw_label.grid(row=1, column=0, sticky="w", pady=(8, 0))
            self.pw_entry.grid(row=1, column=1, columnspan=3, sticky="we", padx=(6, 0), pady=(8, 0))
        else:
            # show key widgets
            self.key_entry.grid()
            self.key_browse_btn.grid()
            # hide password widgets
            self.pw_label.grid_remove()
            self.pw_entry.grid_remove()

    def _run_in_thread(self, target):
        t = threading.Thread(target=target, daemon=True)
        t.start()

    def _set_status(self, text):
        def _():
            self.status_label.config(text=text)
        self.after(0, _)

    def _disable_buttons(self):
        def _():
            self.encrypt_btn.config(state=tk.DISABLED)
            self.decrypt_btn.config(state=tk.DISABLED)
        self.after(0, _)

    def _enable_buttons(self):
        def _():
            self.encrypt_btn.config(state=tk.NORMAL)
            self.decrypt_btn.config(state=tk.NORMAL)
        self.after(0, _)

    def encrypt(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected to encrypt.")
            return
        mode = self.mode.get()
        key = self.key_path.get().strip() or "secret.key"
        password = self.password_var.get() if mode == "password" else None

        if mode == "password" and not password:
            messagebox.showerror("Error", "Please enter a password for encryption.")
            return
        self._disable_buttons()
        self._set_status("Encrypting...")

        try:
            if mode == "password":
                encrypt_file(self.file_path, password=password)
            else:
                encrypt_file(self.file_path, key)
            enc_path = self.file_path + ".encrypted"
            if os.path.exists(enc_path):
                messagebox.showinfo("Success", f"File encrypted: {enc_path}")
                self._set_status(f"Encrypted: {enc_path}")
            else:
                messagebox.showwarning("Warning", "Encryption completed but output file not found. Check console for details.")
                self._set_status("Encryption finished (no output found)")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {e}")
            self._set_status("Encryption failed")
        finally:
            self._enable_buttons()

    def decrypt(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected to decrypt.")
            return
        mode = self.mode.get()
        key = self.key_path.get().strip() or "secret.key"
        password = self.password_var.get() if mode == "password" else None

        if mode == "password" and not password:
            messagebox.showerror("Error", "Please enter a password for decryption.")
            return
        self._disable_buttons()
        self._set_status("Decrypting...")

        try:
            if mode == "password":
                decrypt_file(self.file_path, password=password)
            else:
                decrypt_file(self.file_path, key)
            # determine output path
            if self.file_path.endswith('.encrypted'):
                out = os.path.splitext(self.file_path)[0] + ".decrypted"
            else:
                out = self.file_path + ".decrypted"

            if os.path.exists(out):
                messagebox.showinfo("Success", f"File decrypted: {out}")
                self._set_status(f"Decrypted: {out}")
            else:
                messagebox.showwarning("Warning", "Decryption completed but output file not found. Check console for details.")
                self._set_status("Decryption finished (no output found)")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")
            self._set_status("Decryption failed")
        finally:
            self._enable_buttons()


def main():
    app = EncryptionApp()
    app.mainloop()


if __name__ == "__main__":
    main()
