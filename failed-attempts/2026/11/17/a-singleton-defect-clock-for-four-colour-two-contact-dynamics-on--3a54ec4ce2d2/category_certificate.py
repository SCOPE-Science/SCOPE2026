#!/usr/bin/env python3
"""Exhaustive three-symbol population-quotient certificate for a four-colour contact system."""
from itertools import product
from collections import Counter
from math import comb

# Category: 0=empty, 1=singleton, 2=at least two vertices.
def quotient_step(s):
    result=[]
    for i in range(4):
        a,b,c=s[(i-1)%4],s[i],s[(i+1)%4]
        if b==0: v=0
        elif b==1: v=0 if c==2 else 1
        elif c!=2: v=2
        else: v=a
        result.append(v)
    return tuple(result)

def polynomial():
    forms={k:Counter() for k in ('0','1','2','3','4')}
    patterns={k:[] for k in forms}
    for p in product(range(3),repeat=4):
        if p==(2,2,2,2): category='4'
        else:
            s=p; t=0
            while quotient_step(s)!=s:
                s=quotient_step(s);t+=1
                assert t<=3,('nonsettling pattern',p)
            category=str(t)
        a=p.count(2);b=p.count(1)
        forms[category][(a,b)]+=1
        patterns[category].append(p)
    expected={
        '0': {(0,0):1,(0,1):4,(0,2):6,(0,3):4,(0,4):1,(1,0):4,(1,1):8,(1,2):4,(2,0):2},
        '1': {(1,1):4,(1,2):8,(1,3):4,(2,0):4,(2,1):8,(2,2):2},
        '2': {(3,0):4,(2,1):4,(2,2):4},
        '3': {(3,1):4},
        '4': {(4,0):1}
    }
    for k in forms:
        assert dict(forms[k])==expected[k],(k,forms[k])
        print(k,'patterns',len(patterns[k]),'monomials',sorted(forms[k].items()))
    assert sum(map(len,patterns.values()))==81
    # First-entry 3 occurs precisely for a single singleton and three heavy colours.
    assert set(patterns['3'])==set(tuple([1 if i==j else 2 for i in range(4)]) for j in range(4))
    # Each quotient fixed point is a truly fixed labelled state (no positive transfers).
    for p in patterns['0']:
        assert all(not(p[i]>0 and p[(i+1)%4]==2) for i in range(4))
    # The only nonfixed return in the quotient is four heavy colours.
    print('certificate OK')

if __name__=='__main__':polynomial()
