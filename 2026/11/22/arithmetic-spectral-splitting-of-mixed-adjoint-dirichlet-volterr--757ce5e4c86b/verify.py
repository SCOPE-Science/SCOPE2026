"""Standalone finite arithmetic checks for a Dirichlet–Volterra spectral theorem.

Standard-library only. Finite tests diagnose formulas; the proof is analytic.
"""
from fractions import Fraction
from math import gcd, log, isclose, exp


def coefficient_from_two_actions(a, b, n):
    A, B = log(a), log(b)
    output = None
    total = 0.0
    if (b*n) % a == 0:
        output = b*n//a
        # V_b then V_a^*.
        total += (B / log(b*n)) * (A / log(b*n))
    if n % a == 0:
        target = b*(n//a)
        assert output is None or output == target
        output = target
        # V_a^* then V_b.
        total -= (A / log(n)) * (B / log(target))
    return output, total


def coefficient_from_split(a, b, n):
    d = gcd(a, b)
    ap = a//d
    if n % ap:
        return None, 0.0
    m = n//ap
    A, B = log(a), log(b)
    target = b*m//d
    if m % d:
        return target, A*B/log(b*ap*m)**2
    k = m//d
    u = log(k)
    F = 1/((u+A)*(u+B)) - 1/(u+A+B)**2
    return target, -A*B*F


def cubic_F(u, A, B):
    return 1/((u+A)*(u+B)) - 1/(u+A+B)**2


def rationalized_F(u, A, B):
    num = (u+A+B)**2-(u+A)*(u+B)
    den = (u+A)*(u+B)*(u+A+B)**2
    return num/den


assertions = 0
for a, b in [(2,3), (3,2), (4,6), (6,4), (2,2), (9,9), (12,18), (8,15), (6,35)]:
    old_outputs = set()
    for n in range(1, 501):
        x, v = coefficient_from_two_actions(a,b,n)
        y, w = coefficient_from_split(a,b,n)
        assert x == y
        assert isclose(v, w, rel_tol=2e-10, abs_tol=1e-14)
        if x is not None:
            assert x not in old_outputs  # distinct input columns have disjoint outputs
            old_outputs.add(x)
        assertions += 3
    A, B = log(a), log(b)
    prev = 1000.0
    for k in range(1, 100):
        u = log(k)
        z = A*B*cubic_F(u, A, B)
        assert 0 < z < prev
        prev = z
        assertions += 1

# Finite singular multiset: K maps distinct inputs to distinct outputs,
# so the list of nonzero column norms is precisely the singular list.
for a,b in [(2,3),(4,6),(2,2),(6,35)]:
    d=gcd(a,b); ap=a//d
    values=[]
    for n in range(1,800):
        _,v=coefficient_from_two_actions(a,b,n)
        if v: values.append(abs(v))
    split=[]
    for m in range(1,800//ap+1):
        n=ap*m
        if n>=800: break
        _,v=coefficient_from_split(a,b,n)
        split.append(abs(v))
    assert len(values)==len(split)
    for v,w in zip(sorted(values,reverse=True),sorted(split,reverse=True)):
        assert isclose(v,w,rel_tol=3e-10,abs_tol=2e-14)
        assertions+=1

# Exact rational identities for the two distinct terms of F.
for A in [Fraction(1),Fraction(2),Fraction(3,2)]:
 for B in [Fraction(1),Fraction(5,3),Fraction(7,2)]:
  for u in [Fraction(0),Fraction(1,3),Fraction(11),Fraction(500)]:
   assert cubic_F(u,A,B)==rationalized_F(u,A,B)
   assertions+=1

# Verify cubic leading and next coefficients on the rationalized expression.
for A,B in [(log(2),log(3)),(log(4),log(6)),(log(2),log(2))]:
    C=A*B*(A+B)
    D=-A*B*(2*A*A+5*A*B+2*B*B)
    for u in (200.0,500.0,1000.0):
        # rationalized form avoids subtraction cancellation
        f=A*B*rationalized_F(u,A,B)
        ratio=(f-C/u**3)*u**4/D
        assert abs(ratio-1.0)<0.07
        assertions+=1

print(f"PASS: {assertions} finite arithmetic/monotonicity/singular-list checks")
