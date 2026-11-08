"""Exact finite-word checks for the three-edge logarithmic averaging law."""
from fractions import Fraction as Q
from itertools import product
from math import comb, exp, sqrt, log

def P(v, i):
    # outgoing edge i and incoming edge i-1 are replaced by geometric mean
    w=list(v); j=(i-1)%3; z=(w[j]+w[i])/2; w[j]=z; w[i]=z
    return tuple(w)

def norm2(v): return sum(z*z for z in v)

start=(Q(1),Q(2),Q(-3))
assert sum(start)==0
checks=0
for i in range(3):
    v=P(start,i)
    assert sum(v)==0 and norm2(v)>0
    for j in range(3):
        u=P(v,j)
        assert norm2(u)==norm2(v)*(Q(1) if i==j else Q(1,4)); checks+=1
    for n in range(2,9):
        frequencies=[0]*n
        for path in product(range(3),repeat=n-1):
            indices=(i,)+path
            x=start
            for k in indices:x=P(x,k)
            switches=sum(indices[k]!=indices[k-1] for k in range(1,n))
            assert norm2(x)==norm2(v)*Q(1,4)**switches
            frequencies[switches]+=1
            checks+=1
        assert frequencies==[comb(n-1,k)*2**k for k in range(n)]
        checks+=n

# Check actual diagonal-similarity balancing on a directed 3-cycle.
from itertools import cycle
for initial in [(1.,3.,5.),(.1,4.,11.),(2.,.2,.5)]:
    e=[log(a) for a in initial]
    c=sum(e)/3
    y=tuple(ei-c for ei in e)
    current=list(initial)
    for idx in [0,1,2,1,0,2,1,2,0]:
        j=(idx-1)%3
        new=sqrt(current[j]*current[idx]); current[j]=current[idx]=new
        y=P(y,idx)
        assert max(abs(log(current[t])-c-y[t]) for t in range(3))<2e-12
        assert abs(current[0]*current[1]*current[2]-initial[0]*initial[1]*initial[2])<2e-10*max(1.,initial[0]*initial[1]*initial[2])
        checks+=2
print('PASS',checks,'exact-geometry and numerical-matrix checks')
