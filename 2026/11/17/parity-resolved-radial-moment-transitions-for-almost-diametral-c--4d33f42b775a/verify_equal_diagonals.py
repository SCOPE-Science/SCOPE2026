"""Independent finite checks for the equal-span polygon-diagonal radial law.

Uses only Python's standard library.  Run: python3 verify_equal_diagonals.py
"""
import math
from collections import Counter

CHECKS = 0

def check(condition, detail):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail)


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def intersection_strict(a, b, c, d):
    u = (b[0] - a[0], b[1] - a[1])
    v = (d[0] - c[0], d[1] - c[1])
    w = (c[0] - a[0], c[1] - a[1])
    den = cross(u, v)
    if abs(den) < 1.e-11:
        return None
    s = cross(w, v) / den
    t = cross(w, u) / den
    if min(s, t, 1 - s, 1 - t) < 1.e-9:
        return None
    return (a[0] + s * u[0], a[1] + s * u[1])


def exact_radii(n, k):
    delta = n / 2 - k
    return [math.sin(math.pi * delta / n) /
            math.sin(math.pi * (delta + ell) / n)
            for ell in range(1, k)]


def moments(n, k, q):
    z = exact_radii(n, k)
    return sum(v ** q for v in z) / len(z)


def qlimit(n, delta, q):
    if q < 1:
        from math import gamma
        beta = gamma((1 - q) / 2) * gamma(0.5) / gamma(1 - q / 2)
        return math.pi ** (q - 1) * delta ** q * beta
    if q > 1:
        return 2 * delta ** q * sum((delta + j) ** (-q) for j in range(1, 60000))
    return 2 * delta


def run():
    for n in range(5, 60):
        pts = [(math.cos(2*math.pi*j/n), math.sin(2*math.pi*j/n))
               for j in range(n)]
        for k in range(2, (n - 1)//2 + 1 if n % 2 else n//2):
            d = n/2-k
            crossings = []
            for j in range(1, n):
                z = intersection_strict(pts[0], pts[k], pts[j], pts[(j+k) % n])
                if z is not None:
                    crossings.append((j, math.hypot(*z)))
            check(len(crossings) == 2*(k-1), ('count', n, k))
            check(set(j for j, _ in crossings) ==
                  set(range(1, k)) | set(range(n-k+1, n)), ('indices', n, k))
            seen = Counter()
            for j, r in crossings:
                jj = min(j, n-j)
                ell = k-jj
                expected = exact_radii(n, k)[ell - 1]
                check(abs(r - expected) < 1.e-9, ('radial', n, k, j, r, expected))
                seen[ell] += 1
            check(all(seen[ell] == 2 for ell in range(1, k)), ('multiplicity',n,k))
            check(abs(sum(r for _, r in crossings)/len(crossings) - moments(n,k,1))
                  < 1.e-10, ('mean',n,k))
    # Check finite-to-asymptotic scaling in both parity classes.
    for delta in (0.5, 1., 1.5, 2.):
        for n in (3001, 9001, 30001) if delta % 1 else (3000, 9000, 30000):
            k = int(n/2 - delta)
            for q, tolerance in ((0.25,0.017),(0.5,0.075),(2.,0.035),(3.,0.035)):
                val = moments(n,k,q)
                scaled = n**q * val if q<1 else n*val
                target = qlimit(n,delta,q)
                check(abs(scaled/target-1) < tolerance, ('moment regime',n,delta,q,scaled,target))
            v = n*moments(n,k,1)/math.log(n)
            check(abs(v/(2*delta)-1) < 0.25, ('critical',n,delta,v))
            # Macroscopic staircase, evaluated away from thresholds.
            for r in (0.11, 0.22, 0.37):
                count = sum(r0 >= r for r0 in exact_radii(n,k))
                expected = max(0, int(math.floor(delta/r-delta)))
                check(count == expected, ('rare tail',n,delta,r,count,expected))
    print('PASS: {} independent finite assertions'.format(CHECKS))

if __name__ == '__main__':
    run()
