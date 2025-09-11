import tkinter as tk
from tkinter import messagebox


def add():
  user_data = userData.get()
  user_password = userPassword.get()

  if user_data and user_password:
    with open("passwords.txt",'a') as f:
      f.write(f"{user_data} {user_password}\n")
    messagebox.showinfo("Sucess","Added")

  else:
    messagebox.showerror("Error","Null field")

def get():
  user_data = userData.get()
  user_password = {}
  try:
    with open("passwords.txt",'r') as f:
      for k in f:
        i = k.split(' ')
        user_password[i[0]] = i[1]

  except:
    print("ERROR")

  if user_password:
    mess = "your passwords:\n"
    for i in user_password:
      if i == user_data:
        mess += f"User:{user_data}\nPassword:{user_password[i]}\n"
        break
    else:
      mess += "No such username"
    messagebox.showinfo("Passwords", mess)
  else:
    messagebox.showinfo("Passwords", "Empty list")

def get_list():
  user_password = {}
  try:
    with open("passwords.txt", 'r') as f:
      for k in f:
        i = k.split(' ')
        user_password[i[0]] = i[1]
  except:
    print("Not found")
  if user_password:
    mess = "Password Manager\n\n"
    for name, password in user_password.items():
      mess += f"User:{name}\nPassword:{password}\n\n"
    messagebox.showinfo("Passwords", mess)
  else:
    messagebox.showinfo("Passwords", "Empty list")

def delete():
  user_data = userData.get()

  temp_passwords = []

  try:
    with open("passwords.txt",'r') as f:
      for k in f:
        i = k.split(' ')
        if i[0] != user_data:
          temp_passwords.append(f"{i[0]} {i[1]}")
    with open("passwords.txt",'w') as f:
      for line in temp_passwords:
        f.write(line)
    messagebox.showinfo("Sucess", f"User {user_data} deleted")
  except Exception as e:
    messagebox.showerror("Error", f"Error deleting user {user_data} {e}")
if __name__ == "__main__":
  app = tk.Tk()
  app.title("Coluna Maker by Luciano")
  app.geometry("560x270")

  #User entry box
  labelUser = tk.Label(app,text = "USER ENTRY")
  labelUser.grid(row=0, column=0,padx=15,pady=15)
  userData = tk.Entry(app)
  userData.grid(row=0, column=1, padx=15, pady=15)

  # Password entry box
  labelPassword = tk.Label(app, text="PASSWORD ENTRY")
  labelPassword.grid(row=1, column=0, padx=10, pady=5)
  userPassword = tk.Entry(app)
  userPassword.grid(row=1, column=1, padx=10, pady=5)

  #Add Button
  buttonAdd = tk.Button(app, text="Add", command=add)
  buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

  #Get Button
  buttonGet = tk.Button(app, text="Get", command=get)
  buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

  #List Button
  buttonList = tk.Button(app, text="List", command=get_list)
  buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

  #Delete Button
  buttonDelete = tk.Button(app, text="Delete", command=delete)
  buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")


  app.mainloop()