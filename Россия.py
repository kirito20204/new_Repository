from tkinter import *   #подключение модуля tkinter
okno=Tk()  #создание главного окна
okno.title("Начало")  #заголовок окна
okno.geometry('800x600')  #размеры окна
holst=Canvas(okno, bg='white',
             width=1000, height=700)
holst.pack()