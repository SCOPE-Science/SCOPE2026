#!/usr/bin/env python3
"""Independently enumerate maximum distance bisectors of Cartesian complete-graph products.
All enumeration is over vertices and unordered pairs, with distances computed directly.
"""
import itertools
from collections import Counter
from math import comb,prod

def theorem(qs):
    n=prod(qs)
    c=Counter(qs)
    Q=max(qs)
    b=c[2]
    if Q>=5: return (n*(Q-2)//Q, c[Q]*comb(Q,2))
    if Q==4: return (n//2,6*c[4]+2*comb(b,2))
    if Q==3:
        if b>=2:return (n//2,2*comb(b,2))
        return (n//3,3*c[3]+6*comb(c[3],2)+6*b*c[3])
    if b>=2:return (n//2,2*comb(b,2))
    return (0,1)

def check(qs):
    vertices=list(itertools.product(*(range(q) for q in qs)))
    dist=[[sum(x!=y for x,y in zip(a,b)) for b in vertices] for a in vertices]
    highest=-1; masks=set()
    for i in range(len(vertices)):
        for j in range(i+1,len(vertices)):
            mask=sum(1<<w for w in range(len(vertices)) if dist[i][w]==dist[j][w])
            card=mask.bit_count()
            if card>highest:highest=card;masks={mask}
            elif card==highest:masks.add(mask)
    obs=(highest,len(masks)); expected=theorem(qs)
    assert obs==expected, (qs,obs,expected)
    print('q=',tuple(qs),'order=',len(vertices),'max=',highest,'count=',len(masks),'OK')

if __name__=='__main__':
    for a in range(2,8):check((a,))
    for a in range(2,7):
        for b in range(a,7):check((a,b))
    for qs in [(2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,2,4),(2,3,4),
               (2,2,5),(2,3,5),(3,3,4),(2,2,2,3),(2,2,3,3),(2,3,3,3),
               (2,3,3,4),(2,2,2,4),(2,2,3,4),(2,2,3,5),
               (2,2,2,2,2),(2,2,2,2,3),(2,2,2,3,3),
               (3,3,3,3),(2,2,2,2,4),(2,2,2,2,5)]:
        check(qs)
    print('VERIFY_OK')
