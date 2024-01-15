
def add_contact(file):
    last_name = input('фамилия ')
    first_name = input('имя ')
    patronymic = input('отчество ')
    phone = input('номер ')
    with open(file, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name},{first_name},{patronymic},{phone}\n')

def get_contacts_from_file(file):
    with open(file, 'r', encoding='utf-8') as fd:
        contacts = fd.readlines()
    # c = [contact.rstrip().split(',') for in contacts]
    # for contact in contacts:
    #     [0].append(contact.rstrip().split(','))
    result = []
    for i, c in enumerate(contacts):
        i += 1
        # print(f'{i} = {c}')
        lst = [str(i)]
        lst.extend(c.rstrip().split(','))
        # print(lst)
        result.append(lst)
    return result
    # return [[idx].extend(contact.rstrip().split(',')) for idx, contact in enumerate(contacts)]

def print_contacts(contacts_list):
    for contact in contacts_list:
        print(' | '.join(contact))

def show_all(file):
    contacts = get_contacts_from_file(file)

    print_contacts(contacts)

def search_contacts(file):
    search_str = input('введите фамилию для поиска: ').lower()
    contacts = get_contacts_from_file(file)
    search_result = []
    for contact in contacts:
        if search_str in contact[1].lower():
            search_result.append(contact)
    # print(search_result)
    print_contacts(search_result)
    return search_result


def copy_data (file, target_file):
    try:
        line_number = int(input('Введите номер строки: '))
        with open(file, 'r') as source:
            lines = source.readlines()
            if line_number < 1 or line_number > len(lines):
                print('Неправильный номер строки')
                return
            line_to_copy = lines[line_number - 1]
            with open(target_file, 'a') as target:
                target.write(line_to_copy)
        print('Данные успешно скопированы')
    except FileNotFoundError:
        print('Файл не найден')


def edit_contacts(f):
    res = search_contacts(f)
    # print_contacts(res)
    select_contact = int(input('выберите индекс '))
    all_contacts = get_contacts_from_file(f)
    print(all_contacts)
    # old_data = all_contacts[select_contact]
    last_name = input('фамилия или enter еслиоставить прежнее ')
    first_name = input('имя или enter еслиоставить прежнее ')
    patronymic = input('отчество или enter еслиоставить прежнее ')
    phone = input('номер или enter еслиоставить прежнее ')
    if len(last_name) > 0:
        all_contacts[select_contact][1] = last_name
    if len(last_name) > 0:
        all_contacts[select_contact][2] = first_name
    if len(last_name) > 0:
        all_contacts[select_contact][3] = patronymic
    if len(last_name) > 0:
        all_contacts[select_contact][4] = phone
    print(all_contacts)
    res = []
    for i in all_contacts:
        res.append(','.join())
def main():
    file_name = 'contacts.txt'
    target_file = 'target_file.txt'
    flag = True
    while flag:
        user_answer = input('Для записи - 1, Для чтения - 2, Для поиска по фамилии - 3,Редактировать контакт - 4, для переноса строки в другой файл - 5, Для выхода - 0   ')
        if user_answer == '1':
            add_contact(file_name)
        elif user_answer == '2':
            show_all(file_name)
        elif user_answer == '3':
            print_contacts(search_contacts(file_name))
        elif user_answer == '4':
            edit_contacts(file_name)
        elif user_answer == '5':
            copy_data(file_name, target_file)
        elif user_answer == '0':
            print('спсибо')    
            flag = False

if __name__ == '__main__':
    main()



