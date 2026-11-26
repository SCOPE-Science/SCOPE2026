#!/usr/bin/env python3
"""Independent finite checks of ternary loopless cyclic digram spectra.

No external libraries. Exhaustively enumerates indexed symbols with cyclic
proper-adjacency condition, deduplicates necklaces by rotations, and compares
observed read-profile and singleton counts with exact formula coefficients.
"""
from collections import defaultdict
from itertools import product
from math import comb

ARCS=((0,1),(1,0),(1,2),(2,1),(2,0),(0,2))

def profile(w):
    n=len(w)
    return tuple(sum(w[i]==a and w[(i+1)%n]==b for i in range(n)) for a,b in ARCS)

def canonical(w):
    return min(w[j:]+w[:j] for j in range(len(w)))

def unique_parameters(p):
    ab,ba,bc,cb,ca,ac=p
    cur=ab-ba
    assert cur==bc-cb==ca-ac
    if cur==0:
        pairs=(ab,bc,ca)
        active=sorted(x for x in pairs if x)
        return len(active)==1 or (len(active)==2 and active[0]==1)
    if cur>0:
        pairs=(ba,cb,ac)
        t=cur
    else:
        pairs=(ab,bc,ca)
        t=-cur
    active=[x for x in pairs if x]
    return not active or (len(active)==1 and (t==1 or active[0]==1))

def profile_count(n):
    ans=0
    if n%2==0:
        s=n//2
        ans+=comb(s+2,2)
    for t in range(1,n//3+1):
        if (n-3*t)%2==0:
            ans+=2*comb((n-3*t)//2+2,2)
    return ans

def singleton_count(n):
    x=0
    if n%2==0 and n>=2:
        x+=3
    if n%2==0 and n>=4:
        x+=3*(1 if n==4 else 2)
    if n>=3 and n%3==0:
        x+=2
    if n>=5 and (n-3)%2==0:
        x+=6  # circulation one, a single active pair of arbitrary size
    if n>=5 and (n-2)%3==0:
        x+=6  # one reciprocal pair, any positive circulation
    if n==5:
        x-=6  # joint intersection was counted twice
    return x

def iter_words(n):
    def rec(prefix):
        if len(prefix)==n:
            if prefix[-1]!=prefix[0]:
                yield tuple(prefix)
            return
        for x in range(3):
            if x!=prefix[-1]:
                prefix.append(x)
                yield from rec(prefix)
                prefix.pop()
    for first in range(3):
        yield from rec([first])

def verify():
    words=0
    profs=0
    uniques=0
    for n in range(2,17):
        classes=defaultdict(set)
        for w in iter_words(n):
            words+=1
            classes[profile(w)].add(canonical(w))
        if len(classes)!=profile_count(n):
            raise AssertionError(('profile_count',n,len(classes),profile_count(n)))
        actual=sum(len(v)==1 for v in classes.values())
        if actual!=singleton_count(n):
            raise AssertionError(('singleton_count',n,actual,singleton_count(n)))
        for p, v in classes.items():
            if (len(v)==1)!=unique_parameters(p):
                raise AssertionError(('uniqueness',n,p,len(v),unique_parameters(p)))
        profs+=len(classes)
        uniques+=actual
    # Compare algebraic GF coefficients with direct balanced-flow enumeration.
    from fractions import Fraction
    for n in range(1,101):
        ct=0
        ut=0
        for s in range(n//2+1):
            if n==2*s:
                for x in range(s+1):
                    for y in range(s-x+1):
                        z=s-x-y
                        ct+=1
                        ut+=int(unique_parameters((x,x,y,y,z,z)))
        for t in range(1,n//3+1):
            if (n-3*t)%2: continue
            s=(n-3*t)//2
            for x in range(s+1):
                for y in range(s-x+1):
                    z=s-x-y
                    ct+=2
                    ut+=2*int(unique_parameters((x+t,x,y+t,y,z+t,z)))
        if ct!=profile_count(n) or ut!=singleton_count(n):
            raise AssertionError(('flow',n,ct,ut,profile_count(n),singleton_count(n)))
    print('VERIFY_OK cyclic_words_checked=%d profile_classes_checked=%d singleton_classes_checked=%d lengths=2..16 flow_lengths=1..100' %(words,profs,uniques))
    print('EXAMPLES', [(n,profile_count(n),singleton_count(n)) for n in range(2,17)])

if __name__=='__main__':verify()
