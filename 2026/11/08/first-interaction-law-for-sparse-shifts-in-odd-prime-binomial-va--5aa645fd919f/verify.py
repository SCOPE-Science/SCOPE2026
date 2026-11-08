"""Exact arithmetic checks for the first-interaction law of fixed-shift binomial valuations."""
from fractions import Fraction
from itertools import product
from math import comb


def transfer(p, active, degree):
    """Carry-state digit DP for exact density; coefficients through degree."""
    digits = dict(active)
    last = max(digits) + degree + 2
    state = {(0, 0): 1}
    for j in range(last):
        nxt = {}
        for (carry, r), ways in state.items():
            for digit in range(p):
                nxtcarry = int(digit + digits.get(j, 0) + carry >= p)
                newr = r + nxtcarry
                if newr <= degree:
                    key = (nxtcarry, newr)
                    nxt[key] = nxt.get(key, 0) + ways
        state = nxt
    assert all(carry == 0 for carry, r in state)
    return [Fraction(state.get((0, r), 0), p ** last) for r in range(degree + 1)]


def naive_product(p, values, degree):
    arr = [Fraction(1)] + [Fraction(0)] * degree
    for d in values:
        one = [Fraction(p-d, p)] + [Fraction(d * (p-1), p**(r+1)) for r in range(1, degree+1)]
        arr = [sum(arr[k] * one[r-k] for k in range(r+1)) for r in range(degree+1)]
    return arr


def first_defect(p, active):
    positions = [a for a, d in active]
    values = [d for a, d in active]
    g = min(b-a for a, b in zip(positions, positions[1:]))
    err = Fraction(0)
    for i in range(len(active)-1):
        if positions[i+1]-positions[i] == g:
            weight = Fraction(values[i]*values[i+1], p**(g+2))
            for j, v in enumerate(values):
                if j != i and j != i+1:
                    weight *= Fraction(p-v, p)
            err += weight
    return g, err


def valuation(n, p):
    c = 0
    while n and n % p == 0:
        c += 1
        n //= p
    return c


def direct_modulus(p, active, degree):
    # A complete period yields exact natural-density frequencies.
    shift = sum(d * p**a for a, d in active)
    modulus = p ** (max(a for a, d in active) + degree + 2)
    count = [0] * (degree + 1)
    for n in range(modulus):
        k = valuation(comb(n + shift, shift), p)
        if k <= degree:
            count[k] += 1
    return [Fraction(k, modulus) for k in count]


def verify():
    cases = 0
    checks = 0
    for p in (3, 5, 7):
        for gap in (1, 2, 3):
            for positions in ([0, gap, 2*gap], [0, gap, 2*gap+1, 3*gap+1],
                              [0, gap+1, 2*gap+1, 3*gap+2]):
                for pattern in (0, 1, 2):
                    values = [1 if pattern == 0 else (p-1 if pattern == 1 or j % 2 == 0 else 1)
                              for j in range(len(positions))]
                    active = list(zip(positions, values))
                    g, defect = first_defect(p, active)
                    real = transfer(p, active, g)
                    formal = naive_product(p, values, g)
                    assert real[:g] == formal[:g]
                    assert real[g] == formal[g] - defect
                    assert defect > 0
                    cases += 1
                    checks += g+1
    direct_cases = 0
    for p in (3, 5):
        for active in ([(0, 1), (1, 1)], [(0, p-1), (2, 1)],
                       [(0, 1), (1, p-1)], [(0, 1), (2, 1)]):
            g, defect = first_defect(p, active)
            exp = transfer(p, active, g)
            # Direct binomial numbers can be big; use only moderate periods.
            assert direct_modulus(p, active, g) == exp
            direct_cases += 1
    print('VERIFY_OK', 'multidigit_cases='+str(cases), 'exact_rational_coefficients='+str(checks),
          'complete_modulus_binomial_censuses='+str(direct_cases), 'strict_first_defects=yes')


if __name__ == '__main__':
    verify()
