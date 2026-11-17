#!/usr/bin/env python3
"""Exact finite checks for the intrinsic ridge-angle spectrum of two-row full-match assignment polytopes.

Run: python checks/verify_angles.py
All calculations use exact integer/rational arithmetic and the known vertex representation.
"""
from fractions import Fraction
from itertools import combinations
from collections import Counter


def exact_rank(rows):
    if not rows:
        return 0
    a = [[Fraction(z) for z in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        inv = 1 / a[r][c]
        a[r][c:] = [z*inv for z in a[r][c:]]
        for i in range(r + 1, len(a)):
            if a[i][c]:
                q = a[i][c]
                a[i][c:] = [x-q*y for x,y in zip(a[i][c:], a[r][c:])]
        r += 1
        if r == len(a):
            break
    return r


def vertices(n):
    return [tuple((int(k == i) if k < n else int(k-n == j))
                  for k in range(2*n))
            for i in range(n) for j in range(n) if i != j]


def active(v, facet, n):
    t,i = facet
    return v[i] == 0 if t == 'A' else (
        v[n+i] == 0 if t == 'B' else v[i] + v[n+i] == 1)


def face_dimension(pts):
    if not pts:
        return -1
    b = pts[0]
    return exact_rank([tuple(x-y for x,y in zip(p,b)) for p in pts[1:]])


def outward(n,facet):
    t,i = facet
    u = [n*int(j == i)-1 for j in range(n)]
    if t == 'A': return [-x for x in u] + [0]*n
    if t == 'B': return [0]*n + [-x for x in u]
    return u + u


def checked_angle(n,f,g):
    (t,i),(s,j)=f,g
    if t in 'AB' and s == t: return 'acute' if i!=j else 'excluded'
    if t == 'A' and s == 'B': return 'right'
    if s == 'C' and t in 'AB': return 'obtuse' if i!=j else 'excluded'
    return 'excluded'


def verify(n):
    v = vertices(n)
    facets = [(t,i) for t in 'ABC' for i in range(n)]
    dim = face_dimension(v)
    assert dim == 2*n-2, (n,dim)
    for f in facets:
        d=face_dimension([p for p in v if active(p,f,n)])
        assert d==dim-1,(n,f,d)
    counts=Counter()
    for f,g in combinations(facets,2):
        d=face_dimension([p for p in v if active(p,f,n) and active(p,g,n)])
        pair_type=checked_angle(n,f,g)
        expected=(dim-2) if pair_type!='excluded' and (n>=4 or pair_type not in ('acute','right') or f[1]!=g[1]) else None
        # For n=3, same-row and same-index cross-row are additional exceptions.
        if n==3 and ((f[0]==g[0] and f[0] in 'AB') or (f[0]=='A' and g[0]=='B' and f[1]==g[1])):
            expected=None
        if pair_type=='excluded':expected=None
        if expected is not None:
            assert d==expected,(n,f,g,d,expected)
            counts[pair_type]+=1
            af=outward(n,f); ag=outward(n,g)
            dot=sum(a*b for a,b in zip(af,ag))
            nf=sum(a*a for a in af);ng=sum(b*b for b in ag)
            cos_sign=-1 if dot>0 else 1 if dot<0 else 0
            cos2=Fraction(dot*dot,nf*ng)
            target={'acute':(1,Fraction(1,(n-1)**2)),
                    'right':(0,Fraction(0)),
                    'obtuse':(-1,Fraction(1,2*(n-1)**2))}[pair_type]
            assert (cos_sign,cos2)==target,(n,f,g,cos_sign,cos2,target)
        else:
            assert d < dim-2,(n,f,g,d,dim)
    expected_counts=(Counter({'right':6,'obtuse':12}) if n==3 else
                     Counter({'acute':n*(n-1),'right':n*n,'obtuse':2*n*(n-1)}))
    assert counts==expected_counts,(n,counts,expected_counts)
    print(f'n={n} dimension={dim} vertices={len(v)} facets={len(facets)} '
          f'ridges={sum(counts.values())} acute={counts["acute"]} '
          f'right={counts["right"]} obtuse={counts["obtuse"]} PASS')


if __name__ == '__main__':
    for n in range(3,9):
        verify(n)
    print('TWO_ROW_FIXED_RANK_RIDGE_EXACT_PASS')
