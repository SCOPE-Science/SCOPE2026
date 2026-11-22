#!/usr/bin/env python3
from itertools import combinations,product

def terms(n):
    longs=[(h,C) for h in range(n) for C in range(1,1<<n) if C>>h&1]
    return longs

def signature(n, L, M, kind):
    # L bit mask, M bit mask indexed by (h,C) in longs; word absorption test
    longs=terms(n)
    E=0; long_byC=[False]*(1<<n)
    for i,(h,C) in enumerate(longs):
        if M>>i&1: E|=1<<h
    sig=L
    for i,(h,C) in enumerate(longs):
        ok=False
        if E>>h&1:
            H=N=J=False
            for j,(g,D) in enumerate(longs):
                if M>>j&1 and D&C==D:
                    N=True;J=True
                    if g==h: H=True
            if L&C: J=True
            T=bool(L&C&E)
            if kind=='U': ok=H
            if kind=='alpha':ok=(H or bool(L>>h&1)) and N
            if kind=='beta':ok=N
            if kind=='eta':ok=H or bool(L>>h&1) # H includes letter h in subset C
            if kind=='delta':ok=N or T
            if kind=='gamma':ok=J
            if kind=='A':ok=True
        sig|=int(ok)<<(n+i)
    return sig

def brute(n):
    longs=terms(n); t=n+len(longs)
    S={z:set() for z in ('U','alpha','beta','eta','delta','gamma','A')}
    for poly in range(1,1<<t):
        L=poly & ((1<<n)-1); M=poly>>n
        for z in S: S[z].add(signature(n,L,M,z))
    return {z:len(s) for z,s in S.items()}

def antichains(n,h):
    subsets=[s for s in range(1<<n) if s>>h&1]
    ans=[]
    for r in range(1<<len(subsets)):
        choices=[s for j,s in enumerate(subsets) if r>>j&1]
        if all(not((a&b)==a or (a&b)==b) for a,b in combinations(choices,2)):
            ans.append(choices)
    return ans

def canonical(n):
    longs=terms(n)
    opts=[]
    for h in range(n):
        hs=[]
        for a in antichains(n,h):
            m=sum(1<<longs.index((h,C)) for C in a)
            for letter in (0,1): hs.append((letter<<h,m))
        opts.append(hs)
    S={z:set() for z in ('U','alpha','beta','eta','delta','gamma','A')}
    for combination in product(*opts):
        L=0;M=0
        for l,m in combination:L|=l;M|=m
        if L==0 and M==0:continue
        for z in S:S[z].add(signature(n,L,M,z))
    return {z:len(s) for z,s in S.items()}

if __name__=='__main__':
    for n in (1,2,3):
        b=brute(n)
        c=canonical(n)
        print(n,b,c)
        assert b==c
        assert b['U']==(2*{1:2,2:3,3:6}[n])**n-1
        assert b['A']==4**n-1
    print('VERIFY_OK')
