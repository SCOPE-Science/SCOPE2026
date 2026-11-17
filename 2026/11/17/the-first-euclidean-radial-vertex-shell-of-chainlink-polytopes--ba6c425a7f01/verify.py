#!/usr/bin/env python3
"""Exact independent vertex-intersection check for chainlink radial gaps.

Python 3 standard library only. The analytic proof applies to every permitted
real parameter vector; this finite check is not a substitute for that proof.
"""
from fractions import Fraction as F
from itertools import combinations, product


def solve(rows, n):
    a = [[F(t) for t in vec] + [F(rhs)] for vec, rhs in rows]
    for col in range(n):
        p = next((r for r in range(col, n) if a[r][col]), None)
        if p is None:
            return None
        a[col], a[p] = a[p], a[col]
        k = a[col][col]
        a[col] = [q/k for q in a[col]]
        for r in range(n):
            if r != col:
                k = a[r][col]
                if k:
                    a[r] = [x-k*y for x,y in zip(a[r], a[col])]
    return tuple(a[r][-1] for r in range(n))


def constraints(a, ell):
    n = len(a)
    out = []
    for i in range(n):
        v = [0]*n; v[i] = -1; out.append((tuple(v), 0))
        v = [0]*n; v[i] = 1; out.append((tuple(v), a[i]))
        v = [0]*n; v[i] = 1; v[(i+1)%n] = -1
        out.append((tuple(v), a[i]-ell))
    return out


def vertices(a, ell):
    n = len(a); ff=constraints(a,ell); out=set()
    for chosen in combinations(ff,n):
        x=solve(chosen,n)
        if x is not None and all(sum(y*z for y,z in zip(v,x))<=rhs for v,rhs in ff):
            out.add(x)
    return out


def second_shell_prediction(a, ell):
    n=len(a); mn=min(a); pts=set()
    for j in range(n):
        if a[j]!=mn:
            continue
        for r in range(n):
            v=[0]*n
            for k in range(1,r+1):
                v[(j-k)%n]=a[(j-k)%n]
            for z in {ell,a[j]-ell}:
                if mn>2*ell and z==ell and r==0:
                    continue
                if mn>2*ell and z==a[j]-ell and r==n-1:
                    continue
                v[j]=z; pts.add(tuple(map(F,v)))
    return pts


def test(a, ell):
    vv=vertices(a,ell)
    assert tuple(map(F,[0]*len(a))) in vv
    assert tuple(map(F,a)) in vv
    R2=sum(F(aa*aa,4) for aa in a)
    bydelta={v:sum(v[i]*(a[i]-v[i]) for i in range(len(a))) for v in vv}
    positive=[d for d in bydelta.values() if d>0]
    assert positive
    delta=min(positive)
    exp=ell*(min(a)-ell)
    assert delta==exp, (a,ell,delta,exp)
    predicted=second_shell_prediction(a,ell)
    actual={v for v,d in bydelta.items() if d==delta}
    assert actual==predicted, (a,ell,actual,predicted)
    m=sum(x==min(a) for x in a)
    assert len(actual)==(m*len(a) if min(a)==2*ell else 2*m*(len(a)-1))
    assert all(sum((v[i]-F(a[i],2))**2 for i in range(len(a)))==R2-delta for v in actual)
    assert all(d>=0 for d in bydelta.values())


def main():
    profiles=0
    for ell, sample in [(1,[2,3,4]),(2,[4,5,6])]:
        for n in (2,3,4):
            for a in product(sample,repeat=n):
                test(a,ell); profiles+=1
    for a,ell in [((2,3,2,4,3),1),((4,6,5,4,8),2),((3,3,3,4,5),1)]:
        test(a,ell); profiles+=1
    print('CHAINLINK_EXACT_INTERSECTION_PASS profiles='+str(profiles))


if __name__=='__main__':
    main()
