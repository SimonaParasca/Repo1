# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# ex1
# if else este o functie prin care putem pune conditii pentru a afla informatii despre variabila astfel daca prin conditia
# if aflam raspunsul, codul nu va mai rula, iar daca nu, codul va cauta in elif sau pana ajunge la ultima conditie else

# ex2
x = 4
if x % 2 >= 0:
    print("whole number")
else:
    print("not a whole number")
# ex3
if x < 0:
    print("negative number")
elif x == 0:
    print("neutral number")
else:
    print("positive number")
# ex4
if x >= -2 or x <= 13:
    print("x is between this values")
else:
    print("x is not between this values")

# ex5
y = 2

if x - y < 5:
    print("the value is lower than 5")
else:
    print("the value is higher than 5")

# ex 6

print( not (x > 5 or x < 27))

# ex7
print( x == y)
print( x > y)

# ex8


# ex9
x = "s"

if x == ["a","e","i","o","u",]:
    print("x is a vocal")
else:
    print("x is not a vocal")

# ex10

x = int(input("CHOOSE YOUR GRADE"))

if x >= 9:
    print("A")
elif x >= 8:
    print("B")
elif x >= 7:
    print("C")
elif x >= 6:
    print("D")
elif x >= 4:
    print("E")
else:
    print("F")

# ex optionale
# ex1

x = 123
print(len(str("123")))
# ex2
if (len(str("123"))) == 6:
    print("it has 6 digits")
else:
    print("it does not have 6 digits")

print(len(str("123")) == 6)

# ex3

print( x % 2 == 0)

# ex4
x = 5
y = 6
z = 7
print(max(x,y,z,))

# ex5
# ex6

prop = "coral is either the stupidest animal or the smartest rock"
x = 4

print(len(prop))
print(prop[:-4])

# ex7

coral = "coral is either the stupidest animal or the smartest rock"

print(coral[53:58])
print(coral[0:53])

foodOrder = "today my food order was great"
print(len(foodOrder))

assert foodOrder[0] == foodOrder[28]
print("primul si ultimul caracter sunt la fel")


