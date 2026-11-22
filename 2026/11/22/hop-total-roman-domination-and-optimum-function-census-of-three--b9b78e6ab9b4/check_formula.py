"""Arithmetic and combinatorial cross-checks for the closed optimum counts."""
from itertools import combinations
from math import comb, factorial

def formula(n):
    r,s=divmod(n,3)
    if s==0:return factorial(n)//(6**r*factorial(r-1))
    if s==2:return factorial(n)//(2*6**r*factorial(r))
    assert r>=3
    return factorial(n)//(6**r*factorial(r))+factorial(n)//(16*6**(r-2)*factorial(r-2))
for n in range(8,19):
    assert formula(n)>0
    print(n,formula(n))
# independent named-triple subset enumerator in one-overlap boundary n=10
n=10
triples=[frozenset(c) for c in combinations(range(n),3)]
c={8:0,9:0}
for D in combinations(triples,3):
    u=len(D[0]|D[1]|D[2])
    if u in c:c[u]+=1
assert c=={8:37800,9:2800}
assert sum(c.values())==formula(10)
print('n=10 two types',c,'confirmed')
