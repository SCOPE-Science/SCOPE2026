#!/usr/bin/env python3
"""Exact cyclotomic and orbit-reduced character sums for classical parking functions."""
from itertools import product, combinations_with_replacement
from collections import Counter
from math import factorial
import csv
from pathlib import Path

PHI = {
    2: (1, 1),
    3: (1, 1, 1),
    4: (1, 0, 1),
    5: (1, 1, 1, 1, 1),
    6: (1, -1, 1),
}
EXTRA_FIVE = {
    (1, 2, 3, 3, 4),
    (1, 2, 3, 3, 5),
    (1, 2, 3, 4, 5),
    (1, 3, 3, 4, 5),
    (2, 3, 3, 4, 5),
}
EXPECTED = {1: (0, 0), 2: (2, 0), 3: (15, 0),
            4: (124, 0), 5: (1655, 360)}

def parking(n):
    return tuple(x for x in product(range(n), repeat=n)
                 if all(y <= i for i, y in enumerate(sorted(x))))

def reduce_cyclotomic(counts, m):
    phi = PHI[m]
    deg = len(phi)-1
    coeff = list(counts)
    for k in range(m - 1, deg - 1, -1):
        v = coeff[k]
        for j in range(deg):
            coeff[k - deg + j] -= v * phi[j]
        coeff[k] = 0
    return tuple(coeff[:deg])

def orbit_size(t, m):
    ct = Counter(t)
    num = factorial(len(t))
    for a in ct.values():
        num //= factorial(a)
    return num

def run():
    out = []
    for n in range(1, 6):
        m = n + 1
        pf = parking(n)
        assert len(pf) == m ** (n - 1)
        rows = []
        zeros = extras = 0
        extra_orbits = set()
        for t in combinations_with_replacement(range(m), n):
            counts = [0] * m
            for x in pf:
                counts[sum(a*b for a,b in zip(t,x)) % m] += 1
            red = reduce_cyclotomic(counts, m)
            zero = not any(red)
            forced = (sum(t) % m == 0 and any(t))
            weight = orbit_size(t, m)
            if zero:
                zeros += weight
                if not forced:
                    extras += weight
                    extra_orbits.add(t)
            assert not (forced and not zero), (n,t)
            if n == 5:
                rows.append((*t, weight, *red, int(zero), int(forced)))
        assert (zeros,extras) == EXPECTED[n], (n,zeros,extras)
        if n == 5:
            assert extra_orbits == EXTRA_FIVE, extra_orbits
            assert len(rows) == 252 and sum(z[5] for z in rows) == 6**5
            header = ['k1','k2','k3','k4','k5','orbit_size',
                      'coefficient_of_1','coefficient_of_zeta','is_zero','is_forced']
            with (Path(__file__).resolve().parent / 'parking5_frequency_orbits.csv').open('w',newline='',encoding='utf-8') as f:
                wr=csv.writer(f,lineterminator='\n');wr.writerow(header);wr.writerows(rows)
        out.append((n, m**n, len(pf), m**(n-1)-1, extras, zeros, m**n-zeros))
    print('n ambient parking forced extra total_zero rank')
    for r in out:print(*r)
    print('PARKING_SIXTH_ROOT_FIRST_EXTRA_ZERO_PASS')

if __name__ == '__main__':
    run()
