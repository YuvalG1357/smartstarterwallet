import tkinter as tk
from tkinter import messagebox
from app.utils.user_actions import create_user, login_user

class WalletApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartStarter Wallet")
        self.root.geometry("400x300")
        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to SmartStarter Wallet", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.root, text="Create Account", command=self.create_account).pack(pady=10)
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def create_account(self):
        self._render_form("Create Account", create_user)

    def login(self):
        self._render_form("Login", self._handle_login)

    def _render_form(self, title, submit_callback):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=title, font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def on_submit():
            username = username_entry.get()
            password = password_entry.get()
            submit_callback(username, password)

        tk.Button(self.root, text="Submit", command=on_submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def _handle_login(self, username, password):
        user = login_user(username, password)
        if user:
            self.show_dashboard(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_dashboard(self, user):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Welcome, {user.username}!", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text=f"Balance: ${user.balance_usd:.2f}").pack(pady=10)

        tk.Button(self.root, text="Log out", command=self.create_main_menu).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = WalletApp(root)
    root.mainloop()

