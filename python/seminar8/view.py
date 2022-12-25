import data_operation as d

def main_menu(): 
    print("Вас приветствует умный телефонный справочник!\nПожалуйста,\
введите нужную цифру в зависимости от Ваших целей:\n\
    1. Показать все существующие контакты\n\
    2. Добавить новый контакт\n\
    3. Выполнить поиск по существующему контакту\n\
    4. Выход") 
    choice = input("введите выбранную цифру: ") 
    if choice == "1": 
        myfile = open(d.new_file("filename"), "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "В телефонной книге нет контакта") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter чтобы продолжить") 
        main_menu() 
    elif choice == "2": 
        d.newcontact() 
        enter = input("Нажмите Enter чтобы продолжить") 
        main_menu() 
    elif choice == "3": 
        d.searchcontact() 
        enter = input("Нажмите Enter чтобы продолжить") 
        main_menu() 
    elif choice == "4": 
        print("Благодарим Вас за использование телефонной книги!") 
    else: 
        print( "Пожалуйста, предоставьте корректные входные данные!\n") 
        enter = input("Нажмите Enter чтобы продолжить") 
        main_menu() 
 