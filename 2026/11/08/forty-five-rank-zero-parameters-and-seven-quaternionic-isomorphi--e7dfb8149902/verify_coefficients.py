#!/usr/bin/env python3
"""Exact Cartier coefficient extraction for genus-four quaternionic family.
Pure Python 3; no external packages.
"""
from itertools import permutations

def bimul(U,V,p):
    W={}
    for (i,j),u in U.items():
        for (k,l),v in V.items():
            key=(i+k,j+l)
            W[key]=(W.get(key,0)+u*v)%p
    return {k:v for k,v in W.items() if v}

def powf(p):
    f={(9,0):1,(7,1):1,(3,1):p-1,(1,0):p-1}
    r={(0,0):1}
    for _ in range((p-1)//2):r=bimul(r,f,p)
    M=[]
    for i in range(1,5):
        row=[]
        for j in range(1,5):
            d={t:v for (k,t),v in r.items() if k==p*i-j}
            row.append(d)
        M.append(row)
    return M

def polydet(M,p):
    def mul(A,B):
        R={}
        for i,a in A.items():
            for j,b in B.items():R[i+j]=(R.get(i+j,0)+a*b)%p
        return {k:v for k,v in R.items() if v}
    res={}
    for perm in permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        t={0:(-1 if inv%2 else 1)%p}
        for i in range(4):t=mul(t,M[i][perm[i]])
        for k,v in t.items():res[k]=(res.get(k,0)+v)%p
    return {k:v for k,v in res.items() if v}

for p in (7,11):
    M=powf(p)
    if p==7:
        # basis 1,x,x^2,x^3 times dx/y
        E=[[{}, {1:4}, {}, {0:6}],
           [{3:3,1:6}, {}, {2:6,0:3}, {}],
           [{}, {2:1,0:4}, {}, {3:4,1:1}],
           [{0:1}, {}, {1:3}, {}]]
        assert M==E, (p,M)
        # det = -3(a^2-4)^4 in characteristic seven.
        want={}
        from math import comb
        for k in range(5):want[2*k]=(-3*comb(4,k)*(-4)**(4-k))%7
        assert polydet(M,p)=={k:v for k,v in want.items() if v}
    else:
        E=[[{}, {2:1}, {}, {1:6}],
           [{4:8,2:6,0:1}, {}, {5:5,3:1,1:2}, {}],
           [{}, {5:6,3:10,1:9}, {}, {4:3,2:5,0:10}],
           [{1:5}, {}, {2:10}, {}]]
        assert M==E, (p,M)
        assert polydet(M,p)=={}, 'det 11 must vanish identically'
    print('COEFFICIENT_MATRIX_OK',p)
print('COEFFICIENT_VERIFICATION_OK')
