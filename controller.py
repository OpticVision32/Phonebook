import view
import model

def run():
    view.greetings()
    
    while True:
        view.menu()
        answer = input('Ответ: ')
        if answer == '1':
            model.read_phonebook()
        if answer == '2':
            model.find()
        if answer == '3':
            model.add_contact()
            model.read_phonebook()
        if answer == '4':
            model.data_change()
        if answer == '5':
            model.data_delete()
        if answer == '6':
            break
