#!/usr/bin/env python3
"""Independent finite rational checks of common-phase carry covariances.

The proof is analytic and valid in all integer dimensions; the checks below are
finite diagnostic comparisons, not proof of any infinite assertion.
"""
from fractions import Fraction
from math import gcd


def carry(d, j, x):
    return (d*x).__floor__()-(j*x).__floor__()-((d-j)*x).__floor__()


def direct_covariance(d, j, k):
    points = {Fraction(0), Fraction(1)}
    for a in {d, j, d-j, k, d-k}:
        points.update(Fraction(r, a) for r in range(1, a))
    xs = sorted(points)
    both = Fraction(0)
    first = Fraction(0)
    second = Fraction(0)
    for l, r in zip(xs, xs[1:]):
        mid = (l+r)/2
        fj, fk = carry(d, j, mid), carry(d, k, mid)
        both += (r-l)*fj*fk
        first += (r-l)*fj
        second += (r-l)*fk
    assert first == second == Fraction(1,2)
    return both-Fraction(1,4)


def kernel(a, b):
    return Fraction(gcd(a, b)**2, a*b)


def exact_covariance(d, j, k):
    terms = [(j,k),(j,d-k),(d-j,k),(d-j,d-k)]
    numerator = 1+sum(kernel(a,b) for a,b in terms)
    numerator -= kernel(j,d)+kernel(d-j,d)+kernel(k,d)+kernel(d-k,d)
    return numerator/12


def main():
    count=0
    zeros=0
    for d in range(3, 36):
        for j in range(1,d):
            for k in range(j,d):
                c=exact_covariance(d,j,k)
                assert c==direct_covariance(d,j,k), (d,j,k,c,direct_covariance(d,j,k))
                assert c>=0,(d,j,k,c)
                if c==0:
                    zeros+=1
                    assert d%2==0 and (j==d//2 or k==d//2),(d,j,k)
                elif j!=d//2 and k!=d//2:
                    delta_j=d-(j if d%j==0 else 0)-(d-j if d%(d-j)==0 else 0)
                    delta_k=d-(k if d%k==0 else 0)-(d-k if d%(d-k)==0 else 0)
                    assert delta_j>0 and delta_k>0
                count+=1
    print(f'PASS: {count} exact direct-integration vs gcd-covariance comparisons; {zeros} zero covariances, exclusively with central index.')
    for d,j,k in [(5,1,2),(6,1,2),(8,1,3),(12,2,5),(30,6,10)]:
        print(f'd={d} j={j} k={k}: covariance={exact_covariance(d,j,k)}')

if __name__=='__main__':
    main()
