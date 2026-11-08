#!/usr/bin/env python3
"""Direct finite checks for optimal global Roman functions on cycles."""
from itertools import product
from collections import Counter

def is_global(word):
    n=len(word)
    twos={i for i,x in enumerate(word) if x==2}
    for i,x in enumerate(word):
        if x:
            continue
        if not ({(i-1)%n,(i+1)%n}&twos):
            return False
        if not (twos-{(i-1)%n,(i+1)%n}):
            return False
    return True

def formula(n):
    if n==3: return 3,1,1
    if n==4: return 4,5,2
    if n==5: return 5,11,3
    if n%3==0: return 2*n//3,3,1
    if n%3==1: return (2*n+1)//3,n,1
    m=(n-2)//3
    return (2*n+2)//3,n*(m+3)//2,2+m//2

def dihedral_orbits(W):
    W=set(W)
    while W:
        w=W.pop(); n=len(w)
        W.difference_update({w[i:]+w[:i] for i in range(n)})
        rw=w[::-1]
        W.difference_update({rw[i:]+rw[:i] for i in range(n)})
        yield w

def bruteforce(n):
    wexpect,cexpect,oexpect=formula(n)
    # Weight-filtered brute force is independent of templates and of extremal proof.
    minimum=None; opts=[]
    for word in product((0,1,2),repeat=n):
        wt=sum(word)
        if wt>wexpect:continue
        if not is_global(word):continue
        if minimum is None or wt<minimum:minimum=wt;opts=[]
        if wt==minimum:opts.append(word)
    assert minimum==wexpect,(n,'weight',minimum,wexpect)
    assert len(opts)==cexpect,(n,'count',len(opts),cexpect)
    orbs=len(list(dihedral_orbits(opts)))
    assert orbs==oexpect,(n,'orbits',orbs,oexpect)
    return minimum,len(opts),orbs

def rotate(w,j):return w[j:]+w[:j]
def make_from_gaps(gaps):
    w=[]
    for d in gaps:
        if d==2:w.extend([2,0])
        elif d==3:w.extend([2,0,0])
        elif d==4:w.extend([2,0,1,0])
        elif d==5:w.extend([2,0,1,1,0])
        else:raise ValueError(d)
    return tuple(w)

def templates(n):
    if n<6:raise ValueError(n)
    m=n//3;r=n%3
    gaplists=[]
    if r==0:gaplists=[[3]*m]
    elif r==1:
        for a in range(m):
            g=[3]*m;g[a]=4;gaplists.append(g)
    else:
        for a in range(m+1):
            g=[3]*(m+1);g[a]=2;gaplists.append(g)
        for a in range(m):
            g=[3]*m;g[a]=5;gaplists.append(g)
        for a in range(m):
            for b in range(a+1,m):
                g=[3]*m;g[a]=g[b]=4;gaplists.append(g)
    templates=set()
    for gs in gaplists:
        w=make_from_gaps(gs)
        assert len(w)==n,(gs,n)
        for i in range(n):templates.add(rotate(w,i))
    return templates

if __name__=='__main__':
    for n in range(3,13):
        print('DIRECT_3ARY_BRUTE_OK',n,*bruteforce(n))
    for n in range(6,81):
        T=templates(n)
        assert len(T)==formula(n)[1],('template count',n,len(T),formula(n))
        assert all(is_global(w) and sum(w)==formula(n)[0] for w in T)
        assert len(list(dihedral_orbits(T)))==formula(n)[2]
    print('ALL_TEMPLATES_CONSTRUCTIVE_AND_ORBITS_OK n=6..80')
    print('VERIFY_OK')
