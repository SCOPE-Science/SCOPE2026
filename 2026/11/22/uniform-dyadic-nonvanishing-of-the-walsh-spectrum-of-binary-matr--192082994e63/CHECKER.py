"""Independent rank-character and diagonal-completion checks, Python 3."""
from itertools import product
from math import comb

def rank(rows, n):
    a=list(rows); p=0
    for j in range(n):
        k=next((i for i in range(p,n) if (a[i]>>j)&1),None)
        if k is None: continue
        a[p],a[k]=a[k],a[p]
        for i in range(n):
            if i!=p and (a[i]>>j)&1:a[i]^=a[p]
        p+=1
    return p

def full_gl_character(n,r):
    f=(-1)**r*2**(n*(n-1)//2)
    for j in range(1,n-r+1):f*=2**j-1
    return f

def formula(n,b):
    assert len(b)==n
    numer=sum(full_gl_character(n,rank([b[i]^(((mask>>i)&1)<<i) for i in range(n)],n))
              for mask in range(1<<n))
    assert numer%(1<<n)==0
    return numer//(1<<n)

def rows_of(n,z):
    t=0; rows=[0]*n
    for i in range(n):
        for j in range(n):
            if i==j:continue
            if z>>t&1:rows[i]|=1<<j
            t+=1
    return rows

def dot_parity(a,b):return sum((x&y).bit_count() for x,y in zip(a,b))%2

for n in (2,3,4):
    vectors=[rows_of(n,z) for z in range(1<<(n*(n-1)))]
    good=[v for v in vectors if rank(v,n)==n]
    for b in vectors:
        direct=sum(1-2*dot_parity(a,b) for a in good)
        by_formula=formula(n,b)
        assert direct==by_formula,(n,b,direct,by_formula)
    print(f"n={n} direct/formula agree for {len(vectors)} characters PASS")

# Dimension five: exact formula with nontrivial deterministic diagonal completions.
n=5
for z in [0,1,7,19,255,9001,345678,1048575]:
    b=rows_of(n,z)
    v=formula(n,b)
    assert v%128==64,(z,v)
print('n=5 rank-formula tests and dyadic congruence PASS')
