

c = "This is a 'string' inside a string"
print(c)
d = "Another way of adding \"quotes\" is this"
print(d)
e = "this is a single \
string"
print(e)

f = "1abc2abc3abc4abc"
print(f.replace("abc","ABC",2))
g = "This is a string"
print(f[1:6:2]) #It takes string from 1 till 5 and storing every secondth letter
print(g[:-1])

#To print reverse of a string
print(g[::-1])

h = ["This is a string"]
h.append("Trying new")
print(h)
h.insert(1,"Inserting in between")
print(h)

cars = ["audi","bmw","honda","toyota","volkswagen","ford","mazda"]
less_cars = cars[::-2]
print(less_cars)

#To pop the last element from the list
y = cars.pop()
print(y)
print(cars)

#To remove a particular element from the list
cars.remove("bmw")
print(cars)

slicing = cars[1:]

#List sorting
cars.sort()
print("#%"*20)
print(cars)
#Reverse list sorting
print(cars[::-1])


# To iterate items of more than 2 lists at the same time, use zip
#It will execute till the shortest list
for a,b in zip(h, cars):
    print (a+' ' +b)
