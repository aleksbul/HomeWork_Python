FILE_PATH = r'new.txt'

def add_user():
    with open (FILE_PATH, 'a', encoding='utf8') as f:
        surname = input("Введите фамилию: ").title()
        name = input("Введите имя: ").title()
        phone_number = input("Введите номер телефона: ")
        f.write(f'\n{surname} {name} {phone_number}')
    print()
    print("Контакт успешно добавлен.")
      

def read_all_user():
    with open (FILE_PATH, 'r', encoding='utf8') as f:
        for line in f:
            print(line.strip())

def user_search():
    with open (FILE_PATH, 'r', encoding='utf8') as f:
        key_word = input('Поиск: ').casefold()
        result = []
        for line in f:
            if key_word in line.casefold():
                result.append(line)
        if len(result) == 1:
            print(f'Найден 1 контакт: ')
            return result[0]
        
        if len(result) > 1:
            print(f'Найдено {len(result)} контакта: ')
            print()
            for i, val in enumerate(result, start=1):
                print(f'{i} - {val}')
        
            index = int(input('Введите порядковый номер контакта, с которым хотите произвести дальнейшие операции: ')) - 1
            
            return result[index]

        if len(result) == 0:
            print("Совпадений не найдено.")
            
def edit_user(result):
    with open (FILE_PATH, 'r', encoding='utf8') as f:
        lines = f.readlines()
        
        for i in range(len(lines)):
            if lines[i] == result:
                surname = input("Введите новую фамилию: ").title()
                name = input("Введите новое имя: ").title()
                phone_number = input("Введите новый номер телефона: ")
                lines[i] = f'{surname} {name} {phone_number}\n'
    

    with open (FILE_PATH, 'w', encoding='utf8') as f:
        f.writelines(lines)
    print("Контакт изменен.")         

def delete_user(result):
    with open (FILE_PATH, 'r', encoding='utf8') as f:
        lines = f.readlines()    
        lines.remove(result)
    

    with open (FILE_PATH, 'w', encoding='utf8') as f:
        f.writelines(lines)
        print("Контакт удален.")


while (user_action := int(input("[1] - Показать весь список контактов\n[2] - Добавить контакт\n[3] - Найти контакт\n[4] - Выйти из программы\n\nВыберите действие: "))) != 4:
    match user_action:
        case 1:
            read_all_user()
            print()
        case 2:
            add_user()  
            print() 
        case 3:
            result = user_search()
            print()
            
            if result != None:
                print(result)
                while(user_action2 := int(input("[5] - Редактировать запись\n[6] - Удалить запись\n[7] - Выйти в предыдущее меню\nВыберите действие: "))) != 7:
                    match user_action2:
                        case 5:
                            edit_user(result)
                            break
                        case 6:
                            delete_user(result)
                            break
                        case _:
                           print("неверно")                
                           
        case _:
            print("неверно")


