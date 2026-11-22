"""Supplementary finite checks for two-site Fourier trace ratios.
Run: python3 check.py. Uses only the standard library and optional NumPy for matrices.
"""
import cmath
import math
import random
from itertools import permutations

TOL = 3e-10
checks = 0

def near(a, b, tol=TOL):
    global checks
    checks += 1
    assert abs(a-b) <= tol * (1+abs(b)), (a,b)

def c(m):
    return math.sqrt(2)/m / math.tan(math.pi/(2*m))

def d(m):
    return math.sqrt(2)/m * (1/math.tan(math.pi/(2*m)) if m%2==0 else 1/math.sin(math.pi/(2*m)))

def q(m,a,b):
    return sum(abs(a+b*cmath.exp(2j*math.pi*j/m)) for j in range(m))/(m*math.sqrt(abs(a)**2+abs(b)**2))

for m in range(2,121):
    near(q(m, 1, -1),c(m))
    near(q(m, 1, 1),d(m))
    if m>2:
        assert c(m)>c(m-1)
    if m>=5 and m%2:
        assert d(m)<d(m-2)
    for j in range(m):
        near(q(m,1,-cmath.exp(2j*math.pi*j/m)),c(m))

rng=random.Random(940317)
for m in range(2,36):
    for _ in range(100):
        a=cmath.rect(0.02+3*rng.random(), 2*math.pi*rng.random())
        b=cmath.rect(0.02+3*rng.random(), 2*math.pi*rng.random())
        assert q(m,a,b)+TOL>=c(m), (m,a,b)
        checks+=1
        a=0.02+3*rng.random()
        b=0.02+3*rng.random()
        assert q(m,a,b)+TOL>=d(m), (m,a,b)
        checks+=1

# Genuine noncommutative regular matrices on the permutation group S3.
try:
    import numpy as np
except ImportError:
    np=None
if np is not None:
    perms=list(permutations(range(3)))
    by={p:i for i,p in enumerate(perms)}
    def compose(p,q):
        return tuple(p[q[j]] for j in range(3))
    identity=(0,1,2)
    for g in perms:
        order=next(k for k in range(1,7) if (lambda s:s==identity)(
            (lambda powers: powers[-1])(
                [__import__('functools').reduce(compose,[g]*k, identity)])))
        n=len(perms)
        R=np.zeros((n,n),dtype=complex)
        for j,h in enumerate(perms):
            R[by[compose(g,h)],j]=1
        for a,b in [(1,1),(1,-1),(1,1j),(0.7+0.4j, 1.2-0.8j)]:
            actual=float(np.linalg.svd(a*np.eye(n)+b*R,compute_uv=False).sum())
            predicted=n/order*sum(abs(a+b*cmath.exp(2j*math.pi*j/order)) for j in range(order))
            near(actual,predicted)

# At fixed separation the regular representation consists of n/m cycles:
# a direct test independent of any irreducible representation enumeration.
for n in range(2,35):
    for shift in range(1,n):
        m=n//math.gcd(n,shift)
        for a,b in [(1,-1),(1,1),(.3+.8j,-1.9+.3j)]:
            actual=sum(abs(a+b*cmath.exp(2j*math.pi*k*shift/n)) for k in range(n))
            expected=n/m*sum(abs(a+b*cmath.exp(2j*math.pi*j/m)) for j in range(m))
            near(actual,expected)

print('VERIFY_OK checks=',checks)
