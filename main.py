from collections import UserDict


class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str) -> None | str:
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('phone must have 10 symbols')


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone_number: str) -> None | str:
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break
        else:
            raise ValueError(f'phone {phone_number} not found in the record')
        
    def edit_phone(self, old_phone: str, new_phone: str) -> None | str:
        for id, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[id] = Phone(new_phone)
                break
        else:
            raise ValueError(f'phone {old_phone} not found in the record')        
        
    def find_phone(self, phone_number: str) -> Phone | str:
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        # else:
        #     raise ValueError(f'phone {phone_number} not found in the record')          

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"    


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
        
    def find(self, name: str) -> str:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if self.find(name):
            self.data.pop(name)



if __name__ == '__main__':
    book = AddressBook()

    john_record = Record('John')
    john_record.add_phone('1234567890')
    john_record.add_phone('2222222222')
    book.add_record(john_record)
    john = book.find('John')
    #print (john)

    jane_record = Record('Jane')
    jane_record.add_phone('3333333333')
    jane_record.add_phone('4444444444')
    book.add_record(jane_record)
    jane = book.find('Jane')
    print (jane.remove_phone('4444444444'))
    jane = book.find('Jane')
    print (jane)
    jane.edit_phone('3333333333', '0987654321')
    print (jane)
    found_phone = john.find_phone('1234567890')
    print (type(found_phone))


    # print ('s')
    # for name, record in book.data.items():
    #     print(record)