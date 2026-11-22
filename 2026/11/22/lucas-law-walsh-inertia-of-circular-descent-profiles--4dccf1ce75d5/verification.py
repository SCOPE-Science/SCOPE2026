"""Exact finite checks for the cyclic descent Fourier spectrum.
This checker verifies sample dimensions; the manuscript contains the all-n proof.
"""
from itertools import permutations
from math import factorial


def eulerian_rows(n):
    rows = [[1]]
    for m in range(1, n + 1):
        if m == 1:
            rows.append([1])
            continue
        old = rows[-1]
        rows.append([(d + 1) * (old[d] if d < len(old) else 0)
                    + (m - d) * (old[d - 1] if d else 0)
                     for d in range(m)])
    return rows


def signed_eulerian(row):
    return sum((-1)**d * a for d, a in enumerate(row))


def full_formula(n, mask, euler):
    full = (1 << n) - 1
    if mask == full:
        return -n * signed_eulerian(euler[n - 1])
    if mask == 0:
        return factorial(n)
    # Work clockwise after the first gap: all selected runs are then linear.
    gap = next(i for i in range(n) if not (mask >> i) & 1)
    runs = []
    run = 0
    for j in range(1, n + 1):
        i = (gap + j) % n
        if (mask >> i) & 1:
            run += 1
        elif run:
            runs.append(run)
            run = 0
    numerator = factorial(n)
    denominator = 1
    for r in runs:
        numerator *= signed_eulerian(euler[r + 1])
        denominator *= factorial(r + 1)
    assert numerator % denominator == 0
    return numerator // denominator


def matchings_support(n):
    # Each matching's covered vertex set, with cycle edges (i,i+1).
    covered = set()
    for m in range(1 << n):
        if any((m >> i & 1) and (m >> ((i + 1) % n) & 1)
               for i in range(n)):
            continue
        vertices = 0
        for i in range(n):
            if m >> i & 1:
                vertices |= (1 << i) | (1 << ((i + 1) % n))
        covered.add(vertices)
    return covered


def test():
    checks = 0
    for n in range(3, 10):
        vals = [0] * (1 << n)
        for p in permutations(range(n)):
            mask = sum((1 << i) for i in range(n)
                       if p[i] > p[(i + 1) % n])
            vals[mask] += 1
        # FWHT independently of closed form.
        for b in range(n):
            step = 1 << b
            for k in range(0, 1 << n, 2 * step):
                for j in range(step):
                    a, c = vals[k + j], vals[k + j + step]
                    vals[k + j], vals[k + j + step] = a + c, a - c
        eu = eulerian_rows(n)
        observed = {mask for mask, v in enumerate(vals) if v != 0}
        matching_masks = matchings_support(n)
        assert observed == matching_masks, (n, observed ^ matching_masks)
        checks += 1
        fib0, fib1 = 0, 1
        for _ in range(n):
            fib0, fib1 = fib1, fib0 + fib1
        # F_(n-1)+F_(n+1) = 2F_(n+1)-F_n
        lucas = 2 * fib1 - fib0
        assert len(observed) == lucas - (n % 2 == 0), n
        checks += 1
        cyc = [2,1,-1,-2,-1,1][n % 6]
        parity_correction = ((-1)**(n // 2)) if n % 2 == 0 else 0
        signed_rank = cyc - parity_correction
        assert sum(1 if v > 0 else -1 if v < 0 else 0 for v in vals) == signed_rank
        checks += 1
        for mask, v in enumerate(vals):
            assert full_formula(n, mask, eu) == v, (n, mask, v, full_formula(n, mask, eu))
            if v != 0:
                assert (1 if v > 0 else -1) == (-1)**(mask.bit_count()//2), (n, mask)
                checks += 1
            checks += 1
    for n in range(3, 41):
        eu = eulerian_rows(n)
        for m in range(1, n + 1):
            a = signed_eulerian(eu[m])
            assert (a != 0) == (m % 2 == 1), (m, a)
            checks += 1
        assert full_formula(n, (1 << n) - 1, eu) == -n * signed_eulerian(eu[n - 1])
        checks += 1
    print(f"PASS: {checks} exact assertions, full permutation/FWHT for n=3..9")

if __name__ == '__main__':
    test()
