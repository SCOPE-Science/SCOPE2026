"""Independent finite checks for exact additive energy of dyadic norm-one circles.

Requires Python 3 standard library. Prints DYADIC_CIRCLE_ENERGY_CHECK_PASS on success.
"""
from collections import Counter


def circle(k):
    mod = 1 << k
    return [(a, b) for a in range(mod) for b in range(mod)
            if (a*a + b*b - 1) % mod == 0]


def predicted(k):
    return 3*(k-2)*(1 << (2*k+3))


def direct_energy(k):
    mod = 1 << k
    pts = circle(k)
    r = Counter(((a+c) % mod, (b+d) % mod)
                for a, b in pts for c, d in pts)
    return len(pts), sum(n*n for n in r.values())


def mul(p, q, mod):
    return ((p[0]*q[0]-p[1]*q[1]) % mod,
            (p[0]*q[1]+p[1]*q[0]) % mod)


def phase(j, z, mod):
    den = (1+4*z*z) % mod
    inv = pow(den, -1, mod)
    x = ((1-4*z*z)*inv) % mod
    y = (4*z*inv) % mod
    for _ in range(j):
        x, y = (-y) % mod, x
    return x, y


def pair_count_by_angles(k):
    mod = 1 << (k-1)
    n = k-3
    params = list(range(1 << n))
    pts = [[phase(j, a, mod) for a in params] for j in range(4)]
    count = 0
    table = {}
    for j in range(4):
        for l in range(4):
            cur = 0
            for s in pts[j]:
                for w in pts[l]:
                    product = mul(((s[0]-1) % mod, s[1]),
                                  ((w[0]-1) % mod, w[1]), mod)
                    cur += (product[0] == 0)
            table[(j,l)] = cur
            count += cur
    return count, table


def predicted_angle_count(k):
    n = k-3
    return 6*(n+1)*(1 << n)


def check():
    for k in range(4, 10):
        pcount, energy = direct_energy(k)
        assert pcount == (1 << (k+1)), (k, pcount)
        assert energy == predicted(k), (k, energy, predicted(k))
        angles, table = pair_count_by_angles(k)
        assert angles == predicted_angle_count(k), (k, angles)
        assert energy == pcount*16*angles, (k, energy, angles)
        for (j,l), cnt in table.items():
            if (j,l) not in {(0,0),(0,1),(1,0),(0,2),(2,0),
                            (0,3),(3,0),(1,1),(3,3)}:
                assert cnt == 0, (k, j, l, cnt)
        print(f'k={k}: circle={pcount}, energy={energy}, angle_count={angles}, verified')
    print('DYADIC_CIRCLE_ENERGY_CHECK_PASS')

if __name__ == '__main__':
    check()
