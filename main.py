import customtkinter as ctk
from tkinter import *
import os
import shutil
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import threading

window = ctk.CTk()
window.title('KLEENEX')
window.geometry('1920x1080')
window.resizable(height=True, width=True)
window.iconbitmap("icon1.ico")

frame1=ctk.CTkFrame(window,fg_color='#0D7377',width=200,height=1080)
frame1.place(x=0,y=0)

nframe=ctk.CTkFrame(window,width=1720,height=1080)
nframe.place(x=200,y=0)

image_main=ctk.CTkImage(light_image=Image.open(os.path.join('icon1.ico')), size=(300 ,300))
lb = ctk.CTkLabel(nframe, image=image_main,text='')
lb.place(x=200,y=300)
lb1=ctk.CTkLabel(nframe,text='KLEENEX',font=('Times', 100))
lb1.place(x=520, y=400)
lb2=ctk.CTkLabel(nframe,width=1920,height=5,fg_color='#0D7377',text='')
lb2.place(x=0,y=250)
lb3=ctk.CTkLabel(nframe,width=1920,height=5,fg_color='#0D7377',text='')
lb3.place(x=0,y=630)
lb4=ctk.CTkLabel(nframe,width=1920,height=5,fg_color='#0D7377',text='')
lb4.place(x=0,y=230)
lb5=ctk.CTkLabel(nframe,width=1920,height=5,fg_color='#0D7377',text='')
lb5.place(x=0,y=650)


im_checked = ImageTk.PhotoImage(Image.open("checked.png"))
im_unchecked = ImageTk.PhotoImage(Image.open("unchecked.png"))


def delete_pages():
    for frames in nframe.winfo_children():
        frames.destroy()


#about
def about_func():
    frame1=ctk.CTkFrame(nframe,fg_color='grey20',width=1720,height=350)
    frame1.place(x=0,y=70)
    frame2=ctk.CTkFrame(frame1,fg_color='grey20',width=600,height=300)
    frame2.place(x=235,y=80)
    frame3=ctk.CTkFrame(nframe,fg_color='grey20',width=1720,height=330)
    frame3.place(x=0,y=435)
    lb1=ctk.CTkLabel(nframe,text='ABOUT',font=('Times', 30, 'bold'),text_color='#008170')
    lb1.place(x=20,y=15)
    lb2=ctk.CTkLabel(nframe,text='Name               :     KLEENEX',font=('Times', 25),text_color='white',bg_color='grey20')
    lb2.place(x=40,y=90)
    lb3=ctk.CTkLabel(nframe,text='Info                  :',font=('Times', 25),text_color='white',bg_color='grey20')
    lb3.place(x=40,y=145)
    lb4_txt="The Windows Storage Optimizer is a tool designed to enhance the performance and efficiency of your computer's storage. By identifying and removing unnecessary files, optimizing storage configurations, and improving disk usage, this software helps to free up valuable space, increase speed, and reduce the risk of data loss."
    lb4=ctk.CTkLabel(frame2,text=lb4_txt,wraplength=550,font=('Times',20),text_color='white',bg_color='grey20')
    lb4.place(x=0,y=0)
    lb5=ctk.CTkLabel(nframe,text='Target Files      :        Temp, Prefetch, %Temp%, Utilities',font=('Times', 25),text_color='white',bg_color='grey20')
    lb5.place(x=40,y=300)
    lb6=ctk.CTkLabel(nframe,text='Developed by   :       Aadarsh Anand, Priyanshu Singh, Gourav Kr. Singh',font=('Times', 25),text_color='white',bg_color='grey20')
    lb6.place(x=40,y=360)
    lb7=ctk.CTkLabel(nframe,text='Required Specifications  ~',font=('Times', 30),text_color='white',bg_color='grey20')
    lb7.place(x=20,y=450)
    lb8=ctk.CTkLabel(nframe,text='',width=1720,height=1)
    lb8.place(x=0,y=500)
    lb9=ctk.CTkLabel(nframe,text='RAM                  :        4 gigabyte(GB) or above',text_color='white',font=('Times',25),bg_color='grey20')
    lb9.place(x=20,y=540)
    lb10=ctk.CTkLabel(nframe,text='OS                      :        Windows 7 or above',text_color='white',font=('Times',25),bg_color='grey20')
    lb10.place(x=20,y=590)
    lb11=ctk.CTkLabel(nframe,text='Storage               :        min 200 MB',text_color='white',font=('Times',25),bg_color='grey20')
    lb11.place(x=20,y=640)
    lb12=ctk.CTkLabel(nframe,text='Processor            :        62 BIT',text_color='white',font=('Times',25),bg_color='grey20')
    lb12.place(x=20,y=690)
    bt1=ctk.CTkButton(nframe,text='Back',text_color='Black',fg_color='#008170',font=('Times',25),
        height=30,width=100,command=lambda:[delete_pages(),button4_func()])
    bt1.place(x=1150,y=780)

