def calculate(usb_size,memes):  #rozwiazanie dynamiczne

# ---------------------------INICJALIZACJA----------------------------
    usb_size_mb = usb_size * 1024
    wartosci = []
    waga = []
    ilosc_memow = len(memes)
    najlepsza_kolejnosc_memow_nazwy = set()
    najlepsza_kolejnosc_memow_lista = []
    dostepne_miejsce = usb_size_mb

    for i in range(0,len(memes)):
        wartosci.append(memes[i][2])
        waga.append(memes[i][1])

    #tworzenie macierzy o dlugosci ilosci memow oraz szerokosci usb_size_mb
    #w kazdym kroku usb_size_mb bedziemy przechowywac informacje o najwyzszym mozliwym
    #koszcie zestawu memow

    macierz = [[0 for i in range(usb_size_mb+1)] for i in range(ilosc_memow)]

# ---------------------------ALGORYTM----------------------------

    for mem_bierzacy in range (ilosc_memow):
        for waga_macierzy in range(usb_size_mb+1):

            # jesli mem bierzacy nie miesci sie w danej wagi macierzy to dana rubryka
            # macierzy jest wypelniana waga starego mema w tej wadze macierzy (jest to juz znana komorka pamieci)

            if waga[mem_bierzacy] > waga_macierzy:
                macierz[mem_bierzacy][waga_macierzy] = macierz[mem_bierzacy-1][waga_macierzy]
                continue

            #jezeli mem bierzacy miesci sie w danej wagi macierzy to
            #wybieramy wartosc wieksza z: starego mema w tej wadze macierzy lub
            #bierzacego mema ktory miesci sie do tej wagi macierzy oraz poprzedniego mema ale
            #o pomniejszonej wadze macierzy (o tyle ile zajal miejsca ten mem ktorego wkladamy)

            poprzednia_wartosc = macierz[mem_bierzacy-1][waga_macierzy]
            nowa_opcja = wartosci[mem_bierzacy] + macierz[mem_bierzacy-1][waga_macierzy - waga[mem_bierzacy]]
            macierz[mem_bierzacy][waga_macierzy] = max(poprzednia_wartosc,nowa_opcja)

    najlepszy_wynik = macierz[len(memes) - 1][usb_size_mb]
    wynik = najlepszy_wynik

    #dekodowanie powstalej macierzy aby dowiedziec sie jakie dokladnie memy
    #zostaly wykorzystane aby uzyskac najlepszy_wynik
    #dekodowanie bedzie sie odbywalo od gory do dolu macierzy

    for i in range((len(memes)-1), 0, -1):
        if wynik <= 0:
            break

        #jezeli bierzacy wynik nie jest rowny wartosci z brzegu macierzy o wysokosci i
        #to znaczy ze ten mem byl w zestawie najlepszych memow, nastepnie koryguje
        #wynik o wartosci mema ktory wpisalem, i dostepne miejsce

        if wynik == macierz[i - 1][dostepne_miejsce]:
            continue
        else:
            najlepsza_kolejnosc_memow_lista.append(i)
            wynik = wynik - wartosci[i]
            dostepne_miejsce = dostepne_miejsce - waga[i]



    for i in najlepsza_kolejnosc_memow_lista:   #dodawanie do setu nazw memow
        najlepsza_kolejnosc_memow_nazwy.add(memes[i][0])

    return(najlepszy_wynik,najlepsza_kolejnosc_memow_nazwy)
