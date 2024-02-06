import gspread
import test_data
import tkinter as tk

notes=0

def zarplate():
    global notes
    #Адресс серверного акка
    gc = gspread.service_account(filename = 'C:\\Python310\\testdclass-8d9d0e2cb79b.json')
    API = API_entry.get()
    #Предоставление апи
    sht1 = gc.open_by_key(str(API))

    #Получение списка листов
    worksheet_list = sht1.worksheets()

    #Указание программе с каким листом работать
    worksheet_user = worksheet_list[0]
    worksheet_quest = worksheet_list[2]

    try:
        # Тут будет код для нода
         #получение номера строки
        email_list = worksheet_quest.col_values(1) #получение емейла
        login_list = worksheet_quest.col_values(2) #получение логина
        password_list = worksheet_quest.col_values(3) #получение пароля
        neponyatno = worksheet_quest.col_values(4)
        for i in range(1, len(email_list)):
            if email_list[i] == '':
                pass
            my_email = email_list[i] #Берём емейл

            massiv_dcoin = test_data.main(login_list[i], password_list[i]) #получаем массив с оценками передаёт значения (login, password)

            cell = worksheet_user.find(my_email) #ищем мой email
            val = worksheet_user.acell(f'L{cell.row}').value

            for r in massiv_dcoin:

                notes = notes + int(r)

            cell_clear1=worksheet_quest.find(email_list[i])
            if notes == 0:
                worksheet_quest.batch_clear([f'A{cell_clear1.row}:D{cell_clear1.row}'])
            else:
                number_cells='L'+str(cell.row) #получаем координаты клетки
                notes=notes+int(val)

                worksheet_user.batch_clear([number_cells]) #очищаем ячейку
                worksheet_user.update(number_cells, str(notes)) #обновляем ячейку
                val = worksheet_user.acell(f'L{cell.row}').value
                cell_clear1=worksheet_quest.find(email_list[i])


                worksheet_quest.batch_clear([f'A{cell_clear1.row}:D{cell_clear1.row}'])

        return True
    
    except Exception as ex:
        print(ex)

root = tk.Tk()
root.title("Начисление Dcoinов")
root.geometry('400x400')

#Добваление текста
label = tk.Label(root, text='Введите API').pack()

# Добавление поля ввода API
API_entry = tk.Entry(root, show="*")
API_entry.pack()

# Добавление кнопки "Войти"
login_button = tk.Button(root, text="Start", command=zarplate)
login_button.pack()

# Запуск главного цикла
root.mainloop()


