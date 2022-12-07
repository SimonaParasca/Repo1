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

# ex1

note_muzicale=["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
# suprascriere
notemuzicale2=note_muzicale[::-1]
print(notemuzicale2)

# ex2

print(note_muzicale.count("do"))
# ex3
list1=[3,1,0,2]
list2=[6,5,4]
print(list1 + list2)
list1.extend(list2)
print(list1)

# ex4
list3=list1+list2
list3.sort()
print(list3)
list3.remove(0)
print(list3)

# ex5
if len(list3) == 0:
    print("list is empty")
else:
    print("list is not empty")

# ex6
list3.clear()
print(list3)

# ex7
if len(list3) == 0:
    print("list is empty")
else:
    print("list is not empty")

# ex8
dict1={"ana":8, "gigel":10, "dorel":5}
print(dict1.keys())

# ex9

print("ana a luat nota " + str(dict1["ana"]))
print("gigel a luat nota " + str(dict1["gigel"]))
print("dorel a luat nota " + str(dict1["dorel"]))

# ex10
dict1['dorel'] = 6
print(dict1)

# ex11
dict1.pop('gigel')
print(dict1)
dict1["ionica"] = 9
print(dict1)

# ex12

zile_sapt={"luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"}
weekend={"sambata", "duminica"}
zile_sapt.add("luni")
print(zile_sapt)
print(weekend)

# ex 13

if weekend.issubset(zile_sapt):
    print("este un subset")
else:
    print("nu este")

# ex14

diferente = zile_sapt.difference(weekend)
print(diferente)

# ex15
intersectia= zile_sapt.intersection(weekend)
print(intersectia)

# tema5 functii
# ex1
def printSuma(a,b):
    return(a+b)
print(printSuma(3,4))

# ex2

def tipNumar(numar):
    if numar%2==0:
        return True
    else:
        return False

print(tipNumar(6))

# ex3

def numeleMeu(nume, prenume):
   return (len(nume)+len(prenume))

print(numeleMeu("parasca","simona"))

# ex4

def ariaDreptunghiului(lungime,latime):
    return(lungime*latime)
print(ariaDreptunghiului(9,5))

# ex5

# aria cercului pi*r2

def ariaCercului(Pi, raza):
    return(3.14*(raza**2))
print(ariaCercului(3.14,6))

# ex6
def caracter(cuvant):
    if cuvant.__contains__("a"):
        return True
    else:
        return False
print(caracter("simona"))

# ex7

def string_test(a):
    t={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in a:
        if c.isupper():
           t["UPPER_CASE"]+=1
        elif c.islower():
           t["LOWER_CASE"]+=1
        else:
           pass
    print (a)
    print ("No. of Upper case characters : ", t["UPPER_CASE"])
    print ("No. of Lower case Characters : ", t["LOWER_CASE"])

string_test('Simona Parasca')

# ex8

def nrPrime(n):
    list=[]
    for x in n:
        if x> 0:
            list.append(x)
    print(list)
nrPrime([9,45,-6,-89,4])

# ex9

def numere():
    a,s=11,12
    if(a>s):
        return a
    elif (a==s):
        return "numerele sunt egale"
    else:
        return s

print(numere())

# ex 10

def NumberFunction(numar,set):
    if numar not in set:
        print(f"am adaugat un numar nou {numar} in set")
        return True
    else:
        print(f"nu am adaugat un numar nou {numar} in set")
        return False

NumberFunction(9,{7,8,0,3,1})
