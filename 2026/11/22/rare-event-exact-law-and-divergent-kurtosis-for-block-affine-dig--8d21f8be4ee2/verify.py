"""Exact-rational finite-digit checks for block-affine digital integration."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb

checks = 0

def check(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1


def finite_law(n, depth):
    """Distribution of the first depth post-prefix bit contributions."""
    p = Q(1, n)
    distribution = {Q(0): Q(1)}
    for j in range(1, depth + 1):
        weight = Q(1, 2 * n * (2 ** j))
        nxt = defaultdict(Q)
        for val, prob in distribution.items():
            nxt[val] += prob * (1 - p)
            nxt[val + weight] += prob * p / 2
            nxt[val - weight] += prob * p / 2
        distribution = dict(nxt)
    return distribution


def truncated_moments(n, depth):
    p = Q(1,n)
    b2 = sum((Q(1, 2 ** j)) ** 2 for j in range(1,depth+1))
    b4 = sum((Q(1, 2 ** j)) ** 4 for j in range(1,depth+1))
    variance = p * b2 / (4*n*n)
    fourth = (p*b4 + 3*p*p*(b2*b2-b4))/(16*n**4)
    return variance, fourth

# All possible finite suffix output digits: binary row mask and independent shift.
# The first N inputs visit each vector in F_2^em exactly once, so nonzero masks average to 1/2.
for e, m in ((2,1),(2,2),(3,1)):
    n = 2 ** (e*m)
    bits = [tuple((a >> j) & 1 for j in range(e*m)) for a in range(n)]
    for mask in range(n):
        for shift in (0,1):
            observed = Q(sum((sum(bb[j] for j in range(e*m) if (mask >> j)&1) + shift) % 2 for bb in bits),n)
            expected = Q(shift) if mask == 0 else Q(1,2)
            check(observed, expected)

for n, depth in ((4,4),(16,5),(64,6)):
    dist = finite_law(n, depth)
    check(sum(dist.values()),Q(1))
    check(sum(val*p for val,p in dist.items()),Q(0))
    v, f = truncated_moments(n,depth)
    check(sum(val*val*p for val,p in dist.items()),v)
    check(sum(val**4*p for val,p in dist.items()),f)
    check(v, Q(1,12*n**3)*(1-Q(1,4**depth)))

# Directly enumerate every 2^(em) binary mask and random shift for each suffix row.
# For n=4, depth 3, there are 8^3=512 equiprobable mask/shift combinations.
e, m, n, depth = 2, 1, 4, 3
outcomes = defaultdict(int)
for selections in product(range(2*n), repeat=depth):
    v = Q(0)
    for j, choice in enumerate(selections,1):
        mask, shift = divmod(choice,2)
        if mask == 0:
            v += Q(2*shift-1, 2*n*2**j)  # digit mean shift +/-1/2
    outcomes[v] += 1
# Compare with the independent rare-event Bernoulli/Rademacher law.
law = finite_law(n,depth)
check({x:Q(c,(2*n)**depth) for x,c in outcomes.items()},law)

# Exact all-depth identities by convergent geometric series and cumulant expansion.
for n in (4, 8, 16, 64, 256, 1024):
    p = Q(1,n)
    variance = p*Q(1,3)/(4*n*n)
    fourth = (p*Q(1,15)+3*p*p*(Q(1,9)-Q(1,15)))/(16*n**4)
    check(variance,Q(1,12*n**3))
    check(fourth,Q(n+2,240*n**6))
    check(fourth/variance**2,Q(3*(n+2),5))
    # Independently jittered strata instead have finite kurtosis approaching three.
    check(Q(3)-Q(6,5*n), Q(3*n*n- Q(6*n,5),n*n))
print('VERIFY_OK',checks)
