from verify_email import verify_email
import contextlib
import sqlite3
import csv

names_list = []
surnames_list = []
domains_list = []

def transliterate(word):
   dict = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ja', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CZ','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}
        
   for key in dict:
      word = word.replace(key, dict[key])
   return word

def verify_execute(name, surname, email):
    # Проверяем почтовые адреса на валидность и записываем в БД
    if (is_verify == 'y'):
        if (verify_email(email) == True): 
            cursor.execute("INSERT INTO emails VALUES (?,?,?)", (name, surname, email))
            connect.commit()
    else: 
        cursor.execute("INSERT INTO emails VALUES (?,?,?)", (name, surname, email))
        connect.commit()
    

is_verify = input('Проверять адреса на валидность (увеличится время обработки) - y/n: ')
name_index = int(input('Введите номер столбца с именами(какой он по счёту): ')) - 1
surname_index = int(input('Введите номер столбца с фамилиями: ')) - 1
domain_index = int(input('Введите номер столбца с доменами: ')) - 1

print("Читается...")

with open("names.csv", encoding='utf-8') as names:
    file = csv.reader(names, delimiter = ";")
    
    count = 0
    for row in file:
        if (count == 0): 
            count += 1
            continue

        names_list.append(transliterate(row[name_index]))

with open("surnames.csv", encoding='utf-8') as surnames:
    file = csv.reader(surnames, delimiter = ";")
    
    count = 0
    for row in file:
        if (count == 0): 
            count += 1
            continue

        surnames_list.append(transliterate(row[surname_index]))

with open("domains.csv", encoding='utf-8') as domains:
    file = csv.reader(domains, delimiter = ";")
    
    count = 0
    for row in file:
        if (count == 0): 
            count += 1
            continue

        domains_list.append(row[domain_index])


print("Заполняется база...")

with contextlib.closing(sqlite3.connect("emails.db")) as connect: # Автоматически закрывается подключение при завершении процесса
    with connect: # Автоматически делает коммит
        with contextlib.closing(connect.cursor()) as cursor: # Закрывает курсор
            cursor.execute("""CREATE TABLE emails
                (name text, surname text, email text)
            """)

            # Генерация почтовых адресов
            for name in names_list:
                for surname in surnames_list:
                    for domain in domains_list:
                        cursor = connect.cursor()

                        # Записываем в базу данных все имена, фамилии и соответствующие им почтовые адреса
                        verify_execute(name, surname, "{0}@{1}".format(name, domain))
                        verify_execute(name, surname, "{0}@{1}".format(surname, domain))
                        verify_execute(name, surname, "{0}{1}@{2}".format(name, surname, domain))
                        verify_execute(name, surname, "{0}.{1}@{2}".format(name, surname, domain))
                        verify_execute(name, surname, "{0}{1}@{2}".format(name[0], surname, domain))
                        verify_execute(name, surname, "{0}.{1}@{2}".format(name[0], surname, domain))
                        verify_execute(name, surname, "{0}{1}@{2}".format(name, surname[0], domain))
                        verify_execute(name, surname, "{0}.{1}@{2}".format(name, surname[0], domain))
                        verify_execute(name, surname, "{0}{1}@{2}".format(name[0], surname[0], domain))
                        verify_execute(name, surname, "{0}.{1}@{2}".format(name[0], surname[0], domain))
                        verify_execute(name, surname, "{0}{1}@{2}".format(surname, name, domain))
                        verify_execute(name, surname, "{0}.{1}@{2}".format(surname, name, domain))
                        verify_execute(name, surname, "{0}{1}@{2}".format(surname, name[0], domain))
                        verify_execute(name, surname, "{0}.{1}@{2}".format(surname, name[0], domain))
                        verify_execute(name, surname, "{0}{1}@{2}".format(surname[0], name, domain))
                        verify_execute(name, surname, "{0}.{1}@{2}".format(surname[0], name, domain))
                        verify_execute(name, surname, "{0}{1}@{2}".format(surname[0], name[0], domain))
                        verify_execute(name, surname, "{0}.{1}@{2}".format(surname[0], name[0], domain))
                        verify_execute(name, surname, "{0}-{1}@{2}".format(name, surname, domain))
                        verify_execute(name, surname, "{0}-{1}@{2}".format(name[0], surname, domain))
                        verify_execute(name, surname, "{0}-{1}@{2}".format(name, surname[0], domain))
                        verify_execute(name, surname, "{0}-{1}@{2}".format(name[0], surname[0], domain))
                        verify_execute(name, surname, "{0}-{1}@{2}".format(surname, name, domain))
                        verify_execute(name, surname, "{0}-{1}@{2}".format(surname, name[0], domain))
                        verify_execute(name, surname, "{0}-{1}@{2}".format(surname[0], name, domain))
                        verify_execute(name, surname, "{0}-{1}@{2}".format(surname[0], name[0], domain))
                        verify_execute(name, surname, "{0}_{1}@{2}".format(name, surname, domain))
                        verify_execute(name, surname, "{0}_{1}@{2}".format(name[0], surname, domain))
                        verify_execute(name, surname, "{0}_{1}@{2}".format(name, surname[0], domain))
                        verify_execute(name, surname, "{0}_{1}@{2}".format(name[0], surname[0], domain))
                        verify_execute(name, surname, "{0}_{1}@{2}".format(surname, name, domain))
                        verify_execute(name, surname, "{0}_{1}@{2}".format(surname, name[0], domain))
                        verify_execute(name, surname, "{0}_{1}@{2}".format(surname[0], name, domain))
                        verify_execute(name, surname, "{0}_{1}@{2}".format(surname[0], name[0], domain))


print('Операция прошла успешно, результат записан в файл email.db')
print('Для повторной операции удалите файл email.db и замените входные файлы')
