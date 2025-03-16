# Generowanie liczby całkowitej z zakresu od 1 do 10 (w tym 1 i 10)
# liczba = random.randint(1, 10)

import random
import os
from time import sleep

zmienne = open('aprint_3d_zmienne.txt', 'r')
lista_zmiennych = []
f = zmienne.readlines()

def salon():
    global czy
    global z_zmiennych
    global energia
    os.system('cls')
    print('Dzień', dzień+1)
    print('Twoja energia to:', energia)
    if energia == 0:
        print('Musisz już iść spać!')
        input()
        sypialnia()
    print('')
    print('Jesteś w salonie. Co robisz: ')
    print('1. Idziesz do komputera')
    print('2. Idziesz do drukarni')
    print('3. Idź do galerii')
    print('4. Idź do sypialni')
    print('5. Zapisz i wyjdź')
    a = input()
    if a == '1':
        energia -= 1
        komputer()
    elif a == '2':
        energia -= 1
        drukarnia()
    elif a == '3':
        energia -= 1
        czy[2] = 1
        licznik()
        galeria()
    elif a == '4':
        sypialnia()
    elif a == '5':
        try:
            z_zmiennych = open('aprint_3d_zmienne.txt', 'w')
            z_zmiennych.write(str(kasa))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(drukarka))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(filament))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(czy[0]))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(czy[1]))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(l_filament))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(l_kasa))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(transport))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(energia))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(dzień))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(d_kasa))
            z_zmiennych.close()
            exit()
        except:
            z_zmiennych = open('aprint_3d_zmienne.txt', 'w')
            z_zmiennych.write(str(kasa))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(drukarka))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(filament))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(czy[0]))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(czy[1]))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(l_filament))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(l_kasa))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(transport))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(energia))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(dzień))
            z_zmiennych.write('\n')
            z_zmiennych.write(str(d_kasa))
            z_zmiennych.close()
            exit()
    else:
        salon()
def galeria():
    os.system('cls')
    print('Masz', kasa, '$')
    print('Do jakiego sklepu idziesz?')
    print('1. Z drukarkami')
    print('2. Z filamentem')
    print('3. Z środkami tramnsportu')
    print('4. Wróć do domu')
    a=input()
    if a == '1':
        s_drukarki()
    elif a == '2':
        s_filament()
    elif a == '3':
        s_transport()
    elif a == '4':
        czy[2]=1
        licznik()
        salon()
    else:
        galeria()
def komputer():
        global czy
        os.system('cls')
        print('Co chcesz sprawdziś w komputerze:')
        print('1. Pocztę')
        print('2. Wróć')
        a = input()
        if a == '1':
            mail()
        elif a == '2':
            salon()
        else:
            komputer()
def drukarnia():
    global drukarka
    global filament
    global czy
    global kasa
    global l_filament
    global l_kasa
    global d_kasa
    os.system('cls')
    if czy[1] == 0:
        os.system('cls')
        print('Nie masz na razie żadnego zlacania')
        a=input()
        salon()
    elif czy[1] == 1:
        os.system('cls')
        print('Masz', filament,'g filamentu')
        print('Potrzebny filament:')
        print(l_filament,'g')
        print('Przewidywany czas drukowania:')
        if drukarka == 0:
            print('Nie masz jeszcze drukarki')
            print('Przed wykonaniem zlecenia musisz ją kupić')
            a=input()
            salon()
        elif drukarka == 1:
            print('2 min')
        elif drukarka == 2:
            print('1 min')
        elif drukarka == 3:
            print('30 sek')
        a=input('Rozpocząć drukowanie zlecenia: ')
        if a == 'tak':
            os.system('cls')
            if filament >= l_filament:
                czy[2] = 0 
                licznik()
                os.system('cls')
                filament-=l_filament
                kasa+=l_kasa
                czy[1]=0
                print('Druk zakończony')
                print('Zdobyleś', l_kasa,'$')
                d_kasa += l_kasa
                l_filament = 0
                l_kasa = 0
                a=input()
                salon()
            elif filament < l_filament:
                os.system('cls')
                print('Nie masz wystarczającej ilości filamentu')
                a=input()
                salon()
        elif a == 'nie':
            salon()
        else:
            drukarnia()
def s_drukarki():
    global kasa
    global drukarka
    global czy
    os.system('cls')
    print('Masz', kasa,'$ pieniędzy')
    if drukarka == 0:
        os.system('cls')
        print('Chcesz kupić swoją pierwszą drukarkę: Ender3 500$')
        a = input()
        if a == 'tak':
            if kasa >= 500:
                os.system('cls')
                kasa=kasa-500
                drukarka=1
                czy[0]=1
                print('Kupiono Endera3!')
                a = input()
                galeria()
            elif kasa < 500:
                os.system('cls')
                print('Masz za malo pieniędzy!')
                a = input()
                galeria()
        elif a == 'nie':
            galeria()
        else:
            s_drukarki()
    elif drukarka == 1:
        os.system('cls')
        print('Chcesz kupić drukarkę: Prusa 800$')
        a = input()
        if a == 'tak':
            if kasa >= 800:
                kasa=kasa-800
                drukarka=2
                print('Kupiono Pruse!')
                a = input()
                galeria()
            elif kasa < 800:
                print('Masz za malo pieniędzy!')
                a = input()
                galeria()
        elif a == 'nie':
            galeria()
        else:
            s_drukarki()
    elif drukarka == 2:
        os.system('cls')
        print('Chcesz kupić drukarkę: Prusa-Pro 1000$')
        a = input()
        if a == 'tak':
            if kasa >= 1000:
                kasa=kasa-1000
                drukarka=3
                print('Kupiono Pruse-Pro!')
                a = input()
                galeria()
            elif kasa < 1000:
                print('Masz za malo pieniędzy!')
                a = input()
                galeria()
        elif a == 'nie':
            galeria()
        else:
            s_drukarki()
    elif drukarka == 3:
        os.system('cls')
        print('Masz już najlepszą drukarkę')
        a = input()
        galeria()
