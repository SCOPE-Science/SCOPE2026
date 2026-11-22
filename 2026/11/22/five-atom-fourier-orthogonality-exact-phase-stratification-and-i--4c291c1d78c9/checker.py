#!/usr/bin/env python3
"""Exact supplemental checks for a five-atom Fourier-orthogonality classification.

Finite torsion enumeration is deliberately not used as a proof for arbitrary
real frequency differences; the accompanying analytic argument handles them.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations


def P(u, a, b, c):
    return 4*a*u*u+2*b*u+c-2*a


def test_rational_resonances():
    count=0
    for q in range(2, 31):
        for p in range(-q+1, q//2+1):
            x=Q(p,q)
            if x>=Q(1,2) or x<=Q(-7,8):
                continue
            a=1/(8*(1-x)**2*(1+x))
            b=(1-2*x)/(4*(1-x)**2)
            c=(1+4*x**3-2*x)/(4*(1-x)**2*(1+x))
            if min(a,b,c)<=0:
                continue
            assert 2*a+2*b+c==1
            assert P(x,a,b,c)==0
            assert P(2*x*x-1,a,b,c)==0
            count+=1
    assert count>100
    return count


def test_special_cases():
    a,b,c=Q(1,8),Q(1,4),Q(1,4)
    assert P(Q(0),a,b,c)==P(Q(-1),a,b,c)==0
    a,b,c=Q(8,45),Q(10,45),Q(9,45)
    x=Q(1,4)
    assert P(x,a,b,c)==P(2*x*x-1,a,b,c)==0
    assert (4*x-1)*(8*x+7)==32*x*x+20*x-7
    a,b=Q(1,12),Q(1,4)
    c=a+b
    assert 2*a+2*b+c==1 and P(Q(-1,2),a,b,c)==0
    # Positive example with no Fourier zero: an entire one-character region.
    a,b,c=Q(1,20),Q(1,20),Q(4,5)
    assert 2*a+2*b+c==1 and c-2*a-b*b/(4*a)>0


def test_finite_torsion_cliques():
    checked=0
    for N in range(2,65):
        for u in range(1,N):
            for v in range(u+1,N):
                S={u%N,(-u)%N,v%N,(-v)%N}
                S.discard(0)
                nodes={0}|S
                for k in (3,4):
                    for clique in combinations(sorted(nodes),k):
                        if 0 not in clique:
                            continue
                        if not all((x-y)%N in S for x,y in permutations(clique,2)):
                            continue
                        checked+=1
                        if k==3:
                            assert any(t in S and 2*t%N in S for t in S)
                        else:
                            D={(x-y)%N for x in clique for y in clique}
                            is4=N%4==0 and D=={(i*N//4)%N for i in range(4)}
                            is5=N%5==0 and D=={(i*N//5)%N for i in range(5)}
                            assert is4 or is5,(N,u,v,clique,S)
    assert checked>100
    return checked

if __name__=='__main__':
    test_special_cases()
    print('exact rational resonance samples:',test_rational_resonances())
    print('torsion 3- and 4-clique instances:',test_finite_torsion_cliques())
    print('PASS (supplementary checks only)')
