class Client:
    def __init__(self, name, lastname, city, balance):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'Client: {self.name}, {self.lastname}, {self.city}, Баланс {self.balance} руб.'
client_1 = Client('Сергей', 'Фролов', 'Москва', 1000)
print(client_1)
