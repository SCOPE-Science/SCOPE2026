"""Numerical corroboration of the sharp coordinate-max stability formula
for Euclidean projection onto a scaled circular cone. Standard library only.
The unrestricted theorem is proved analytically in RESULT.md.
"""
import math
import random


def projection(z, k):
    t, *x = z
    r = math.sqrt(sum(v * v for v in x))
    if t >= k * r:
        return z[:]
    if t <= -r / k:
        return [0.0] * len(z)
    rho = (k * t + r) / (1.0 + k * k)
    return [k * rho] + [rho * v / r for v in x]


def jacobian(k, u, c):
    d = len(u)
    den = 1.0 + k * k
    return [[k * k / den] + [k * v / den for v in u]] + [
        [k * u[i] / den] + [
            (c if i == j else 0.0) + (1.0 / den - c) * u[i] * u[j]
            for j in range(d)
        ] for i in range(d)
    ]


def max_row_sum(m):
    return max(sum(abs(v) for v in row) for row in m)


def optval(func):
    n = 800
    arr = [func(i / n) for i in range(n + 1)]
    best = max(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1] or arr[i] < arr[i + 1]:
            continue
        lo, hi = (i - 1) / n, (i + 1) / n
        for _ in range(65):
            a = lo + (hi - lo) * 0.3819660112501051
            b = hi - (hi - lo) * 0.3819660112501051
            if func(a) > func(b):
                hi = b
            else:
                lo = a
        best = max(best, func((lo + hi) / 2))
    return best


def branches(k, d):
    assert d >= 2 and k > 0
    den = 1 + k*k
    w = math.sqrt(d-1)
    a = (k*k + k*math.sqrt(d))/den
    polar = optval(lambda v:(k*v + v*v + w*v*math.sqrt(max(0.0,1-v*v)))/den)
    cone = 1 + optval(lambda v:(k*v-k*k*v*v + k*k*w*v*math.sqrt(max(0.0,1-v*v)))/den)
    return a, polar, cone


def run():
    rng = random.Random(240117)
    tests = 0
    for d in (2, 3, 4, 5, 6, 12, 30):
        for k in (.2, .5, 1., 2., 4.):
            A, Bm, Bp = branches(k,d)
            bound = max(1., A, Bm, Bp)
            for _ in range(150):
                x = [rng.uniform(-1,1) for _ in range(d)]
                norm = math.sqrt(sum(v*v for v in x))
                u = [v/norm for v in x]
                c = rng.uniform(.05,.95)
                t = ((1+k*k)*c-1)*norm/k
                z = [t]+x
                j = jacobian(k,u,c)
                assert max_row_sum(j) <= bound + 1e-10
                direction = [rng.uniform(-1,1) for _ in range(d+1)]
                eps = 1e-6
                f = projection(z,k)
                g = projection([a+eps*b for a,b in zip(z,direction)],k)
                for i in range(d+1):
                    linear = sum(j[i][a]*direction[a] for a in range(d+1))
                    assert abs((g[i]-f[i])/eps-linear) < 2e-4, (d,k,i)
                tests += 1
            if d==4 and k==1.:
                assert abs(bound-1.5416233) < 3e-5
    print('MIDDLE_JACOBIAN_AND_GLOBAL_ROW_BOUNDS_PASS', tests)
    for k in (.2, .35, .75, 1., 1.5, 3., 5.):
        coeff = max(.5,k,.5*k*k)/(1+k*k)
        vals = []
        for d in (300, 1200, 5000):
            v = max(1.,*branches(k,d))/math.sqrt(d)
            vals.append(abs(v-coeff))
        assert vals[2] < vals[0] and vals[2] < .03, (k, vals)
    print('THREE_APERTURE_REGIMES_ASYMPTOTIC_CHECKS_PASS')
    for k,expected in ((.2,1),(.75,0),(3.,2)):
        vals = branches(k,2000)
        assert vals.index(max(vals)) == expected,(k,vals)
    print('THREE_DISTINCT_EVENTUAL_ACTIVE_ROW_BRANCHES_PASS')
    print('ALL_SCALED_CONE_PROJECTION_CHECKS_PASS')

if __name__ == '__main__':
    run()
