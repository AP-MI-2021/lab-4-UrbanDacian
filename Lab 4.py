def citire_lista():
    """
    Formeaza lista necesara prin citirea numarului de elemente si a elementelor propiu-zise.
    :return: Returneaza lista citita.
    """
    lst = []
    n = int(input("Dati nr. de elemente: "))
    print("Dati siruri de caractere formate din litere mici a-z, fara numere, simboluri sau spatii")
    for i in range(n):
        lst.append((input("l[" + str(i) + "]=")))
    return lst


def apare_in_lista(lista, sir):
    """
    Verifica daca un sir apare in lista.
    :param lista: Lista initiala.
    :param sir: Sirul cautat in lista.
    :return: Returneaza "DA" daca sirul apare in lista si "NU" in caz contrar.
    """
    copie = lista[:]
    if copie.count(sir) > 0:
        return "DA"
    else:
        return "NU"


def test_apare_in_lista():
    assert apare_in_lista(['a', 'abc', 'def', 'b', 'ghi'], 'c') == "NU"
    assert apare_in_lista(['aaa', 'bbb', 'cmtc', 'drd', 'aaa'], 'drd') == "DA"
    assert apare_in_lista([], 'a') == "NU"


def elemente_care_se_repeta(lista):
    """
    Creeaza o lista formata din elemntele care se repeta de mai multe ori in lista initiala.
    :param lista: Lista initiala
    :return: Returneaza o lista formata din elemntele care se repeta de mai multe ori in lista initiala.
    """
    copie = lista[:]
    rezultat = []
    ok = 0
    for x in copie:
        if copie.count(x) > 1 and rezultat.count(x) == 0:
            rezultat.append(x)
            ok = 1
    if ok == 1:
        return rezultat
    else:
        return "UNIC"


def test_elemente_care_se_repeta():
    assert elemente_care_se_repeta(['aaa', 'bbb', 'cmtc', 'drd']) == "UNIC"
    assert elemente_care_se_repeta(['a', 'b', 'c', 'a']) == ['a']
    assert elemente_care_se_repeta(['a', 'b', 'zzz', 'c', 'zzz', 'a']) == ['a', 'zzz']


def elemente_palindrom(lista):
    """
    Creeaza o lista formata din elemente dintr-o lista initiala care sunt palindrom.
    :param lista: Lista initiala.
    :return: Returneaza o lista formata din elemente care sunt palindrom.
    """
    copie = lista[:]
    rezultat = []
    for x in copie:
        if x == x[::-1]:
            rezultat.append(x)
    return rezultat


def test_elemente_palindrom():
    assert elemente_palindrom(['ada', 'abc', 'cmtc', 'drd', 'aaa']) == ['ada', 'drd', 'aaa']
    assert elemente_palindrom(['abc', 'def', 'ghi', 'jkl']) == []
    assert elemente_palindrom(['abc', 'def', 'mmm', 'ghi', 'jkl']) == ['mmm']


def main():
    test_apare_in_lista()
    test_elemente_care_se_repeta()
    test_elemente_palindrom()
    lista = []
    while True:
        print("1. Citire lista.")
        print("2. Verificati dacă un șir de caractere citit de la tastatură se găsește în listă.")
        print("3. Afișați o listă cu toate șirurile de caractere care se repetă în listă.")
        print("4. Afișați toate șirurile de caractere din lista care sunt un palindrom.")
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = citire_lista()
        elif optiune == "2":
            sirul = input("Dati sirul:")
            print(apare_in_lista(lista, sirul))
        elif optiune == "3":
            print(elemente_care_se_repeta(lista))
        elif optiune == "4":
            print(elemente_palindrom(lista))
        elif optiune == "x":
            print("Ati iesit din program!")
            break
        else:
            print("!!! Optiune gresita !!!")


main()