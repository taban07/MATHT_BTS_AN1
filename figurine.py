from random import randint


def Verifielesfigurines(collection) :
    res = True
    for i in range(1, 10) :
        if collection[i] == 0 :
                res = False
    return res

def ajoute(collection) :
    figurines = randint(0, 9)
    collection[figurines] +=1

def test():
    collection = [0] * 10
    achats = 0
    while True :
        ajoute(collection)
        achats +=1
        if Verifielesfigurines(collection) :
            break
    return achats

print(test())