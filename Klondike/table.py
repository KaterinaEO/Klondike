import pandas as pd
import datetime

dt = datetime.datetime.now()
today = dt.date()
time = dt.time()


df = pd.read_excel(r'C:\Users\Лиза\Downloads\СЕТКА.xlsx', sheet_name = 'Лист1')
n = 115 #количество значимых строк(кол-во оргов + первые 2)

arr = df.to_numpy()
arr = arr[:n-1]
name_columns = arr[0][9::]
# print(name_columns)

# print(columns)
def my_timetable_all(username):
    text = ''
    for el in arr:
        if el[2] == username:
            for i in range(len(name_columns)):
                text += str(name_columns[i]) + ' ' + el[i+9] +'\n'
            return text

def my_timetable_continue(username):
    text = ''
    for el in arr:
        if el[2] == username:
            print('Дальнейшее расписание: ')
            for i in range(len(name_columns)):
                if name_columns[i] >= time:
                    index = i
                    break
            for i in range(index, len(name_columns)):
                text += str(name_columns[i]) + ' ' + el[i+9] +'\n'
            return text

def my_timetable_now(username):
    text = ''
    for el in arr:
        if el[2] == username:
            for i in range(len(name_columns)-1):
                if name_columns[i] <= time and name_columns[i+1] > time:
                    text += str(name_columns[i]) + ' ' + el[i+9] +'\n'
                    return text

def timetable_by_familia(familia):
    text = ''
    for el in arr:
        if el[0] == familia:
            text += el[0] + ' ' + el[1] + '\n'
            text += 'Отдел: ' + el[5] + '\n'
            text += 'Сейчас на точке: '
            text += my_timetable_now(el[2])
            text += my_timetable_continue(el[2])
            return text

def timetable_by_username(username):
    text = ''
    for el in arr:
        if el[2] == username:
            text += el[0] + ' ' + el[1] + '\n'
            text += 'Отдел: ' + el[5] + '\n'
            text += 'Сейчас на точке: '
            text += my_timetable_now(el[2])
            text += my_timetable_continue(el[2])
            return text

def timetable_department(name):
    text = name.upper() + '\n'
    for el in arr:
        a = el[5].split(',')
        if name.lower() in a:
             text += (el[0] + ' ' + el[1] + ': ').upper()
             text += str(my_timetable_now(el[2]))
    return text
