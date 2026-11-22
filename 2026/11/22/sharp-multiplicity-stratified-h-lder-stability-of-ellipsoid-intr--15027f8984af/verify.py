"""Reproducible finite checks for ellipsoid intrinsic-volume inverse stability.
Standard-library Python 3 only. The mathematical uniform and sharp-exponent
statements require the separate analytic proof, not finite tests.
"""
import math
from fractions import Fraction


def elementary(lam):
    a = [1.0] + [0.0] * len(lam)
    for x in lam:
        for k in range(len(lam), 0, -1):
            a[k] += x * a[k - 1]
    return a


def normalized_intrinsic(lam, k, intervals=8192):
    n = len(lam)
    s = elementary(lam)

    def integrand(z):
        if z <= 0:
            return s[1] if k == 1 else 0.0
        if z >= 1:
            return 0.0
        u = (z / (1.0-z)) ** 2
        q = sum(s[j] * (u ** j) for j in range(n + 1))
        # The cross-sum representation avoids subtracting close polynomials.
        num = sum((b-a) * s[a] * s[b] * u ** (a+b-1)
                  for a in range(k) for b in range(k, n+1))
        du = 2.0 * z / ((1.0-z) ** 3)
        return 0.5 * (u ** (-k / 2.0)) * num * du / q ** 1.5

    h = 1.0 / intervals
    total = integrand(0.0) + integrand(1.0)
    for j in range(1, intervals):
        total += (4 if j % 2 else 2) * integrand(j * h)
    return total * h / 3.0


def main():
    tests = 0
    def check(x, label):
        nonlocal tests
        assert x, label
        tests += 1

    for n in (2, 3, 4):
        lam = [1.0] * n
        for k in range(1, n+1):
            actual = normalized_intrinsic(lam, k)
            reference = math.comb(n,k) * (math.pi**(n/2)/math.gamma(1+n/2)) / ((math.pi**(k/2)/math.gamma(1+k/2))*(math.pi**((n-k)/2)/math.gamma(1+(n-k)/2)))
            check(abs(actual-reference) < 2e-6, ('unit ball', n,k,actual))

    # Independent exact beta-integral coefficients for n=3 at the unit ball.
    expected = ((Fraction(8,35), Fraction(4,105), Fraction(1,35)),
                (Fraction(4,105), Fraction(8,35), Fraction(6,35)),
                (Fraction(0), Fraction(0), Fraction(1,2)))
    for k in (1,2):
        for j in (1,2,3):
            h = 0.0002
            s = [1.0,3.0,3.0,1.0]
            def v_from_coeff(coeff):
                def g(z):
                    if z <= 0: return coeff[1] if k == 1 else 0.0
                    if z >= 1: return 0.0
                    u = (z/(1-z))**2
                    q = sum(coeff[i]*u**i for i in range(4))
                    num = sum((b-a)*coeff[a]*coeff[b]*u**(a+b-1)
                              for a in range(k) for b in range(k,4))
                    return (u**(-k/2) * num * z / (1-z)**3) / q**1.5
                N=8192
                return (g(0)+g(1)+sum((4 if i%2 else 2)*g(i/N) for i in range(1,N)))/(3*N)
            sp = s.copy(); sp[j]+=h
            sm = s.copy(); sm[j]-=h
            observed=(v_from_coeff(sp)-v_from_coeff(sm))/(2*h)
            check(abs(observed-float(expected[k-1][j-1]))<2e-6,
                  ('unit ball derivative',k,j,observed))

    # Two axis spectra share their first two squared-axis symmetric functions.
    ratios=[]
    for eps in (0.12,0.08,0.05,0.03):
        pos=[1+2*eps,1-eps,1-eps]
        neg=[1-2*eps,1+eps,1+eps]
        sp=elementary(pos); sn=elementary(neg)
        check(abs(sp[1]-sn[1])<1e-12 and abs(sp[2]-sn[2])<1e-12,
              ('same coefficients', eps))
        check(abs((sp[3]-sn[3])-4*eps**3)<1e-12, ('cubic difference',eps))
        data=max(abs(normalized_intrinsic(pos,k)-normalized_intrinsic(neg,k))
                 for k in (1,2,3))
        dist=max(abs(math.sqrt(a)-math.sqrt(b)) for a,b in
                 zip(sorted(pos),sorted(neg)))
        ratios.append((eps,dist/eps,data/eps**3))
        check(abs(data/eps**3-2)<0.09, ('cubic data',eps,data))
    check(abs(ratios[-1][1]-1)<0.05, 'semiaxis linear separation')
    print('PASS:',tests,'finite checks')
    print('eps, axis-distance/eps, normalized-data-distance/eps^3:')
    for line in ratios:
        print(' %.3f %.10f %.10f' % line)
    print('Exact analytic 3D Jacobian determinant:',Fraction(8,315))

if __name__=='__main__':
    main()
