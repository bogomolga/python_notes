import function

def show_menu():
    print("1 - добавить заметку")
    print("2 - редактировать заметку по номеру")
    print("3 - вывести все заметки")
    print("4 - удалить заметку по номеру")
    print("5 - вывести заметку по номеру")
    print("6 - выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            function.add_note()
        elif choice == "2":
            function.edit_note()
        elif choice == "3":
            function.view_notes()
        elif choice == "4":
            function.delete_note()
        elif choice == "5":
            function.view_note()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неправильный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()