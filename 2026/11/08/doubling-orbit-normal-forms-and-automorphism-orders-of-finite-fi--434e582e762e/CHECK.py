"""Exact modular checks for weighted permutation evolution algebras.

Run: python CHECK.py
Only arithmetic of the cyclic group of nonzero field elements is required.
"""
from collections import defaultdict
from itertools import permutations, product
from math import gcd, factorial


def cycles(sigma):
    n = len(sigma)
    seen = set()
    ans = []
    for i in range(n):
        if i not in seen:
            c = []
            k = i
            while k not in seen:
                seen.add(k)
                c.append(k)
                k = sigma[k]
            assert k == i
            ans.append(c)
    return ans


def key(sigma, weights, field_size):
    m = field_size - 1
    typ = []
    for c in cycles(sigma):
        ell = len(c)
        d = gcd(m, 2 ** ell - 1)
        a = sum((2 ** (ell - 1 - j)) * weights[c[j]] for j in range(ell)) % d
        typ.append((ell, min((pow(2, t, d) * a) % d for t in range(ell))))
    return tuple(sorted(typ))


def predicted_aut(sigma, weights, field_size):
    m = field_size - 1
    cnt = defaultdict(int)
    for c in cycles(sigma):
        ell = len(c)
        d = gcd(m, 2 ** ell - 1)
        a = sum((2 ** (ell - 1 - j)) * weights[c[j]] for j in range(ell)) % d
        h = next(h for h in range(1, ell + 1) if (pow(2, h, d) * a) % d == a)
        assert ell % h == 0
        cnt[(ell, min((pow(2, t, d) * a) % d for t in range(ell)), h)] += 1
    order = 1
    for (ell, orbit, h), count in cnt.items():
        order *= (gcd(m, 2 ** ell - 1) * ell // h) ** count * factorial(count)
    return order


def mapped(sigma, weights, perm, u, m):
    n = len(sigma)
    new_sigma = [None] * n
    new_weights = [None] * n
    for i in range(n):
        new_sigma[perm[i]] = perm[sigma[i]]
        new_weights[perm[i]] = (weights[i] + 2 * u[i] - u[sigma[i]]) % m
    return (tuple(new_sigma), tuple(new_weights))


def exhaustive(field_size, n):
    m = field_size - 1
    all_states = set((p, w) for p in permutations(range(n)) for w in product(range(m), repeat=n))
    actions = list(product(list(permutations(range(n))), list(product(range(m), repeat=n))))
    orbit_count = 0
    comparison_count = 0
    while all_states:
        s = min(all_states)
        sigma, weights = s
        orbit = {mapped(sigma, weights, perm, u, m) for perm, u in actions}
        assert orbit <= all_states
        own_key = key(sigma, weights, field_size)
        expected_aut = predicted_aut(sigma, weights, field_size)
        assert len(actions) % len(orbit) == 0
        assert len(actions) // len(orbit) == expected_aut, (field_size, n, s, expected_aut)
        assert all(key(*x, field_size) == own_key for x in orbit)
        all_states.difference_update(orbit)
        orbit_count += 1
        comparison_count += len(orbit)
    print('EXACT_ORBITS', field_size, n, orbit_count, comparison_count)


def necklace_counts():
    for q in (2, 3, 4, 5, 7, 8, 9, 11, 16, 31):
        m = q - 1
        for ell in range(1, 11):
            d = gcd(m, 2**ell - 1)
            act_orbits = set()
            for a in range(d):
                act_orbits.add(tuple(sorted(set((pow(2,t,d)*a) % d for t in range(ell)))))
            count = sum(gcd(d, 2**r-1) for r in range(ell)) // ell
            assert len(act_orbits) == count
        print('NECKLACE', q, 'OK')

if __name__ == '__main__':
    necklace_counts()
    for q,n in ((2,4),(3,4),(4,3),(5,3),(7,3),(8,2),(9,2)):
        exhaustive(q,n)
    print('VERIFY_OK')
