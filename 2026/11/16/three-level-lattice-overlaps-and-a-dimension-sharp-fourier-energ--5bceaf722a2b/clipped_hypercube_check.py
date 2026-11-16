"""Reproduce lattice-translate multiplicity checks for clipped hypercubes.
Only finite corroboration; proofs are in RESULT.md.
"""
from itertools import product
from math import factorial
import numpy as np

def exact(d,a):
    h=max(0.0,a-0.5)
    mean=2**d*a**d/factorial(d)
    p2=2**d*h**d/factorial(d-1)
    p1=mean-2*p2
    p0=1-p1-p2
    energy=mean-mean**2+2*p2
    return np.array([p0,p1,p2]),energy

def mesh_check(d,a,N):
    vals=(np.arange(N)+.371)/N
    mesh=np.meshgrid(*([vals]*d),indexing='ij',sparse=True)
    removed=np.zeros((N,)*d,dtype=np.uint8)
    for bits in product((0,1),repeat=d):
        deficit=sum((mesh[i] if bits[i] else (1-mesh[i])) for i in range(d))
        removed+=(deficit<a).astype(np.uint8)
    assert removed.max()<=2
    actual=np.bincount(removed.ravel(),minlength=3)/removed.size
    expected, energy=exact(d,a)
    assert max(abs(actual-expected)) < 0.06, (d,a,actual,expected)
    assert abs(np.var(removed)-energy)<0.07,(d,a,np.var(removed),energy)
    return actual,expected

if __name__=='__main__':
    for d,N in [(2,160),(3,55),(4,28)]:
        for a in [0.2,0.43,0.58,0.78,0.94]:
            act, exp=mesh_check(d,a,N)
            print('d=%d a=%.2f mesh=%s exact=%s'%(d,a,np.round(act,4),np.round(exp,4)))
    assert abs(exact(2,0.8)[1]-(2*0.8**2-4*0.8**4+8*0.3**2))<1e-12
    print('CLIPPED_HYPERCUBE_THREE_LEVEL_PASS dimensions=2,3,4 cases=15')
