def tel_kleine_letters(woord):
    aantal_kleine_letters = 0
    for karakter in woord:
        if 'a' <= karakter <= 'z':
            aantal_kleine_letters += 1
    return aantal_kleine_letters

def tel_alle_kleine_letters(woord1):
    totaal = 0
    for woord in woord1:
        aantal_letters = tel_kleine_letters(woord)
        totaal += aantal_letters
        print(f"{woord} {aantal_letters}")
    return totaal

string = ['Bit', 'Academy', 'Bit-Academy', 'bit', '-', 'AcAdEmY']
print("Totaal aantal letters", tel_alle_kleine_letters(string))
