#1. single values accessing

cars = {'model': 'mercedez','year':'1998','safety':'yes'}
print(cars['model'])
print(cars.get('year'))

#2. multiple values
cars = {'model': 'mercedez','year':'1998','safety':'yes'}
print(cars.values())

#3. accessing keys

cars = {'model': 'mercedez','year':'1998','safety':'yes'}
print(cars.keys())

#4. accessing key value pairs

cars = {'model': 'mercedez','year':'1998','safety':'yes'}
print(cars.items())