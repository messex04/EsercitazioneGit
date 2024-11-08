print("inserisci quanti numeri vuoi per interrompere mettere 0")
w = 0 
s = 0 
while w==0:
    x= int(input("metti un numero\n"))
    if x!=0:
        s+=x
    else:
        w=1
print(f"questo è la tua somma{s}")

