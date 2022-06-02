class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return {'name':self.name, 'age':self.age}

    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'
