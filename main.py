# Python standard libraries
from tkinter import filedialog, messagebox, Button, Tk, Label
import shutil
import os
# need to "pip install easygui"
import easygui


# To return the file path
def file_open_box():
    path = easygui.fileopenbox()
    return path


# To return the directory path
def directory_open_box():
    path = filedialog.askdirectory()
    return path


# To open the files
def open_file():
    path = file_open_box()
    try:
        os.startfile(path)
    except TypeError:
        messagebox.showinfo("!بازکردن فایل با خطا مواجه شد", "!فایل مورد نظر یافت نشد")


# To copy file
def copy_file():
    source = file_open_box()
    destination = directory_open_box()
    try:
        shutil.copy(source, destination)
        messagebox.showinfo("!عملیات موفق", "!فایل با موفقیت کپی شد")
    except:
        messagebox.showinfo("خطا در انجام عملیات", "!کپی کردن فایل با خطا مواجه شد")


# To delete file
def delete_file():
    path = file_open_box()
    try:
        os.remove(path)
        messagebox.showinfo("!عملیات موفق", "!فایل با موفقیت حذف شد")
    except:
        messagebox.showinfo("خطا در انجام عملیات", "!حذف فایل با خطا مواجه شد")


# To rename file
def rename_file():
    try:
        file = file_open_box()
        path1 = os.path.dirname(file)
        extension = os.path.splitext(file)[1]
        new_name = input("New Name: ")
        path2 = os.path.join(path1, new_name + extension)
        os.rename(file, path2)
        messagebox.showinfo("!عملیات موفق", "!نام فایل با موفقیت تغییر یافت")
    except:
        messagebox.showinfo("خطا در انجام عملیات", "!تغییر نام فایل با خطا مواجه شد")


# To move file
def move_file():
    source = file_open_box()
    destination = directory_open_box()
    if source == destination:
        messagebox.showinfo("خطا در انجام عملیات", "!مسیر انتقال فایل را تغییر دهید")
    else:
        try:
            shutil.move(source, destination)
            messagebox.showinfo("!عملیات موفق", "!فایل با موفقیت انتقال یافت")
        except:
            messagebox.showinfo("خطا در انجام عملیات", "!انتقال فایل با خطا مواجه شد")


# To make directory
def make_directory():
    path = directory_open_box()
    name = input("Directory name: ")
    path = os.path.join(path, name)
    try:
        os.mkdir(path)
        messagebox.showinfo("!عملیات موفق", "!ساخت پوشه با موفقیت انجام شد")
    except:
        messagebox.showinfo("خطا در انجام عملیات", "!ساخت پوشه با خطا مواجه شد")


# To remove directory
def remove_directory():
    path = directory_open_box()
    try:
        os.rmdir(path)
        messagebox.showinfo("!عملیات موفق", "!حذف پوشه با موفقیت انجام شد")
    except:
        messagebox.showinfo("خطا در انجام عملیات", "!حذف پوشه با خطا مواجه شد")


# To list directory
def list_files():
    path = directory_open_box()
    try:
        file_list = sorted(os.listdir(path))
        for i in file_list:
            print(i)
    except:
        messagebox.showinfo("خطا در انجام عملیات", "!لیست کردن فایل ها با خطا مواجه شد")


window = Tk()
window.title("مدیریت فایل")
window.configure(bg="#5C6BC0")
window.geometry("300x400")
Label(window, bg="#5C6BC0", fg="white", font=("Arial", 14), text="چه کاری انجام دهم؟").pack(pady=15)

# Buttons
Button(window, command=open_file, text="بازکردن فایل", fg="#1A237E",activebackground="#9FA8DA",
       bg="#C5CAE9", width=30).pack(pady=6)

Button(window, command=copy_file, text="کپی کردن فایل", fg="#1A237E", activebackground="#9FA8DA",
       bg="#C5CAE9", width=30).pack(pady=6)

Button(window, command=delete_file, text="حذف کردن فایل", fg="#1A237E", activebackground="#9FA8DA",
       bg="#C5CAE9", width=30).pack(pady=6)

Button(window, command=rename_file, text="تغییر نام فایل", fg="#1A237E", activebackground="#9FA8DA",
       bg="#C5CAE9", width=30).pack(pady=6)

Button(window, command=move_file, text="انتقال فایل", fg="#1A237E", activebackground="#9FA8DA",
       bg="#C5CAE9", width=30).pack(pady=6)

Button(window, command=make_directory, text="ایجاد پوشه", fg="#1A237E", activebackground="#9FA8DA",
       bg="#C5CAE9", width=30).pack(pady=6)

Button(window, command=remove_directory, text="حذف کردن پوشه", fg="#1A237E", activebackground="#9FA8DA",
       bg="#C5CAE9", width=30).pack(pady=6)

Button(window, command=list_files, text="لیست تمام فایل ها", fg="#1A237E", activebackground="#9FA8DA",
       bg="#C5CAE9", width=30).pack(pady=6)

window.mainloop()
