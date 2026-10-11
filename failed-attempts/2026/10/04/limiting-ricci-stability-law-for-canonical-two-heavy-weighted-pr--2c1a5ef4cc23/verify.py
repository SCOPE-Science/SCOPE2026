from fractions import Fraction
from math import log


def canonical_by_ages(r, a, b):
    for k in range(1, a):
        if r*k + (k*b) % a < a:
            return False
    for k in range(1, b):
        if r*k + (k*a) % b < b:
            return False
    return True


def canonical_closed(r, a, b):
    d = b-a
    return 0 <= d <= r and 1 <= a <= r+d


def ricci(r, a, b):
    return Fraction(r+2, r+a+b)


for r in range(2, 41):
    seen = []
    for a in range(1, 2*r+2):
        for b in range(a, 3*r+3):
            direct = canonical_by_ages(r, a, b)
            closed = canonical_closed(r, a, b)
            assert direct == closed, (r, a, b, direct, closed)
            if closed:
                seen.append((a, b))
    assert len(seen) == 3*r*(r+1)//2
    values = [ricci(r, a, b) for a, b in seen]
    assert max(values) == 1 and values.count(Fraction(1, 1)) == 1
    lower = Fraction(r+2, 6*r)
    assert min(values) == lower and values.count(lower) == 1


def survival_from_L(L):
    if L <= 0:
        return 0.0
    if L <= 1:
        return L*L/6
    if L <= 2:
        return (2*L-1)/6
    if L <= 5:
        return (-L*L+10*L-7)/18
    return 1.0


for L, target in [(0, 0), (1, 1/6), (2, 1/2), (5, 1)]:
    assert abs(survival_from_L(L)-target) < 1e-14

for r in [10, 50, 200, 1000]:
    total = 0.0
    count = 0
    for d in range(r+1):
        for a in range(1, r+d+1):
            total += (r+2)/(r+2*a+d)
            count += 1
    empirical = total/count
    if r == 1000:
        assert abs(empirical-log(3)/3) < 7e-4

print("VERIFY_OK")
