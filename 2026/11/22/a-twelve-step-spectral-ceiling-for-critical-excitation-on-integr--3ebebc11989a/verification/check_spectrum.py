#!/usr/bin/env python3
"""Exact strongly regular graph eigenvalue verification from (v,k,lambda,mu)."""
from math import isqrt

def spectrum(v,k,la,mu):
    # For any strongly regular graph, A^2=(k-mu)I+(la-mu)A+mu J.
    disc=(la-mu)**2+4*(k-mu)
    s=isqrt(disc)
    assert s*s==disc
    assert (la-mu+s)%2==0 and (la-mu-s)%2==0
    a,b=((la-mu+s)//2,(la-mu-s)//2)
    # m_a + m_b=v-1; k+a*m_a+b*m_b=0.
    assert (-k-b*(v-1))%(a-b)==0
    ma=(-k-b*(v-1))//(a-b)
    mb=v-1-ma
    assert ma>=0 and mb>=0
    assert k*k==(k-mu)+(la-mu)*k+mu*v
    assert ma*a*a+mb*b*b+k*k==v*k
    return {k:1,a:ma,b:mb}

for name,params in [('Gewirtz',(56,10,0,2)),('Higman-Sims',(100,22,0,6))]:
    spec=spectrum(*params)
    r=params[1]//2
    assert not set(spec).intersection({-r,0,r})
    print(name,'SRG parameters',params,'spectrum',dict(sorted(spec.items())), 'critical threshold',r, 'spectral obstruction verified')
