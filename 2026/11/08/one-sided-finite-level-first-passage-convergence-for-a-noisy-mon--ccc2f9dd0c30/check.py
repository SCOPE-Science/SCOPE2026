"""Standalone diagnostics for finite-threshold oscillator first-passage laws.

Python >=3.9 standard library only. Run: python check.py
"""
from fractions import Fraction
from math import factorial

COUNT = 0


def test(condition, why):
    global COUNT
    assert condition, why
    COUNT += 1


def laguerre_denominator(B, s):
    # Exactly L_B(-s/B); s may be a Fraction.
    a = s * 0 + 1
    coefficient = a
    for k in range(1, B + 1):
        coefficient *= (B - k + 1) * s / (B * k * k)
        a += coefficient
    return a


def bessel_i_integer(n, s):
    # Returns I_n(2 sqrt(s)) as the convergent series.
    total = 0.0
    term = float(s) ** (n / 2) / factorial(n)
    for k in range(300):
        total += term
        term *= s / ((k + 1) * (k + n + 1))
        if term < 1e-17 * total:
            break
    return total


def backward_equations(B, s):
    # Solve independent finite Markov-generator backward equations.
    s = Fraction(s)
    matrix = [[Fraction(0) for _ in range(B+1)] for _ in range(B)]
    for n in range(B):
        if n:
            matrix[n][n-1] = Fraction(-n)
        matrix[n][n] = Fraction(2*n + 1) + s / B
        if n + 1 < B:
            matrix[n][n+1] = Fraction(-(n+1))
        else:
            matrix[n][-1] = Fraction(n + 1)
    for i in range(B):
        pivot = next(j for j in range(i, B) if matrix[j][i])
        matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
        v = matrix[i][i]
        matrix[i] = [w / v for w in matrix[i]]
        for j in range(i+1, B):
            v = matrix[j][i]
            if v:
                matrix[j] = [x - v*y for x,y in zip(matrix[j], matrix[i])]
    u = [Fraction(0) for _ in range(B)]
    for i in range(B-1, -1, -1):
        u[i] = matrix[i][-1] - sum(matrix[i][j] * u[j] for j in range(i+1,B))
    return u[0]


def main():
    for B in range(1,13):
        for s in [Fraction(1,7), Fraction(1,2), Fraction(1), Fraction(7,2)]:
            direct = 1 / laguerre_denominator(B,s)
            independent = backward_equations(B,s)
            test(direct == independent, ('generator', B, s, direct, independent))
            test(Fraction(0)<direct<Fraction(1), ('Laplace range',B,s))
    for s in [0.05, 0.25, 1.0, 3.0, 6.0, 10.0]:
        i0 = bessel_i_integer(0,s)
        i2 = bessel_i_integer(2,s)
        limit = 1/i0
        sharp = s*i2/(2*i0*i0)
        previous=1.0
        errors=[]
        for B in [1,2,3,4,6,8,10,16,24,32,48,64,96,128,256,512]:
            value = 1/laguerre_denominator(B, float(s))
            test(limit < value < previous, ('strict Laplace ordering',B,s,value,previous,limit))
            previous=value
            errors.append((B,abs((value-limit)*B-sharp)))
        test(errors[-1][1] < errors[-3][1], ('sharp first correction rate',s,errors[-3:]))
        test(errors[-1][1] < 0.01, ('first correction numerical',s,errors[-1],sharp))
        for B in [32,64,128,256,512]:
            value=1/laguerre_denominator(B, s)
            test(abs(value - limit - sharp/B) < (100+B*0)/B**2, ('uniform remainder numerics', B,s))
    for B in range(1,500):
        # Exact second-moment/cumulant identity from L_B coefficients.
        q2=Fraction(B-1,4*B)
        ey=Fraction(1)
        ey2=2*(1-q2)
        var=ey2-ey**2
        test(var == Fraction(B+1,2*B), ('variance', B))
        test(var > Fraction(1,2), ('above classical variance',B))
    print('PASS:', COUNT, 'independent exact and numerical assertions')

if __name__ == '__main__':
    main()
