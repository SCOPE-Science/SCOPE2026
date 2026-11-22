#!/usr/bin/env python3
"""Exact checks supporting a parity-sensitive vertex-convexification formula.

Uses only the Python standard library. Finite checks supplement the proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def facet_signatures(n):
    if n % 2:
        m = (n - 1)//2
        for missing in range(n):
            rest = [j for j in range(n) if j != missing]
            for plus in combinations(rest, m):
                pos = set(plus)
                yield tuple(0 if j == missing else (1 if j in pos else -1) for j in range(n))
    else:
        for plus in combinations(range(n), n//2):
            pos = set(plus)
            yield tuple(1 if j in pos else -1 for j in range(n))


def roots(n):
    out = []
    for i in range(n):
        b = [0]*n
        b[i] += 1
        b[(i+1) % n] -= 1
        out.append(tuple(b))
    return out


def rank(rows):
    if not rows:
        return 0
    a = [[F(x) for x in row] for row in rows]
    m, n = len(a), len(a[0])
    k = 0
    for j in range(n):
        idx = next((i for i in range(k,m) if a[i][j]), None)
        if idx is None:
            continue
        a[k], a[idx] = a[idx], a[k]
        pivot=a[k][j]
        a[k] = [v/pivot for v in a[k]]
        for i in range(m):
            if i != k:
                factor = a[i][j]
                if factor:
                    a[i] = [a[i][u]-factor*a[k][u] for u in range(n)]
        k += 1
        if k==m:
            break
    return k


def check_facets():
    total=0
    for n in range(3,11):
        r=roots(n)
        count=0
        for c in facet_signatures(n):
            assert sum(c)==0
            points=[]
            for j in range(n):
                if c[j]:
                    points.append(tuple(c[j]*v for v in r[j]))
            assert len(points)==n-1 if n%2 else len(points)==n
            assert rank([tuple(x-y for x,y in zip(p,points[0])) for p in points[1:]])==n-2
            if n%2 == 0:
                plus=[tuple(c[j]*v for v in r[j]) for j in range(n) if c[j]==1]
                minus=[tuple(c[j]*v for v in r[j]) for j in range(n) if c[j]==-1]
                assert tuple(map(sum,zip(*plus)))==tuple(map(sum,zip(*minus)))
                assert rank([tuple(x-y for x,y in zip(p,plus[0])) for p in plus[1:]])==n//2-1
                assert rank([tuple(x-y for x,y in zip(p,minus[0])) for p in minus[1:]])==n//2-1
            count+=1
        expected=(n*comb(n-1,(n-1)//2) if n%2 else comb(n,n//2))
        assert count==expected,(n,count,expected)
        total+=count
    return total


def centered_vertex(r,k):
    return tuple(F(int(i==k))-F(1,r) for i in range(r))


def add_scalar(x,y,t):
    return tuple(a+t*b for a,b in zip(x,y))


def gauge(x,y):
    return -len(x)*min(x)-len(y)*min(y)


def covered(x,y, lam):
    for k in range(len(x)):
        v=centered_vertex(len(x),k)
        xmove=add_scalar(x,v,-lam)
        if gauge(xmove,y)<=1-lam:
            return True
    for k in range(len(y)):
        v=centered_vertex(len(y),k)
        ymove=add_scalar(y,v,-lam)
        if gauge(x,ymove)<=1-lam:
            return True
    return False


def average_vertices(p,q,weights,indices):
    x=tuple(F(0) for _ in range(p))
    y=tuple(F(0) for _ in range(q))
    for k,w in zip(indices,weights):
        if k<p:
            x=add_scalar(x,centered_vertex(p,k),w)
        else:
            y=add_scalar(y,centered_vertex(q,k-p),w)
    return x,y


def check_free_sum():
    sample=0
    for p in range(2,6):
        for q in range(2,6):
            d=p+q-2
            lam=F(1,d)
            for k in range(p+q):
                for j in range(p+q):
                    for w in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                        x,y=average_vertices(p,q,(w,1-w),(k,j))
                        assert gauge(x,y)<=1
                        assert covered(x,y,lam),(p,q,k,j,w)
                        sample+=1
            a=F(p-1,d)
            b=F(q-1,d)
            x=tuple(-a/F(p) if i==0 else a/F(p*(p-1)) for i in range(p))
            y=tuple(-b/F(q) if i==0 else b/F(q*(q-1)) for i in range(q))
            assert gauge(x,y)==1
            assert covered(x,y,lam)
            assert not covered(x,y,lam+F(1,10000))
    return sample

if __name__=='__main__':
    facets=check_facets()
    samples=check_free_sum()
    print('CYCLE_VERTEX_GENERATION_PASS facets=%d free_sum_samples=%d n=3..10 p,q=2..5'%(facets,samples))
