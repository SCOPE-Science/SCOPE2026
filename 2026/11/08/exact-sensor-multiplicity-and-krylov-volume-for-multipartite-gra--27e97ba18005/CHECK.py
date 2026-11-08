"""Exact reproducibility checks for multipartite quotient random-walk sampling.
Run with Python 3.9+; only the standard library is required.
"""
from fractions import Fraction
from itertools import product, combinations
from math import prod

checks = 0

def quotient(ns):
    n = sum(ns)
    k = len(ns)
    return [[Fraction(ns[j], n-ns[i]) if i != j else Fraction(0)
             for j in range(k)] for i in range(k)]

def multiply(A,B):
    return [[sum((A[i][z]*B[z][j] for z in range(len(B))),Fraction(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def identity(n):
    return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]

def observations(P, sensors, times):
    k=len(P); power=identity(k); rows=[]
    for _ in range(times):
        rows.extend([list(power[j]) for j in sensors])
        power=multiply(power,P)
    return rows

def rank(A):
    if not A:return 0
    X=[list(row) for row in A]
    rows=len(X); cols=len(X[0]); q=0
    for c in range(cols):
        p=next((i for i in range(q,rows) if X[i][c]),None)
        if p is None:continue
        X[q],X[p]=X[p],X[q]
        v=X[q][c]; X[q]=[z/v for z in X[q]]
        for i in range(q+1,rows):
            t=X[i][c]
            if t:
                X[i]=[a-t*b for a,b in zip(X[i],X[q])]
        q+=1
        if q==rows:break
    return q

def det(A):
    X=[list(row) for row in A]; n=len(X); res=Fraction(1)
    for j in range(n):
        p=next((i for i in range(j,n) if X[i][j]),None)
        if p is None:return Fraction(0)
        if p!=j:X[j],X[p]=X[p],X[j];res=-res
        v=X[j][j];res*=v
        for i in range(j+1,n):
            if X[i][j]:
                t=X[i][j]/v
                X[i]=[a-t*b for a,b in zip(X[i],X[j])]
    return res

def expected(ns, sensors):
    if not sensors:return False
    return all(sum(1 for i in sensors if ns[i]==size)>=sum(n==size for n in ns)-1
               for size in set(ns))

def formula(ns,j):
    k=len(ns); n=sum(ns); t=[Fraction(z,n-z) for z in ns]
    other=[i for i in range(k) if i!=j]
    v=Fraction(prod(ns[i] for i in other),(n-ns[j])**(k-1))
    for a,b in combinations(other,2):v*=abs(t[b]-t[a])
    return v

def optimal_count(ns):
    groups={x:sum(y==x for y in ns) for x in set(ns)}
    if all(m==1 for m in groups.values()):return sum(ns),1
    return (prod(r*(s**(r-1)) for s,r in groups.items() if r>1),
            sum(r-1 for r in groups.values()))

for k in range(2,6):
    for ns in product((1,2,3),repeat=k):
        P=quotient(ns)
        for i in range(k):
            assert sum(P[i]) == 1
            checks+=1
        for mask in range(1<<k):
            sensors=tuple(i for i in range(k) if mask & (1<<i))
            actual=rank(observations(P,sensors,k))==k
            assert actual==expected(ns,sensors),(ns,sensors,actual)
            checks+=1
        for j in range(k):
            actual=abs(det(observations(P,(j,),k)))
            assert actual==formula(ns,j),(ns,j,actual,formula(ns,j))
            assert (actual>0)==expected(ns,(j,))
            checks+=2
        ways,minimum=optimal_count(ns)
        sizes={x:sum(z==x for z in ns) for x in set(ns)}
        assert minimum==min(len(S) for r in range(1,k+1) for S in combinations(range(k),r) if expected(ns,S))
        ways2=0
        for r in range(1,k+1):
            for S in combinations(range(k),r):
                if len(S)==minimum and expected(ns,S):
                    ways2+=prod(ns[i] for i in S)
        assert ways==ways2,(ns,ways,ways2)
        checks+=2
# Independent larger examples with three distinct size groups and collisions.
for ns in ((1,2,3,4,5,6),(2,2,3,3,5,5),(2,2,2,3,4,5),(1,1,2,3,4,5),(3,3,3,3,3,3)):
    k=len(ns);P=quotient(ns)
    for mask in range(1<<k):
        sensors=tuple(i for i in range(k) if mask & (1<<i))
        assert (rank(observations(P,sensors,k))==k)==expected(ns,sensors)
        checks+=1
    for j in range(k):
        assert abs(det(observations(P,(j,),k)))==formula(ns,j)
        checks+=1
print('PASS',checks,'exact assertions')
