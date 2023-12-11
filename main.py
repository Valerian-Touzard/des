import random

while True:
    x = int(input("1 pour lancer le dés, 0 pour quitter le programme: "))

    if x == 0:
        print('Bye, à la prochaine')
        break
    elif x == 1:
        print("le nombre "+str(random.randint(1,6)))
    else:
        print('je n\'ais pas compris')