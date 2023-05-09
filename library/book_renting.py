import csv

WYPOZYCZENIE KSIAZKI/KSIAZEK

def rent_a_book(*books):
    users_IDs = books[0]

    with open('book.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)     # each line as dict
        list_of_IDs = []
        for row in csv_reader:
            ID_value = list(row.values())[0]
            list_of_IDs.append(ID_value)


    for ID in users_IDs:

    if ID_check:
        print(f'Pomyslnie wypozyczyles ksiazki o ID: {users_IDs}.')
    else:
        print('Nie udalo Ci wypozyczyc ksiazek.')


# users_IDs_var = []
# var1 = input('Czy chcesz wypozyczyc ksiazke?')
# while var1 == 'tak':
#     ID = input('wprowadz id ksiazki jaka chcesz wypozyczyc: ')
#     while ID:
#         try:
#             int(ID)
#             users_IDs_var.append(ID)
#             var1 = input('Czy chcesz wypozyczyc kolejna ksiazke?')  # obsluga wyjatku
#             break
#         except ValueError:
#             print('Prosze wprowadzic numer ID!')
#             break


# rent_a_book(users_IDs_var)


# ZWROT KSIAZKI


# def return_a_book(ID):
#     with open('book.csv', mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)     # each line as dict
#         list_of_IDs = []
#         for row in csv_reader:
#             ID_value = list(row.values())[0]
#             list_of_IDs.append(ID_value)
#         csv_file.close()
#
#     if str(ID) in list_of_IDs:
#         print('Pomyslnie zwrociles ksiazke!')
#     else:
#         print('Nie odnaleziono podanego numeru ID ksiazki.')


# ID_return = input('Wprowadz numer ID ksiazki: ')
# while ID_return:
#     try:
#         ID_return = int(ID_return)
#         break
#     except ValueError:
#         print('Prosze wprowadzic numer ID!')
#         break
#
# return_a_book(ID_return)
















