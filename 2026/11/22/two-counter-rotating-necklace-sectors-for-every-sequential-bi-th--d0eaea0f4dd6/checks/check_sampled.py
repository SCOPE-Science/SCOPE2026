"""Independently check the coloured wall description and word rotations."""
from itertools import permutations
from random import Random
from math import gcd

def update(bits, order):
    n=len(bits)
    z=bits[:]
    for i in order:
        s=z[(i-1)%n]+z[i]+z[(i+1)%n]
        z[i]=int(s>= (3 if z[i] else 1))
    return z

def check_order(order):
    n=len(order); pos=[0]*n
    for rank,i in enumerate(order):pos[i]=rank
    A=[i for i in range(n) if pos[i]<pos[(i+1)%n]]
    B=[i for i in range(n) if i not in A]
    a,b=len(A),len(B)
    # Test every initial state, and independently test permutation action
    # on each wall-exclusive subspace, including binary-word periods.
    for mask in range(1<<n):
        x=[(mask>>i)&1 for i in range(n)]
        walls=[x[i]^x[(i+1)%n] for i in range(n)]
        only_a=all(walls[i]==0 for i in B)
        only_b=all(walls[i]==0 for i in A)
        if only_a or only_b:
            y=update(x,order)
            if not all((y[i]^y[(i+1)%n])==0 for i in (B if only_a else A)):
                raise AssertionError(('component unstable',order,mask))
            for size,which in [(a,B),(b,A)]:
                if not all(walls[i]==0 for i in which):continue
                z=x[:]
                for k in range(size):z=update(z,order)
                if z!=x:raise AssertionError(('nonshift period',order,mask,size))
        else:
            z=x[:];count=sum(walls)
            for k in range(a*b):
                z=update(z,order)
                nw=sum(z[i]^z[(i+1)%n] for i in range(n))
                if nw<count:break
            else:raise AssertionError(('mixed survival',order,mask))

rng=Random(29630)
scans=0
for n in range(3,7):
    for p in permutations(range(n)):
        check_order(p);scans+=1
    print('n',n,'all scans PASS')
for n,k in [(7,50),(8,50),(9,45),(10,25)]:
    for t in range(k):
        p=list(range(n));rng.shuffle(p);check_order(p);scans+=1
    print('n',n,'sampled scans PASS',k)
print('PASS sampled_orbit_checks scans=',scans)
