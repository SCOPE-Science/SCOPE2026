"""Reproducible numerical and exact-rational checks of the two-phase blur theorem.

Uses only the Python standard library. These finite checks illustrate and stress-test,
but do not replace the all-size Fourier proof in RESULT.md.
"""
from fractions import Fraction
from math import cos, sin, pi, sqrt
from random import Random


def leading_sigma(p, q, theta):
    a, d = 1 - p, 1 - q
    trace = a*a + d*d + p*p + q*q
    det = (a*d)**2 + (p*q)**2 - 2*a*d*p*q*cos(theta)
    return sqrt(max(0.0, (trace + sqrt(max(0.0, trace*trace - 4*det)))/2))


def gain(m, p, q):
    g0 = sqrt(((1 - 2*p)**2 + (1 - 2*q)**2)/2)
    return max(g0, leading_sigma(p, q, 2*pi/m))


def apply(m, p, q, x):
    return [((1 - (p if j % 2 == 0 else q))*x[j]
             + (p if j % 2 == 0 else q)*x[(j + 1) % (2*m)])
            for j in range(2*m)]


def norm(x):
    return sqrt(sum(t*t for t in x))


def power_gain(m, p, q, trials=4000):
    # Power iteration for the singular norm of P restricted to mean-zero vectors.
    rng = Random(m * 997 + round(p * 1000) + round(q * 100000))
    x = [rng.gauss(0, 1) for _ in range(2*m)]
    x = [a - sum(x)/(2*m) for a in x]
    for _ in range(trials):
        y = apply(m,p,q,x)
        z = [(1-(p if j%2==0 else q))*y[j]
             + (q if j%2==0 else p)*y[(j-1)%(2*m)]
             for j in range(2*m)] # this adjacency formula is P transpose
        mu = sum(z)/(2*m)
        z = [a-mu for a in z]
        r = norm(z)
        if r < 1e-15:
            return 0.0
        x = [a/r for a in z]
    return norm(apply(m,p,q,x))/norm(x)


def main():
    checks = 0
    for ip in range(1, 10):
      for iq in range(1, 10):
        p, q = Fraction(ip, 10), Fraction(iq, 10)
        for ic in [-1, Fraction(-1,2), 0, Fraction(1,2), 1]:
            a,d = 1-p, 1-q
            T = a*a + p*p + q*q + d*d
            Delta = (a*d)**2 + (p*q)**2 - 2*a*d*p*q*ic
            left = 1 - T + Delta
            right = 2*p*q*a*d*(1-ic) - (p-q)**2
            assert left == right
            checks += 1
    for m in range(2, 13):
      for ip,iq in [(2,8), (4,6), (3,3), (7,4), (1,9), (5,6)]:
        p,q=ip/10,iq/10
        analytic=gain(m,p,q)
        estimate=power_gain(m,p,q,1600)
        assert abs(analytic-estimate)<6e-4, (m,p,q,analytic,estimate)
        threshold = 2*sqrt(p*q*(1-p)*(1-q))*sin(pi/m)
        expected = 1 if abs(p-q)>threshold+1e-12 else -1
        actual = 1 if analytic>1+1e-12 else -1
        assert expected==actual, (m,p,q,analytic,threshold)
        checks += 2
    assert gain(7,0.4,0.6)<1<gain(8,0.4,0.6)
    checks += 1
    print('VERIFY_OK', checks, 'checks: exact-rational Gram identity, finite-mode spectral gains, phase boundaries')

if __name__ == '__main__':
    main()
