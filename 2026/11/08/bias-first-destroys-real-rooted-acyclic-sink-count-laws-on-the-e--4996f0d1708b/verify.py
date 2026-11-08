"""Exact finite checks for biased circular sink polynomials (Python 3 standard library)."""
from fractions import Fraction as F
from itertools import product
from math import comb


def coefficients(n, u):
    out = [F(0) for _ in range(n//2 + 1)]
    for k in range(n//2 + 1):
        independent_sets = F(n, n-k) * comb(n-k, k)
        for j in range(k+1):
            out[j] += independent_sets * u**k * comb(k,j) * (-1)**(k-j)
    return out


def direct(n, p):
    out = [F(0) for _ in range(n//2 + 1)]
    for w in product((0,1), repeat=n):
        sinks = sum(w[i] == 1 and w[(i+1)%n] == 0 for i in range(n))
        out[sinks] += p**sum(w) * (1-p)**(n-sum(w))
    return out


def discriminant_cubic(a,b,c,d):
    return b*b*c*c - 4*a*c*c*c - 4*b*b*b*d - 27*a*a*d*d + 18*a*b*c*d


def main():
    checks = 0
    for n in range(3,11):
        for p in (F(1,10),F(1,4),F(1,2)):
            u = p*(1-p)
            coef = coefficients(n,u)
            assert coef == direct(n,p)
            checks += 1
            assert coef[0] == p**n+(1-p)**n
            checks += 1
            assert sum(coef) == 1
            checks += 1
    u=F(9,100)
    q8=coefficients(8,u)[1:]
    expected=[F(21523356,50000000),F(6389766,50000000),F(556956,50000000),F(6561,50000000)]
    assert q8==expected
    checks += 1
    assert discriminant_cubic(6561,556956,6389766,21523356)==-548120008099593420688656
    checks += 1
    assert discriminant_cubic(6561,556956,6389766,21523356)<0
    checks += 1
    for n in (6,7):
        for p in (F(1,10), F(1,3), F(1,2)):
            u=p*(1-p)
            q=coefficients(n,u)[1:]
            assert len(q)==3
            assert q[1]*q[1]-4*q[0]*q[2] > 0
            checks += 1
    print(f'VERIFY_OK {checks} exact checks')

if __name__=='__main__': main()
