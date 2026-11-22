"""Independent exhaustive checks for the seven-site Fano triple-interaction model.
Run with Python 3.8+; no third-party dependencies.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

VERTICES = tuple(range(1,8))
LINES = tuple(sorted({tuple(sorted((i,j,i^j))) for i in VERTICES for j in VERTICES if i < j}))
assert len(LINES) == 7 and all(len(L) == 3 for L in LINES)
assert all(sum(set(pair).issubset(L) for L in LINES) == 1 for pair in combinations(VERTICES,2))
SPECIAL = (1,2,3)

# Method A: directly evaluate all 128 spin assignments and all seven triple products.
direct = Counter()
for positive_mask in range(1 << 7):
    sigma = {j: 2*bool(positive_mask & (1 << (j-1)))-1 for j in VERTICES}
    q = sigma[1]*sigma[2]*sigma[3]
    B = sum(sigma[a]*sigma[b]*sigma[c] for (a,b,c) in LINES if (a,b,c) != SPECIAL)
    M = sum(sigma.values())
    direct[(B,q,M)] += 1
assert sum(direct.values()) == 128

# Method B: geometric incidence count, independent of spin-product evaluations.
geometry = Counter()
for k in range(8):
    for S in combinations(VERTICES,k):
        S = set(S)
        contained_lines = sum(all(x in S for x in L) for L in LINES)
        T = 2*k*(4-k)+8*contained_lines-7
        r = len(S.intersection(SPECIAL))
        q = (-1) ** (3-r)
        geometry[(T-q,q,2*k-7)] += 1
assert geometry == direct

# All signatures and multiplicities, including fixed magnetization.
expected = {
    (-6,-1,-7):1,(-6,-1,1):7,
    (-2,1,-5):3,(-2,1,-1):12,(-2,1,3):9,
    (0,-1,-5):4,(0,-1,-1):16,(0,-1,3):12,
    (0,1,-3):12,(0,1,1):16,(0,1,5):4,
    (2,-1,-3):9,(2,-1,1):12,(2,-1,5):3,
    (6,1,-1):7,(6,1,7):1,
}
assert direct == expected

# The five candidate magnetization sectors at strictly positive magnetic field.
active = {(-6,-1,1):7,(-2,1,3):9,(0,1,5):4,(2,-1,5):3,(6,1,7):1}

def exact_ground(lam,field,states=direct):
    energies = {key: Fraction(B) + lam*q - field*M for key in states for B,q,M in [key]}
    low = min(energies.values())
    return low, sum(states[key] for key,v in energies.items() if v == low)

for nlam in range(-20,21):
    for nh in range(1,101):
        lam, field = Fraction(nlam,4), Fraction(nh,8)
        assert exact_ground(lam,field,active) == exact_ground(lam,field)

# Zero-field threshold: the full ground states include all lower-magnetization twins.
for nlam in range(-24,25):
    lam=Fraction(nlam,8)
    e,d=exact_ground(lam,Fraction(0))
    assert (e,d)==(min(-6-lam,-2+lam),8 if lam > -2 else 24 if lam < -2 else 32)

# Explicit positive-field open-region sequence and special coexistence points.
for lam,field,count in [(-3,Fraction(1,2),9),(-3,1,13),(-3,2,4),(-3,3,5),
                         (-Fraction(3,2),Fraction(1,2),16),(-1,1,20),
                         (0,Fraction(3,2),11),(0,3,5),(1,2,14),(1,3,8),
                         (2,2,10),(2,4,4)]:
    assert exact_ground(Fraction(lam),Fraction(field))[1] == count, (lam,field)

print('PASS: 7 lines, Steiner property, 128 configurations, independent methods,')
print('16 exact signatures, 4100 rational parameter comparisons, zero-field and')
print('coexistence multiplicities.')
print('state table (B,Q,M): multiplicity')
for key in sorted(direct): print(key,direct[key])
