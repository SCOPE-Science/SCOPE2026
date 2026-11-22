"""Finite rational checks for square-torus taxicab covering constructions.

These samples are not substitutes for the universal geometric proof.
"""
from fractions import Fraction
from math import ceil


def centers(n):
    r = Fraction(1, 2*n)
    return sorted({((a+b)*r % 1, (a-b)*r % 1)
                   for a in range(2*n) for b in range(2*n)})


def taxicab(p,q):
    dx = abs(p[0]-q[0]); dy = abs(p[1]-q[1])
    return min(dx, 1-dx) + min(dy, 1-dy)


def main():
    samples=0
    for n in range(1,7):
        r=Fraction(1,2*n)
        cs=centers(n)
        assert len(cs)==2*n*n, (n,len(cs))
        for i in range(4*n):
            for j in range(4*n):
                point=(Fraction(i,4*n),Fraction(j,4*n))
                assert min(taxicab(point, c) for c in cs)<=r, (n,point)
                samples+=1
        assert Fraction(1,2*r*r)==2*n*n
        if n>=2:
            m=ceil(Fraction(1,r))
            assert ceil(Fraction(m,2*r))==2*n*n
    assert ceil(Fraction(ceil(Fraction(1,Fraction(49,100))),2*Fraction(49,100)))==4
    print(f'PASS: n=1..6; {samples} finite grid checks; exact center counts and arithmetic bounds')

if __name__=='__main__': main()
