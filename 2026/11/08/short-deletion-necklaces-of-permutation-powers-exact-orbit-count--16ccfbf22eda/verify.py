"""Independent finite checks for cyclic deletion-mask orbit formula.
Uses only Python standard library; no external data. Not an infinite proof.
"""
from itertools import combinations
from math import comb, gcd


def phi(d):
    return sum(gcd(i, d) == 1 for i in range(1, d + 1))


def formula(q, k, t):
    total = sum(phi(d) * comb(q*k//d, t//d)
                for d in range(1, gcd(k, t) + 1)
                if gcd(k, d) == d and t % d == 0)
    # gcd(k,t) divisor computation below has exact divisors
    assert total % k == 0
    return total // k - (q - 1 if t == q else 0)


def necklace(seq):
    return min(tuple(seq[i:] + seq[:i]) for i in range(len(seq)))


def mask_orbit(mask, q, k):
    n = q*k
    return min(tuple(sorted((j + s*q) % n for j in mask)) for s in range(k))


def verify(q, k, t):
    n = q*k
    src = tuple(range(q)) * k
    outputs = {}
    for removed in combinations(range(n), t):
        rem = set(removed)
        result = tuple(src[j] for j in range(n) if j not in rem)
        canon = necklace(result)
        morbit = mask_orbit(removed, q, k)
        outputs.setdefault(canon, set()).add(morbit)
    orbits = set().union(*outputs.values())
    expected = formula(q, k, t)
    assert len(outputs) == expected, (q, k, t, len(outputs), expected)
    assert len(orbits) == expected + (q - 1 if t == q else 0)
    if t < q:
        assert all(len(mask_orbits) == 1 for mask_orbits in outputs.values())
    else:
        special = necklace(tuple(range(q)) * (k - 1))
        assert len(outputs[special]) == q
        assert all(len(v) == 1 for key, v in outputs.items() if key != special)
    return comb(n,t)


def main():
    configurations = 0
    masks = 0
    for q in range(2, 7):
        for k in range(2, 5):
            for t in range(q + 1):
                configurations += 1
                masks += verify(q, k, t)
    print(f'PASS configurations={configurations} deletion_masks={masks}')

if __name__ == '__main__':
    main()
