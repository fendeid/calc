#!Моя первая графическая программа.
from tkinter import *
from tkinter import messagebox
#Доступные символы
strs = ['-','+','0','1','2','3','4','5','6','7','8','9','.','*','/','=']

#Калькулятор	
def calc(key):	
	block = 0
	if key == '=':
		for i in digitin.get():
			if i not in strs:			
				digitin.delete(0, END)
				digitin.insert(END,'ERROR')
				break
		try:
			result = str(eval(digitin.get()))			
			digitin.insert(END,'='+ result)			
		except:
			# Проверка итерации, первая ли.
			for i in digitin.get():												
				if i == '=':					
					block = 1
					newstr = digitin.get()[digitin.get().find('=')+1:]					
					digitin.delete(0, END)						
					digitin.insert(END,newstr)					
					break
			# Если проверка прошла успешно
			if block == 1:					
				try:			
					result = str(eval(digitin.get()))						
					digitin.insert(END,'=' + result)	
				except:
					digitin.delete(0, END)
					digitin.insert(END,'ERROR')	
			# Если ошибка таки ошибка..			
			elif block == 0:
				digitin.delete(0, END)
				digitin.insert(END,'ERROR')
			block = 0		
	elif key == '←':
		digitin.delete(int(len(digitin.get())) - 1, END)

	elif key == 'C':
		digitin.delete(0, END)	

	else:			
		digitin.insert(END, key)		
#Окно
root = Tk()
root.title('Калькулятор 0.8')
root.geometry('260x330')
root.resizable(width=False, height=False)

#Строка ввода
digitin = Entry(root,justify=CENTER, font=30,bd=2,textvariable = None, state = NORMAL)
digitin.place(height = 60, width = 240, bordermode = OUTSIDE, y=10, x=10)

#Кнопки
digit = 1
y = 80
for r in range(3):
	x = 10	
	for c in range(3):	
		cmd = lambda x = digit: calc(x)	
		btnd = Button(root,text="{}".format(digit), command = cmd)
		btnd.place(x = x, y = y, height = 50, width = 50)			
		digit += 1
		x += 65
	y += 65

#Точка
dit_cmd = lambda x = '.': calc(x)		
btnd = Button(root,text='.', command = dit_cmd)
btnd.place(x = 75, y = 270, height = 50, width = 50)

# Кнопка равенства
result_cmd = lambda : calc('=')
resultbtn = Button(root,text = '=', font=20,  command = result_cmd)
resultbtn.place(x = 200, y = 80, height = 115, width = 50)

# Ноль
zero_cmd = lambda x = '0': calc(x)
fountbtn = Button(root,text='0', font=30, command = zero_cmd)
fountbtn.place(x = 200, y = 210 , height = 50, width = 50)

# Стереть
back_cmd = lambda x = '←': calc(x)
backbtn = Button(root,text='←', font=30,command = back_cmd)# Задать команду
backbtn.place(x=140, y=270, height = 50, width = 50)

# Очистить
clear_cmd = lambda x = 'C': calc(x)
clearbtn = Button(root,text = 'C', font=30,command=clear_cmd)# Задать команду
clearbtn.place(x=10, y=270,width = 50, height = 50)

# Плюс
plus_cmd = lambda x = '+': calc(x)
btn_plus = Button(root, text = '+', font=30,command=plus_cmd)# Задать команду
btn_plus.place(x=200, y=270,width = 25, height = 25) # 0.5 растояние

#Минус
minus_cmd = lambda x = '-': calc(x)
btn_plus = Button(root, text = '-', font=30,command=minus_cmd)# Задать команду
btn_plus.place(x=225, y=270,width = 25, height = 25)

#Умножить
multi_cmd = lambda x = '*': calc(x)
btn_plus = Button(root, text = '*', font=30,command=multi_cmd)# Задать команду
btn_plus.place(x=200, y=295,width = 25, height = 25)

#Делить
div_cmd = lambda x = '/': calc(x)
btn_plus = Button(root, text = '/', font=30,command=div_cmd)# Задать команду
btn_plus.place(x=225, y=295,width = 25, height = 25)

#Бинды

root.mainloop()