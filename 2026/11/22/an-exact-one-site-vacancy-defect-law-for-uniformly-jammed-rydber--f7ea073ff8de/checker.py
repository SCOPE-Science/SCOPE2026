"""Standalone finite-ring combinatorial verification of one inactive site in a blockade array.

Run with Python 3.10+: python checker.py. Only standard library is used.
This is finite evidence supplementing, not replacing, the analytic thermodynamic proof.
"""
from collections import Counter
from functools import lru_cache
from math import exp, log

@lru_cache(maxsize=None)
def compositions(total, parts, b):
    if parts == 0:
        return int(total == 0)
    return sum(compositions(total - d, parts - 1, b)
               for d in range(b + 1, 2 * b + 2) if total >= d)


def enumerate_ring(b, length):
    intact, inactive, old_inactive, extra = (Counter() for _ in range(4))
    for state in range(1, 1 << length):
        chosen = [i for i in range(length) if state & (1 << i)]
        k = len(chosen)
        gaps = [(chosen[(j + 1) % k] - chosen[j]) % length for j in range(k)]
        if k == 1:
            gaps = [length]
        if any(d < b + 1 for d in gaps):
            continue
        def covered(j):
            return any(min((j - i) % length, (i - j) % length) <= b for i in chosen)
        is_intact = all(covered(j) for j in range(length))
        is_inactive = 0 not in chosen and all(covered(j) for j in range(1, length))
        if is_intact:
            intact[k] += 1
            if 0 not in chosen:
                old_inactive[k] += 1
        if is_inactive:
            inactive[k] += 1
            if not is_intact:
                extra[k] += 1
    return intact, inactive, old_inactive, extra


def check_exact(b, length):
    orig, defect, old, exceptional = enumerate_ring(b, length)
    count = 0
    for k in range(1, length + 1):
        c = compositions(length, k, b)
        predicted_original = length * c // k
        assert length * c % k == 0, ('cyclic count integrality', b, length, k)
        assert orig[k] == predicted_original, ('original', b, length, k)
        assert old[k] * length == orig[k] * (length - k), ('vacant exclusion', b, length, k)
        predicted_extra = compositions(length - 2 * b - 2, k - 1, b)
        assert exceptional[k] == predicted_extra, ('extra', b, length, k)
        assert defect[k] == old[k] + exceptional[k], ('defect partition', b, length, k)
        count += 5
    for y in (1, 2, 3):
        actual = sum(y**k * v for k, v in defect.items())
        expected = sum(y**k * (old[k] + exceptional[k]) for k in range(1, length + 1))
        assert actual == expected
        count += 1
    return count


def root_and_density(b):
    low, high = 0.0, 1.0
    for _ in range(90):
        z = (low + high) / 2
        mass = sum(z**d for d in range(b + 1, 2 * b + 2))
        if mass < 1:
            low = z
        else:
            high = z
    z = (low + high) / 2
    rho = 1 / sum(d * z**d for d in range(b + 1, 2 * b + 2))
    P = rho * z ** (2 * b + 2) / (1 - rho + rho * z ** (2 * b + 2))
    assert 0 < P < 1 and 0 < rho < 1
    return z, rho, P


def main():
    assertions = 0
    cases = 0
    for b, lengths in ((1, range(9, 18)), (2, range(13, 18)), (3, range(17, 19))):
        for length in lengths:
            assertions += check_exact(b, length)
            cases += 1
    for b in (1, 2, 3, 4, 8, 16, 32, 100, 1000):
        z, rho, p = root_and_density(b)
        assert 0 < z < 1 and 0 < p < rho
        assertions += 1
        if b == 1:
            assert abs(z - 0.7548776662466927) < 1e-12
            assertions += 1
    # Illustrative slow convergence of the rigorous large-blockade logarithmic law.
    z, rho, p = root_and_density(1000)
    scaled = p * 1000**3 / log(1000)**2
    assert 0.2 < scaled < 2
    assertions += 1
    print(f'PASS: {cases} exhaustive ring sizes, {assertions} assertions')
    for b in (1, 2, 3, 8, 100):
        z, rho, p = root_and_density(b)
        print(f'b={b}: z={z:.12f}, density={rho:.12f}, anomalous-gap chance={p:.12g}')

if __name__ == '__main__':
    main()
