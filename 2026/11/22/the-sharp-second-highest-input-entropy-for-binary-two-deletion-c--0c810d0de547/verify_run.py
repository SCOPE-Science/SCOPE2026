"""Run-functional certificate and independent finite enumeration (integer arithmetic)."""
from itertools import groupby, product
from math import comb

def run_product(y):
    n = len(y)
    r = [len(tuple(g)) for _, g in groupby(y)]
    long = [(i, k) for i, k in enumerate(r) if k >= 2]
    unit = 27 * 2 ** (4 * n)
    if not long:
        return unit ** n * (n + 1) ** (n + 1)
    U = sum(k for _, k in long)
    w = [long[0][1] + long[0][0] + 1]
    for (i, k), (j, l) in zip(long, long[1:]):
        w.append(k + l + (j - i - 1) + 1)
    w.append(long[-1][1] + (len(r) - 1 - long[-1][0]) + 1)
    result = unit ** (n - U)
    for _, k in long:
        t = comb(k + 2, 2)
        result *= t ** t * (k + 1) ** ((2 * n - k) * (k + 1))
    for k in w:
        result *= k ** k
    return result

def second_formula(n):
    a = (n + 4) // 2
    b = (n + 5) // 2
    # 2^(n B_n + c_n) = (2^n unit^{n-2}) etc via u=2 and h_n(2)
    return (27 * 2 ** (4 * n)) ** (n - 2) * (6 ** 6) * (3 ** (3 * (2 * n - 2))) * a ** a * b ** b

def expected(n):
    results = set()
    for left in range(n - 1):
        right = n - 2 - left
        if abs(left - right) > 1: continue
        for first in (0, 1):
            runs = (1,) * left + (2,) + (1,) * right
            word = []
            bit = first
            for k in runs:
                word.extend((bit,) * k)
                bit ^= 1
            results.add(tuple(word))
    return results

for n in range(2, 16):
    vals = [(run_product(y), y) for y in product((0, 1), repeat=n)]
    base = (27 * 2 ** (4 * n)) ** n * (n + 1) ** (n + 1)
    smaller = sorted(set(v for v, _ in vals))[:2]
    assert smaller[0] == base
    assert smaller[1] == second_formula(n)
    assert {y for v, y in vals if v == smaller[1]} == expected(n)
    print('n=', n, 'word_count=', len(vals), 'exact_run_check=PASS', flush=True)
print('RUN_EXACT_PASS')
