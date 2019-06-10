def sortowanie(lista_memow,wagi_memow,ceny_memow,wielkosc_mb_memow):    #sortowanie babelkowe
    for i in range(0,len(lista_memow)):
        j=len(lista_memow)-1
        while j>i:  #sortowanie od najbardziej oplacalnego do najmniej wagi(cena/wielkosc)
            if wagi_memow[j] > wagi_memow[j-1]:
                tmp1 = wagi_memow[j]
                wagi_memow[j] = wagi_memow[j-1]
                wagi_memow[j-1] = tmp1

                #jednoczesnie sortujac wage synchronizuje kazdy przeniesiony
                #element wzgledem pozostalych parametrow (element z listy, cena, wielkosc)

                tmp2 = lista_memow[j]
                lista_memow[j] = lista_memow[j-1]
                lista_memow[j-1] = tmp2

                tmp3 = ceny_memow[j]
                ceny_memow[j] = ceny_memow[j-1]
                ceny_memow[j-1] = tmp3

                tmp4 = wielkosc_mb_memow[j]
                wielkosc_mb_memow[j] = wielkosc_mb_memow[j - 1]
                wielkosc_mb_memow[j - 1] = tmp4
            j-=1
    return lista_memow,wagi_memow,ceny_memow,wielkosc_mb_memow

def calculate(usb_size, memes): #algorytm zachlanny

# ---------------------------INICJALIZACJA----------------------------

    usb_size_mb = usb_size * 1024
    ilosc_memow = len(memes)
    lista_memow = (list(range(0,ilosc_memow)))
    wielkosc_mb_memow = []
    wagi_memow = []
    ceny_memow = []
    blokada = 0
    najlepsza_kolejnosc_memow_nazwy = set()
    cena=0

    for i in range(0, len(lista_memow)):
        ceny_memow.append(memes[i][2])
        wielkosc_mb_memow.append(memes[i][1])
        wagi_memow.append(ceny_memow[i] / wielkosc_mb_memow[i])

    najmniejszy_mem = min(wielkosc_mb_memow)

# ---------------------------ALGORYTM----------------------------

    sortowanie(lista_memow,wagi_memow,ceny_memow,wielkosc_mb_memow)

    for i in range(0,ilosc_memow):  #wkladanie do listy rozwiazania memow i kolejno najwiekszej wadze
        if ( (usb_size_mb - wielkosc_mb_memow[i]) >= 0 ) and blokada != 1:
            usb_size_mb -= wielkosc_mb_memow[i]
            cena += ceny_memow[i]

            najlepsza_kolejnosc_memow_nazwy.add(memes[lista_memow[i]][0])
            if usb_size_mb < najmniejszy_mem:   #jesli pozostala dostepna waga jest mniejsza niz najmniejszy mem to program nie pozwala wejsc do petli powyzej
                blokada = 1

    return(cena,najlepsza_kolejnosc_memow_nazwy)