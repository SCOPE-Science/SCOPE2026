#!/usr/bin/env python3
"""Exact checks for the fourth symplectic dual-polar distance spectrum."""
import math
from collections import Counter, deque


def qint(q, k):
    return (q**k - 1)//(q-1)


def spectral_rows(q):
    d=4
    rows=[]
    for j in range(5):
        theta=q*qint(q,4-j)-qint(q,j)
        p=[1,theta]
        for i in range(1,4):
            numerator=theta*p[i]-q**i*qint(q,5-i)*p[i-1]-(q-1)*qint(q,i)*p[i]
            assert numerator%qint(q,i+1)==0
            p.append(numerator//qint(q,i+1))
        rows.append(p)
    return rows


def polynomial_rows(q):
    return [
        [1,q*(q+1)*(q*q+1),q**3*(q*q+1)*(q*q+q+1),q**6*(q+1)*(q*q+1),q**10],
        [1,q**3+q*q+q-1,q*(q-1)*(q+1)*(q*q+q+1),q**3*(q**3-q*q-q-1),-q**6],
        [1,q*q-1,-2*q*q,-q*q*(q*q-1),q**4],
        [1,-q*q-1,0,q*q*(q*q+1),-q**4],
        [1,-(q+1)*(q*q+1),q*(q*q+1)*(q*q+q+1),-q**3*(q+1)*(q*q+1),q**6],
    ]


def rref(rows):
    basis=[int(r) for r in rows if r]
    for c in range(8):
        candidates=[i for i in range(len(basis)) if (basis[i]>>c)&1]
        if not candidates: continue
        ix=candidates[0]
        pivot=basis[ix]
        # previously reduced columns may occur in pivot; all maintained
        for i in range(len(basis)):
            if i!=ix and (basis[i]>>c)&1: basis[i]^=pivot
        # ensure independent row set; adjust processing ordering
    return tuple(sorted((x for x in basis if x),key=lambda x: (x & -x).bit_length()))


def canonical(rows):
    a=[int(r) for r in rows if r]
    pos=0
    for col in range(8):
        ix=next((i for i in range(pos,len(a)) if (a[i]>>col)&1),None)
        if ix is None:continue
        a[pos],a[ix]=a[ix],a[pos]
        for j in range(len(a)):
            if j!=pos and ((a[j]>>col)&1): a[j]^=a[pos]
        pos+=1
        if pos==len(a):break
    return tuple(a[:pos])


def parity(v):return v.bit_count()&1

def pair(x,y):
    a=x&15;b=x>>4;c=y&15;d=y>>4
    return parity((a&d)^(b&c))


def transvection(basis,w):
    return canonical([x^(w if pair(x,w) else 0) for x in basis])


def rank(vectors):return len(canonical(vectors))


def distance_origin(basis):return rank([x>>4 for x in basis])


def finite_geometry():
    origin=(1,2,4,8)
    seen={origin}; q=deque([origin]); layer_counts=Counter()
    representatives={}
    while q:
        L=q.popleft()
        assert len(L)==4
        for i in range(4):
            for j in range(i):assert pair(L[i],L[j])==0
        d=distance_origin(L)
        layer_counts[d]+=1
        representatives.setdefault(d,L)
        for w in range(1,256):
            T=transvection(L,w)
            if T not in seen:
                seen.add(T);q.append(T)
        assert len(seen)<=2295
    assert len(seen)==2295,(len(seen),layer_counts)
    expected=[row[0] for row in polynomial_rows(2)]
    # First spectral row consists of distance-shell valencies.
    assert [layer_counts[i] for i in range(5)]==polynomial_rows(2)[0]
    for i,L in representatives.items():
        neighbors={transvection(L,w) for w in range(1,256)}-{L}
        assert len(neighbors)==30,(i,len(neighbors))
        census=Counter(distance_origin(N) for N in neighbors)
        assert census[i-1] if i else True
        assert census.get(i-1,0)==(qint(2,i) if i else 0),(i,census)
        assert census.get(i,0)==(qint(2,i) if i else 0),(i,census)
        assert census.get(i+1,0)==(2**(i+1)*qint(2,4-i) if i<4 else 0),(i,census)
    return layer_counts


def main():
    for q in (2,3,4,5,7,8,9,11):
        rows=spectral_rows(q)
        assert rows==polynomial_rows(q),(q,rows)
        for row in rows[1:]:assert sum(row)==0
        assert sum(rows[0])==(q+1)*(q*q+1)*(q**3+1)*(q**4+1)
        for t in (.001,.05,.1,.2,.5,1,2,4):
            lambdas=[sum(row[i]*i**t for i in range(1,5)) for row in rows]
            assert lambdas[4]>max(lambdas[1:4]),(q,t,lambdas)
    counts=finite_geometry()
    print('SYMPLECTIC_DUAL_POLAR_FOURTH_METRIC_PASS', 'q_values=8', 'lagrangians=2295', 'shells='+str(dict(counts)))

if __name__=='__main__':main()
