#!/usr/bin/env python3
"""Exact finite-dimensional checks for geometric-spiral intensity reconstruction."""
import sympy as s
I=s.I

def lifted_nodes(lam, d):
    conjugate=s.conjugate(lam)
    return [s.expand(lam**a * conjugate**b) for a in range(d+1) for b in range(d+1)]

def exact_distinct(lam,d):
    t=lifted_nodes(lam,d)
    return len({s.simplify(v) for v in t})==len(t)

# lambda/conjugate(lambda)=(3+4i)/5, which cannot be a root of unity
# in Q(i), whose sole roots of unity are 1,-1,i,-i.
lam=(2+I)/5
assert s.simplify(lam/s.conjugate(lam) - (3+4*I)/5)==0
assert all(s.simplify(lam/s.conjugate(lam)-v)!=0 for v in (1,-1,I,-I))
for d in range(5):
    assert exact_distinct(lam,d)

# All four expected numerator/denominator resonance classes.
for q, lamr in [(1,s.Rational(1,2)),(2,I/2),(4,(1+I)/4)]:
    for d in range(q):
        assert exact_distinct(lamr,d),(q,d)
    assert not exact_distinct(lamr,q),(q,'first collision')
    for n in range(1,20):
        z=s.expand(lamr**n)
        assert s.simplify(s.Abs(1+I*z**q)**2-s.Abs(1-I*z**q)**2)==0

# Exact inversion of a full 9-by-9 lifted Vandermonde matrix for a quadratic.
d=2
cs=[1+2*I, 2-I, -1+I]
t=lifted_nodes(lam,d)
N=len(t)
V=s.Matrix([[t_j**(n+1) for t_j in t] for n in range(N)])
assert V.det()!=0
h=s.Matrix([s.expand(cs[a]*s.conjugate(cs[b])) for a in range(d+1) for b in range(d+1)])
y=V*h
assert all(s.simplify(x)==0 for x in (V.inv()*y-h))
for n in range(1,N+1):
    z=lam**n
    p=sum(cs[k]*z**k for k in range(d+1))
    assert s.simplify(y[n-1] - p*s.conjugate(p))==0
print('GEOMETRIC_SPIRAL_PHASE_VERIFY_PASS distinct=12 collision=3 resonance=57 exact_vandermonde=9')
