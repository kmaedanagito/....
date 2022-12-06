#FARMER

import random

temp = 0
bun = 0
bunn = [1,2,3,4,5,6,13,14,15,16,17,18]
sheep = 0
sheepp = [7,8,19,20,21]
pig = 0
pigg = [9,10,22]
cow = 0
coww = [23]
horse = 0
horsee = [11]
wolf = [24]
fox = [12]
dog = 1
bigdog = 1

def roll():
    global bun, sheep, pig, cow, horse, dog, bigdog
    dier = random.randint(1,12)
    dieb = random.randint(13,24)
    print(dier, dieb)
    if dier in bunn or dieb in bunn:
        temp = bun
        if dier in bunn and dieb in bunn:
            bun += 1
        if bun > 0:
            bun = bun//2 + bun
            print("Dostałeś ", bun - temp, "królików!")
    if dier in sheepp or dieb in sheepp:
        temp = sheep
        if dier in sheepp and dieb in sheepp:
            sheep += 1
        if sheep > 0:
            sheep = sheep//2 + sheep
            print("Dostałeś ", sheep - temp, " owiec!")
    if dier in pigg or dieb in pigg:
        temp = pig
        if dier in pigg and dieb in pigg:
            pig += 1
        if pig > 0:
            pig = pig//2 + pig
            print("Dostałeś ", pig - temp, "świń!")
    if dieb in coww:
        temp = cow
        if cow > 0:
            cow = cow//2 + cow
            print("Dostałeś ", cow - temp, "krów!")
    if dier in horsee:
        temp = horse
        if horse > 0:
            horse = horse//2 + horse
            print("Dostałeś ", horse - temp, "koni!")
    if dieb in wolf:
        if bigdog == 0:
            bun = 0
            sheep = 0
            pig = 0
            cow = 0
            horse = 0
            print("Niestety wilk pożarł twoje zwierzęta :(")
        else:
            bigdog -= 1
            print("Wilk pożarł twojego wielkiego psa!")
    if dier in fox:
        if dog == 0:
            bun = 0
            print("Niestety lis pożarł twoje króliki :(")
        else:
            dog -= 1
            print("Lis pożarł twojego psa!")

def wym(zwierze):
    global bun, sheep, pig, cow, horse, dog, bigdog
    if zwierze == "królik":
        ile = int(input("Ile owiec chcesz zamienić na króliki?\n"))
        if ile <= sheep:
            bun += 6*ile
            sheep -= ile
        else:
            print("Nie starczy ci owiec na wymianę!")
    elif zwierze == "owca":
        jakie = (input("Na owce chcesz zamienić króliki(K), świnie(S) czy psy(P)?"))
        ile = int(input("Ile owiec chcesz otrzymać w wyniku wymiany?\n"))
        if jakie == "K":
            if ile <= (bun//6):
                sheep += ile
                bun -= 6*ile
            else:
                print("Nie starczy ci królików na wymianę!")
        elif jakie == "S":
            if ile % 2 != 0:
                print("Nieprawidłowa liczba świń!")
            elif ile <= pig*2:
                sheep += ile
                pig -= ile/2
            else:
                print("Nie starczy ci świń na wymianę!")
        elif jakie == "P":
            if ile <= dog:
                sheep += ile
                dog -= ile
            else:
                print("Nie starczy ci psów na wymianę!")
    elif zwierze == "świnia":
        jakie = (input("Na świnie chcesz zamienić owce(O) czy krowy(K)?"))
        ile = int(input("Ile świń chcesz otrzymać w wyniku wymiany?\n"))
        if jakie == "O":
            if ile <= (sheep//2):
                pig += ile
                sheep -= 2*ile
            else:
                print("Nie starczy ci owiec na wymianę!")
        elif jakie == "K":
            if ile % 3 != 0:
                print("Nieprawidłowa liczba świń!")
            elif ile <= cow*3:
                pig += ile
                cow -= ile/3
            else:
                print("Nie starczy ci krów na wymianę!")
    elif zwierze == "krowa":
        jakie = (input("Na krowy chcesz zamienić świnie(S) czy duże psy(DP)?"))
        ile = int(input("Ile krów chcesz otrzymać w wyniku wymiany?\n"))
        if jakie == "S":
            if ile <= (pig//3):
                cow += ile
                pig -= 3*ile
            else:
                print("Nie starczy ci świń na wymianę!")
        elif jakie == "DP":
            if ile <= bigdog:
                cow += ile
                bigdog -= ile
            else:
                print("Nie starczy ci psów na wymianę!")
    elif zwierze == "pies":
        ile = int(input("Ile psów chcesz otrzymać w wyniku wymiany za owce?\n"))
        if ile <= sheep:
                dog += ile
                sheep -= ile
        else:
                print("Nie starczy ci owiec na wymianę!")
    elif zwierze == "dużypies":
        ile = int(input("Ile dużych psów chcesz otrzymać w wyniku wymiany za krowy?\n"))
        if ile <= cow:
                bigdog += ile
                cow -= ile
        else:
                print("Nie starczy ci krów na wymianę!")
    elif zwierze == "koń":
        if 2 <= cow:
                horse += 1
                print("✧･ﾟ: *✧･ﾟ:*BRAWO!!!! WYGRYWASZ!!!!*:･ﾟ✧*:･ﾟ✧")
        else:
                print("Nie starczy ci krów na wymianę!")

while horse < 1:
    print("Posiadasz: \n-", bun, "królików\n-", sheep, "owiec\n-", pig, "świń\n-", cow, "krów\n-", horse, "koni\n-",dog,"psów\n-", bigdog,"dużych psów")
    print("Rzuć kostkami (R) / Wymień zwierzęta(W)")
    decision = input()
    if decision == "R":
        roll()
    elif decision == "W":
        print("--------MARKET---------\n|1 owca = 6 królików  |\n|1 świnia = 2 owce    |\n|1 krowa = 3 świnie   |\n|1 koń = 2 krowy      |\n|1 pies = 1 owca      |\n|1 duży pies = 1 krowa|\n-----------------------")
        print("Jakie zwierze chcesz otrzymać w wyniku wymiany?(królik, owca, świnia, krowa, koń, pies, dużypies)")
        wym(input())
    else:
        print("Nieprawidłowa komenda!")




