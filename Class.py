#Class with def function in it and call

##Example 1
class Building:
    
    def __init__(self, number):
        self.number = number

b = Building(245)

b.number

#Output

245

##Example 2
class Dog:    
    def woof(self):
        return 'woof!'

t = Dog()
t.woof()

#Output
'woof!'

#Example 3
class Candy:
    flavor = 'sweet'
    
    def __init__(self, name):
        self.name = name
        
c = Candy('Chocolate')

c.name

#Ouput
'Chocolate'
#Class with multiple def function in it and call

class Dog:
    def __init__(self):
        pass
    
    def bark(self):
        return "bark bark bark bark bark bark..."

d = Dog()
d.bark()


#Ouput 
"bark bark bark bark bark bark..."



