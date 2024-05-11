class object1():
    def __init__(self):
        self.name = "object1"
class object2():
    def __init__(self):
        self.name = "object2"

class object3():
    def __init__(self):
        self.name = "object3"


class Factory:
    @staticmethod
    def create_object(some_property):
        if some_property == 'A':
            return object1()
        if some_property == 'B':
            return object2()
        if some_property == 'C':
            return object3()
        return None




ob = Factory.create_object("A")
print(ob.name)

#================================================================


class singletone:
    def __new__(cls):
        return cls 

    def __init__(self) -> None:
        self.name = None


obj = singletone()
obj.name = "I am a Singleton"
second_obj = singletone()
print(second_obj.name)  

#================================================================
class Washing:
    def wash(self):
        print('Washing')

class Drying:
    def dry(self):
        print('Drying')

class Machine:
    def __init__(self):
        self.washing = Washing()  # Create an instance of Washing
        self.drying = Drying()    # Create an instance of Drying

    def start(self):
        self.washing.wash()  # Call the wash method of the Washing instance
        self.drying.dry()    # Call the dry method of the Drying instance

obu = Machine()
obu.start()


