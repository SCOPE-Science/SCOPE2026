#!/usr/bin/env python3
"""Exact finite path-cover certificates and independent LP checks for progression copula capacity."""
from fractions import Fraction
from scipy.optimize import linprog

def capacity(k,p,q):
    assert k>=3 and 0<p<q
    m, rem=divmod(q,p)
    return Fraction(k*(m//k)*p + (k if m%k==k-1 else 0)*rem,q)

def construct(q,p,k):
    good=0
    maps=[list(range(q)) for _ in range(k)]
    for t in range(p):
        path=list(range(t,q,p))
        for j in range(0,len(path)//k*k,k):
            block=path[j:j+k]
            good+=k
            for h,v in enumerate(block):
                for label in range(k):
                    maps[label][v]=block[(h+label)%k]
    for m in maps: assert sorted(m)==list(range(q))
    for a in range(q):
        b=sorted(m[a] for m in maps)
        ev=len(set(b))==k and all(b[i+1]-b[i]==p for i in range(k-1))
        assert ev == (len(set(m[a] for m in maps))==k)
    return Fraction(good,q)

def lp(q,p,k):
    edges=[]
    for a in range(q):
        if a+(k-1)*p<q: edges.append([a+i*p for i in range(k)])
    if not edges:return Fraction(0)
    A=[[int(i in e) for e in edges] for i in range(q)]
    z=linprog([-1]*len(edges),A_ub=A,b_ub=[1]*q,bounds=(0,None),method='highs')
    assert z.success
    return z.fun*-k/q

def run():
    n=0
    for q in range(4,43):
        for p in range(1,q):
            for k in range(3,min(q,7)):
                expected=capacity(k,p,q)
                assert construct(q,p,k)==expected, (q,p,k)
                n+=1
                if q<=20:
                    observed=lp(q,p,k)
                    assert abs(observed-float(expected))<1e-8,(q,p,k,observed,expected)
                    n+=1
    print('PASS', n, 'exact finite certificates and independent linear-program tests')
    print('Examples:',[(str(Fraction(p,q)),str(capacity(3,p,q))) for p,q in [(1,3),(1,4),(1,5),(1,6),(2,7),(3,11)]])
if __name__=='__main__':run()
