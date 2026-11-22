#!/usr/bin/env python3
"""Exact finite-field check of the exterior tangent-contact theorem.

No nonstandard libraries are required.  All field arithmetic and all
projective points are explicitly enumerated.  Exhaustion checks selected
fields; the unrestricted theorem has a separate symbolic proof.
"""
from collections import Counter


class Field:
    def __init__(self, p, extension=1):
        self.p, self.extension = p, extension
        self.q = p ** extension
        assert extension in (1, 2)
        if extension == 2:
            self.d = next(d for d in range(2, p)
                          if pow(d, (p - 1) // 2, p) == p - 1)
        self.a = [[0] * self.q for _ in range(self.q)]
        self.m = [[0] * self.q for _ in range(self.q)]
        for x in range(self.q):
            for y in range(self.q):
                if extension == 1:
                    self.a[x][y] = (x + y) % p
                    self.m[x][y] = x * y % p
                else:
                    x0, x1 = x % p, x // p
                    y0, y1 = y % p, y // p
                    self.a[x][y] = (x0 + y0) % p + p * ((x1 + y1) % p)
                    self.m[x][y] = ((x0 * y0 + self.d * x1 * y1) % p
                                    + p * ((x0 * y1 + x1 * y0) % p))
        self.zero, self.one = 0, 1
        self.neg = [next(y for y in range(self.q)
                         if self.a[x][y] == 0) for x in range(self.q)]
        self.inv = [0] * self.q
        for x in range(1, self.q):
            self.inv[x] = next(y for y in range(1, self.q)
                               if self.m[x][y] == 1)
        self.three = 3

    def add(self, x, y):
        return self.a[x][y]

    def sub(self, x, y):
        return self.a[x][self.neg[y]]

    def mul(self, x, y):
        return self.m[x][y]

    def pow(self, x, n):
        z = 1
        while n:
            if n & 1:
                z = self.m[z][x]
            x = self.m[x][x]
            n >>= 1
        return z

    def chi(self, x):
        return 0 if x == 0 else (1 if self.pow(x, (self.q - 1) // 2) == 1 else -1)


def projective_points(field):
    q = field.q
    return ([(1, a, b) for a in range(q) for b in range(q)]
            + [(0, 1, b) for b in range(q)] + [(0, 0, 1)])


def check(p, ext=1):
    k = Field(p, ext)
    q, a, m = k.q, k.a, k.m
    pts = projective_points(k)
    assert len(pts) == q*q+q+1
    center = (1, 1, 1)
    smooth, exterior = [], []
    for x, y, z in pts:
        s = a[a[x][y]][z]
        if x and y and z and s and (x, y, z) != center:
            smooth.append((x, y, z, s))
        else:
            exterior.append((x, y, z, s))
    assert len(smooth) == (q-1)*(q-2)
    assert len(exterior) == 4*q-1

    grad = []
    for x, y, z, s in smooth:
        c = m[3][k.inv[s]]
        grad.append((k.sub(k.inv[x], c),
                     k.sub(k.inv[y], c),
                     k.sub(k.inv[z], c)))
    assert all(g != (0, 0, 0) for g in grad)

    e = k.chi(k.neg[3])
    expected_hist = Counter({q-5: 2*(q-6-e),
                             q-4: 4*(1+e),
                             q-3: 2*q+6-2*e})
    expected_hist[q-6-e] += 1
    expected_hist = +expected_hist
    observed_hist = Counter()

    for x, y, z, s in exterior:
        if (x, y, z) == center:
            expected = q-6-e
        elif [x, y, z, s].count(0) >= 2:
            expected = q-3
        elif s:  # Exactly one coordinate vanishes.
            nonzero = [t for t in (x, y, z) if t]
            t = m[nonzero[0]][k.inv[s]]
            d = a[k.sub(m[t][t], t)][1]
            expected = q-4-k.chi(d)
        else:  # Coordinate sum zero and all coordinates nonzero.
            t = m[x][k.inv[y]]
            d = a[a[m[t][t]][t]][1]
            expected = q-4-k.chi(d)

        found = 0
        for gx, gy, gz in grad:
            if a[a[m[gx][x]][m[gy][y]]][m[gz][z]] == 0:
                found += 1
        assert found == expected, (q, (x, y, z), found, expected)
        observed_hist[found] += 1
    assert observed_hist == expected_hist, (q, observed_hist, expected_hist)
    assert min(observed_hist) == (0 if q in (5,7) else
                                  min(q-6-e,q-5 if 2*(q-6-e) else q-3))
    print(f'F_{q}: smooth={len(smooth)}, exterior={len(exterior)}, '
          f'chi(-3)={e}, histogram={sorted(observed_hist.items())}: PASS')


if __name__ == '__main__':
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        check(p)
    for p in (5, 7, 11):
        check(p, 2)
    print('ALL_EXTERIOR_TANGENT_CONTACT_TESTS_PASSED')
