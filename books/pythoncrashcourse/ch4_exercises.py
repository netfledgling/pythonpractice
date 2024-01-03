#4-1 Pizzas
pizzas = ['cheese', 'chicken', 'deep']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")

#4-2 Animals
animals = ['dog', 'cat', 'hamster']
for animal in animals:
    print(f"A {animal} would make a great pet!")
print("These animals are popular pets.")

#4-3 Counting to Twenty 
for value in range(1,21):
    print(value)

#4-4 One Million
numbers = list(range(1,1000001))
#for i in numbers:
#    print(numbers)

#4-5 Summing a Million
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6 Odd Numbers
odd_numbers = list(range(1,20,2))
for odd in odd_numbers:
    print(odd)

#4-7 Threes - FIX THIS
multiples = []
for value in range(3,30):
    multiples.append(value*3)
print(multiples)

multiples = [value*3 for value in range(3,30)] #using list comprehension

#4-8 Cubes
cubes = []
for value in range(1,11):
    cubes.append(value**3)
for cube in cubes:
    print(cube)

#4-9 Cube Comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)

#4-10 Slices
print("The first three items in the list are: ")
print(cubes[0:3])

print("Three items from the middle of the list are: ")
#print(cubes[])

print("The last three items are: ")
print(cubes[-3:])

#4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append("butter chicken")
friend_pizzas.append("pepperoni")
print("My favorite pizzas are: ") 
print(pizzas[:])
print("My friend's favorite pizzas are: ") 
print(friend_pizzas[:])

#4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
for food in my_foods:
    print(food)

#4-13 Buffet
buffet = ('chicken', 'rice', 'water', 'sauce', 'dessert')
#buffet[0] = 'drink' #should result in error

buffet = ('drinks', 'water', 'rice', 'sauce', 'dessert') #modified
for item in buffet:
    print(item)

#4-14 PEP 8
# Access PEP 8 Documentation - Done

#4-15 Code Review
# Modify programs to match PEP 8 - Done 
