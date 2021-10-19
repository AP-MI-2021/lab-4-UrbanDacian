def termen_din_sir(l):
    '''
    Determina daca un sir de elemente se afla in lista
    :param l: Lista de siruri de elemente
    :return: True daca exista sirul in lista , respectiv False altfel
    '''
    sir = str(input("Introduceti termenul de verificat : "))
    for i in l:
        if i == sir:
            return True
    return False


def printMenu():
    print("1. Citire lista")
    print("2. Verifica daca un sir de caractere exista in lista")
    print("3. Afiseaza o lista cu toate palindroamele din lista initiala")
    print("x. Inchide programul")


def citire_lista():
    l=[]
    listAsString  = input("Lista de elemente ")
    givenString = listAsString.split(",")
    for x in givenString:
        l.append(x)
    return l

def este_palindrom(l):
    rezultat = []
    for x in l:
        if x == x[::-1]:
            rezultat.append(x)
    return rezultat

def main():
    l=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l=citire_lista()
        elif optiune == "2":
            print(termen_din_sir(l))
        elif optiune == "3":
            print(este_palindrom(l))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati.")


main()