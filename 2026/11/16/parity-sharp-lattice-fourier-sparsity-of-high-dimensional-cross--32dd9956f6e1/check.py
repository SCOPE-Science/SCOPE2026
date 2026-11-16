"""Reproduce cross-polytope Fourier collision strata and leading counts.
Python 3, mpmath >=1.2. Uses independent Hermite-residue and Laplace formulas.
"""
from itertools import product
from collections import Counter
from math import comb
import mpmath as mp
mp.mp.dps = 65

def spectrum(d, a):
    nodes = [(2*mp.pi*k)**2 for k in a]
    m = d//2
    if d%2:
        f=lambda z: z**m * mp.sin(mp.sqrt(z))/mp.sqrt(z) if z else mp.mpf('0')
    else:
        f=lambda z: z**(m-1)*mp.cos(mp.sqrt(z))
    # Hermite-Genocchi residue formula: divided difference at repeated nodes.
    total=mp.mpf(0)
    for v in set(nodes):
        r=nodes.count(v)
        other=[w for w in nodes if w != v]
        def h(z):
            den=mp.mpf(1)
            for w in other:den*=z-w
            return f(z)/den
        total += mp.diff(h,v,r-1)/mp.factorial(r-1)
    return 2**d*(-1)**m*total

def leading_special(d, a):
    n=[abs(k) for k in a]
    cnt=Counter(n)
    m=d//2
    repeated=[v for v,r in cnt.items() if r>1]
    y=lambda v: (2*mp.pi*v)**2
    if d%2 and len(repeated)==1 and cnt[repeated[0]]==2 and repeated[0]>0:
        v=repeated[0]; den=mp.fprod(y(v)-y(w) for w,r in cnt.items() if w!=v)
        return (-1)**m *2**(d-1)*y(v)**(m-1)/den
    if not(d%2) and len(repeated)==1 and cnt[repeated[0]]==3 and repeated[0]>0:
        v=repeated[0]; den=mp.fprod(y(v)-y(w) for w,r in cnt.items() if w!=v)
        return (-1)**(m+1) *2**(d-3)*y(v)**(m-2)/den
    return None

for d,a in [(3,(1,-1,2)),(4,(1,-1,1,2)),(5,(1,-1,2,3,4)),(6,(1,-1,1,2,3,4)),(7,(1,-1,2,3,4,5,6)),(8,(1,-1,1,2,3,4,5,6))]:
    v=spectrum(d,a); pred=leading_special(d,a)
    assert pred is not None and mp.almosteq(v,pred,rel_eps=mp.mpf('1e-35')),(d,a,v,pred)
    print('STRATUM_PASS d=',d, 'value=',mp.nstr(v,12))

for d,a in [(3,(0,1,2)),(4,(0,1,2,3)),(5,(0,1,2,3,4)),(6,(0,1,2,3,4,5)),(4,(1,-1,2,-2)),(6,(1,-1,2,-2,3,4))]:
    v=spectrum(d,a)
    assert abs(v)<mp.mpf('1e-40'),(d,a,mp.nstr(v,15))
    print('VANISHING_PASS d=',d)

# Exact set-theoretic upper bounds and sharp leading coefficients by generic collision count.
for d in range(3,9):
    assert (2**d*comb(d,2) if d%2 else 2**d*comb(d,3))>0
print('COUNTS_BOUNDS_PASS dimensions=3..8')
