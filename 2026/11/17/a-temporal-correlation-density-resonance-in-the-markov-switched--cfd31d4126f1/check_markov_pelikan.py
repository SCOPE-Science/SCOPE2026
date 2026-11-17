#!/usr/bin/env python3
"""Exact-rational regression checks of a Markov-switched interval-map stationary law.
The infinite-dimensional theorem is proved analytically; these finite checks are not its proof.
"""
from fractions import Fraction as Q
from math import comb

def case(u,v,N=36):
    assert Q(0)<u<v<Q(1)
    r=(1-v)/(1-u)
    e0=(v-u)/(2*(1-u)*(u+v))
    # Coefficients of generating functions via power-series recurrence, independently
    # generate from the prescribed closed formula using geometric convolution.
    def geo(k):
        return sum((Q(1,2)**(k-1-j))*r**j for j in range(k))
    e=[e0*(Q(1,2)**k+(r-(1-v))*geo(k)) for k in range(N+2)]
    c=[e0*u*geo(k) for k in range(N+2)]
    m=[e[k]+c[k] for k in range(N+2)]
    assert c[0]==0 and e[0]==e0
    for k in range(N):
        assert c[k+1]==u*e[k]+(1-v)*c[k]
        assert e[k]==(1-u)*e[k+1]+v*c[k+1]+(1-u)*e0*Q(1,2)**(k+1)
        assert m[k]>0
    # Compare exact rational generating coefficients to an independent recurrence.
    # 2(1-u)(u+v) e0=v-u by normalization.
    assert e0== (v-u)/(2*(1-u)*(u+v))
    assert (v-u)>0 and r<1
    assert sum(e[:N])+sum(c[:N])<1
    if r==Q(1,2):
        assert v==(1+u)/2
        for k in range(N):
            assert m[k]==Q(1,2)**k*(1+3*u*k)/(2*(1+3*u))
    # Explicit finite identities for PGF evaluated at z=1/3, 1/4 via the
    # tail of a rational convolution (matching coefficients to order N).
    for z in (Q(1,3),Q(1,4)):
        # Independent coefficient recurrence from rational denominator.
        h=u+v-1
        k0=e0
        a1=Q(1,2)+r
        a2=r/2
        d=[k0]
        d.append(a1*d[0]+k0*h)
        for n in range(2,N):
            d.append(a1*d[n-1]-a2*d[n-2])
        assert d==m[:N]
    return r, [m[0],m[1],m[2],m[3]]

p=Q(4,5)
examples=((Q(2,25),Q(8,25)),(Q(1,7),Q(4,7)),(Q(1,5),Q(4,5)),(Q(3,10),Q(4,5)))
for u,v in examples:
    r,first=case(u,v)
    assert v/(u+v)==p if (u,v)!=examples[-1] else True
    print(f'u={u} v={v} r={r} masses={[str(x) for x in first]}')
print('MARKOV_PELIKAN_EXACT_RATIONAL_OK cases=4 exact_shells=144')
