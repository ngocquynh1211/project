from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Function to create the main task management window
def create_task_management_window():
    # Tạo ra cửa sổ ứng dụng
    window = Tk()

    # set up thông tin cho window
    window.title("Task Management System")
    window.geometry("814x650")
    window.config(bg="#535c68")

    # Class
    class Task:
        def __init__(self, name, progress, technician, ID):
            self.name = name
            self.progress = progress
            self.technician = technician
            self.ID = ID
    # tạo list để lưu trữ tiến độ công việc
    task_list = []

    # Mô tả các function cho ứng dụng
    # add/search/update/delete/complete/reset
    def add_task():
        # lấy giá trị từ các entry
        name_value = name.get()
        progress_value = int(progress.get())
        technician_value = technician.get()
        ID_value = int(ID.get())

        new_task = Task(name_value, progress_value, technician_value, ID_value)

        # thêm vào list
        task_list.append(new_task)

        # cập nhật Listbox
        update_task_listbox()

        # hiển thị thông báo
        messagebox.showinfo("Add Task", f"{name_value} is added successfully")

        # xóa giá trị ở entry
        name.delete(0, END)
        progress.delete(0, END)
        technician.delete(0, END)
        ID.delete(0, END)

    def update_task_listbox():
        task_listbox.delete(*task_listbox.get_children())
        for task in task_list:
            task_listbox.insert('', 'end', values=(task.ID, task.name, task.progress, task.technician))

    def search_task():
        search_value = search_name.get()
        is_found = False

        for task in task_list:
            if task.name == search_value or str(task.ID) == search_value:
                messagebox.showinfo("Search Task", f"Name: {task.name}, Progress: {task.progress}%")
                is_found = True
                break

        if not is_found:
            messagebox.showinfo("Search Task", f"{search_value} is not found")

    # Xóa giá trị ở entry
        search_name.delete(0, END)  

    def delete_task():
        delete_value = delete_name.get()
        is_found = False

        for task in task_list:
            if task.name == delete_value or str(task.ID) == delete_value:
                task_list.remove(task)
                messagebox.showinfo("Delete Task", f"{delete_value} is deleted successfully")
                is_found = True
                break

        if not is_found:
            messagebox.showinfo("Delete Task", f"{delete_value} is not found")

        # cập nhật Listbox
        update_task_listbox()

        # Xóa giá trị ở entry
        delete_name.delete(0, END)

    def update_task():
        update_value = update_name.get()
        new_progress = int(update_progress.get())
        is_found = False

        for task in task_list:
            if task.name == update_value or str(task.ID) == update_value:
                task.progress = new_progress
                messagebox.showinfo("Update Task", f"{update_value} progress updated to {new_progress}%")
                is_found = True
                break

        if not is_found:
            messagebox.showinfo("Update Task", f"{update_value} is not found")

        # cập nhật Listbox
        update_task_listbox()

        # Xóa giá trị ở entry
        update_name.delete(0, END)
        update_progress.delete(0, END)


    def complete_task():
        complete_value = complete_name.get()
        is_found = False

        for task in task_list:
            if task.name == complete_value:
                task.progress = 100
                messagebox.showinfo("Complete Task", f"{complete_value} is completed successfully")
                is_found = True
                break

        if not is_found:
            messagebox.showinfo("Complete Task", f"{complete_value} is not found")

        # cập nhật Listbox
        update_task_listbox()

        # xóa giá trị ở entry
        complete_name.delete(0, END)

    def reset():
        name.delete(0, END)
        progress.delete(0, END)
        technician.delete(0, END)
        ID.delete(0, END)
        search_name.delete(0, END)
        delete_name.delete(0, END)
        update_name.delete(0, END)
        update_progress.delete(0, END)
        complete_name.delete(0, END)

    # set up các widget
    # tạo label
    header_label = Label(window, text="Task Management System", bg="#2c3e50", fg="white", font=("Helvetica", 20))
    name_lbl = Label(window, text="Name:", bg="#535c68", fg="white")
    progress_lbl = Label(window, text="Progress(%):", bg="#535c68", fg="white")
    technician_lbl = Label(window, text="Technician:", bg="#535c68", fg="white")
    ID_lbl = Label(window, text="ID:", bg="#535c68", fg="white")
    search_lbl = Label(window, text="Search Task:", bg="#535c68", fg="white")
    delete_lbl = Label(window, text="Delete Task:", bg="#535c68", fg="white")
    update_lbl = Label(window, text="Update Task:", bg="#535c68", fg="white")
    complete_lbl = Label(window, text="Complete Task:", bg="#535c68", fg="white")

    # tạo entry
    name = Entry(window)
    progress = Entry(window)
    technician = Entry(window)
    ID = Entry(window)
    search_name = Entry(window)
    delete_name = Entry(window)
    update_name = Entry(window)
    update_progress = Entry(window)
    complete_name = Entry(window)

    # tạo button
    add_btn = Button(window, text="Add", command=add_task, bg="lightblue", fg="black")
    search_btn = Button(window, text="Search", command=search_task, bg="lightgreen", fg="black")
    delete_btn = Button(window, text="Delete", command=delete_task, bg="lightcoral", fg="black")
    update_btn = Button(window, text="Update", command=update_task, bg="lightgoldenrodyellow", fg="black")
    complete_btn = Button(window, text="Complete", command=complete_task, bg="lightpink", fg="black")
    reset_btn = Button(window, text="Reset", command=reset, bg="lightgrey", fg="black")

    # tạo listbox
    task_listbox = ttk.Treeview(window, columns=("ID", "Name", "Progress", "Technician"), show="headings", style="Custom.Treeview")
    task_listbox.heading("ID", text="Task ID")
    task_listbox.heading("Name", text="Task Name")
    task_listbox.heading("Progress", text="Progress")
    task_listbox.heading("Technician", text="Technician")
    task_listbox.grid(row=10, column=0, columnspan=4, pady=5, padx=5, sticky="nsew")

    # Custom style for Treeview
    window.style = ttk.Style()
    window.style.theme_use("clam")
    window.style.configure("Custom.Treeview", background="#ecf0f1", fieldbackground="#ecf0f1", foreground="#2c3e50", borderwidth=0, anchor="center")

    # dán các widget lên window
    header_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")
    ID_lbl.grid(row=1, column=0, pady=5, padx=5, sticky="w")
    ID.grid(row=1, column=1, pady=5, padx=5, sticky="w")
    name_lbl.grid(row=2, column=0, pady=5, padx=5, sticky="w")
    name.grid(row=2, column=1, pady=5, padx=5, sticky="w")
    progress_lbl.grid(row=3, column=0, pady=5, padx=5, sticky="w")
    progress.grid(row=3, column=1, pady=5, padx=5, sticky="w")
    technician_lbl.grid(row=4, column=0, pady=5, padx=5, sticky="w")
    technician.grid(row=4, column=1, pady=5, padx=5, sticky="w")
    add_btn.grid(row=5, column=0, columnspan=1, pady=5, padx=5, sticky="we")

    search_lbl.grid(row=6, column=0, pady=5, padx=5, sticky="w")
    search_name.grid(row=6, column=1, pady=5, padx=5, sticky="w")
    search_btn.grid(row=6, column=2, pady=5, padx=5, sticky="w")

    delete_lbl.grid(row=7, column=0, pady=5, padx=5, sticky="w")
    delete_name.grid(row=7, column=1, pady=5, padx=5, sticky="w")
    delete_btn.grid(row=7, column=2, pady=5, padx=5, sticky="w")

    update_lbl.grid(row=8, column=0, pady=5, padx=5, sticky="w")
    update_name.grid(row=8, column=1, pady=5, padx=5, sticky="w")
    update_progress.grid(row=8, column=2, pady=5, padx=5, sticky="w")
    update_btn.grid(row=8, column=3, pady=5, padx=5, sticky="w")

    complete_lbl.grid(row=9, column=0, pady=5, padx=5, sticky="w")
    complete_name.grid(row=9, column=1, pady=5, padx=5, sticky="w")
    complete_btn.grid(row=9, column=2, columnspan=1, pady=5, padx=5, sticky="w")

    reset_btn.grid(row=10, column=0, columnspan=1, pady=5, padx=5, sticky="we")

    task_listbox.grid(row=11, column=0, columnspan=4, pady=5, padx=5, sticky="nsew")

    # chạy ứng dụng
    window.mainloop()

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "quynh" and password == "test":  # Hardcoded credentials for simplicity
        messagebox.showinfo("Login", "Login Successful!")
        login_window.destroy()
        create_task_management_window()
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create the login window
login_window = Tk()
login_window.title("Login")
login_window.geometry("300x250")
login_window.config(bg="#535c68")

# Set up login widgets
login_label = Label(login_window, text="Login", bg="#535c68", font=("Helvetica", 16), fg="white")
username_label = Label(login_window, text="Username:", bg="#535c68", fg="white")
password_label = Label(login_window, text="Password:", bg="#535c68", fg="white")
username_entry = Entry(login_window)
password_entry = Entry(login_window, show="*")
login_button = Button(login_window, text="Login", command=login, bg="lightblue", fg="black")

# Place the widgets on the window
login_label.pack(pady=10)
username_label.pack(pady=5)
username_entry.pack(pady=5)
password_label.pack(pady=5)
password_entry.pack(pady=5)
login_button.pack(pady=20)

# Run the login window
login_window.mainloop()