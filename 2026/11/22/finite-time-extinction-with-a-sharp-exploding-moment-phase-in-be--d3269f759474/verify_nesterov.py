"""Exact-rational checks of Bernoulli-interpolated scalar Nesterov recurrences."""
from fractions import Fraction as Q
from itertools import product


def coeff(g, beta):
    return beta * sum((beta**j for j in range(g)), Q(0))


def direct(n, p, beta):
    result = Q(0)
    for outcomes in product((0, 1), repeat=n):
        xprev = x = Q(1)
        prob = Q(1)
        for bit in outcomes:
            prob *= (p if bit else (1-p))
            xnew = (1-bit) * ((1+beta)*x-beta*xprev)
            xprev, x = x, xnew
        result += prob*x*x
    return result


def renewal(nmax, p, beta):
    q = 1-p
    # K(z) = sum_{m>=2} p q^{m-1} c_{m-1}^2 z^m
    kernel = [Q(0)] * (nmax+1)
    for m in range(2, nmax+1):
        kernel[m] = p*q**(m-1)*coeff(m-1,beta)**2
    # H(z) = 1 / ((1-qz)(1-K(z))).
    # First 1/(1-K(z)), then convolution with 1/(1-qz).
    renew = [Q(0)]*(nmax+1)
    renew[0] = Q(1)
    for n in range(1,nmax+1):
        renew[n] = sum(kernel[m]*renew[n-m] for m in range(2,n+1))
    return [sum(q**(n-j)*renew[j] for j in range(n+1)) for n in range(nmax+1)]


def scalar_threshold_test(p, b):
    q = 1-p
    # The probability-normalized squared predecessor at successive active draws.
    a = b*b*q*(1+b*q)/((1-b*q)*(1-b*b*q))
    return (a-1)*(1-b*q)*(1-b*b*q) == q*b*(1+2*b)-1


def run():
    checks=0
    for p in (Q(1,4),Q(7,15),Q(1,2),Q(2,3)):
        for b in (Q(1,4),Q(1,2),Q(3,4),Q(9,10)):
            assert scalar_threshold_test(p,b)
            checks+=1
            seq=renewal(14,p,b)
            for n in range(0,11):
                assert direct(n,p,b)==seq[n], (p,b,n)
                checks+=1
            assert seq[0]==1 and seq[1]==1-p
            checks+=2
    # Critical case: b=3/4 and p=7/15; compare exact K(1) with 1.
    p=Q(7,15);b=Q(3,4);q=1-p
    K1=b*b*q*(1+b*q)/((1-b*q)*(1-b*b*q))
    assert K1==1
    checks+=1
    # Nontrivial strictly unstable and strictly stable adjacent examples.
    for p,sgn in ((Q(1,4),1),(Q(1,2),-1)):
        q=1-p;b=Q(3,4)
        K1=b*b*q*(1+b*q)/((1-b*q)*(1-b*b*q))
        assert (K1>1) if sgn==1 else (K1<1)
        checks+=1
    print('VERIFY_OK',checks,'exact rational equalities/inequalities')


if __name__ == '__main__':
    run()
