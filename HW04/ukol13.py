a=int(input("Zadej pocet radku ctverce:"))

for cislo_radku in range(a):
    print("X", end=" ")
    for cislo_sloupce in range(a-2):
        if cislo_radku == 0 or cislo_radku == a-1:
            print ("X", end=" ")
        else:
            print (" ", end=" ")
    
    print("X",sep=" ", end= "\n")
