from datetime import date

today = date.today()
huidig_jaar = today.year
huidige_maand = today.month
huidige_dag = today.day

print('Wat is het jaar?')
jaar = int(input())
print ('Wat is het maandnummer?')
maand = int(input())
print('Wat is de dag?')
dag = int(input())

t1 = date(year = huidig_jaar, month = huidige_maand, day = huidige_dag)
t2 = date(year = jaar, month = maand, day = dag)
t3 = t1 - t2
print("t3 =", t3)
