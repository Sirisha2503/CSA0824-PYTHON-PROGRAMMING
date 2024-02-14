import itertools
n=input("enter the number")
p=list(itertools.permutations(n))
print(*[''.join(p)for p in p])
