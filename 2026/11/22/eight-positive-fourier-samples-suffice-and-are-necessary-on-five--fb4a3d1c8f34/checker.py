"""Supplementary exact and finite diagnostics for sparse positive cyclic Fourier sampling.

The proof of the all-primes theorem is analytic; these checks are not a
substitute for its cyclotomic obstruction or uniform positivity argument.
Requires Python 3.9+ standard library only.
"""
from fractions import Fraction as F
from math import comb, cos, pi, sin


def elementary_sign_sum(a, b, degree):
    return sum((-1) ** (degree - j) * comb(a, j) * comb(b, degree - j)
               for j in range(degree + 1) if j <= a and degree-j <= b)


def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**.5)+1))


def exact_five_level_weights(c, d):
    u, v = c*c, d*d
    D = (4*u-1)/(8*(1-v)*(u-v))
    C = (1-4*v)/(8*(1-u)*(u-v))
    E = (3-4*u-4*v+8*u*v)/(8*(1-u)*(1-v))
    delta_C = -d*(1-v)*D/(c*(1-u))
    delta_E = d*(u-v)*D/(1-u)
    levels = [(1, (E+delta_E)/2),(-1, (E-delta_E)/2),
              (c,(C+delta_C)/2),(-c,(C-delta_C)/2),(d,D)]
    return levels, (E,C,D,delta_E,delta_C)


def main():
    e2 = [elementary_sign_sum(a,6-a,2) for a in range(7)]
    e3 = [elementary_sign_sum(a,7-a,3) for a in range(8)]
    assert e2 == [15, 5, -1, -3, -1, 5, 15]
    assert e3 == [-35, -5, 5, 3, -3, -5, 5, 35]
    assert all(x % 7 for x in e2)
    assert all(all(x % p for x in e3) for p in range(11,311) if prime(p))

    # Fully exact rational arithmetic validates all five moment identities
    # and positivity for one interior admissible parameter pair.
    levels, vals = exact_five_level_weights(F(3,5),F(1,10))
    assert min(w for _,w in levels)>0
    assert [sum(w*x**k for x,w in levels) for k in range(5)] == [
        F(1),F(0),F(1,2),F(0),F(3,8)]

    n=0
    for p in range(11,502):
        if not prime(p):
            continue
        n+=1
        a, b = p//4+1, (p-1)//2
        assert p/4 < a < p/3
        c, d = cos(pi*a/p), sin(pi/(2*p))
        assert .25 < c*c < .5 and 0<d<.25
        levels,(E,C,D,de,dc) = exact_five_level_weights(c,d)
        assert min(w for _,w in levels)>0
        assert E>de>0 and C>abs(dc) and D>0
        weights={0:(E+de)/2,p:(E-de)/2,
                 a:(C+dc)/4,2*p-a:(C+dc)/4,
                 p-a:(C-dc)/4,p+a:(C-dc)/4,
                 b:D/2,2*p-b:D/2}
        assert len(weights)==8 and min(weights.values())>0
        assert abs(sum(weights.values())-1)<2e-13
        for k in range(1,5):
            moment=sum(w*complex(cos(pi*j*k/p),sin(pi*j*k/p))
                       for j,w in weights.items())
            assert abs(moment)<5e-12, (p,k,moment)
    for p, count in [(3,6),(5,5),(7,7)]:
        N=2*p
        nodes=range(N) if p==3 else range(0,N,2)
        assert len(list(nodes))==count
        for k in range(1,5):
            z=sum(complex(cos(2*pi*j*k/N),sin(2*pi*j*k/N))
                  for j in nodes)/count
            assert abs(z)<5e-14,(p,k,z)
    print('PASS: parity symmetric sums, rational exact moment identities,')
    print('positive eight-node Fourier rules for',n,'odd primes in [11,501],')
    print('and exact subgroup witnesses at primes 3, 5, 7.')


if __name__ == '__main__':
    main()
