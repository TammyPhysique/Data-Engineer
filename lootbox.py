from itertools import count
from collections import Counter
from rewards import get_new_skin
import rewards

#loot_generation
lootbox=[]
for i in range(5):
    loot=str(get_new_skin())
    lootbox.append(loot)
#print(lootbox, "LOOTBOX")
#loot_processing
wordlist= lootbox
# Count each word
wordfreq = [wordlist.count(w) for w in wordlist] # a list comprehension
# Convert to set to remove repetitions
lootprice=dict(zip(wordlist, wordfreq))
#print(lootprice, "LOOTPRICE")
#loot_ordering
lootorder= ["COMMON","RARE", "EPIC","LEGENDARY"]
looty=(sorted(lootprice.items(), key=lambda i:lootorder.index(i[0])))
for a, b in looty:  # <-- this unpacks the tuple like a, b = (0, 1)
    print(b, "X",a)
