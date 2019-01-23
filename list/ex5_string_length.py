lists = ['abc', 'xyz', 'aba', '1221','fgf']
count = 0
for x in lists:
    if len(x)>2 and x[0]== x[len(x)-1]:
        count += 1

print(count)
