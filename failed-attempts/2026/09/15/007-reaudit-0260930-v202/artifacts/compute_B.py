"""Compute explicit uniform bound B(D) and sanity-check Northcott counting."""
import math
from fractions import Fraction
import random


def B(D: int) -> int:
    return D ** 2 * (2 * 8 ** D + 1) ** (D + 1)


def mahler_bound(D: int) -> float:
    # max Mahler measure for degree<=D, height<=2 log 2
    return math.exp(D * 2 * math.log(2))  # = 4^D


for D in [1, 2, 3, 4, 5]:
    M = mahler_bound(D)
    assert abs(M - 4 ** D) < 1e-6
    coeff = 2 ** D * M
    assert coeff <= 8 ** D + 1e-9, (D, coeff)
    print(f"D={D} B(D)={B(D)} Mahler<={M:.1f} coeff<={coeff:.1f}")

assert B(1) == 289
assert B(2) == 8586756

# D=1 check: all rational h<=2log2 have numerator/denominator bounded.
# h(p/q)=log max(|p|,|q|) for coprime; bound max<=4.
n = sum(1 for q in range(1, 5) for p in range(-4, 5) if math.gcd(p, q) == 1 and max(abs(p), abs(q)) <= 4)
print("D=1 rationals with h<=2log2:", n, "<= B(1) =", B(1))
assert n <= B(1)


# height inequality spot check: |h(f(x))-d h(x)|<=h(c)+log2 on random rationals
def H(p: Fraction) -> float:
    return math.log(max(abs(p.numerator), abs(p.denominator)))


random.seed(0)
for _ in range(1000):
    x = Fraction(random.randint(-20, 20), random.randint(1, 20))
    c = Fraction(random.randint(-5, 5), random.randint(1, 5))
    d = random.randint(2, 5)
    f = x ** d + c
    assert abs(H(f) - d * H(x)) <= H(c) + math.log(2) + 1e-9
print("height inequality spot checks passed")
