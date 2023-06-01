# write a program to remove duplicates from list

def DuplicateImposter(lst):
    for ele in lst:
        if lst.count(ele) > 1:
            lst.remove(ele)
    print(lst)

lst = [34,56,43,23,34,65,43,78,23,90]
DuplicateImposter(lst)

# Another way
lst = set(lst)
print(list(lst))