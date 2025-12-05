import flask
baza = {}


while True:
    ism = input("Ism kiriting: ")
    parol = input('Parol kiriting: ')
    if ism:
        baza['ism'] = ism
        break
    else:
        print("Ism kiritilmagan !")
print(baza)