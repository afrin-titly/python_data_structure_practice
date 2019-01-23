dictionary = {1: 123, 2: 32, 3:56, 4:3}
#descending
print("Descending")
s = [(k, dictionary[k]) for k in sorted(dictionary, key=dictionary.get, reverse=True)]
for k, v in s:
    k, v
    print(k,v)
print("---------------")
#ascending
print("Ascending")
s = [(k, dictionary[k]) for k in sorted(dictionary, key=dictionary.get, reverse=False)]
for k, v in s:
    k, v
    print(k,v)
