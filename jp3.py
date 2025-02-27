class Person:
    def __init__(self, name, age, address, sex):
        self.__name = name  
        self.__age = age    
        self.__address = address
        self.__sex = sex
    def get_name(self):
        return self.__name
    
    
    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address        

    def set_address(self, address):
        self.__address=address   

    def get_sex(self):
        return self.__sex
    
    def set_sex(self, sex):
        self__sex=sex

    def get_age(self):
        return self.__age
    
    
    def set_age(self, age):
        if age >= 0:  
            self.__age = age
        else:
            print("Age cannot be negative")
    
# Example of using encapsulation
person = Person("JOHNPATRICK", 22, "caibaan", "male")
print(person.get_name())
print(person.get_address()) 
print(person.get_sex()) 
person.set_age(22)
print(person.get_age())   
