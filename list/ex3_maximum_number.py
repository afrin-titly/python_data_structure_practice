lists = [23,12,67,34,97,21]
lists.sort()
# savage solution
print(lists[len(lists)-1])

#typical solution
lists = [23,12,67,34,97,21]
max = lists[0]
for x in lists:
    if x > max:
        max = x

print(max)
