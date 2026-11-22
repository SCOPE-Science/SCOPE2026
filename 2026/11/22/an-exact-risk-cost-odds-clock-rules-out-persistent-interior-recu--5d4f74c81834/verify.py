"""Exact-arithmetic verification of the risk--cost odds identity and sharpness examples.

Run: python verify.py
This checks arithmetic implications; the infinite-time theorem is proved in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, log
from random import Random


def derivs(x, r, c, alpha, beta, mu1, mu2, t1, t2, t3, t4, N, M, b):
    pivotal = F(comb(N - 1, M - 1)) * x ** (M - 1) * (1 - x) ** (N - M)
    return (
        x * (1 - x) * (b * pivotal * r - c),
        r * (1 - r) * (mu1 * (1 - x) - mu2 * x),
        (alpha - c) * (c - beta) * (t1 * (1 - x) - t2 * x + t3 * r - t4 * (1 - r)),
    )


def identity_check(x, r, c, alpha, beta, mu1, mu2, t1, t2, t3, t4, N, M, b):
    dx, dr, dc = derivs(x, r, c, alpha, beta, mu1, mu2, t1, t2, t3, t4, N, M, b)
    k = (alpha - beta) * (t1 + t2) / (mu1 + mu2)
    rstar = (t2 * mu1 - t1 * mu2 + t4 * (mu1 + mu2)) / ((t3 + t4) * (mu1 + mu2))
    h = (alpha - beta) * (t3 + t4)
    dL = (alpha - beta) * dc / ((alpha - c) * (c - beta)) - k * dr / (r * (1 - r))
    assert dL == h * (r - rstar)
    assert dr / (r * (1 - r)) == mu1 - (mu1 + mu2) * x


def check():
    rng = Random(430391)
    count = 0
    for _ in range(200):
        mu1, mu2, t1, t2, t3, t4 = (F(rng.randint(1, 12), rng.randint(1, 9)) for j in range(6))
        beta = F(rng.randint(1, 6), 7)
        alpha = beta + F(rng.randint(1, 6), 5)
        x = F(rng.randint(1, 99), 100)
        r = F(rng.randint(1, 99), 100)
        c = beta + (alpha - beta) * F(rng.randint(1, 99), 100)
        N = rng.randint(2, 9)
        M = rng.randint(1, N)
        b = F(rng.randint(1, 12), 3)
        identity_check(x, r, c, alpha, beta, mu1, mu2, t1, t2, t3, t4, N, M, b)
        count += 1

    # Strictly positive feedback parameters producing each excluded regime.
    for t1, t2, expect in [(F(10), F(1), F(-7, 4)), (F(1), F(10), F(11, 4))]:
        mu1=mu2=t3=t4=F(1)
        rstar=(t2*mu1-t1*mu2+t4*(mu1+mu2))/((t3+t4)*(mu1+mu2))
        assert rstar == expect

    # For every rational target risk in (0,1), the sharpness construction
    # gives a genuine strict-interior equilibrium of the SAME three-variable ODE.
    for j in range(1, 20):
        q=F(j, 20)
        alpha=(1+q)/2
        beta=q/2
        x=F(1, 2)
        c=q
        t1=t2=mu1=mu2=F(1)
        t3=1-q
        t4=q
        assert F(0)<beta<c<alpha and F(0)<q<1
        assert derivs(x,q,c,alpha,beta,mu1,mu2,t1,t2,t3,t4,3,2,F(2)) == (0,0,0)
        rstar=(t2*mu1-t1*mu2+t4*(mu1+mu2))/((t3+t4)*(mu1+mu2))
        assert rstar == q
        count += 1
    print(f'PASS: {count} independent exact-rational identity/equilibrium cases; 2 excluded-regime witnesses')


if __name__ == '__main__':
    check()
