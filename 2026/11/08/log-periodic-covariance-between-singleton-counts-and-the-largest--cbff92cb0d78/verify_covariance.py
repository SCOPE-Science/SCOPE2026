"""Reproduce finite covariance identities and diagnostic asymptotics for uniform compositions.
The infinite asymptotic theorem is established analytically, not by these checks.
"""
from fractions import Fraction
from math import exp, log, log2

checks = 0


def assert_equal(left, right):
    global checks
    assert left == right, (left, right)
    checks += 1


def counts(n, m):
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    a[0] = 1
    for t in range(1, n + 1):
        for j in range(1, min(m, t) + 1):
            a[t] += a[t-j]
            b[t] += b[t-j]
        b[t] += a[t-1]
    return a[n], b[n]


def stats(n):
    n_comp = 1 << (n-1)
    total_s = total_m = total_sm = 0
    cdf_counts = [(0, 0) for _ in range(n + 1)]
    for bits in range(n_comp):
        parts = []
        run = 1
        for j in range(n-1):
            if (bits >> j) & 1:
                parts.append(run)
                run = 1
            else:
                run += 1
        parts.append(run)
        s = sum(x == 1 for x in parts)
        m = max(parts)
        total_s += s
        total_m += m
        total_sm += s*m
        for cutoff in range(m, n+1):
            a, b = cdf_counts[cutoff]
            cdf_counts[cutoff] = a+1, b+s
    covariance = Fraction(total_sm, n_comp) - Fraction(total_s*total_m, n_comp*n_comp)
    return total_s, total_m, covariance, cdf_counts


for n in range(2, 15):
    s, msum, observed_cov, cumul = stats(n)
    assert_equal(Fraction(s, 1 << (n-1)), Fraction(n+2, 4))
    calculated_cov = Fraction(0)
    for m in range(1, n):
        a, b = counts(n, m)
        assert_equal((a,b), cumul[m])
        increment = Fraction(4*b-(n+2)*a, 4*(1 << (n-1)))
        assert increment >= 0
        checks += 1
        calculated_cov -= increment
    assert_equal(calculated_cov, observed_cov)
    assert observed_cov < 0
    checks += 1


def approx(n, mmax=40):
    total = 0.0
    for m in range(1, mmax+1):
        weights = [2.0**(-j) for j in range(1,m+1)]
        a = [0.0]*(n+1)
        b = [0.0]*(n+1)
        a[0] = 1.0
        for t in range(1,n+1):
            aa = 0.0
            bb = 0.5*a[t-1]
            for j in range(1,min(m,t)+1):
                aa += weights[j-1]*a[t-j]
                bb += weights[j-1]*b[t-j]
            a[t] = aa
            b[t] = bb
        total += 2.0*((n+2)/4*a[n] - b[n])
    return total

errors=[]
for n in (256,512,1024,2048,4096):
    exact_numeric = approx(n)
    poisson_sum = -sum(m * (n * 2.0**(-m-1)) * exp(-n*2.0**(-m-1)) for m in range(1, 80))/4
    diff = abs(exact_numeric-poisson_sum)
    errors.append(diff)
    print(f"n={n}, covariance={exact_numeric:.10f}, expansion={poisson_sum:.10f}, difference={diff:.5g}")
assert all(errors[i+1] < errors[i] for i in range(len(errors)-1))
checks += len(errors)-1

# Nonconstancy may be verified analytically by the Gamma integral; these
# numerical values only test the coefficient's normalization.
phi0 = sum(2.0**(-j-1) * exp(-2.0**(-j-1)) for j in range(-35, 35))
assert abs(phi0 - 1/log(2)) < 0.0001
checks += 1
print("PASSED",checks,"finite assertions")
