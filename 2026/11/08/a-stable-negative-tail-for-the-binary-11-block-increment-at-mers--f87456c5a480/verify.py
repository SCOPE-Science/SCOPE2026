"""Exact coefficient certificate for the binary 11-block difference theorem.
Uses integer/rational Laurent polynomials and a finite 8-state carry machine.
No libraries beyond Python's standard library are needed.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product

STATES = list(product((0, 1), repeat=3))
INDEX = {state: i for i, state in enumerate(STATES)}
ZERO = {}

def atom(exp=0, coeff=1):
    coeff = Q(coeff)
    return {exp: coeff} if coeff else {}

def add(*parts):
    d = defaultdict(Q)
    for part in parts:
        for e, a in part.items():
            d[e] += a
    return {e: a for e, a in d.items() if a}

def neg(p):
    return {e: -a for e, a in p.items()}

def sub(p, q):
    return add(p, neg(q))

def scale(p, a):
    return {e: a * v for e, v in p.items() if a * v}

def shift(p, n):
    return {e+n: a for e,a in p.items()}

def mul(p, q):
    return add(*(scale(shift(q, e), a) for e,a in p.items())) if p else {}

z = atom(1)
one = atom()
B = add(scale(z, 2), atom(0, -1))  # common denominator 2z-1

def t_apply(bit, v):
    nxt = [{} for _ in STATES]
    for i, (carry, px, py) in enumerate(STATES):
        for x in (0, 1):
            s = x + bit + carry
            y = s % 2
            j = INDEX[(s // 2, x, y)]
            nxt[i] = add(nxt[i], scale(shift(v[j], py*y-px*x), Q(1,2)))
    return nxt

def n_tail(c, px, py):
    if not c:
        if px == py:
            return B
        return scale(mul(add(one, atom(py-px)), B), Q(1,2))
    return scale(mul(add(z, one), add(shift(B, py), atom(1-px))), Q(1,4))

def same(v, w):
    return all(p==q for p,q in zip(v,w))

def power_apply(bit, v, n):
    for _ in range(n):
        v = t_apply(bit,v)
    return v

def gcum(k):
    return power_apply(1, tails, k)[INDEX[(0,0,0)]]

tails = [n_tail(*s) for s in STATES]
assert same(t_apply(0, tails), tails), 'zero suffix not fixed'
w = [sub(a,b) for a,b in zip(t_apply(1,tails),tails)]
u = power_apply(1,w,3)
v = t_apply(1,u)
assert same(v, [scale(shift(p,1),Q(1,2)) for p in u]), 'period polynomial identity fails'

N4 = scale(mul(add(z,one),add(scale(atom(4),4),scale(atom(2),11),scale(z,10),atom(0,7))),Q(1,64))
assert gcum(4)==N4, 'incorrect G4 numerator'
P = mul(mul(mul(sub(z,one),sub(z,one)), add(z,one)),add(scale(atom(2),2),z,atom(0,2)))
P = scale(P,Q(1,128))
assert power_apply(1,w,4)[INDEX[(0,0,0)]] == mul(P,B), 'incorrect first-step numerator'

# Sharp threshold: exact probability of a negative delta for k=1,2,3,4.
# Compute the limiting negative tail by finite transfer, using the rational
# common denominator and exact coefficient series at infinity.
def coeff_inf(num, degree):
    # coefficient of z^degree in num / (2z-1), expanded for |z|>1/2.
    return sum((a*Q(1,2**(e-degree)) for e,a in num.items() if e>=degree+1), Q(0))

expected_pos = {1:Q(13,16),2:Q(47,64),3:Q(87,128),4:Q(83,128)}
for k, positive in expected_pos.items():
    num = gcum(k)
    # Negative coefficients are geometric after the smallest numerator degree.
    # Sum exact negative weights through a finite prefix and a geometric tail.
    min_power = min(num)
    cutoff = min(-1,min_power-1)
    finite = sum((coeff_inf(num,e) for e in range(cutoff+1,0)),Q(0))
    tailmass = 2*coeff_inf(num,cutoff) # geometric sum of j>=1 from cutoff-1
    negative = finite+tailmass
    assert 1-negative==positive,(k,positive,negative)

assert sum(P.values())==0, 'increments must preserve total mass'
assert N4 and coeff_inf(N4,-1)==Q(45,256), 'tail coefficient mismatch'

# Independent integer test: exact sample on 2^19 consecutive arguments.
def r11(n):
    return (n & (n>>1)).bit_count()
for k in range(1,9):
    t = (1<<k)-1
    n = 1<<19
    actual = sum(r11(v+t)>=r11(v) for v in range(n))
    goal = expected_pos[k] if k <=4 else Q(83,128)
    assert abs(Q(actual,n)-goal)<Q(1,128), (k,actual,goal)
print('VERIFY_OK states=8 zero_suffix=invariant polynomial_identity=exact G4=exact recurrence=exact sharp_thresholds=1..4 negative_tail=45/(128*2^j) finite_integer_samples=8x524288')
