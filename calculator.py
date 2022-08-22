x = input("Welke operatie wil je uitvoern?(+, -, /, *, %)")

if x not in "+-*/%":
    print(x + " is geen geldige operatie, kies een van +, -, /, * of % ")
    exit()

try:
    invoer1 = input("eerste getal?")
    getal1 = float(invoer1)
except ValueError:
    print("Kan" + invoer1 + "niet omzetten naar een getal. Zorg dat je een '.'in plaats van ','gebruikt!")
    exit()
try:
    invoer2 = input("tweede getal?")
    getal2 = float(invoer2)
except ValueError:
    print("Kan" + invoer2 + "niet omzetten naar een getal. Zorg dat je een '.'in plaats van ','gebruikt!")
    exit()

getal0 = 0

if getal2 == getal0:
    print("Kan niet delen door 0")
elif x == "/":
    print("Resultaat: ", getal1 / getal2)
elif x == "%":
    print("Resultaat: ", getal1 % getal2)
if x == "+":
    print("Resultaat: ", getal1 + getal2)
elif x == "-":
    print("Resultaat: ", getal1 - getal2)
elif x == "*":
    print("Resultaat: ", getal1 * getal2)
