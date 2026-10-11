#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, parts - 1, prefix + (x,))


def gap_counts(order, n, m):
    pos = {label: i for i, label in enumerate(order)}
    cpos = sorted(pos[f"C{i}"] for i in range(n))
    out = [0] * (n + 1)
    for j in range(m):
        p = pos[f"F{j}"]
        g = sum(cp < p for cp in cpos)
        out[g] += 1
    return tuple(out)


def dm_pmf(k, a):
    m = sum(k)
    A = sum(a)
    num = factorial(m) * factorial(A - 1)
    den = factorial(A + m - 1)
    for kh, ah in zip(k, a):
        num *= factorial(ah + kh - 1)
        den *= factorial(kh) * factorial(ah - 1)
    return Fraction(num, den)


def band_dp(n, m, lower, upper):
    prev = [0] * (m + 1)
    prev[0] = 1
    for b in range(n):
        pref = []
        run = 0
        for v in prev:
            run += v
            pref.append(run)
        cur = [0] * (m + 1)
        for s in range(m + 1):
            if lower[b] <= s <= upper[b]:
                cur[s] = pref[s]
        prev = cur
    return sum(prev)


def main():
    n, m = 4, 3
    labels = tuple(f"C{i}" for i in range(n)) + tuple(f"F{j}" for j in range(m))
    counts = {}
    for order in permutations(labels):
        k = gap_counts(order, n, m)
        counts[k] = counts.get(k, 0) + 1
    expected_patterns = comb(n + m, n)
    assert len(counts) == expected_patterns
    expected_each = factorial(n) * factorial(m)
    assert set(counts.values()) == {expected_each}
    assert sum(counts.values()) == factorial(n + m)

    # Aggregate fine gaps into blocks cut at calibration ranks b=(1,3).
    # The block sizes in calibration-gap units are a=(1,2,2).
    agg = {}
    for k, multiplicity in counts.items():
        q = (k[0], k[1] + k[2], k[3] + k[4])
        agg[q] = agg.get(q, 0) + multiplicity
    total = factorial(n + m)
    for q, multiplicity in agg.items():
        assert Fraction(multiplicity, total) == dm_pmf(q, (1, 2, 2))

    # Exact means and covariance for empirical coverages at b=1 and b=3.
    vals = []
    for q, multiplicity in agg.items():
        c1 = Fraction(q[0], m)
        c3 = Fraction(q[0] + q[1], m)
        p = Fraction(multiplicity, total)
        vals.append((p, c1, c3))
    e1 = sum(p*x for p,x,y in vals)
    e3 = sum(p*y for p,x,y in vals)
    cov = sum(p*(x-e1)*(y-e3) for p,x,y in vals)
    assert e1 == Fraction(1,5)
    assert e3 == Fraction(3,5)
    formula = Fraction(m+n+1, m*(n+2)) * Fraction(1,5) * Fraction(2,5)
    assert cov == formula == Fraction(8,225)

    # Prefix-band DP versus brute-force weak-composition enumeration.
    n2, m2 = 4, 5
    lower = (0, 1, 2, 2)
    upper = (2, 3, 4, 5)
    brute = 0
    for k in compositions(m2, n2 + 1):
        pref = 0
        ok = True
        for b in range(n2):
            pref += k[b]
            if not (lower[b] <= pref <= upper[b]):
                ok = False
                break
        brute += int(ok)
    dp = band_dp(n2, m2, lower, upper)
    assert dp == brute
    assert 0 < dp < comb(m2+n2, n2)

    print("VERIFY_OK")
    print(f"fine_compositions={len(counts)} each_labeled_orders={expected_each}")
    print(f"aggregated_states={len(agg)} covariance={cov}")
    print(f"band_count={dp}/{comb(m2+n2,n2)}")


if __name__ == "__main__":
    main()
