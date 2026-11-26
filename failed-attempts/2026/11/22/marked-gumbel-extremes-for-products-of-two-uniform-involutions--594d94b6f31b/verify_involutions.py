#!/usr/bin/env python3
"""Finite, exact checks for alternating components of two involutions.

Run with Python 3. This script independently enumerates involutions and tests
component-weight coefficient identities; it does not prove asymptotic limits.
"""
from collections import Counter
from math import factorial


def involutions(n):
    a = [-1]*n
    def rec():
        try:
            i = a.index(-1)
        except ValueError:
            yield tuple(a)
            return
        a[i] = i
        yield from rec()
        for j in range(i+1,n):
            if a[j] == -1:
                a[i], a[j] = j,i
                yield from rec()
                a[j] = -1
        a[i] = -1
    yield from rec()


def components(sigma, tau):
    n=len(sigma)
    seen=set()
    out=[]
    for v in range(n):
        if v in seen:
            continue
        stack=[v]; seen.add(v); comp=[]
        while stack:
            x=stack.pop();comp.append(x)
            for p in (sigma,tau):
                y=p[x]
                if y not in seen:
                    seen.add(y);stack.append(y)
        k=len(comp)
        degrees={x:int(sigma[x]!=x)+int(tau[x]!=x) for x in comp}
        if k==1 or any(d<=1 for d in degrees.values()):
            if k==1:
                kind='both'
            elif k%2==1:
                ends=[x for x in comp if degrees[x]==1]
                assert len(ends)==2
                assert sum(sigma[x]==x for x in ends)==1
                kind='opposite'
            else:
                ends=[x for x in comp if degrees[x]==1]
                assert len(ends)==2
                s_fixed=[sigma[x]==x for x in ends]
                assert s_fixed in ([True,True],[False,False])
                kind='sigma' if s_fixed[0] else 'tau'
            out.append(('P',k,kind))
        else:
            assert k%2==0 and all(d==2 for d in degrees.values())
            out.append(('C',k,'cycle'))
    return out


def main():
    invcounts=[len(list(involutions(n))) for n in range(9)]
    checked=0
    for n in range(1,8):
        perms=list(involutions(n))
        assert len(perms)==invcounts[n]
        tally=Counter()
        second=Counter()
        maximum=Counter()
        for s in perms:
            for t in perms:
                comps=components(s,t)
                paths=[(length,kind) for typ,length,kind in comps if typ=='P']
                cycles=[length for typ,length,kind in comps if typ=='C']
                for k,mark in paths:
                    tally[('P',k,'all')]+=1
                    tally[('P',k,mark)]+=1
                for k in cycles:
                    tally[('C',k,'all')]+=1
                counts=Counter(k for k,_ in paths)
                for k,ck in counts.items():
                    for ell,cl in counts.items():
                        second[(k,ell)]+=ck*(cl-(k==ell))
                # independent check: cycles of composition = path lengths + doubled half-cycle lengths
                prod=tuple(t[s[x]] for x in range(n))
                visited=set();pl=[]
                for i in range(n):
                    if i not in visited:
                        x=i;k=0
                        while x not in visited:
                            visited.add(x);k+=1;x=prod[x]
                        pl.append(k)
                expected=sorted([k for k,_ in paths]+[k//2 for k in cycles for _ in range(2)])
                assert sorted(pl)==expected
                checked+=1
                maximum[(max(pl),max([k for k,_ in paths],default=0))]+=1
        # first moments from exact coefficient extraction
        for k in range(1,n+1):
            num=factorial(n)//factorial(n-k)*invcounts[n-k]**2
            assert tally[('P',k,'all')]==num,(n,k,'path')
            checked+=1
            if k==1:
                assert tally[('P',k,'both')]==num
            elif k%2==1:
                assert tally[('P',k,'opposite')]==num
            else:
                assert 2*tally[('P',k,'sigma')]==num
                assert 2*tally[('P',k,'tau')]==num
            checked+=1
            if k%2==0:
                assert tally[('C',k,'all')]*k==num
                checked+=1
        for k in range(1,n+1):
            for ell in range(1,n+1-k):
                s=k+ell
                expected=factorial(n)//factorial(n-s)*invcounts[n-s]**2
                assert second[(k,ell)]==expected,(n,k,ell,'second factorial')
                checked+=1
        # For all pairs, max permutation cycle length >= max graph path length
        assert sum(v for (a,b),v in maximum.items() if a<b)==0
        checked+=1
    print('PASS:',checked,'counted exact enumeration/component checks; involution counts',invcounts)

if __name__=='__main__':
    main()
