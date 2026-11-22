"""Independent checks of cycle-clique hard-core root thresholds (standard library)."""
from fractions import Fraction
from math import atan, comb, cos, exp, log, pi, sqrt


def cycle_coefficients(n):
    return [n * comb(n - k, k) // (n - k) for k in range(n // 2 + 1)]


def spectral_weights(n):
    return [4 * cos((2*j-1)*pi/(2*n))**2 for j in range(1, n//2+1)]


def crossings(n):
    a = spectral_weights(n)
    def phase(y):
        return sum(atan(t*y) for t in a)
    out = []
    for j in range((len(a) - 4)//4 + 1):
        target = (4*j+3)*pi/2
        left, right = 0.0, 1.0
        while phase(right) < target:
            right *= 2
        for _ in range(90):
            mid = (left+right)/2
            if phase(mid) < target: left = mid
            else: right = mid
        y = (left+right)/2
        log_h = sum(log(1+(t*y)**2)/2 for t in a) - log(y)
        out.append((j,y,exp(log_h) if log_h < 700 else float('inf')))
    return out


def routh_rhp(coeff_low_to_high):
    """Exact rational Routh array, for sample parameters without zero pivots."""
    c = list(reversed([Fraction(i) for i in coeff_low_to_high]))
    d = len(c)-1
    width = (d+2)//2
    a = [c[0::2]+[Fraction(0)]*width, c[1::2]+[Fraction(0)]*width]
    a = [r[:width] for r in a]
    for i in range(2,d+1):
        if a[i-1][0] == 0:
            raise ArithmeticError('Routh pivot zero, not a nonsingular test case')
        row = []
        for j in range(width):
            b = a[i-2][j+1] if j+1<width else Fraction(0)
            e = a[i-1][j+1] if j+1<width else Fraction(0)
            row.append((a[i-1][0]*b - a[i-2][0]*e)/a[i-1][0])
        a.append(row)
    signs = [1 if row[0]>0 else -1 for row in a]
    return sum(signs[i] != signs[i+1] for i in range(len(signs)-1))


def main():
    count = 0
    for n in range(3,13):
        direct = [0]*(n//2+1)
        for mask in range(1<<n):
            if any((mask>>i&1) and (mask>>((i+1)%n)&1) for i in range(n)):
                continue
            direct[mask.bit_count()] += 1
        assert direct == cycle_coefficients(n)
        count += 1
    print('EXACT_INDEPENDENT_SET_ENUMERATIONS',count)
    check=0
    for n in range(3,17):
        a = spectral_weights(n)
        assert abs(sum(a)-n)<1e-9
        assert abs(sum(t*t for t in a)-3*n)<1e-8
        for h in (1,5,10,30,60,100,151,152,300,1000):
            c = cycle_coefficients(n); c[1]+=h
            expected = 2*sum(h>v[2]+1e-6 for v in crossings(n))
            try: actual = routh_rhp(c)
            except ArithmeticError: continue
            assert actual == expected,(n,h,expected,actual)
            check+=1
    assert routh_rhp([1,8+151,20,16,2])==0
    assert routh_rhp([1,8+153,20,16,2])==2
    assert abs(crossings(8)[0][2]-(72+56*sqrt(2)))<1e-10
    print('EXACT_ROUTH_THRESHOLD_COMPARISONS',check)
    for n in (200,400,1000,2000):
        cs = crossings(n)
        threshold = min(v[2] for v in cs)
        assert .85< threshold/sqrt(3*exp(1)*n) <1.16
    print('LARGE_N_SCALE_CHECKS',4)
    print('CYCLE_CLIQUE_CHECKS_PASSED')

if __name__=='__main__':main()
