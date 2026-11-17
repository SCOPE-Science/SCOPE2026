#!/usr/bin/env python3
"""Exact finite certificate for the consecutive-pentagonal symmetry classification.

The proof supplies the independent infinite cutoff n>=142. This script
exhausts the n=2..141 interval and checks two independent membership tests.
"""
from math import gcd
from heapq import heappop, heappush
from csv import writer
from pathlib import Path


def pent(n):
    return n*(3*n-1)//2


def in_two(t,a,b):
    return any((t-b*y)%a==0 for y in range(t//b+1))


def min_residue(t,a,b):
    # a and b are coprime; the least y>=0 satisfying by=t mod a.
    if a==1:
        return 0
    return (t * pow(b,-1,a))%a


def gluing_pairs(n):
    v=(pent(n),pent(n+1),pent(n+2))
    for i,j,k in [(0,1,2),(0,2,1),(1,2,0)]:
        d=gcd(v[i],v[j])
        if d>1:
            a,b=v[i]//d,v[j]//d
            q=min_residue(v[k],a,b)
            bound=v[k]//b
            independently=in_two(v[k],a,b)
            assert (q<=bound)==independently, (n,i,j,k,q,bound)
            if q<=bound:
                yield (i,j,k,d,(v[k]-q*b)//a,q)


def apéry(n):
    a,b,c=(pent(n+i) for i in range(3))
    inf=10**30
    D=[inf]*a
    D[0]=0
    h=[(0,0)]
    while h:
        val,r=heappop(h)
        if val!=D[r]:
            continue
        for z in (b,c):
            s=(r+z)%a
            if val+z<D[s]:
                D[s]=val+z
                heappush(h,(val+z,s))
    assert all(x<inf for x in D)
    return max(D)-a, sum((D[r]-r)//a for r in range(a))


def main():
    matches=[]
    rows=[]
    for n in range(2,142):
        a,b,c=(pent(n+i) for i in range(3))
        assert gcd(gcd(a,b),c)==1
        assert gcd(a,c)==gcd(35,6*n+5)
        assert gcd(a,b)==(2 if n%4==3 else 1)
        assert gcd(b,c)==(2 if n%4==2 else 1)
        d=gcd(a,c)
        if d>1:
            a0,c0=a//d,c//d
            y=min_residue(b,a0,c0)
            bound=b//c0
            rows.append((n,d,y,bound, int(y<=bound)))
            assert (y<=bound)==in_two(b,a0,c0)
        # Three minimal generators except n=2 and n=5.
        minimal=(n not in (2,5))
        if minimal:
            # Herzog's three-generator criterion: symmetry iff any gluing.
            fits=list(gluing_pairs(n))
            if fits:
                matches.append((n,fits))
        else:
            assert in_two(c,a,b)
    assert [n for n,fl in matches]==[3,40],matches
    assert [n for n,d,y,bd,yes in rows if yes]==[5,40]
    assert len(rows)==44
    # Independent gap-based confirmation of exceptional Frobenius/genus.
    for n,F,G in [(2,43,22),(3,133,67),(5,1699,850),(40,258529,129265)]:
        assert apéry(n)==(F,G),(n,apéry(n))
        assert 2*G==F+1
    assert apéry(4)==(287,145)
    assert 2*145 != 287+1
    out=Path(__file__).resolve().parent/'finite_residue_certificate.csv'
    with out.open('w',newline='',encoding='utf-8') as f:
        w=writer(f);w.writerow(('n','gcd(P_n,P_n+2)','minimal_y','max_y','representable'))
        w.writerows(rows)
    print('Finite complete interval: n=2..141 (140 indices).')
    print('Nontrivial (A,C)-gcd indices checked:',len(rows))
    print('All gluing-positive minimal triples:',matches)
    print('Two-generator exceptions: [2,5].')
    print('Full symmetric list: [2,3,5,40].')
    print('Exceptional F/genus values checked by independent Apéry Dijkstra.')
    print('Non-symmetric n=4 has odd Frobenius number 287 but genus 145.')
    print('Symbolic proof handles every n>=142; no finite search extrapolated.')

if __name__=='__main__':
    main()