#home
def button0_func():
    image_main=ctk.CTkImage(light_image=Image.open(os.path.join('icon1.ico')), size=(300 ,300))
    lb = ctk.CTkLabel(nframe, image=image_main,text='')
    lb.place(x=200,y=300)
    lb1=ctk.CTkLabel(nframe,text='KLEENEX',font=('Times', 100))
    lb1.place(x=520, y=400)
    lb2=ctk.CTkLabel(nframe,width=1920,height=5,fg_color='#0D7377',text='')
    lb2.place(x=0,y=250)
    lb3=ctk.CTkLabel(nframe,width=1920,height=5,fg_color='#0D7377',text='')
    lb3.place(x=0,y=630)
    lb4=ctk.CTkLabel(nframe,width=1920,height=5,fg_color='#0D7377',text='')
    lb4.place(x=0,y=230)
    lb5=ctk.CTkLabel(nframe,width=1920,height=5,fg_color='#0D7377',text='')
    lb5.place(x=0,y=650)

#search dup
def button1_func():
    sframe= ctk.CTkScrollableFrame(nframe,fg_color = 'grey25',height=600,width=1315)
    sframe.place(x=0,y=80)
    entryn=ctk.CTkEntry(nframe,placeholder_text='',height=30,width=300,bg_color='grey25')
    entryn.place(x=150,y=120)
    def browse_directory():
        directory = filedialog.askdirectory()
        if directory:
            # Schedule the search_duplicates function to run in the main thread after 100 milliseconds
            window.after(100, lambda: search_duplicates(directory))
        entryn.insert(0,directory)
    
    lb1=ctk.CTkLabel(nframe,text='SEARCH FOR DUPLICATE FILES',font=('Times', 30, 'bold'),text_color='#008170')
    lb1.place(x=20,y=15)
    lb2=ctk.CTkLabel(nframe,text='SEARCH',font=('Times', 25),text_color='white',fg_color='grey25',bg_color='grey25')
    lb2.place(x=20,y=120)

    def cancel_search():
        duplicates_tree.delete(*duplicates_tree.get_children())  # Clear the search results

    def delete_selected():
        selected_items = duplicates_tree.selection()
        if not selected_items:
            messagebox.showinfo("Error", "Please select files to delete.")
            return

        for item in selected_items:
            file_path = duplicates_tree.item(item, "values")[1]
            try:
                os.remove(file_path)
                duplicates_tree.delete(item)
            except Exception as e:
                messagebox.showinfo("Error", f"Error deleting file: {e}")

    browse_button=ctk.CTkButton(nframe,text='Browse',text_color='white',fg_color='grey15',
                                hover_color='grey30',bg_color='grey25',height=30,width=60,font=('Times', 25),command=browse_directory)
    browse_button.place(x=500,y=120)
    search_button=ctk.CTkButton(nframe,text='Cancel',text_color='white',fg_color='grey15',
                                hover_color='grey30',bg_color='grey25',height=30,width=60,font=('Times', 25),command=cancel_search)
    search_button.place(x=600,y=120)
    delete_button=ctk.CTkButton(nframe,text='DELETE',text_color='black',fg_color='#008170',
                                hover_color='grey30',height=50,width=150,font=('Times', 25),command=delete_selected)
    delete_button.place(x=600,y=750)

    def check_event(event):
        rowid = duplicates_tree.identify_row(event.y)
        tag = duplicates_tree.item(rowid, "tags")[0]
        tags = list(duplicates_tree.item(rowid, "tags"))
        tags.remove(tag)
        duplicates_tree.item(rowid, tags=tags)
        if tag == "checked":
            duplicates_tree.item(rowid, tags = "unchecked")
        else:
            duplicates_tree.item(rowid, tags = "checked")

    columns = ("Name", "Path", "Size")
    duplicates_tree = ttk.Treeview(nframe, columns=columns, selectmode="extended")
    style = ttk.Style(duplicates_tree)
    style.configure('Treeview', rowheight = 50)
    duplicates_tree.place(x=450, y=250)

    def search_duplicates(directory):
        duplicates_tree.delete(*duplicates_tree.get_children())  # Clear the previous search results
        file_contents = {}

        try:
            for foldername, _, filenames in os.walk(directory):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)

                    try:
                        file_size = str(round(os.path.getsize(filepath) / (1024 * 1024), 2)) + ' MB'

                        if file_size not in file_contents:
                            file_contents[file_size] = [(filename, filepath)]
                        else:
                            file_contents[file_size].append((filename, filepath))

                    except Exception as e:
                        print(f"Error reading {filepath}: {e}")

            # Display files with the same size
            for size, files in file_contents.items():
                if len(files) > 1:
                    for file in files:
                        duplicates_tree.insert('', 'end', values=(file[0], file[1], size), tags="unchecked")

        except Exception as e:
            print(f"Error: {e}")

        
    

    duplicates_tree.tag_configure('checked', image = im_checked)
    duplicates_tree.tag_configure('unchecked', image = im_unchecked)

    #format column
    duplicates_tree.column("#0", width=120, minwidth=25, anchor="center")
    duplicates_tree.column("#1", anchor="w")
    duplicates_tree.column("#2", anchor="w")
    duplicates_tree.column("#3", anchor="center")

    #configure column headings
    duplicates_tree.heading('#0', text = "Select")
    duplicates_tree.heading('#1', text="Name")
    duplicates_tree.heading('#2', text="Contains Path")
    duplicates_tree.heading('#3', text="Size")

    duplicates_tree.bind('<Button 1>', check_event)

