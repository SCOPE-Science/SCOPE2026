"""Exact finite checks for a dyadic binomial-column doubling theorem.

Run with Python 3. This script is supplementary: the infinite statement
is proved by the unique-closest-factor argument in RESULT.md.
"""
from collections import Counter
from math import comb, factorial

checks = 0

def test(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def v2(n):
    if n == 0:
        return float('inf')
    return (abs(n) & -abs(n)).bit_length() - 1

# Independently evaluate the unique dominant factor and the exact scale of
# all 2-adic branches, including input classes at integer roots.
for m in range(1, 33):
    L = m.bit_length()
    a = L - 1
    for r in range(1 << L):
        vals = [v2(r - j) for j in range(m)]
        top = max(vals)
        test(vals.count(top) == 1 and top >= a,
             f'closest-factor failure: m={m}, r={r}')
        j_star = vals.index(top)
        second = max((vals[j] for j in range(m) if j != j_star),
                     default=-1)
        test(second < min(top, L),
             f'valuation separation failure: m={m}, r={r}')
        S = sum(vals[j] for j in range(m) if j != j_star)
        d = L + S - v2(factorial(m))
        test(d >= 0, f'negative branch scale: m={m}, r={r}')
        x = comb(r, m)
        for eps in (0, 1):
            y = comb(2*r + eps, 2*m)
            test((x - y) % (1 << d) == 0,
                 f'center mismatch: m={m}, r={r}, eps={eps}')
        # Check the 2-adic distance formula on a local finite test grid.
        for t in range(5):
            for s in range(t):
                q1 = comb(r + (1 << L)*t, m)
                q2 = comb(r + (1 << L)*s, m)
                test(v2(q1-q2) == d + v2(t-s),
                     f'original branch distance: m={m},r={r},t={t},s={s}')
                for eps in (0, 1):
                    p1 = comb(2*(r+(1<<L)*t)+eps, 2*m)
                    p2 = comb(2*(r+(1<<L)*s)+eps, 2*m)
                    test(v2(p1-p2) == d + v2(t-s),
                         f'doubled branch distance: m={m},r={r},eps={eps},t={t},s={s}')

# Exhaustive finite-modulus distributions: for every fixed input residue
# class, either parity of the doubled top index has the same output histogram.
for m in range(1, 25):
    L = m.bit_length()
    for k in range(1, 7):
        mod = 1 << k
        blocks = 1 << L
        hist_original = [Counter() for _ in range(blocks)]
        hist_even = [Counter() for _ in range(blocks)]
        hist_odd = [Counter() for _ in range(blocks)]
        for n in range(1 << (L+k)):
            r = n % blocks
            hist_original[r][comb(n,m) % mod] += 1
            hist_even[r][comb(2*n,2*m) % mod] += 1
            hist_odd[r][comb(2*n+1,2*m) % mod] += 1
        for r in range(blocks):
            test(hist_original[r] == hist_even[r] == hist_odd[r],
                 f'fiber mismatch: m={m},k={k},r={r}')

# A nonuniform illustration: lower indices 5 and 10 have identical
# limiting output laws with densities 1/2, 1, 3 on the three dyadic shells.
for k in range(3, 10):
    for m in (5, 10):
        L = m.bit_length()
        N = 1 << (L+k)
        count = Counter(comb(n,m) % (1 << k) for n in range(N))
        for y in range(1 << k):
            expected = (N // (1 << k)) * (1 + (y % 2 == 0) + 4 * (y % 8 == 0)) // 2
            test(count[y] == expected, f'explicit histogram m={m}, k={k}, y={y}')
print(f'PASS: {checks} exact assertions (including full residue histograms).')
