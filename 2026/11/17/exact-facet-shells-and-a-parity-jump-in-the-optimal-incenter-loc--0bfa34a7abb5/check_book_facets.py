#!/usr/bin/env python3
"""Independent rational verification of the triangular-book facet spectrum.
Run: python3 check_book_facets.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        s = a[r][j]
        a[r] = [z / s for z in a[r]]
        for i in range(r + 1, len(a)):
            if a[i][j]:
                c = a[i][j]
                a[i] = [u - c*v for u,v in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def tight_connected(w):
    q=len(w)-2
    edges=[(0,1)] + [(i,j) for i in range(2,q+2) for j in (0,1)]
    tight=[(u,v) for u,v in edges if abs(w[u]-w[v])==1]
    seen={0}
    while True:
        new=seen | {v for u,v in tight if u in seen} | {u for u,v in tight if v in seen}
        if new==seen: break
        seen=new
    return len(seen)==q+2, len(tight)


def enumerate_facets(q):
    N=q+2
    facets=[]
    for d in (-1,0,1):
        leafvals = {-1:(-1,0), 0:(-1,0,1), 1:(0,1)}[d]
        for leaves in product(leafvals,repeat=q):
            w=(0,d)+leaves
            good,size=tight_connected(w)
            if not good: continue
            k=Fraction(N*sum(z*z for z in w)-sum(w)**2, N)
            facets.append((d, leaves, k, size, w))
    return facets


def test():
    total=0
    norm_tests=0
    ranks=0
    second_tests=0
    for q in range(1,11):
        N=q+2
        fac=enumerate_facets(q)
        assert len(fac)==3*(2**q),(q,len(fac))
        total+=len(fac)
        observed=Counter((f[2],f[3]) for f in fac)
        expected=Counter()
        for t in range(q+1):
            s=2*t-q
            expected[(Fraction(q*N-s*s,N),2*q)]+=comb(q,t)
        for k in range(1,q+2):
            expected[(Fraction(k*(N-k),N),q+1)]+=2*comb(q,k-1)
        assert observed==expected, (q,observed,expected)
        norm_tests+=len(fac)
        if q>=2:
            R=Fraction(q*N-(q%2)**2,N)
            vals=sorted({f[2] for f in fac},reverse=True)
            assert vals[0]==R,(q,vals[:2],R)
            delta=4*((q%2)+1)
            assert R-vals[1]==Fraction(delta,N),(q, R,vals[1])
            tangent=[f[4] for f in fac if f[2]==R]
            assert len(tangent)==(comb(q,q//2) if q%2==0 else 2*comb(q,(q-1)//2))
            # subtract mean implicitly, using rows of N*w - sum(w)*ones
            rows=[tuple(N*x-sum(w) for x in w) for w in tangent]
            tang_rank=rank(rows)
            assert (N-1-tang_rank)==(2 if q%2==0 else 1),(q,tang_rank)
            ranks+=1
            second=[f for f in fac if f[2]==vals[1]]
            if q==2: assert len(second)==6
            elif q==3: assert len(second)==14
            elif q%2==0: assert len(second)==2*comb(q,q//2-1) and all(f[3]==2*q for f in second)
            else: assert len(second)==2*comb(q,(q-3)//2) and all(f[3]==2*q for f in second)
            second_tests+=1
    # Check exact threshold inequalities in a wide integer range.
    for q in range(2,501):
        N=q+2
        R=Fraction(q*N-(q%2)**2,N)
        RA2=Fraction(q*N-(q%2+2)**2,N)
        RBmax=Fraction((N//2)*(N-N//2),N)
        assert RA2>=RBmax
        assert RA2==RBmax if q in (2,3) else RA2>RBmax
        assert R-RA2==Fraction(4*(q%2+1),N)
    print(f'TRIANGULAR_BOOK_FACET_SHELL_CHECKS_PASSED facets={total} norm_entries={norm_tests} incenter_ranks={ranks} second_shells={second_tests} integer_inequalities=499')

if __name__=='__main__':
    test()
