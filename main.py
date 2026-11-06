from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Listbox Example")
window.geometry("350x500")

# Create Listbox
listbox = Listbox(
    window,
    bg="#f7ffde",
    font=("Constantia", 24),
    width=12,
    selectmode=SINGLE
)
listbox.pack(pady=10)

# Insert items
items = ["Pizza", "Burger", "Pasta", "Salad", "Doughnuts"]

for item in items:
    listbox.insert(END, item)

# Adjust Listbox height
def update_listbox_height():
    listbox.config(height=max(1, listbox.size()))

update_listbox_height()

# Entry
entryBox = Entry(window, font=("Helvetica", 18), width=20)
entryBox.pack(pady=10)


# Submit selected item
def submit():
    selected = listbox.curselection()

    if selected:
        item = listbox.get(selected[0])
        messagebox.showinfo("Selection", f"You selected: {item}")
    else:
        messagebox.showwarning(
            "No Selection",
            "Please select an item."
        )


# Add item
def add_item():
    item = entryBox.get().strip()

    if item:
        listbox.insert(END, item)
        update_listbox_height()
        entryBox.delete(0, END)
    else:
        messagebox.showwarning(
            "Empty Entry",
            "Please enter an item."
        )


# Delete selected item
def delete_item():
    selected = listbox.curselection()

    if selected:
        listbox.delete(selected[0])
        update_listbox_height()
    else:
        messagebox.showwarning(
            "No Selection",
            "Please select an item to delete."
        )


# Buttons
submitButton = Button(
    window,
    text="Submit",
    font=("Arial", 12),
    command=submit
)
submitButton.pack(pady=5)

addButton = Button(
    window,
    text="Add",
    font=("Arial", 12),
    command=add_item
)
addButton.pack(pady=5)

deleteButton = Button(
    window,
    text="Delete",
    font=("Arial", 12),
    command=delete_item
)
deleteButton.pack(pady=5)

window.mainloop()