# a list of cafe drink menu
drink_manu = ["Americano","Espresso","Latte","Mocha"]
print(drink_manu)

drink_manu.append("Green_tea")
print(drink_manu)

drink_manu.remove("Espresso")
print(drink_manu)

drink_manu.insert(0,"Cappuccino")
print(drink_manu)

print(drink_manu[0])

print(drink_manu[1])

for d in drink_manu:
    print(d)

print(*drink_manu)

for i,d in enumerate(drink_manu):
    print(i,d)

for i,d in enumerate(drink_manu, start=0):
    print('เมนูที่ {} {}'.format(i,d))

for i,d in enumerate(drink_manu, start=1):
    print('เมนูที่ {} {}'.format(i,d))

drink_manu[1] = 'Black_coffee'
print(drink_manu)

del drink_manu[2]
print(drink_manu)

len(drink_manu)

for i in range(4):
    print(drink_manu[i])

drink_manu2 = {'1':'Americano','2':'Espresso','3':'Latte','4':'Mocha'}

print(drink_manu2['1'])

for n in drink_manu2:
    print(n)

for n in drink_manu2.items():
    print(n)

for n in drink_manu2.items():
    print(n[0])

for n in drink_manu2.keys():
    print(n)

for n in drink_manu2.values():
    print(n)
