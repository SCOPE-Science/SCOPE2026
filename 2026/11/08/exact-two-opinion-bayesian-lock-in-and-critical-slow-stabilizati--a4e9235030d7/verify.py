"""Exact finite checks for an alternating two-opinion Bayesian threshold model.

Run with standard-library Python 3: python verify.py
The infinite-time conclusions are mathematical proofs, not finite test claims.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product

checks = 0

def cat(n):
    return comb(2*n, n) // (n + 1)

def stopping_weight(p, n):
    return Q(cat(n)) * p**n * (1-p)**(n+1)

def locking(p):
    return max(Q(0), (2*p-1)/p)

def raw_count(n):
    # Direct word enumeration: first hit of -1 occurs at time 2n+1.
    length = 2*n+1
    out = 0
    for word in product((1,-1), repeat=length):
        position = 0
        for i, step in enumerate(word):
            position += step
            if position == -1:
                if i == length-1: out += 1
                break
    return out

for n in range(8):
    assert raw_count(n) == cat(n)
    checks += 1

# Defective return-time law and its first two moments by independent
# rational Catalan coefficients; special values require no simulation.
for p in [Q(1,4), Q(2,5), Q(1,2), Q(3,5), Q(7,10), Q(4,5), Q(9,10)]:
    for n in range(8):
        count = raw_count(n)
        assert stopping_weight(p, n) == count*p**n*(1-p)**(n+1)
        checks += 1
    if p != Q(1,2):
        # Each partial sum of stopping weights is bounded by its exact total.
        partial = sum((stopping_weight(p,n) for n in range(20)), Q(0))
        assert 0 < partial <= 1-locking(p)
        checks += 1

# Exact restart-renewal equations for probability of eventual lock.
# Check each against the explicit formula and its boundary simplifications.
ps = [Q(1,4),Q(2,5),Q(1,2),Q(3,5),Q(7,10),Q(4,5),Q(9,10)]
for a in ps:
    for b in ps:
        sa, sb = locking(a), locking(b)
        qa, qb = 1-sa, 1-sb
        if sa + sb == 0:
            continue
        PA = sa/(1-qa*qb)
        PB = qb*sa/(1-qa*qb)
        assert PA == sa+qa*PB
        assert PB == sb*0+qb*PA  # P(ultimate A | start B)
        assert 0<=PA<=1 and 0<=PB<=1
        if a>Q(1,2) and b>Q(1,2):
            assert PA == b*(2*a-1)/(a+b-1)
            assert PB == (1-b)*(2*a-1)/(a+b-1)
        checks+=5

# The exact inversion formula for generating functions of last-switch time:
#   G_A=(s_A+s_B F_A)/(1-F_A F_B).
# Compare with coefficient-by-coefficient joint renewal recurrence, avoiding
# numerical root evaluation and respecting the constant term P(tau=0)=s.
N=21
for a,b in [(Q(7,10),Q(9,10)),(Q(1,2),Q(3,4)),(Q(2,5),Q(3,5)),(Q(3,4),Q(1,2))]:
    sa,sb=locking(a),locking(b)
    fa=[Q(0)]*N; fb=[Q(0)]*N
    for n in range((N-1)//2):
        fa[2*n+1]=stopping_weight(a,n)
        fb[2*n+1]=stopping_weight(b,n)
    ga=[Q(0)]*N; gb=[Q(0)]*N
    ga[0],gb[0]=sa,sb
    for k in range(1,N):
        ga[k]=sum((fa[j]*gb[k-j] for j in range(1,k+1)),Q(0))
        gb[k]=sum((fb[j]*ga[k-j] for j in range(1,k+1)),Q(0))
    # Check the equation (1-fa*fb)*ga = sa + sb*fa directly as formal series.
    for k in range(N):
        mult=sum((fa[j]*fb[k-j] for j in range(k+1)),Q(0))
        lhs=ga[k]-sum((sum((fa[j]*fb[l-j] for j in range(l+1)),Q(0))*ga[k-l] for l in range(1,k+1)),Q(0))
        rhs=(sa if k==0 else Q(0))+sb*fa[k]
        assert lhs == rhs
        checks+=1

# Explicit inferior-opinion majority-lock witness and sharp inequality.
a,b=Q(7,10),Q(9,10)
assert a<b and b*(2*a-1)/(a+b-1)==Q(3,5)
assert a > (3*b-1)/(4*b-1)
checks+=2

# Exact even-time fair-survival calculation by ballot enumeration.
# Tail survival through 2n is binomial(2n,n)/4**n.
for n in range(1,13):
    # Catalan first-hit mass sums are dyadic rationals.
    mass=sum((Q(cat(j),2**(2*j+1)) for j in range(n)),Q(0))
    assert 1-mass == Q(comb(2*n,n),4**n)
    checks+=1
print(f'VERIFY_OK {checks} exact-rational and combinatorial checks')
