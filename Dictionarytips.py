
car = {"make":"bmw","model":"X1","year":2016}
print(car)
car["one"] = 1
print(car)

#nested dictionary
d = {'k1': {'nestk1':
                  {'tertiary_nested_k1' : 'tertiary_nested_val_1', 'tertiary_nested_k2':'tertiary_nested_val_2'}

                }

       }

print(d['k1']['nestk1']['tertiary_nested_k2'])

cars = {"bmw":{'model':'X1','year':'2016'}, "benz":{'model':'E350','year':'2014'}}
print(cars.keys())
print(cars.values())
print(cars.items())

# To make a copy of a dictionary
cars_copy = cars.copy()
print(cars_copy)

# To clear the dictionary
cars_copy.clear()

# To remove a key- value pair from dictionary
car.pop('year')
print(car)

#Tuple
t = (1,2,3,4,5,'3',4,5)
print(t[3])
#print the index of a particular element
print("The index of the string '3' is ",t.index('3'))

#print the count of the element in the tuple
print(t.count(4))

#To access both key and value of the dictionary:
for k,v in car.items():
    print ("key is:", k)
    print("value is", v)

