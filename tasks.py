def add_task(lista_zadań):
    zadanie = input("Dodaj treść zadania: ").strip().lower()

    if zadanie:
        lista_zadań.append(zadanie)
        print("Zadanie dodano")
    else:
        print("Zadanie nie może być puste")