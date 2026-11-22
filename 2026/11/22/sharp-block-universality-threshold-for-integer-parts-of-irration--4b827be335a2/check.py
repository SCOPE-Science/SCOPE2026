"""Exact integer sampling and independent weighted-uniform calculations.

Run: python3 check.py
Only standard Python libraries are used.  Finite checks are not an infinite proof.
"""
from collections import Counter
from decimal import Decimal, getcontext
from math import comb, factorial, isqrt

getcontext().prec = 65
ALPHA = Decimal(2).sqrt()

def weights(d):
    return [(-1) ** (d - 1 - i) * comb(d, i) for i in range(d)]

def model(d):
    w = weights(d)
    v = [abs(z) for z in w]
    minus = sum(-z for z in w if z < 0)
    assert sum(v) == 2**d - 1 and minus == 2**(d-1)-1
    return w, v, minus

def distribution(d):
    w, v, minus = model(d)
    theta = factorial(d) * ALPHA
    q = int(theta.to_integral_value(rounding='ROUND_FLOOR'))
    product = factorial(d)
    for k in v:
        product *= k
    sub = []
    for mask in range(1 << d):
        ss = sum(v[i] for i in range(d) if mask & (1 << i))
        sgn = -1 if mask.bit_count() % 2 else 1
        sub.append((ss, sgn))
    def F(t):
        total = Decimal(0)
        for ss, sgn in sub:
            z = t - ss
            if z > 0:
                total += sgn * z**d
        return total / product
    j_lo = q - minus
    j_hi = q + 2**(d - 1)
    probs = {}
    for j in range(j_lo, j_hi+1):
        t = Decimal(j) - theta + minus
        probs[j] = F(t+1) - F(t)
        assert probs[j] > 0, (d, j, probs[j])
    assert len(probs) == 2**d
    assert abs(sum(probs.values()) - 1) < Decimal('1e-35')
    assert abs(F(Decimal(sum(v))) - 1) < Decimal('1e-35')
    return probs

def floor_poly(d, n, shifted=False):
    # Exact floor: sqrt(2)*n^d or sqrt(2)*n^d + (3n/8 if d>=2) + 3/5.
    if shifted:
        p = 40 * n**d
        return (isqrt(2*p*p)+(15*n if d >= 2 else 0)+24)//40
    p = n**d
    return isqrt(2*p*p)

def finite_difference(seq, d, n):
    w, _, _ = model(d)
    return seq[n+d] - sum(w[i]*seq[n+i] for i in range(d))

def main():
    tally = 0
    for d in range(1, 6):
        probs = distribution(d)
        q_support = set(probs)
        for m in (2, 3, 5, 9, 17, 41):
            # All residue prefixes have precisely the predicted number of last letters.
            for r in range(m):
                assert len({(r+j) % m for j in q_support}) == min(m, 2**d)
            tally += m
        for shifted in (False, True):
            N = 25000 if d <= 3 else 12000
            seq = [floor_poly(d, n, shifted) for n in range(N+d)]
            observed = Counter()
            for n in range(N):
                j = finite_difference(seq, d, n)
                assert j in probs
                observed[j] += 1
            # Oscillatory polynomial samples have no fixed finite-N discrepancy theorem here.
            # Check only a broad diagnostic tolerance, not a purported proof.
            for j, p in probs.items():
                assert abs(observed[j]/N - float(p)) < 0.045, (d, shifted, j, p, observed[j])
            if d <= 3:
                m = 5
                patterns = Counter(tuple(seq[n+i] % m for i in range(d+1)) for n in range(N))
                for pat in patterns:
                    prefix, final = pat[:-1], pat[-1]
                    r = (final - sum(weights(d)[i]*prefix[i] for i in range(d))) % m
                    assert any(j % m == r for j in probs)
                # All observed frequencies must be allowed, but rare allowed patterns may
                # not yet appear in a finite prefix.
                assert len(patterns) <= (m**d) * min(m, 2**d)
                if not shifted and d in (2, 3):
                    assert len(patterns) == (m**d) * min(m, 2**d)
            tally += N
    print(f'PASS: all-parameter support algebra for d=1..5 and 6 moduli; {tally} exact integer / distribution checks')
    print('First correction probabilities for d=2:')
    print({j: str(v)[:24] for j, v in distribution(2).items()})

if __name__ == '__main__':
    main()
