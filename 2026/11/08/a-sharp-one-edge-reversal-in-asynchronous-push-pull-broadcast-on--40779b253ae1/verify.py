"""Exact certificate for an asynchronous push-pull broadcast comparison.

Run: python3 rumor_edge_checker.py
Requires Python standard library only. All arithmetic is rational.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial


def H(n):
    return sum((Q(1, j) for j in range(1, n + 1)), Q(0))


def product(m):
    z = Q(1)
    for i in range(1, m - 1):
        z *= Q(2*i*(m+1), 2*i*(m+1)+3*m+2)
    return z


def explicit(m):
    assert isinstance(m, int) and m >= 2
    lam = Q(m+1, m)
    h = Q(m+2, 2*m)
    c = Q(3*m+2, 2*m)
    E_star = (1 + H(m-1))/lam
    E_tail_one = H(m-2)/lam + product(m)/c
    E_edge = Q(1)/(1+h) + h/(1+h)*E_tail_one + Q(1)/(1+h)*(Q(1)/(2*h) + H(m-2)/lam)
    return E_star, E_edge


def full_labeled(m, edge=False):
    n=m+1
    neigh=[set(range(1,n))]+[{0} for _ in range(m)]
    if edge:
        neigh[1].add(2)
        neigh[2].add(1)
    deg=[len(a) for a in neigh]
    @lru_cache(None)
    def e(mask):
        if mask==(1<<n)-1:
            return Q(0)
        rates={}
        for v in range(n):
            if mask & (1<<v): continue
            rates[v]=sum((Q(1,deg[u])+Q(1,deg[v]) for u in neigh[v] if mask&(1<<u)),Q(0))
        total=sum(rates.values(),Q(0))
        assert total>0
        return (1+sum((rate*e(mask|(1<<v)) for v,rate in rates.items() if rate),Q(0)))/total
    return e(1<<1)


def difference_polynomial(m):
    F=product(m)
    A=3*m**4-10*m**3-32*m*m-28*m-8
    B=m**4+4*m**3+3*m*m-4*m-4
    return Q(m*(A+2*F*B), (m-1)*(m+1)*(m+2)*(3*m+2)**2)


def run():
    expected={2:Q(-1,3),3:Q(-13599,91960),4:Q(-226,4165),5:Q(20155225,3059601384)}
    for m in range(2,15):
        x,y=explicit(m)
        assert y-x==difference_polynomial(m), (m,x,y)
        if m in expected: assert y-x==expected[m], (m,y-x,expected[m])
        assert (y<x if m<=4 else y>x)
        if m<=11:
            assert full_labeled(m,False)==x, ('star',m)
            assert full_labeled(m,True)==y, ('edge',m)
    # Exact bound needed in the all-size sign argument:
    # A(m) is increasing and positive from m=6 onward; B(m)>0 from m=2 onward.
    assert 3*6**4-10*6**3-32*6**2-28*6-8 == 400
    assert 12*6**3-30*6**2-64*6-28 > 0
    assert 36*6*6-60*6-64>0
    # Sanity-check asymptotic limit at large m with exact rational formula.
    for m in (100,200,400):
        d=difference_polynomial(m)
        assert Q(0)<d<Q(1,3)
    print('PASS: 13 exact product identities, 20 independently computed labeled-state expectations, four boundary fractions, signs, polynomial and asymptotic checks')
    for m in range(2,7):
        a,b=explicit(m)
        print(f'm={m}: star={a}; edge={b}; difference={b-a}')

if __name__=='__main__':
    run()
