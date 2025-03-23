from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similar("surname","name"))

if 'name'=='surname':
    print('a')