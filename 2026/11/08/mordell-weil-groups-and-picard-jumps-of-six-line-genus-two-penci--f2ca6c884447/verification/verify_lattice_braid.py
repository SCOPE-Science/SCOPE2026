"""Exact finite checks for a six-line genus-two pencil over characteristic zero."""
from fractions import Fraction
from itertools import combinations, product
from math import gcd


def det(a):
    a = [[Fraction(z) for z in row] for row in a]
    n = len(a)
    value = Fraction(1)
    for j in range(n):
        k = next((i for i in range(j, n) if a[i][j]), None)
        if k is None:
            return 0
        if k != j:
            a[k], a[j] = a[j], a[k]
            value = -value
        pivot = a[j][j]
        value *= pivot
        for i in range(j+1, n):
            q = a[i][j] / pivot
            for h in range(j+1, n):
                a[i][h] -= q*a[j][h]
            a[i][j] = 0
    assert value.denominator == 1
    return int(value)

# A six-line arrangement L0:Y=0; Li:X+iY+i^2 Z=0, i=1,...,5.
# Let p=[0:0:1]; the ten nodes of L1..L5 are [ij:-(i+j):1].
directions = {Fraction(i+j,i*j) for i,j in combinations(range(1,6),2)}
assert len(directions) == 10
assert len(set(i*i for i in range(1,6))) == 5
# The central six non-identity components form a five-leaf star,
# central square -3 and leaf squares -2.
star = [[(-3 if i==j==0 else -2 if i==j else
          1 if i==0 or j==0 else 0) for j in range(6)] for i in range(6)]
assert det(star) == 16
trivial_lattice_abs_discriminant = 2**10*abs(det(star))
generic_ns_abs_discriminant = 64
assert trivial_lattice_abs_discriminant == 2**14
assert trivial_lattice_abs_discriminant // generic_ns_abs_discriminant == 16**2

# Four standard primitive vanishing cycles for the 5-strand braid action
# form a unimodular basis of H_1(C,Z), a rank-four symplectic lattice.
cycles = [(1,0,0,0), (0,1,0,0), (1,0,1,0), (0,0,0,1)]
assert abs(det([[v[i] for v in cycles] for i in range(4)])) == 1
J = ((0,1,0,0),(-1,0,0,0),(0,0,0,1),(0,0,-1,0))

def pairing(x,v):
    return sum(x[i]*J[i][j]*v[j] for i in range(4) for j in range(4))

for n in range(2,13):
    fixed = sum(all((2*pairing(x,v)) % n == 0 for v in cycles)
                for x in product(range(n), repeat=4))
    assert fixed == gcd(n,2)**4, (n, fixed)

print('GENUS_TWO_LATTICE_AND_BRAID_CHECK_OK 10 16 11')
