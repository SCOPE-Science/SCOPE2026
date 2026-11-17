#!/usr/bin/env python3
"""Independent numerical diagnostic for a two-radius four-point convex-position limit."""
import math
import numpy as np

def convex_batch(x):
    # A generic quadruple is not in convex position iff one point lies in the triangle of the others.
    inside = np.zeros(len(x), dtype=bool)
    for j in range(4):
        y=np.delete(x,j,axis=1)
        v0=y[:,1]-y[:,0]
        v1=y[:,2]-y[:,0]
        v=x[:,j]-y[:,0]
        cross=lambda a,b: a[:,0]*b[:,1]-a[:,1]*b[:,0]
        den=cross(v0,v1)
        a=cross(v,v1)/den
        b=cross(v0,v)/den
        inside |= (a>0)&(b>0)&(a+b<1)
    return ~inside

def main():
    rng=np.random.default_rng(20261110)
    radius=0.00001
    target=np.array([1,0.75,0.5,0.5,1])
    observed=[]
    for k in range(5):
        n=200000
        radii=np.array([radius]*k+[1]*(4-k))
        angles=rng.uniform(0,2*math.pi,(n,4))
        xy=np.stack([radii*np.cos(angles),radii*np.sin(angles)],axis=-1)
        count=np.count_nonzero(convex_batch(xy))
        value=count/n
        observed.append(value)
        print('inner_count',k,'estimate',round(value,6),'limit',target[k])
        assert abs(value-target[k])<0.012
    p=1/math.sqrt(3)
    weights=np.array([math.comb(4,k)*p**k*(1-p)**(4-k) for k in range(5)])
    estimate=np.dot(weights,observed)
    theory=1-2/(3*math.sqrt(3))
    print('mixture',estimate,'limit',theory)
    assert abs(estimate-theory)<0.012
    print('TWO_SHELL_SYLVESTER_DIAGNOSTIC_OK')
if __name__=='__main__':
    main()
