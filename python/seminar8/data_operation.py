def new_file(filename):
    filename = "myphonebook.txt" 
    myfile = open(filename, "a+")
    return(filename) 
    
def searchcontact(): 
    searchname = input( "Пожалуйста, укажите действительное имя пользователя для поиска контактной записи:: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(new_file("filename"), "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Ваша необходимая контактная информация - это:", end = " ",) 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "Искомый контакт недоступен в электронной книге", searchname) 
 
def input_firstname(): 
    first = input( "Введите имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
def input_lastname(): 
    last = input( "Введите фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите номер телефона: ") 
    emailID = input( "Введите E-mail адрес: ") 
    
    with open("myphonebook.txt", "a") as file:
        file.write(firstname + "\n")
        file.write(lastname + "\n")
        file.write(phoneNum + "\n")
        file.write(emailID+ "\n")
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n")
   
    print( "Следующие контактные данные: \n " + contactDetails + "\nбыли успешно сохранены!") 
 
# filename = "myphonebook.txt" 
# myfile = open(filename, "a+") 
# myfile.close 
def main_menu(): 
    print("Вас приветствует умный телефонный справочник!\nПожалуйста,\
введите нужную цифру в зависимости от Ваших целей:\n\
    1. Показать все существующие контакты\n\
    2. Добавить новый контакт\n\
    3. Выполнить поиск по существующему контакту\n\
    4. Выход") 
    choice = input("введите выбранную цифру: ") 
    if choice == "1": 
        myfile = open(new_file("filename"), "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "В телефонной книге нет контакта") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter чтобы продолжить") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter чтобы продолжить") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter чтобы продолжить") 
        main_menu() 
    elif choice == "4": 
        print("Благодарим Вас за использование телефонной книги!") 
    else: 
        print( "Пожалуйста, предоставьте корректные входные данные!\n") 
        enter = input("Нажмите Enter чтобы продолжить") 
        main_menu() 
 