#optimize
def button2_func():
    frame1=ctk.CTkFrame(nframe,fg_color='grey25',height=400,width=550)
    frame1.place(x=70,y=100)
    frame2=ctk.CTkFrame(nframe,fg_color='grey25',height=400,width=550)
    frame2.place(x=720,y=100)
    lb1=ctk.CTkLabel(nframe,text='OPTIMIZE',font=('Times', 30, 'bold'),text_color='#008170')
    lb1.place(x=20,y=15)
    lb2=ctk.CTkLabel(nframe,text='Target Type :',font=('Times', 25),text_color='white',bg_color='grey25')
    lb2.place(x=90,y=140)
    lb3=ctk.CTkLabel(nframe,text='Target :',font=('Times', 25),text_color='white',bg_color='grey25')
    lb3.place(x=90,y=230)
    lb4=ctk.CTkLabel(nframe,text='Location :',font=('Times', 25),text_color='white',bg_color='grey25')
    lb4.place(x=90,y=320)
    lb5=ctk.CTkLabel(nframe,text='Junk Files',font=('Times', 25),text_color='white',bg_color='grey25')
    lb5.place(x=300,y=140)
    lb6=ctk.CTkLabel(nframe,text='Files',font=('Times', 25),text_color='white',bg_color='grey25')
    lb6.place(x=300,y=230)
    entry1=ctk.CTkEntry(nframe, placeholder_text='',placeholder_text_color='white',bg_color='grey23',width=300,font=('Times', 20))
    entry1.place(x=300,y=320)
    lb7=ctk.CTkLabel(nframe,text='Start In :',font=('Times', 25),text_color='white',bg_color='grey25')
    lb7.place(x=750,y=140)
    lb8=ctk.CTkLabel(nframe,text='Comment :',font=('Times', 25),text_color='white',bg_color='grey25')
    lb8.place(x=750,y=230)
    lb9=ctk.CTkLabel(nframe,text='File Type :',font=('Times', 25),text_color='white',bg_color='grey25')
    lb9.place(x=750,y=320)
    lb10=ctk.CTkLabel(nframe,text='Deletes specified junk Files',text_color='white',bg_color='grey25',width=300,font=('Times', 25))
    lb10.place(x=940,y=230)
    entry2=ctk.CTkEntry(nframe, placeholder_text='',placeholder_text_color='white',bg_color='grey25',width=300,font=('Times', 20))
    entry2.place(x=950,y=140)

    abpath = os.path.abspath(__file__)
    entry1.insert(0, abpath)

    def file_location():
        loc = entry2.get()
        file_dia = filedialog.askopenfile(initialdir=loc)
        print(loc)
    
    initial_target_path = "C:\Windows\Temp"
    entry2.insert(0, initial_target_path)

    def combofunction(event):
        s = combobox.get()
        if s != 'all':
            combobox.set(s)
        m = combobox.get()
        if m == "temp":
            path = "C:\\Windows"
            for i in os.listdir(path):
                if "Temp" == i:
                    path_of = os.path.join(path, i)
                    entry2.delete(0, END)
                    entry2.insert(0, path_of)
        elif m == "Prefetch":
            path = "C:\\Windows"
            for i in os.listdir(path):
                if "Prefetch" == i:
                    path_of = os.path.join(path, i)
                    entry2.delete(0, END)
                    entry2.insert(0, path_of)
        elif m == "%temp%":
            path = 'C:\\Users'
            for i in os.listdir(path):
                if i != 'Default User' and i != 'All Users' and i != 'Public' and i != 'Default' and i != 'desktop.ini':
                    path_line = os.path.join(path, i)
                    for j in os.listdir(path_line):
                        if j == 'AppData':
                            path_line2 = os.path.join(path_line, j)
                            for k in os.listdir(path_line2):
                                if k == 'Local':
                                    path_line3 = os.path.join(path_line2, k)
                                    for l in os.listdir(path_line3):
                                        if l == 'Temp':
                                            path_line4 = os.path.join(path_line3, l)
                                            entry2.delete(0, END)
                                            entry2.insert(0, path_line4)
        elif m == "all":
            pass
        else:
            messagebox.showerror("Problem with File type",
                                "Enter correct keyword! Keyword list: Temp,prefetch,%temp%,All.Keywords are case sensitive.")

    combobox=ctk.CTkComboBox(nframe,values=['Temp','Prefetch','%temp%','all'],width=300,font=('Times', 20),bg_color='grey25',command=combofunction)
    combobox.place(x=950,y=320)

    def search():
        global path_of_prefetch
        global path_of_appdataTemp
        global path_of_temp
        global l1
        l1 = []
        path_of_temp = 'C:\Windows\Temp'
        path_of_prefetch = 'C:\Windows\prefetch'
        path_of = 'C:\\Users'
        for i in os.listdir(path_of):
            if i != 'Default User' and i != 'All Users' and i != 'Public' and i != 'Default' and i != 'desktop.ini':
                path_line = os.path.join(path_of, i)
                for j in os.listdir(path_line):
                    if j == 'AppData':
                        path_line2 = os.path.join(path_line, j)
                        for k in os.listdir(path_line2):
                            if k == 'Local':
                                path_line3 = os.path.join(path_line2, k)
                                for l in os.listdir(path_line3):
                                    if l == 'Temp':
                                        path_of_appdataTemp = os.path.join(path_line3, l)
        l1 = [path_of_temp, path_of_prefetch, path_of_appdataTemp]


    def optimize():
        search()
        path = entry2.get()
        input_for_g = combobox.get()
        if input_for_g == "All":
            for j in l1:
                for thefile in os.listdir(j):
                    file_path = os.path.join(j, thefile)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except:
                        pass
        for thefile in os.listdir(path):
            file_path = os.path.join(path, thefile)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                pass


    loc_button=ctk.CTkButton(nframe,text='File Location',text_color='black',fg_color='#008170',height=70,width=250,font=('Times', 30),command=file_location)
    loc_button.place(x=800,y=600)
    optimize_button=ctk.CTkButton(nframe,text='OPTIMIZE',text_color='black',fg_color='#008170',height=70,width=150,font=('Times', 25),command=optimize)
    optimize_button.place(x=1100,y=600)


