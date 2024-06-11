#Return the doc of the function
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

factorial.__doc__

#Output
'returns n!'

#Set Global Variable
this_var = 30

def func():
  nonlocal this_var
  global this_var
  this_var = 20
  print(this_var)
    
print(this_var)
func()
print(this_var)

#Output
30  
20  
20

#Example with iter()
w = 'python'

w_iterator = iter(w)

next(w_iterator)

#Output
'p'

#Example
def add_two(x: int)-> int:
  return x + 2

add_two(1)

#Output
3

