myname = 'Staverescu Iulian'
for letter in myname:
    print(letter)
mycards = ['ing','raifaisen','bcr','revolut']
mycards2 = [card for card in mycards if card[0]=='i']
print('My cards are {}'.format(mycards))
print('A card starting with {} are {}'.format('i',mycards2))

firstLetter = input('Enter first letter => ')
filtered_cards = [c for c in mycards if c[0] == firstLetter]
print('Filter on card using criteria starting with letter {} are {}'.format(firstLetter,filtered_cards))
print ('I have {} cards'.format(len(mycards)))
print (mycards.count('ing'))