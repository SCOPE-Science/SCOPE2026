#!/usr/bin/env python3
# Replays finite sanity checks for the theorem using only the Python standard library.
# The infinite theorem is proved in RESULT.md; these computations do not replace that proof.

from itertools import product

def mm(A,B,p):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)

def neg(A,p): return tuple((-x)%p for x in A)
I=(1,0,0,1)

def canon(A,p):
    B=neg(A,p)
    return min(A,B)

def sl2(p):
    out=set()
    for a,b,c,d in product(range(p), repeat=4):
        if (a*d-b*c)%p==1:
            out.add(canon((a,b,c,d),p))
    return sorted(out)

def pmul(A,B,p):
    return canon(mm(A,B,p),p)

def involutions(G,p):
    e=canon(I,p)
    return [A for A in G if A!=e and pmul(A,A,p)==e]

def commute(A,B,p):
    return pmul(A,B,p)==pmul(B,A,p)

def stats(p):
    G=sl2(p)
    X=involutions(G,p)
    degs=[]
    edges=0
    for i,A in enumerate(X):
        d=0
        for j,B in enumerate(X):
            if i!=j and commute(A,B,p):
                d+=1
        degs.append(d)
    edges=sum(degs)//2
    chi=1 if p%4==1 else -1
    n_expected=p*(p+chi)//2
    k_expected=(p-chi)//2
    e_expected=p*(p*p-1)//8
    assert len(X)==n_expected, (p,len(X),n_expected)
    assert len(set(degs))==1 and degs[0]==k_expected, (p,set(degs),k_expected)
    assert edges==e_expected, (p,edges,e_expected)
    return len(G),len(X),degs[0],edges

# Prime-field instances, including the exceptional chordal q=5 case and
# several odd non-chordal cases. Prime-power q=9 is covered symbolically
# in the proof, not by this prime-field enumerator.
for p in (5,7,11,13):
    print("p=%d |G|=%d involutions=%d degree=%d edges=%d" % ((p,)+stats(p)))

# Explicit induced 6-cycle in the involution commuting graph of PSL_2(7).
C=[
 (2,3,3,5),
 (0,1,6,0),
 (2,4,4,5),
 (1,1,5,6),
 (1,3,4,6),
 (1,2,6,6),
]
for A in C:
    assert (A[0]*A[3]-A[1]*A[2])%7==1
    assert pmul(A,A,7)==canon(I,7)
for i in range(6):
    for j in range(i+1,6):
        adjacent=(j==i+1 or (i==0 and j==5))
        assert commute(C[i],C[j],7)==adjacent, (i,j,adjacent)

# The density contradiction used in the proof: for every odd integer q>5,
# with chi chosen by q mod 4, the involution graph has minimum degree at
# least 4 and therefore at least 2n edges, exceeding the chordal
# omega<=3 bound 2n-3. Checking a broad finite range catches arithmetic slips.
for q in range(7,1000,2):
    chi=1 if q%4==1 else -1
    n=q*(q+chi)//2
    k=(q-chi)//2
    e=n*k//2
    assert k>=4
    assert e>=2*n
    assert e>2*n-3

print("VERIFY_OK")
