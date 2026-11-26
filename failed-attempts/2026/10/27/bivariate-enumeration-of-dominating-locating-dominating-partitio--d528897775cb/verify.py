#!/usr/bin/env python3
"""Reproduce cyclic domination--location partition enumerator independently."""
from collections import Counter

def valid_graph(n, bits):
    # Bit 1 = locating-dominating class L; bit 0 = dominating class D.
    locate = {i for i in range(n) if (bits >> i) & 1}
    dominate = set(range(n)) - locate
    if not locate or not dominate:
        return False
    if any(not ({(v-1)%n, (v+1)%n} & dominate) for v in locate):
        return False
    sig = [frozenset({(v-1)%n, (v+1)%n} & locate) for v in dominate]
    return all(sig) and len(sig) == len(set(sig))

def valid_word(n, bits):
    w = ''.join('1' if (bits >> i) & 1 else '0' for i in range(n))
    return not any(any(''.join(w[(i+j)%n] for j in range(k)) == p
                       for i in range(n)) for p,k in [('000',3),('111',3),('00100',5)])

def add_scaled(dest, src, shift, coef=1):
    for deg, val in src.items():
        dest[deg+shift] += coef * val

def bivariate_coefficients(through):
    # -z*d_z log Q, Q=1-u*z²-u²*(z³+z⁴+z⁵)-u³*z⁶.
    # Store coefficient polynomials as Counters: exponent of u -> integer.
    b = [Counter() for _ in range(through+1)]
    numerator = {2:(1,2), 3:(2,3), 4:(2,4), 5:(2,5), 6:(3,6)}
    for n in range(through+1):
        if n in numerator:
            k,v = numerator[n]; b[n][k] += v
        for step,upow in [(2,1),(3,2),(4,2),(5,2),(6,3)]:
            if n>=step: add_scaled(b[n], b[n-step], upow)
    return b

B = bivariate_coefficients(60)
expected = {
    5:{2:5,3:5},6:{3:14,4:3},7:{3:7,4:14},
    8:{4:30,5:8},9:{4:18,5:36,6:3},
    10:{4:5,5:62,6:25},11:{5:44,6:88,7:11},
    12:{5:12,6:138,7:72,8:3},
}
for n in range(5,18):
    observed=Counter()
    for bits in range(1<<n):
        g=valid_graph(n,bits)
        w=valid_word(n,bits)
        assert g==w, ('forbidden-factor mismatch',n,bits,g,w)
        if g: observed[bits.bit_count()] += 1
    assert observed==B[n], ('rational coefficient mismatch',n,observed,B[n])
    if n in expected: assert dict(observed)==expected[n]

# Independent algebraic check that the 2-by-2 zero-run transfer matrix has Q.
# T = [[z²u+z³u²,z²u+z³u²], [z³u+z⁴u²,z⁴u²]].
# Compute det(I-T) by sparse Laurent-free polynomial arithmetic.
def mul(a,b):
    c=Counter()
    for (z1,u1),v in a.items():
        for (z2,u2),w in b.items():c[(z1+z2,u1+u2)] += v*w
    return dict(c)
A={(0,0):1,(2,1):-1,(3,2):-1}
D={(0,0):1,(4,2):-1}
neg_B={(2,1):-1,(3,2):-1}
neg_C={(3,1):-1,(4,2):-1}
Q=Counter(mul(A,D))
for t,v in mul(neg_B,neg_C).items():Q[t]-=v
Q={k:v for k,v in Q.items() if v}
expected_Q={(0,0):1,(2,1):-1,(3,2):-1,(4,2):-1,(5,2):-1,(6,3):-1}
assert Q==expected_Q, (Q,expected_Q)
# Total counts equal the documented earlier generic Fielder sequence A001636,
# a coincident sequence, not a prior graph-partition classification.
assert [sum(B[n].values()) for n in range(5,16)] == [10,17,21,38,57,92,143,225,351,555,868]
print('VERIFY_OK n=5..17 all partitions compared against cyclic factors and bivariate rational coefficients')
print('TRANSFER_Q_OK determinant: 1-u*z^2-u^2*(z^3+z^4+z^5)-u^3*z^6')
print('INITIAL_BIVARIATE',[(n,dict(sorted(B[n].items()))) for n in range(5,13)])
print('OEIS_A001636_UNIVARIATE_MATCH n=5..15')
