"""Reproduce finite cyclic-product Fourier and capped-Hamming calculations.

Only the Python standard library is required.  This is a finite corroboration,
not a substitute for the proof of the all-dimension theorem.
"""
from itertools import product
from math import comb, cos, sin, pi, log
from cmath import exp


def critical(n, q):
    assert n >= 4 and q >= 3
    k = ((q - 1) * n + 3) // q
    t = (q - 1) * n - q * k
    return k, t


def krawtchouk(n, q, k):
    t = (q - 1) * n - q * k
    second = (t*t - (q-2)*t - (q-1)*n) // 2
    assert 2*second == t*t - (q-2)*t - (q-1)*n
    return t, second


def eigenvalue(n, q, k, p):
    t, second = krawtchouk(n, q, k)
    return t + second * (2**p) - (1 + t + second) * (3**p)


def critical_exponent(n, q):
    k, _ = critical(n, q)
    low, high = 0.0, 1.0
    assert eigenvalue(n,q,k,low) < 0 < eigenvalue(n,q,k,high)
    for _ in range(72):
        mid = (low + high)/2
        if eigenvalue(n,q,k,mid) > 0: high = mid
        else: low = mid
    return (low+high)/2


def complex_product(roots, frequency, point):
    z = 1+0j
    q = len(roots)
    for a,b in zip(frequency,point):
        z *= roots[(a*b)%q]
    return z


spectral_parameter_cases = 0
for q in range(3, 17):
    for n in range(4, 60):
        k, t = critical(n,q)
        assert -3 <= t <= q-4
        assert 1 <= k <= n
        for p in (0.01, 0.12, 0.35, 0.6, 0.9, 0.999):
            values = [eigenvalue(n,q,i,p) for i in range(1,n+1)]
            assert max(range(n), key=lambda i: values[i]) == k-1, (q,n,p,k)
        root = critical_exponent(n,q)
        assert 0 < root < 1
        assert abs(eigenvalue(n,q,k,root)) < 1e-8
        assert all(eigenvalue(n,q,i,root) < -1e-8 for i in range(1,n+1) if i != k)
        spectral_parameter_cases += 1


# Independent direct character sums on (Z/qZ)^n, using the actual capped
# Hamming kernel rather than Krawtchouk expressions.
direct_characters = 0
for q,n in ((3,4),(4,4),(5,3),(3,5)):
    roots = [exp(2j*pi*t/q) for t in range(q)]
    words = list(product(range(q),repeat=n))
    for frequency in words:
        k = sum(z != 0 for z in frequency)
        if k == 0: continue
        for p in (0.23,0.71):
            direct = sum(min(sum(z != 0 for z in x),3)**p *
                         complex_product(roots,frequency,x)
                         for x in words)
            formula = eigenvalue(n,q,k,p)
            assert abs(direct-formula) < 1e-7, (q,n,frequency,p,direct,formula)
        direct_characters += 1


for q in (3,4,5,7):
    alpha = 2 / ((q-1)*log(3/2))
    for n in (200,400,800):
        k,t = critical(n,q)
        k2zero = (t*t - (q-2)*t)/2
        beta = alpha**2 * (log(3)*(1+t)+log(3/2)*k2zero -(log(3)+log(2))/2)
        root = critical_exponent(n,q)
        # Verify the predicted order-three remainder after two asymptotic terms.
        assert abs(root-(alpha/n+beta/n**2)) * n**3 < 2000

print('QARY_CAP_THREE_NEGATIVE_TYPE_PASS parameter_cases=%d direct_characters=%d' %
      (spectral_parameter_cases,direct_characters))
