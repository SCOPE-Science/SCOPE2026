"""Exact finite corroboration for atomless Boolean disjointness type matrices.
Run: python3 verify.py. Only Python standard library is used.
"""
from itertools import product
from math import comb

B = ((1,1,1),(1,1,0),(1,0,0))
C = ((0,0,1),(0,1,-1),(1,-1,0))

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
assert mm(B,C)==[[1,0,0],[0,1,0],[0,0,1]]
assert mm(C,B)==[[1,0,0],[0,1,0],[0,0,1]]

# Fraction-free Bareiss determinant: all calculations are exact integers.
def det(a):
    n=len(a)
    a=[list(row) for row in a]
    if n==0:return 1
    sign=1; previous=1
    for k in range(n-1):
        if a[k][k]==0:
            p=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k];sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=v*a[i][j]-a[i][k]*a[k][j]
                assert num%previous==0
                a[i][j]=num//previous
        for i in range(k+1,n):a[i][k]=0
        previous=v
    return sign*a[n-1][n-1]

def build(m):
    words=[w for w in product(range(3),repeat=m) if 1 in w]
    return words,[[int(all(B[u][v] for u,v in zip(s,t))) for t in words] for s in words]

def expected(m):return (-1)**(m*(1+2**(m-1)))

# Independent finite-universe feasibility: each named atom has exactly four subatoms.
# For one old atom the possible pieces are 0, proper nonempty, and full.
for state1 in range(3):
    for state2 in range(3):
        choices=lambda s:[z for z in range(16) if (z==0 if s==0 else z==15 if s==2 else 0<z<15)]
        feas=any((a&b)==0 for a in choices(state1) for b in choices(state2))
        assert feas==bool(B[state1][state2])
print('LOCAL_PATTERNS_OK')
for m in (1,2,3,4):
    words,M=build(m)
    d=det(M)
    assert d==expected(m),(m,d)
    assert len(M)==3**m-2**m
    assert sum(M[i][j] for i in range(len(M)) for j in range(len(M)))>0
    print('m',m,'size',len(M),'det',d,'unimodular',abs(d)==1)
print('ALL_EXACT_CHECKS_PASS')
