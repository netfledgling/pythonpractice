#3-1 Names
names = ['Basheer', 'Noor', 'Sana', 'Husna', 'Abdullah']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

#3-2 Greetings
print(f"Assalamualeykum dear {names[0]}!")
print(f"Assalamualeykum dear {names[1]}!")
print(f"Assalamualeykum dear {names[2]}!")
print(f"Assalamualeykum dear {names[3]}!")
print(f"Assalamualeykum dear {names[4]}!")

#3-3 Your Own List
vehicles = ['honda', 'toyota', 'bmw']
print(f"In the past, my parents owned a {vehicles[0]}, {vehicles[1]}, and a {vehicles[-1]}.")

#3-4 Guest List
guests = ['a', 'b', 'c']
print(f"Dear {guests[0]}, please join me for dinner!")
print(f"Dear {guests[1]}, please join me for dinner!")
print(f"Dear {guests[2]}, please join me for dinner!")

#3-5 Changing Guest List
print(f"Oh no! {guests[1].title()} can't make it.")
guests[1] = 'd'
print(f"Dear {guests[0]}, please join me for dinner!")
print(f"Dear {guests[1]}, please join me for dinner!")
print(f"Dear {guests[2]}, please join me for dinner!")

#3-6 More Guests
print("Dear Guests, I have a new table!")
guests.insert(0, 'e')
guests.insert(1, 'f')
guests.append('g')
print(f"Dear {guests[0]}, please join me for dinner!")
print(f"Dear {guests[1]}, please join me for dinner!")
print(f"Dear {guests[2]}, please join me for dinner!")
print(f"Dear {guests[3]}, please join me for dinner!")
print(f"Dear {guests[4]}, please join me for dinner!")
print(f"Dear {guests[5]}, please join me for dinner!")

#3-7 Shrinking Guest List
print("Dear guests, I sadly have space for only 2 of you.")
guest1 = guests.pop(1)
print(f"Dear {guest1}, I'm sorry we can't have you over.")
guest2 = guests.pop(2)
print(f"Dear {guest2}, I'm sorry we can't have you over.")
guest3 = guests.pop(3)
print(f"Dear {guest3}, I'm sorry we can't have you over.")
guest4 = guests.pop(0)
print(f"Dear {guest4}, I'm sorry we can't have you over.")

print(f"Dear {guests[0]}, please join us!")
print(f"Dear {guests[1]}, please join us!")

del guests[0]
del guests[-1]
print(guests)

#3-8 Seeing the World
places = ['turkey', 'dubai', 'qatar', 'malaysia', 'maldives']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3-9 Dinner Guests
# using original list from 3-4
guests = ['a', 'b', 'c']
print(f"So excited to see all {guests.len} of you at dinner!")

#3-10 Every Function
lang = ['c++', 'java', 'python', 'rust', 'swift']
# functions include: pop() remove() del() sort() sorted() reverse()
# functions cont.: insert() append() len() 

