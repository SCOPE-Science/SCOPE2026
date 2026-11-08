#!/usr/bin/env python3
"""Independent finite checks for cyclic run-profile rearrangement theorem."""
from itertools import combinations_with_replacement, permutations
from random import Random

def make_word(a,b):
    return ''.join('1'*u + '0'*v for u,v in zip(a,b))

def maxima(w):
    n=len(w); double=w*2
    vals=[0]*(n+1)
    for ell in range(1,n+1):
        counts=[double[j:j+ell].count('1') for j in range(n)]
        vals[ell]=max(counts)
    return vals

def sorted_prefix(a,b):
    w=make_word(sorted(a,reverse=True),sorted(b))
    return [w[:j].count('1') for j in range(len(w)+1)]

def check(a,b):
    p=sum(a)+sum(b); goal=sorted_prefix(a,b)
    assert goal == maxima(make_word(sorted(a,reverse=True),sorted(b))), (a,b,'PN')
    aps=set(permutations(a)); bps=set(permutations(b))
    for ap in aps:
        for bp in bps:
            w=make_word(ap,bp)
            f=maxima(w)
            assert all(v<=t for v,t in zip(f,goal)),(a,b,ap,bp,goal,f)
    return len(aps)*len(bps),p

def position_check(a,b):
    w=make_word(a,b); sortedw=make_word(sorted(a,reverse=True),sorted(b))
    P=len(w); ones=w.count('1')
    coords=[i for i in range(3*P) if (w*3)[i]=='1']
    goal_coords=[i for i in range(3*P) if (sortedw*3)[i]=='1']
    for t in range(1,ones+1):
        target=goal_coords[t-1]+1
        for i in range(ones):
            assert coords[i+t-1]-coords[i]+1>=target,(w,sortedw,i,t)

if __name__=='__main__':
    c=0; profiles=0; positions=0
    for k in range(1,4):
        for a in combinations_with_replacement(range(1,5),k):
            for b in combinations_with_replacement(range(1,5),k):
                n,_=check(a,b); c+=n; profiles+=1
                for aa in set(permutations(a)):
                    position_check(aa,b)
                    positions+=1
    r=Random(301128)
    for k in range(4,10):
        for trial in range(240):
            a=[r.randrange(1,11) for _ in range(k)]
            b=[r.randrange(1,11) for _ in range(k)]
            w=make_word(a,b); goal=sorted_prefix(a,b)
            assert all(x<=y for x,y in zip(maxima(w),goal))
            position_check(a,b)
            positions+=1
    print('PASS profiles',profiles,'all_permutation_pairs',c,'position_profiles',positions,'random_large_profiles',1440)
