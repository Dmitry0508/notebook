#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=float(input('Введите число a:'))
operation=str(input('Введите символ операции:'))
b=float(input('Введите число b:'))
c=['+','-','*','/','mod','div','pow']
for i in operation:
    if operation in c:
        if operation=='+':
            print('Сумма двуч чисел равна:\t',a+b)
            break
        elif operation=='-':
            print('Разность двух чисел равна:\t',a-b)
            break   
        elif operation=='*':
            print('Произведение двух чисел равно:\t',a*b)
            break   
        elif operation=='div':
            if b==0:
                    print("Деление на ноль!")
                    break
            else:
                print('Результат целочисленного деления двух чисел:\t',a//b)
                break
                    
        elif operation=='mod':
            if b==0:
                print("Деление на ноль!")
                break
            else:
                print('Остаток  от деления двух чисел :\t',a%b)
                break
        elif operation=='/':
            if b==0:
                print("Деление на ноль!")
                break
            else:
                print('Результат деления двух чисел:\t',a/b)
                break
                
        elif operation=='pow':
            print('Результат возведения в степень (a)^b:\t',a**b)
            break
    else:
            print('Ошибка!Вы ввели неправильный символ:',operation)
            break


# In[ ]:




