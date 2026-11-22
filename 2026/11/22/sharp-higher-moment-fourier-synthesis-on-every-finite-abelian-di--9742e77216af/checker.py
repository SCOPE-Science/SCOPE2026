#!/usr/bin/env python3
"""Reproduce finite group-algebra checks for a sharp higher-moment Fourier inequality.

The universal real-exponent theorem is proved analytically in RESULT.md;
these finite exact and numerical examples check normalizations and identities.
"""
import cmath
import random
from fractions import Fraction
from math import isclose, pi


def difference_counts(E, group_order, combine):
    counts = [0] * group_order
    for a in E:
        for b in E:
            counts[combine(a, b)] += 1
    assert counts[0] == len(E)
    lam = counts[1]
    assert all(x == lam for x in counts[1:]), counts
    return lam


def nfold_convolution(c, group_order, combine, power):
    v = [0j] * group_order
    v[0] = 1
    for _ in range(power):
        nxt = [0j] * group_order
        for x, a in enumerate(v):
            if a == 0:
                continue
            for y, b in c.items():
                nxt[combine(x, y)] += a * b
        v = nxt
    return v


def finite_example(name, group_order, E, combine, add, phase):
    k = len(E)
    lam = difference_counts(E, group_order, combine)
    assert k * (k - 1) == lam * (group_order - 1)
    a = Fraction(k - lam, k)
    fourth = 1 + Fraction(lam * (k - 1), k)
    assert fourth == Fraction(k * k + (group_order - 1) * a * a, group_order)
    sixth = Fraction(k**3 + (group_order-1) * a**3, group_order)
    rnd = random.Random(32017 + group_order)
    count = 0
    for _ in range(220):
        c = {e: complex(rnd.randint(-3, 3), rnd.randint(-3, 3)) for e in E}
        S = sum(round(z.real)**2+round(z.imag)**2 for z in c.values())
        if S == 0:
            continue
        sq = nfold_convolution(c, group_order, add, 2)
        cube = nfold_convolution(c, group_order, add, 3)
        moment4 = sum(round(z.real)**2+round(z.imag)**2 for z in sq)
        moment6 = sum(round(z.real)**2+round(z.imag)**2 for z in cube)
        assert Fraction(moment4, S*S) <= fourth, (name, c, sq, moment4, S, fourth)
        assert Fraction(moment6, S**3) <= sixth
        # Exact decomposition of the fourth-moment deficit.
        amps = {e: round(z.real)**2+round(z.imag)**2 for e,z in c.items()}
        Qamp = sum(t*t for t in amps.values())
        fiber = 0
        for d in range(1, group_order):
            pairs = [(e,f) for e in E for f in E if combine(e,f) == d]
            R = sum((c[e]*c[f].conjugate() for e,f in pairs), 0j)
            B = sum(amps[e]*amps[f] for e,f in pairs)
            fiber += lam * B - (round(R.real)**2+round(R.imag)**2)
        assert fiber >= 0
        fourth_def = fourth-Fraction(moment4,S*S)
        assert fourth_def == lam*(Fraction(Qamp,S*S)-Fraction(1,k))+Fraction(fiber,S*S)
        # Exact cubic Hermite remainder, expressed through moments only.
        Eu2 = Fraction(moment4,S*S)
        Eu3 = Fraction(moment6,S**3)
        residual = -Eu3+(k+2*a)*Eu2-(2*k*a+a*a)+k*a*a
        assert residual == sixth-Eu3-(k+2*a)*fourth_def
        assert residual >= 0
        count += 5
    # Every character restriction has two-point squared magnitude distribution.
    for x0 in range(group_order):
        c = {e: cmath.exp(-1j * phase(e, x0)) for e in E}
        vals = [sum(c[e] * cmath.exp(1j * phase(e, x)) for e in E) for x in range(group_order)]
        u = [abs(z)**2 / k for z in vals]
        assert isclose(u[x0], k, abs_tol=1e-11)
        assert all(isclose(u[x], float(a), abs_tol=1e-11) for x in range(group_order) if x != x0)
        for p in (4, 4.25, 5, 6, 7.75, 10):
            expected = (k**(p/2) + (group_order-1)*float(a)**(p/2)) / group_order
            actual = sum(t**(p/2) for t in u) / group_order
            assert isclose(expected, actual, rel_tol=1e-10, abs_tol=1e-10)
            count += 1
    # Numerical checks for arbitrary coefficient patterns at nonintegral exponents.
    for _ in range(45):
        c = {e: complex(rnd.uniform(-2,2),rnd.uniform(-2,2)) for e in E}
        S = sum(abs(z)**2 for z in c.values())
        vals = [sum(c[e]*cmath.exp(1j*phase(e,x)) for e in E) for x in range(group_order)]
        u = [abs(z)**2/S for z in vals]
        for p in (4.25,5,7.75,10):
            lhs = sum(t**(p/2) for t in u)/group_order
            rhs = (k**(p/2)+(group_order-1)*float(a)**(p/2))/group_order
            assert lhs <= rhs+1e-9, (name,p,lhs,rhs)
            count += 1
    return name, k, lam, count


def main():
    examples = []
    for v, E in ((7, (0,1,3)), (13, (0,1,3,9)), (11, tuple(sorted({j*j % 11 for j in range(1,11)}))), (19, tuple(sorted({j*j % 19 for j in range(1,19)})))):
        examples.append(finite_example(f'Z{v}', v, E, lambda x,y,v=v:(x-y)%v, lambda x,y,v=v:(x+y)%v, lambda e,x,v=v:2*pi*e*x/v))
    E16 = tuple(x for x in range(16) if (((x>>0)&1)*((x>>1)&1)) ^ (((x>>2)&1)*((x>>3)&1)))
    examples.append(finite_example('Z2^4',16,E16,lambda x,y:x^y,lambda x,y:x^y,lambda e,x:pi*((e&x).bit_count()%2)))
    # Exact sixth moment constants include the two familiar small Singer groups.
    assert Fraction(3**3 + 6 * Fraction(2,3)**3, 7) == Fraction(37,9)
    assert Fraction(4**3 + 12 * Fraction(3,4)**3, 13) == Fraction(85,16)
    assert Fraction(5**3 + 10 * Fraction(3,5)**3, 11) == Fraction(289,25)
    # Exact quadratic Hermite majorants for exponents s=3 and s=4.
    for k,a in ((3,Fraction(2,3)),(4,Fraction(3,4)),(5,Fraction(3,5)),(6,Fraction(2,3))):
        for s in (3,4):
            A = (Fraction(k**s)-a**s-s*a**(s-1)*(k-a))/(k-a)**2
            for j in range(81):
                t = Fraction(k*j,80)
                Q = a**s+s*a**(s-1)*(t-a)+A*(t-a)**2
                assert Q >= t**s
                if s == 3:
                    assert Q-t**3 == (t-a)**2*(k-t)
                else:
                    assert Q-t**4 == (t-a)**2*(k-t)*(t+k+2*a)
    print('VERIFY_OK',examples,'Hermite_grid=648', 'sixth_constants=(37/9,85/16,289/25)')

if __name__ == '__main__':
    main()
