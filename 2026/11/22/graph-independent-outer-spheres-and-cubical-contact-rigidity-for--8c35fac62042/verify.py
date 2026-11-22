"""Reproducible finite tests for contact geometry of regular-rim discotopes.

The mathematical proof is analytic; this checker tests its explicit formulas.
Only the Python standard library is needed.
"""
from fractions import Fraction
from itertools import product
from math import sqrt, isclose
import random


def graph_cycle(n):
    return [(i, (i + 1) % n) for i in range(n)]


def graph_disjoint_cycles(lengths):
    edges = []
    base = 0
    for length in lengths:
        edges += [(base+i, base+(i+1) % length) for i in range(length)]
        base += length
    return base, edges


def graph_circulant(n, d):
    assert 1 <= d < n and (n*d) % 2 == 0
    edges = set()
    for k in range(1, d//2 + 1):
        for i in range(n):
            edges.add(tuple(sorted((i, (i+k)%n))))
    if d % 2:
        assert n % 2 == 0
        for i in range(n//2):
            edges.add((i, i+n//2))
    return sorted(edges)


def checked_graph(n, edges):
    deg=[0]*n
    for i,j in edges:
        assert 0<=i<j<n
        deg[i]+=1; deg[j]+=1
    assert len(set(deg))==1
    return deg[0]


def supporting(edges,n,u):
    return sum(sqrt(u[0]**2+u[i+1]**2) for i in range(n)) + sum(sqrt(u[i+1]**2+u[j+1]**2) for i,j in edges)


def exposed(edges,n,u):
    v=[0.0]*(n+1)
    for i in range(n):
        h=sqrt(u[0]**2+u[i+1]**2)
        v[0]+=u[0]/h; v[i+1]+=u[i+1]/h
    for i,j in edges:
        h=sqrt(u[i+1]**2+u[j+1]**2)
        v[i+1]+=u[i+1]/h; v[j+1]+=u[j+1]/h
    return v


def test(n, edges, seed):
    d=checked_graph(n,edges)
    assert 1<=d<=n-2
    r2=Fraction(n*n,1) * (1 + Fraction(d*d,2*(n-1)))
    b=Fraction(d*d,(n-1)*(d*d+2*(n-1)))
    a=1-n*b
    assert a>0 and b>0 and a+n*b==1
    hub2=Fraction(n*n,1)*(1-Fraction(d*d,2*(n-1)**2))
    rim2=Fraction(n*n*d*d,2*(n-1)**2)
    assert hub2+n*rim2==r2
    rng=random.Random(seed)
    random_checks=0
    for _ in range(250):
        u=[rng.gauss(0,1) for _ in range(n+1)]
        v=sqrt(sum(t*t for t in u));u=[t/v for t in u]
        assert supporting(edges,n,u)<=sqrt(float(r2))+1e-10
        random_checks+=1
    exact_contacts=0
    for signs in product([-1,1],repeat=n+1):
        u=[signs[0]*sqrt(float(a))]+[signs[i+1]*sqrt(float(b)) for i in range(n)]
        norm=sqrt(sum(t*t for t in u))
        assert abs(norm-1)<1e-12
        h=supporting(edges,n,u)
        assert abs(h-sqrt(float(r2)))<1e-9
        x=exposed(edges,n,u)
        pred=[signs[0]*sqrt(float(hub2))]+[signs[i+1]*sqrt(float(rim2)) for i in range(n)]
        assert max(abs(c-z) for c,z in zip(x,pred))<1e-9
        assert abs(sum(z*z for z in pred)-float(r2))<1e-9
        assert max(abs(z-sqrt(float(r2))*t) for z,t in zip(x,u))<1e-9
        exact_contacts+=1
    return random_checks,exact_contacts


def main():
    cases=[]
    for n in range(4,11):
        for d in range(1,n-1):
            if n*d%2 == 0:
                cases.append((n,graph_circulant(n,d)))
    # Same n,d, different edge arrangements (including disconnected rim graphs):
    for lengths in ([3,3],[6],[4,4],[3,5],[3,3,3],[5,5]):
        n,e=graph_disjoint_cycles(lengths)
        cases.append((n, sorted(tuple(sorted(edge)) for edge in e)))
    checks=contacts=0
    for ix,(n,e) in enumerate(cases):
        a,b=test(n,e,27277+ix)
        checks+=a;contacts+=b
    print('REGULAR_CONE_DISCOTOPE_PASS', 'graph_cases='+str(len(cases)),
          'random_support_checks='+str(checks), 'explicit_contacts='+str(contacts))

if __name__=='__main__':
    main()
