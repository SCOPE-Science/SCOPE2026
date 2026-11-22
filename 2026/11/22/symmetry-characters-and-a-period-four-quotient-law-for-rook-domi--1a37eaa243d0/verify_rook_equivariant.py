#!/usr/bin/env python3
"""Independent finite Lefschetz and character checks for rook dominance complexes.
Standard library only. The general theorem is proved mathematically, not by these tests.
"""
from itertools import permutations
from collections import Counter

def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def make_permutation(m,n,row=None,col=None,transpose=False):
    row=tuple(range(m)) if row is None else tuple(row)
    col=tuple(range(n)) if col is None else tuple(col)
    if transpose:
        assert m==n
        return tuple(col[j]*n+row[i] for i in range(n) for j in range(n))
    return tuple(row[i]*n+col[j] for i in range(m) for j in range(n))

def cycles(perm):
    seen=set(); out=[]
    for i in range(len(perm)):
        if i in seen: continue
        C=[]; v=i
        while v not in seen:
            seen.add(v); C.append(v); v=perm[v]
        out.append(C)
    return out

def is_face(mask,m,n):
    # Complement contains a rook in every row OR in every column
    rows=all((mask & (((1<<n)-1) << (i*n))) != (((1<<n)-1) << (i*n)) for i in range(m))
    cols=all(any(not(mask & (1<<(i*n+j))) for i in range(m)) for j in range(n))
    return rows or cols

def orbit_lefschetz(m,n,perm):
    C=cycles(perm); v=0
    for sel in range(1<<len(C)):
        mask=0
        for j,c in enumerate(C):
            if sel>>j &1:
                for a in c: mask|=1<<a
        if is_face(mask,m,n): v+=(-1)**(sel.bit_count())
    return -v

def direct_lefschetz(m,n,perm):
    v=-1
    for mask in range(1,(1<<(m*n))):
        if not is_face(mask,m,n):continue
        elements=[i for i in range(m*n) if mask>>i&1]
        image=[perm[i] for i in elements]
        if set(image)!=set(elements):continue
        order={j:k for k,j in enumerate(elements)}
        relative=[order[j] for j in image]
        v+=(-1)**(len(elements)-1)*parity(relative)
    return v

def theoretical(m,n,row,col,flip):
    a,b=parity(row),parity(col)
    d_cross=(m-1)*(n-1)
    chi_cross=a**(n+1)*b**(m+1)
    if flip:
        assert m==n
        flip_chi=(-1)**(n*(n-1)//2 + (n-2)**2)
        return (-1)**d_cross*chi_cross*flip_chi
    return ((-1)**(m*n-m-1))*a**(n+1)*b**m + ((-1)**(m*n-n-1))*a**n*b**(m+1) + ((-1)**d_cross)*chi_cross

def run():
    cases=[(3,3),(3,4),(4,4)]
    for m,n in cases:
        row_candidates=[tuple(range(m)),tuple([1,0]+list(range(2,m))),tuple(list(range(1,m))+[0])]
        col_candidates=[tuple(range(n)),tuple([1,0]+list(range(2,n))),tuple(list(range(1,n))+[0])]
        count=0
        for row in row_candidates:
            for col in col_candidates:
                for flip in ([False,True] if m==n else [False]):
                    P=make_permutation(m,n,row,col,flip)
                    pred=theoretical(m,n,row,col,flip)
                    orb=orbit_lefschetz(m,n,P)
                    direct=direct_lefschetz(m,n,P)
                    assert pred==orb==direct,(m,n,row,col,flip,pred,orb,direct)
                    count+=1
        fcount=sum(is_face(mask,m,n) for mask in range(1<<(m*n)))-1
        print('BOARD',m,n,'FACES',fcount,'ACTIONS',count,'LEFSCHETZ_PASS')
    # Full-automorphism averages: reduced quotient Euler characteristics.
    for m,n in [(3,3),(3,4),(4,4)]:
        acc=0; count=0
        for row in permutations(range(m)):
            for col in permutations(range(n)):
                for flip in ([False,True] if m==n else [False]):
                    perm=make_permutation(m,n,row,col,flip)
                    val=orbit_lefschetz(m,n,perm)
                    assert val==theoretical(m,n,row,col,flip)
                    acc+=val; count+=1
        assert acc%count==0
        expected=1 if m==n==3 else (-1 if (m,n)==(3,4) else 0)
        assert acc//count==expected,(m,n,acc,count,expected)
        print('FULL_GROUP',m,n,'ORDER',count,'QUOTIENT_REDUCED_EULER',expected,'PASS')
    print('ROOK_EQUIVARIANT_CERTIFICATE_PASS')
if __name__=='__main__':run()
