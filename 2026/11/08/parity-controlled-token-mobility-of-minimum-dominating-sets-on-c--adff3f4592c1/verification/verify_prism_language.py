#!/usr/bin/env python3
"""Structural-word checker, independent of brute-force subset enumeration."""
from collections import Counter

def pattern(n,first,c):
    m=(n+1)//2
    other={'A':'B','B':'A'}
    w=['C']*n
    w[first]=c
    y=c if n%4==1 else other[c]
    w[(first+1)%n]=y
    for t in range(m-2):
        w[(first+3+2*t)%n]=other[y] if t%2==0 else y
    return tuple(w)

def minwords(n):
    if n==3:
        return {tuple('D' if a==b==i else 'A' if a==i else 'B' if b==i else 'C' for i in range(n)) for a in range(n) for b in range(n)}
    if n%4==0:
        R=set()
        for p in range(2):
            for q in range(2):
                w=['C']*n
                for t in range(n//2):w[(p+2*t)%n]='A' if (t+q)%2==0 else 'B'
                R.add(tuple(w))
        return R
    return {pattern(n,i,c) for i in range(n) for c in 'AB'}

def valid(w):
    n=len(w)
    for i,x in enumerate(w):
        if x=='C' and not (('A' in (w[(i-1)%n],w[(i+1)%n]) or 'D' in (w[(i-1)%n],w[(i+1)%n])) and ('B' in (w[(i-1)%n],w[(i+1)%n]) or 'D' in (w[(i-1)%n],w[(i+1)%n]))):return False
    return True

def bits(w):
    n=len(w)
    return frozenset((i,k) for i,x in enumerate(w) for k in range(2) if (x in ('A','D') if k==0 else x in ('B','D')))

def analyze(n):
    W=minwords(n)
    assert len(W)==(9 if n==3 else 4 if n%4==0 else 2*n)
    assert all(valid(w) for w in W)
    B={w:bits(w) for w in W}
    TJ={w:set() for w in W}; TS={w:set() for w in W}
    for a in W:
        for b in W:
            if a==b:continue
            gone=B[a]-B[b]; added=B[b]-B[a]
            if len(gone)==len(added)==1:
                TJ[a].add(b)
                u=next(iter(gone));v=next(iter(added))
                if ((u[0]==v[0] and u[1]!=v[1]) or (u[1]==v[1] and (u[0]-v[0])%n in (1,n-1))):TS[a].add(b)
    def components(A):
        seen=set();sizes=[]
        for z in A:
            if z in seen:continue
            Q=[z];seen.add(z)
            for h in Q:
                for k in A[h]:
                    if k not in seen:seen.add(k);Q.append(k)
            sizes.append(len(Q))
        return sorted(sizes),Counter(map(len,A.values()))
    cTS,dTS=components(TS);cTJ,dTJ=components(TJ)
    if n==3:expected=[9];deg=4
    elif n%4==0:expected=[1]*4;deg=0
    else:expected=[2*n];deg=2
    assert cTJ==expected and set(dTJ)=={deg}
    if n%4==1:cTS2=[1]*(2*n); dTS2=0
    else:cTS2=expected;dTS2=deg
    assert cTS==cTS2 and set(dTS)=={dTS2}
    return len(W),sum(map(len,TJ.values()))//2,sum(map(len,TS.values()))//2

for n in range(3,130):
    if n%4==2:continue
    a,b,c=analyze(n)
    if n<=15 or n in (31,65,129):print('PASS n={} minimum={} jump_edges={} slide_edges={}'.format(n,a,b,c))
print('PASS: independent word construction and every allowed token replacement through n=129')
