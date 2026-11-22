"""Exact rational and finite-residue checks for the tetration period-density theorem."""
from fractions import Fraction
from math import ceil, floor, gcd


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = e
        p += 1
    if n > 1:
        out[n] = 1
    return out


def tail(p, k):
    if p == 2:
        return Fraction(1) if k <= 2 else Fraction(1, 2 ** (k - 2))
    return Fraction(1) if k <= 1 else Fraction(1, p ** (k - 1))


def product(seq):
    a = Fraction(1)
    for z in seq:
        a *= z
    return a


def atom(r, t):
    fac = factors(r)
    return product(tail(p, ceil(e*t)) for p, e in fac.items()) - product(tail(p, floor(e*t)+1) for p, e in fac.items())


def mass(r, d):
    fac = factors(r)
    ts = sorted({Fraction(j, e) for p, e in fac.items() for j in range(1, 2*e+1)})
    return sum((atom(r, t) * (Fraction(1) if t <= 1 else Fraction(r, r-1)) for t in ts if t.denominator == d), Fraction(0))


def distribution(r):
    fac = factors(r)
    ds = {Fraction(j, e).denominator for p, e in fac.items() for j in range(1, e+1)}
    return {d: mass(r, d) for d in sorted(ds)}


def ord_valuation_unit(a, p, cutoff):
    if p == 2:
        v = a*a - 1
        if v == 0:
            return cutoff
        c = 0
        while v % 2 == 0:
            c += 1
            v //= 2
        return min(c-1, cutoff)
    z = (pow(a, p-1, p**cutoff)-1) % (p**cutoff)
    if z == 0:
        return cutoff
    c = 0
    while z % p == 0:
        z //= p
        c += 1
    return min(c, cutoff)


def test_finite_residues(r):
    fac = factors(r)
    m = product(p ** (2*e+1) for p,e in fac.items())
    assert m.denominator == 1
    m = int(m)
    tot=0
    counts={}
    for a in range(1,m+1):
        if gcd(a,r)>1:
            continue
        tot += 1
        slope = min(Fraction(ord_valuation_unit(a,p,2*e+1),e) for p,e in fac.items())
        if slope<=2:
            counts[slope] = counts.get(slope,0)+1
    for t in sorted({Fraction(j,e) for p,e in fac.items() for j in range(1,2*e+1)}):
        assert Fraction(counts.get(t,0),tot)==atom(r,t),(r,t,counts.get(t,0),tot,atom(r,t))
    tail_prob = product(tail(p,2*e+1) for p,e in fac.items())
    assert Fraction(tot-sum(counts.values()),tot)==tail_prob
    return m,tot


def delta(r):
    rad=product(factors(r).keys())
    rad=int(rad)
    if r%2:return Fraction(r-rad,r-1)
    if r%4:return Fraction((r+1)*(r-rad),r*(r-1))
    return Fraction(r+1-2*rad,r-1)


def main():
    expected={
        64:{1:Fraction(2,63), 2:Fraction(16,63), 3:Fraction(40,63),6:Fraction(5,63)},
        144:{1:Fraction(10,143),2:Fraction(120,143),4:Fraction(1,11)},
        72:{1:Fraction(10,71),2:Fraction(48,71),3:Fraction(13,71)},
    }
    for r in [4,8,9,12,18,36,60,64,72,144,216,720]:
        row=distribution(r)
        assert sum(row.values())==1
        assert 1-row[1]==delta(r)
        if r in expected:
            assert row==expected[r],(r,row)
        for t in [Fraction(7,6),Fraction(3,2),Fraction(5,3),Fraction(2)]:
            assert atom(r,t+1)==atom(r,t)/r
    for r in [4,9,36,64,72,144]:
        m,tot=test_finite_residues(r)
        print('finite CRT:', r, 'modulus',m,'units',tot,'distribution',distribution(r))
    print('TETRATION_PERIOD_DENSITY_OK')

if __name__=='__main__':main()
