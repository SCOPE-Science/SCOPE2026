"""Numerical and symbolic consistency checks for a convex-geometric midpoint law."""
from fractions import Fraction
from itertools import combinations
import numpy as np


def theory(d, lengths):
    lengths=np.asarray(lengths, dtype=float)
    w=1/lengths; w=w/w.sum(); survival=1-float(w@w)
    return w, survival

def random_midpoints(lengths,n,seed):
    d=len(lengths); w,s=theory(d,lengths)
    rng=np.random.default_rng(seed)
    f1=rng.choice(d,n,p=w); f2=rng.choice(d,n,p=w)
    x=rng.random((n,d)); y=rng.random((n,d))
    x[np.arange(n),f1]=rng.integers(0,2,size=n)
    y[np.arange(n),f2]=rng.integers(0,2,size=n)
    z=(x+y)/2
    return z, f1!=f2

def continuous_density(z,w):
    d=len(w); t=4*np.minimum(z,1-z)
    f=np.zeros(z.shape[0]);
    for i,j in combinations(range(d),2):
        idx=[k for k in range(d) if k not in (i,j)]
        f+=2*w[i]*w[j]*np.prod(t[:,idx],axis=1)
    return f

def check(lengths,seed):
    d=len(lengths); w,s=theory(d,lengths)
    n=220000
    z,E=random_midpoints(lengths,n,seed)
    assert abs(E.mean()-s)<0.004,(d,E.mean(),s)
    for i,j in combinations(range(d),2):
        idx=[k for k in range(d) if k not in (i,j)]
        statistic=np.prod(4*np.minimum(z[E][:,idx],1-z[E][:,idx])-1,axis=1)
        experimental=statistic.mean()
        expected=2*w[i]*w[j]/s/3**(d-2)
        assert abs(experimental-expected)<0.011,(d,i,j,experimental,expected)
    if d>=3:
        c={(i,j):2*w[i]*w[j]/s for i,j in combinations(range(d),2)}
        def k(i,j):return c[tuple(sorted((i,j)))]
        v=[]
        for i in range(d):
            other=[j for j in range(d) if j!=i]
            j,k0=other[:2]
            v.append((k(i,j)*k(i,k0)/k(j,k0))**.5)
        v=np.array(v); v/=v.sum()
        assert np.allclose(v,w,atol=1e-12)
    # Independently integrate an unnormalized density over uniform cube points.
    rng=np.random.default_rng(seed+400)
    x=rng.random((230000,d))
    assert abs(continuous_density(x,w).mean()-s)<0.008
    print('dimension',d,'face_weights',np.round(w,6),'interior_mass',round(s,6),'moment_checks',d*(d-1)//2)

for lengths,seed in [([1,1],12),([1,4],43),([1,1,1],78),([1,2,3],99),([1,2,3,4],222),([1,4,7,10,13],333)]:
    check(lengths,seed)

# Exact cubical three-dimensional total-variation values via piecewise Irwin-Hall cubic density.
import sympy as sp
x=sp.symbols('x')
phi2=(-2*x*x+6*x-3)/2
phi3=(3-x)**2/2
conditional=sp.integrate((sp.Rational(2,3)*x-1)*phi2,(x,sp.Rational(3,2),2))+sp.integrate((sp.Rational(2,3)*x-1)*phi3,(x,2,3))
unconditional=sp.Rational(1,3)+sp.integrate((sp.Rational(4,9)*x-1)*phi3,(x,sp.Rational(9,4),3))
assert conditional==sp.Rational(13,96)
assert unconditional==sp.Rational(521,1536)
print('VERIFY_OK', 'simulated_shapes=6', 'monte_carlo_midpoints=1320000', 'conditional_tv_cube='+str(conditional),'unconditional_tv_cube='+str(unconditional))
