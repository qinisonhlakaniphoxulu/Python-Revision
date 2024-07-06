class Person():
    def __init__ (self, name):
        self.name = name
    
    def talk(self):
        print("talked")

first_person = Person("Qiniso")
first_person.talk()