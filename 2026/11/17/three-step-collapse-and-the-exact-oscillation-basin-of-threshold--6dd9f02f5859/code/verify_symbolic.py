"""Finite quotient and combinatorial verification of a 3-state threshold-two CCA.
For capped pair counts, pair types map deterministically. We also track all six
initial pair types individually to establish equality in the uncapped system.
"""
from itertools import product
from math import comb
P=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
W=(1,2,2,1,2,1)

def tagged_step(h,original_counts,tags):
    """Original capped multiplicities are immutable; the tagged types move."""
    following=(h+1)%3
    seen=sum(original_counts[i]*((a==following)+(b==following))
             for i,(a,b) in enumerate(tags))
    H=following if seen>=2 else h
    new_tags=[]
    for a,b in tags:
        u=(a+1)%3 if h==(a+1)%3 and b==(a+1)%3 else a
        v=(b+1)%3 if h==(b+1)%3 and a==(b+1)%3 else b
        new_tags.append(tuple(sorted((u,v))))
    return H,original_counts,tuple(new_tags)

def capped_identity():
    for h in range(3):
        for cnt in product(range(3),repeat=6):
            state=(h,tuple(cnt),P)
            for _ in range(3): state=tagged_step(*state)
            after3=state
            for _ in range(3): state=tagged_step(*state)
            # Tags of absent types can still change after time 3: equality only
            # needs to hold for types with positive initial multiplicity.
            assert state[0]==after3[0] and all(
                state[2][i]==after3[2][i] for i,c in enumerate(cnt) if c), (h,cnt,after3,state)
    print('PASS: universal F^6=F^3 on 2187 capped-count classes with tagged pairs')


def compositions(k,parts):
    if parts==1:yield (k,);return
    for j in range(k+1):
        for tail in compositions(k-j,parts-1):yield (j,)+tail

def weighted(t):
    rem=sum(t);weight=1
    for n,w in zip(t,W):
        weight*=comb(rem,n)*w**n;rem-=n
    return weight

def good(t):
    A,B,C,D,E,F=t
    return B+2*D+E>=2 and E+2*F>=2 and A+C>=1 and B+D>=1

def bad(k):
    if k==1:return 9
    return 3*6**k+2*k*6**(k-1)+2*k*4**(k-1)-(3+2*k)*3**k-2*k

def basin():
    for k in range(1,28):
        b=sum(weighted(t) for t in compositions(k,6) if not good(t))
        assert b==bad(k),(k,b,bad(k))
    print('PASS: direct six-type weighted enumeration k=1..27 agrees with closed formula')

if __name__=='__main__':
    capped_identity()
    basin()