#large files
def button3_func():
    sframe= ctk.CTkScrollableFrame(nframe,fg_color = 'grey25',height=600,width=1315)
    sframe.place(x=0,y=80)
    entryn1=ctk.CTkEntry(nframe,placeholder_text='',height=30,width=300,bg_color='grey25')
    entryn1.place(x=150,y=120)
    entryn2=ctk.CTkEntry(nframe,placeholder_text='',height=30,width=100,bg_color='grey25')
    entryn2.place(x=330,y=620)
    def browse_directory():
        directory = filedialog.askdirectory()
        if directory:
            search_thread = threading.Thread(target=find_large_files, args=(directory,))
            search_thread.start()
        entryn1.insert(0,directory)
    
    lb1=ctk.CTkLabel(nframe,text='SEARCH FOR LARGE FILES',font=('Times', 30, 'bold'),text_color='#008170')
    lb1.place(x=20,y=15)
    lb2=ctk.CTkLabel(nframe,text='SEARCH',font=('Times', 25),text_color='white',fg_color='grey25',bg_color='grey25')
    lb2.place(x=20,y=120)
    lb3=ctk.CTkLabel(nframe,text='Enter the min size (in MB) : ',font=('Times', 25),text_color='white',fg_color='grey25',bg_color='grey25')
    lb3.place(x=20,y=620)

    def cancel_search():
        largef_tree.delete(*largef_tree.get_children())  # Clear the search results


    browse_button=ctk.CTkButton(nframe,text='Browse',text_color='white',fg_color='grey15',
                                hover_color='grey30',bg_color='grey25',height=30,width=60,font=('Times', 25),command=browse_directory)
    browse_button.place(x=500,y=120)
    search_button=ctk.CTkButton(nframe,text='Search',text_color='white',fg_color='grey15',
                                hover_color='grey30',bg_color='grey25',height=30,width=60,font=('Times', 25),command=cancel_search)
    search_button.place(x=600,y=120)
    delete_button=ctk.CTkButton(nframe,text='DELETE',text_color='black',fg_color='#008170',
                                hover_color='grey30',height=50,width=150,font=('Times', 25))
    delete_button.place(x=600,y=750)

    def check_event(event):
        rowid = largef_tree.identify_row(event.y)
        tag = largef_tree.item(rowid, "tags")[0]
        tags = list(largef_tree.item(rowid, "tags"))
        tags.remove(tag)
        largef_tree.item(rowid, tags=tags)
        if tag == "checked":
            largef_tree.item(rowid, tags = "unchecked")
        else:
            largef_tree.item(rowid, tags = "checked")

    columns = ("Name", "Path", "Size")
    largef_tree = ttk.Treeview(nframe, columns=columns, selectmode="extended")
    style = ttk.Style(largef_tree)
    style.configure('Treeview', rowheight = 50)
    largef_tree.place(x=450, y=220)

    def find_large_files(directory):
        size_threshold=3000
        large_files = {}
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    try:
                        with open(file_path, 'rb') as file:
                            content = file.read()

                        if file_size > size_threshold:
                            large_files[content] = (file, file_path)
                            largef_tree.insert('', 'end', values=(files, file_path, file_size), tags="unchecked")
                            largef_tree.insert('', 'end', values=(large_files[content][0], large_files[content][1], file_size), tags="unchecked")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
        except Exception as e:
            print(f"Error: {e}")
        return large_files

    # Configure column headings
    largef_tree.heading('#0', text = "")
    largef_tree.heading('#1', text="Name")
    largef_tree.heading('#2', text="Contains Path")
    largef_tree.heading('#3', text="Size")

    im_checked = ImageTk.PhotoImage(Image.open("checked.png"))
    im_unchecked = ImageTk.PhotoImage(Image.open("unchecked.png"))

    largef_tree.tag_configure('checked', image = im_checked)
    largef_tree.tag_configure('unchecked', image = im_unchecked)


    largef_tree.bind('<Button 1>', check_event)

