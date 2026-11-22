"""Diagnostics for the Poisson quorum allocation theorem (Python standard library)."""
import math
import random


def tail(r, x):
    """Poisson(x) survival at r, avoiding subtraction cancellation near zero."""
    if x == 0:
        return 0.0
    if x < 15 and r < 18:
        p = math.exp(-x) * x**r / math.factorial(r)
        s = p
        for j in range(r + 1, r + 240):
            p *= x / j
            s += p
            if p < 1e-18 * max(s, 1e-200):
                break
        return min(1.0, s)
    k = math.exp(-x)
    s = k
    for j in range(1, r):
        k *= x / j
        s += k
    return max(0.0, 1.0 - s)


def derivative(r, x):
    if x <= 0:
        return 0.0
    return math.exp(-x + (r-1)*math.log(x)-math.lgamma(r))


def halfsplit_benchmark(r, s, x):
    return max(tail(r, s), 2 * tail(r, s / 2)) - tail(r, x) - tail(r, s - x)


def bisect(f, left, right):
    fl, fr = f(left), f(right)
    assert fl * fr < 0, (left, right, fl, fr)
    for _ in range(92):
        mid = (left + right) / 2
        if (f(mid) > 0) == (fl > 0):
            left, fl = mid, f(mid)
        else:
            right, fr = mid, f(mid)
    return (left + right) / 2


def optimum_density_point(r):
    return bisect(lambda x: x*derivative(r,x)-tail(r,x), float(r-1), float(4*r+10))


def thresholds(r, n):
    a = optimum_density_point(r)
    out = []
    for m in range(1, n):
        f = lambda B: m*tail(r,B/m)-(m+1)*tail(r,B/(m+1))
        B = bisect(f, m*a,(m+1)*a)
        out.append(B)
    return a, out


def check():
    rng = random.Random(731112)
    tests = 0
    # Independent finite probes for the pairwise global extremum lemma.
    for r in range(2, 11):
        for _ in range(1700):
            s = 10**rng.uniform(-1.5,1.7)
            x = s*rng.uniform(0.0001,0.4999)
            assert halfsplit_benchmark(r,s,x) >= -4e-14, (r,s,x)
            tests += 1
    # Numerical monotone-root and strictly adjacent phase checks.
    for r in range(2, 10):
        a, B = thresholds(r, 12)
        assert all(m*a < B[m-1] < (m+1)*a for m in range(1,12))
        assert all(B[j+1] > B[j] for j in range(len(B)-1))
        tests += 22
        criticals = [0.0] + B + [B[-1]*1.5]
        for m in range(1,13):
            budget = (criticals[m-1] + criticals[m])/2
            vals = [j*tail(r,budget/j) for j in range(1,13)]
            assert vals[m-1] > max(vals[:m-1]+vals[m:]) + 1e-9, (r,m,budget,vals)
            tests += 1
        for m in range(1,12):
            budget=B[m-1]
            vals=[j*tail(r,budget/j) for j in range(1,13)]
            assert abs(vals[m-1]-vals[m]) < 4e-12
            assert abs(max(vals)-vals[m]) < 4e-12
            tests += 2
    # Boundary checks: r=1 has uniform full spreading.
    for B in [0.01,0.1,1,3,30]:
        assert 5*(1-math.exp(-B/5)) > 4*(1-math.exp(-B/4))
        tests += 1
    print('PASS',tests,'independent diagnostic assertions')
    for r in [2,3,5]:
        a, B = thresholds(r,5)
        print('r=',r,'a=',format(a,'.10f'),'B1..B4=',[round(x,9) for x in B])

if __name__=='__main__':
    check()
