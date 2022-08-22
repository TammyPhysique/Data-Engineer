getal = input("Even getal?")
lijst_getallen = list(range(0, (getal+1)))

def tel_alle_getallen(x):
    totaal = 0
    for x in lijst_getallen:
        totaal = totaal + x
    return totaal
    print(totaal)
