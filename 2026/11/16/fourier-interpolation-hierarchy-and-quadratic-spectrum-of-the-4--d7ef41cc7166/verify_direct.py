"""Independent direct character-evaluation check. Run: python verify_direct.py
Requires NumPy and SymPy. Uses neither Krawtchouk polynomials nor row-pattern enumeration.
"""
from itertools import combinations
from math import comb
from collections import Counter
import numpy as np
from sympy import Matrix, Symbol, prod

T=[]
for a in range(1<<16):
    if any((a>>(4*i)&15).bit_count()!=2 for i in range(4)):continue
    if any(sum((a>>(4*i+j))&1 for i in range(4))!=2 for j in range(4)):continue
    T.append(a)
assert len(T)==90

# Exact elimination in the prime field gives rigorous lower bounds on rational rank.
def rank_mod(A,prime=65521):
    a=(A.astype(np.int64)%prime).tolist()
    m,n=len(a),len(a[0]); pivot=0
    for col in range(n):
        p=next((i for i in range(pivot,m) if a[i][col]%prime),None)
        if p is None:continue
        a[pivot],a[p]=a[p],a[pivot]
        inv=pow(int(a[pivot][col]),-1,prime)
        row=a[pivot]
        for j in range(col,n):row[j]=row[j]*inv%prime
        for i in range(pivot+1,m):
            v=a[i][col]
            if v:
                ai=a[i]
                for j in range(col,n):ai[j]=(ai[j]-v*row[j])%prime
        pivot+=1
        if pivot==m:break
    return pivot

masks=[]
x=Symbol('x')
expected_rank=(1,10,39,75,90)
for r in range(5):
    for I in combinations(range(16),r):
        masks.append(sum(1<<j for j in I))
    H=np.fromiter((1-2*((a&s).bit_count()&1) for a in T for s in masks),dtype=np.int64).reshape(90,len(masks))
    B=H @ H.T  # 64-bit exact: each entry is sum of at most 2517 values in {-1,1}.
    rank=rank_mod(B)
    assert rank==expected_rank[r], (r,rank)
    assert np.all(np.diag(B)==len(masks))
    if r==2:
        assert len(masks)==137
        expected_charpoly=x**51*(x-160)**9*(x-256)**9*(x-320)**4*(x-384)**12*(x-512)**4*(x-650)
        actual=Matrix(B.tolist()).charpoly(x).as_expr()
        assert actual.expand()==expected_charpoly.expand()
        D=np.array([[(a^b).bit_count() for b in T] for a in T],dtype=np.int64)
        assert np.array_equal(B,137-34*D+2*D**2)
    print('degree',r,'number_characters',len(masks),'rank_mod_65521',rank)
print('DIRECT_WALSH_CERTIFICATE_PASS')
