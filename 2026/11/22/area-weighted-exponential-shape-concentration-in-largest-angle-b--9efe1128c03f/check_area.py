#!/usr/bin/env python3
"""Finite numerical corroboration of area-weighted LAB child geometry.
Only a finite test; the all-depth result is proved analytically in RESULT.md.
"""
import math

def D(a):
    a,b,c=a
    return math.log(max(b/a,0.5)/min(c/a,0.5))

def children(a):
    A,B,C=a
    p=math.sin(B)/(math.sin(B)+math.sin(C))
    left=tuple(sorted((A/2,B,C+A/2),reverse=True))
    right=tuple(sorted((A/2,C,B+A/2),reverse=True))
    return (p,left),(1-p,right)

def check():
    roots=[(math.pi*.6, math.pi*.3, math.pi*.1),
           (math.pi/2,math.pi/4,math.pi/4),
           (math.pi*.45,math.pi*.35,math.pi*.2)]
    for root in roots:
        c=min(root[2],root[0]/2)
        delta=math.sin(c)/(1+math.sin(c))
        rootD=D(root)
        level=[(root,1.)]
        for depth in range(1,12):
            next_level=[]
            for angles,w in level:
                ch=children(angles)
                for p,a in ch:
                    assert delta-1e-12 <= p <= 1-delta+1e-12
                    assert abs(sum(a)-math.pi)<1e-12
                    assert min(a)>=c-1e-12
                    assert D(a)<=D(angles)+1e-12
                    next_level.append((a,w*p))
            level=next_level
            assert abs(sum(w for _,w in level)-1)<1e-10
            assert max(D(a) for a,_ in level)<=rootD+1e-12
    print('PASS: area ratios, bounded conditional child probabilities, and projective monotonicity to depth 11')

if __name__=='__main__': check()
