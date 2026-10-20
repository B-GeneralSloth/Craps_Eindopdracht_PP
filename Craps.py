# Craps

# Random en sleep
from random import randint
from time import sleep

numlist = [1,2,3,4,5,6]

gooi1 = numlist[randint(0,5)]
gooi2 = numlist[randint(0,5)]

uitwerpgooi = gooi1 + gooi2
print("uitwerpgooi: ", uitwerpgooi)

# uitwerpgooi verlies en winst
if uitwerpgooi == 7:
    print("je hebt gewonnen")
elif uitwerpgooi == 11:
    print("je hebt gewonnen")
elif uitwerpgooi == 2:
    print("je hebt verloren")
elif uitwerpgooi == 3:
    print("je hebt verloren")
elif uitwerpgooi == 12:
    print("je hebt verloren")

# uitwerpgooi anders
else:
    print("point: ", uitwerpgooi)
    print()
    point = uitwerpgooi
    besluitlist = [point,7]
    gooi = 0

    # opnieuw gooien
    while gooi not in besluitlist:
        # 2 seconden wachten
        sleep(2)

        # gooien en besluiten
        gooi1 = numlist[randint(0,5)]
        gooi2 = numlist[randint(0,5)]
        gooi = gooi1 + gooi2
        print("gooi: ", gooi)

        if gooi == 7:
            print("je hebt verloren")
        elif gooi == point:
            print("je hebt gewonnen")
        else:
            print("nog een keer gooien")
    
    
