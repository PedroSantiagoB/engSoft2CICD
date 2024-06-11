class Person:
    def __init__(self, name, age, id, net_worth):
        self.name = name
        self.age = age
        self.id = id
        self.net_worth = net_worth

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_net_worth(self):
        return self.net_worth

    def set_net_worth(self, net_worth):
        self.net_worth = net_worth

    def get_id(self):
        return self.id

    def __str__(self):
        return f"Person{{age={self.age}, id={self.id}, net_worth={self.net_worth}, name='{self.name}'}}"