#settings
def button4_func():
    bt1=ctk.CTkButton(nframe,text='',fg_color='grey25',width=1720,height=73,hover_color='grey25')
    bt1.place(x=0,y=150)
    recent_img=ctk.CTkImage(light_image=Image.open(os.path.join('recent.png')), size=(40 ,40))
    lb1_img=ctk.CTkLabel(nframe,width=50,height=70,image=recent_img,bg_color='grey25',text='')
    lb1_img.place(x=20,y=150)
    lb1=ctk.CTkLabel(nframe,width=50,height=70,fg_color='grey25',bg_color='grey25',text='Recent  >',text_color='white',font=('Times', 30))
    lb1.place(x=90,y=150)
    bt2=ctk.CTkButton(nframe,text='',fg_color='grey25',width=1720,height=73,hover_color='grey25',command=lambda: [delete_pages(),about_func()])
    bt2.place(x=0,y=240)
    about_img=ctk.CTkImage(light_image=Image.open(os.path.join('about.png')), size=(40 ,40))
    lb2_img=ctk.CTkLabel(nframe,width=50,height=70,image=about_img,bg_color='grey25',text='')
    lb2_img.place(x=20,y=240)
    lb2=ctk.CTkLabel(nframe,width=50,height=70,fg_color='grey25',bg_color='grey25',text='About  >',text_color='white',font=('Times', 30))
    lb2.place(x=90,y=240)
    bt3=ctk.CTkButton(nframe,text='',fg_color='grey25',width=1720,height=73,hover_color='grey25')
    bt3.place(x=0,y=330)
    change_img=ctk.CTkImage(light_image=Image.open(os.path.join('change.png')), size=(40 ,40))
    lb3_img=ctk.CTkLabel(nframe,width=50,height=70,image=change_img,bg_color='grey25',text='')
    lb3_img.place(x=20,y=330)
    lb3=ctk.CTkLabel(nframe,width=50,height=70,fg_color='grey25',bg_color='grey25',text='Change Mode  ~',text_color='white',font=('Times', 30))
    lb3.place(x=90,y=330)
    sun_img=ctk.CTkImage(light_image=Image.open(os.path.join('sun.png')), size=(40 ,40))
    bt_light=ctk.CTkButton(nframe,text='',fg_color='grey25',width=60,height=60,hover_color='grey25',image=sun_img,command = lambda: ctk.set_appearance_mode('light'))
    bt_light.place(x=100,y=440)
    moon_img=ctk.CTkImage(light_image=Image.open(os.path.join('moon.png')), size=(40 ,40))
    bt_dark=ctk.CTkButton(nframe,text='',fg_color='grey25',width=60,height=60,hover_color='grey25',image=moon_img,command = lambda: ctk.set_appearance_mode('dark'))
    bt_dark.place(x=230,y=440)
    lb4=ctk.CTkLabel(nframe,width=50,height=70,text='SETTINGS',text_color='#008170',font=('Times', 30, 'bold'))
    lb4.place(x=20,y=15)

