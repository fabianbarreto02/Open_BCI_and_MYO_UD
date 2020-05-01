from time import clock

a = 0
while True:
    b = clock()
    if b - a > 2.6:
        print("Cada dos segundos.")
        a = b