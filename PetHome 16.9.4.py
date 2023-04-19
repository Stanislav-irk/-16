class Clients:
    def __init__(self, name, lastname, city):
        self.name = name
        self.lastname = lastname
        self.city = city
    def get_guest(self):
        return f'{self.name}, {self.lastname}, r {self.city}.'


clients_1 = Clients('Сергей', 'Иванов', 'Москва')
clients_2 = Clients('Валерий', 'Петров', 'Иркутск')

guest_list = [clients_1, clients_2]

for guest in guest_list:
    print(guest.get_guest())