#home
home_img=ctk.CTkImage(light_image=Image.open(os.path.join('home.png')), size=(40 ,40))
button0 = ctk.CTkButton(window,text='',fg_color= '#14FFEC',text_color = 'white',hover_color= 'grey29',bg_color='#0D7377',
    corner_radius=20,border_width=0,height=80,width=80,image=home_img,command=lambda: [delete_pages(),button0_func()])
button0.place(x=60, y=80)

#scan
dup_img=ctk.CTkImage(light_image=Image.open(os.path.join('dup.png')), size=(40 ,40))
button1 = ctk.CTkButton(window,text='',fg_color= '#14FFEC',text_color = 'white',hover_color= 'grey29',bg_color='#0D7377',
    corner_radius=20,border_width=0,height=80,width=80,image=dup_img,command=lambda: [delete_pages(),button1_func()])
button1.place(x=60, y=230)

#optimize
broom_img=ctk.CTkImage(light_image=Image.open(os.path.join('broom.png')), size=(40 ,40))
button2 = ctk.CTkButton(window,text='',fg_color= '#14FFEC',text_color = 'white',hover_color= 'grey29',bg_color='#0D7377',
    corner_radius=20,border_width=0,height=80,width=80,image=broom_img,command=lambda: [delete_pages(),button2_func()])
button2.place(x=60, y=380)

#large files
lg_img=ctk.CTkImage(light_image=Image.open(os.path.join('lgfile.png')), size=(40 ,40))
button3 = ctk.CTkButton(window, text='',fg_color = '#14FFEC', text_color = 'white',hover_color = 'grey35',bg_color='#0D7377',
    corner_radius=20,border_width=0,height=80,width=80,image=lg_img,command=lambda: [delete_pages(),button3_func()])
button3.place(x=60, y=530)

#settings
set_img=ctk.CTkImage(light_image=Image.open(os.path.join('setting.png')), size=(40 ,40))
button4 = ctk.CTkButton(window, text='',fg_color = '#14FFEC', text_color = 'white',hover_color = 'grey35',bg_color='#0D7377',
    corner_radius=20,border_width=0,height=80,width=80,image=set_img,command=lambda: [delete_pages(),button4_func()])
button4.place(x=60, y=680)

# run
window.mainloop()
