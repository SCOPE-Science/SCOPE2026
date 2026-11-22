#!/usr/bin/env python3
"""Finite reproducibility tests for Beatty-induced nested forcing."""
import math

def check(alpha, N=250000):
    q = [0] + [1 + math.floor(alpha*n) for n in range(1,N+2)]
    f = [0]*(N+2)
    negatives=0
    invalid=[]
    for n in range(2,N+1):
        t=n-q[n-1]
        assert 1 <= t < n
        f[n]=q[n]-q[t]
        d=f[n]-f[n-1]
        assert d in (-1,0,1)
        m=n-1
        u=(alpha*m)%1
        v=(alpha*(1-alpha)*m)%1
        inferred = ((u < 1-2*alpha) and (((v+alpha*u)%1)>=1-alpha)) if alpha<.5 else False
        dnext = (q[n+1]-q[(n+1)-q[n]])-f[n]
        if (dnext==-1)!=inferred: invalid.append((n,dnext,u,v))
        if d==-1: negatives +=1
    assert not invalid, invalid[:3]
    return negatives, negatives/(N-1)

if __name__ == '__main__':
    for alpha in [1/math.pi, math.pi/10, math.sqrt(2)-1, .5, .6]:
        c,d=check(alpha)
        expected=alpha*(1-2*alpha) if alpha<.5 and alpha not in (math.sqrt(2)-1,) else 0
        print(f'alpha={alpha:.12f}  drops={c} empirical={d:.7f} generic_prediction={expected:.7f}')
        if alpha==math.sqrt(2)-1 or alpha>=.5: assert c==0
        if alpha in (1/math.pi, math.pi/10): assert abs(d-expected)<.0005
    print('PASS: indicator identity, no forbidden increments, resonance, generic frequencies')
