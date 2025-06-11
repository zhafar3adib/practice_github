def name_of_function():
    print("Hello")
    print("World!")

def hello_name(name='Purwadhika'): #set default input value
    print(f'Hello {name}')

def square_it(num):
    squared = num **2
    return squared

name_of_function()
hello_name('zhafar')
hello_name()


print(f'Square of 12 is {square_it(12)}')

def multiply(a,b):
    return a*b

print(multiply(5,4))

def sum_total(*args): #positional variable argument, bebas isi angka apa aja
    sum_number = 0
    for i in args:
        sum_number += i
    return sum_number

print(sum_total(1,2,3,4,5.5))

def print_data(**kwargs): #bebas isi apa aja, format dictionary
    for k,v in kwargs.items():
        print(f'{k} : {v}')

print_data(nama = 'zhafar', umur=25)

multipe = lambda a,b : a*b #hanya untuk single command

print(multipe(10,9))