def s_filament():
    global filament
    global kasa
    os.system('cls')
    print('Masz', kasa,'$ pieniędzy')
    print('Masz', filament,'g filamentu')
    print('Cena za 1 kilogram: 100$')
    print('Wpisz wstecz żeby wyjść')
    a = input('Ile chcesz kupić kg filamentu: ')
    try:
        if int(a) > 0:
            if kasa >= int(a)*100:
                os.system('cls')
                kasa -= int(a)*100
                filament += int(a)*1000
                print('Kupileś ', int(a)*1000,'g filamentu')
                print('Masz lącznie ', filament, 'g filamentu')
                a=input()
                galeria()
            elif int(kasa) < int(a)*100:
                print('Masz za malo pieniędzy')
                a=input()
                s_filament()
        elif int(a) < 0:
            print('Źle wipaiania liczba')
            a=input()
            s_filament()
    except:
        if a == 'wstecz':
            galeria()
        else:
            s_filament()
def s_transport():
    global transport
    global kasa
    os.system('cls')
    if transport == 0:
        print('Chcesz kupić rower: 650$')
        a=input()
        if a == 'tak':
            if kasa >= 650:
                os.system('cls')
                kasa=kasa-650
                transport=1
                print('Kupiono Rower!')
                a = input()
                galeria()
            elif kasa < 650:
                os.system('cls')
                print('Masz za malo pieniędzy!')
                a = input()
                galeria()
        elif a == 'nie':
            galeria()
        else:
            s_transport()
    elif transport == 1:
        print('Chcesz kupić motor: 1000$')
        a=input()
        if a == 'tak':
            if kasa >= 1000:
                os.system('cls')
                kasa=kasa-1000
                transport=2
                print('Kupiono Rower!')
                a = input()
                galeria()
            elif kasa < 1000:
                os.system('cls')
                print('Masz za malo pieniędzy!')
                a = input()
                galeria()
        elif a == 'nie':
            galeria()
        else:
            s_transport()
    elif transport == 2:
        print('Masz już najlepszy środek transportu')
        input()
        galeria()
def sypialnia():
    global dzień
    global d_kasa
    global energia
    os.system('cls')
    dzień += 1
    print('Dzień', dzień, 'ukończony')
    print('Zarobileś', d_kasa, 'pieniędzy')
    energia=10
    d_kasa=0
    input()
    salon()
def mail():
    global czy
    global l_filament
    global l_kasa
    if czy[1] == 1:
        os.system('cls')
        print('Nie masz nowych wiadomości')
        a=input()
        komputer()
    elif czy[1] == 0:
        os.system('cls')
        l_filament = random.randint(300, 500)
        l_kasa = random.randint(200, 400)
        print('Masz nową zlecenie na druk')
        print('Do druku trzeba będzie zlużyć',l_filament,'filamentu')
        print('Wynagrodzenie to', l_kasa,'$')
        czy[1]=1
        a=input()
        komputer()
def licznik():
    global drukarka
    global czy
    global transport
    if czy[2] == 0:
        if drukarka == 1:
            czas=120
        elif drukarka == 2:
            czas=60
        elif drukarka == 3:
            czas=30

    elif czy[2] == 1:
        if transport == 0:
            czas=60
        if transport == 1:
            czas=30
        if transport == 2:
            czas=15

    while czas != 0:
        os.system('cls')
        print(czas)
        czas -= 1
        sleep(1)

while(1==1):
    os.system('cls')
    print('!Witaj w print 3d symulator!')
    print('1. Nowa gra')
    print('2. Wczytaj grę')
    a=input()
    if a=='1':
        czy=[0, 0, 0]
        kasa=600
        drukarka=0
        filament=0
        l_filament = 0
        l_kasa = 0
        transport = 0
        energia = 10
        dzień = 0
        d_kasa = 0
        salon()

    elif a=='2':
        for line in f:
            lista_zmiennych.append(line.strip())
        print(lista_zmiennych)

        czy=[]
        kasa=int(lista_zmiennych[0])
        drukarka=int(lista_zmiennych[1])
        filament=int(lista_zmiennych[2])
        czy.append(int(lista_zmiennych[3]))
        czy.append(int(lista_zmiennych[4]))
        czy.append(0)
        l_filament=int(lista_zmiennych[5])
        l_kasa=int(lista_zmiennych[6])
        transport=int(lista_zmiennych[7])
        energia=int(lista_zmiennych[8])
        dzień=int(lista_zmiennych[9])
        d_kasa=int(lista_zmiennych[10])
        salon()