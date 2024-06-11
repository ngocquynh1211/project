from tkinter import *
from tkinter import messagebox
# Tạo ra cửa sổ ứng dụng 
window = Tk()
# set up thông tin cho windown
window.title("Ingredient Management System")
window.geometry("350x150")
#Class
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
# tạo list để lưu trữ tiagn bộ các object
list_ingredients = []
# Mô tả các function cho ứng dụng
# add/search/update/delete/reset
def add_ingredient():
    # lấy giá trị từ các entry
    name_value = name.get()
    quantity_value = int(quantity.get())

    new_ingredient = Ingredient(name_value, quantity_value)

    # thêm vào list
    list_ingredients.append(new_ingredient)
    # list comperhension
    print([item.name for item in list_ingredients])
    # hiển thị thông báo 
    messagebox.showinfo("Add Ingredient", f"{name_value} is added successfully")

    # xóa giá trị ở entry
    name.delete(0, END)
    quantity.delete(0, END)

def search_ingredient():
    search_value = search_name.get()
    is_exist = False

    for ingredient in list_ingredients:
        if ingredient.name == search_value:
            messagebox.showinfo("Search Ingredient", f"Name: {ingredient.name}, quantity: {ingredient.quantity}")
            break
    if is_exist == False:
        messagebox.showinfo("Search Ingredient", f"{search_value} is not found")

def delete_ingredient():
    delete_value = delete_name.get()
    is_exist = False

    for ingredient in list_ingredients:
        if ingredient.name == delete_value:

            messagebox.showinfo("Delete Ingredient", f"Name: {ingredient.name}, quantity: {ingredient.quantity}")
            break
    if is_exist == False:
        messagebox.showinfo("Delete Ingredient", f"{search_value} is not found")

def update_ingredient():
    update_value = update_name.get()
    is_exist = False

    for ingredient in list_ingredients:
        if ingredient.name == delete_value:
            
            messagebox.showinfo("Update Ingredient", f"Name: {ingredient.name}, quantity: {ingredient.quantity}")
            break
    if is_exist == False:
        messagebox.showinfo("Update Ingredient", f"{search_value} is not found")

def reset():
    name.delete(0, END)
    quantity.delete(0, END)
    search.delete(0, END)

#set up các widget
# tạo label
name_lbl = Label(window, text="Name: ")
quantity_lbl = Label(window, text="Quantity:")
#tạo entry
name = Entry(window)
quantity = Entry(window)
search_name = Entry(window)
# tạo button
add_btn = Button(window, text="Add", command=add_ingredient)
search_btn = Button(window, text="Search", command = search_ingredient)
update_btn = Button(window, text="Update")
delete_btn = Button(window, text="Delete")
reset_btn = Button(window, text="Reset", command = reset)
# dán các widget lên windown
name_lbl.grid(row=0, column=0)
quantity_lbl.grid(row=1, column=0)
name.grid(row=0, column=1)
quantity.grid(row=1, column=1)
search_name.grid(row=3, column=0)
add_btn.grid(row=2, column=0)
delete_btn.grid(row=2, column=1)
reset_btn.grid(row=2, column=2)
search_btn.grid(row=3, column=1)
update_btn.grid(row=3, column=2)
# chạy ứng dụng
window.mainloop()