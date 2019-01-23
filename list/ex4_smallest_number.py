lists = [23,12,67,34,97,21]
#savage solution
lists.sort()
print(lists[0])

#typical solution
lists = [23,12,67,34,97,21]
min = lists[0]
for x in lists:
    if x<min:
        min = x

print(min)
