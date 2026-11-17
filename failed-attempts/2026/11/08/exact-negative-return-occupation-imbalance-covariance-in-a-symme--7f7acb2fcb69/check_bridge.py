"""Exact, standalone verification of the uniform-bridge occupation/returns covariance.
Only the standard library is required. Usage: python check_bridge.py
"""
from math import comb, sqrt, pi
from fractions import Fraction
from itertools import combinations


def statistic_bridge(steps):
    pos = 0
    zeros = 0
    positive_edges = 0
    for step in steps:
        if 2*pos + step > 0:
            positive_edges += 1
        pos += step
        if pos == 0:
            zeros += 1
    assert pos == 0 and positive_edges % 2 == 0
    n = len(steps) // 2
    return zeros, (positive_edges - n) ** 2, positive_edges


def enumeration(n):
    count = sumk = sumd2 = sumkd2 = sumk2 = 0
    occupancy = [0] * (n+1)
    for ups in combinations(range(2*n), n):
        up = set(ups)
        seq = [1 if j in up else -1 for j in range(2*n)]
        k, d2, a = statistic_bridge(seq)
        count += 1
        sumk += k
        sumk2 += k*k
        sumd2 += d2
        sumkd2 += k*d2
        occupancy[a//2] += 1
    assert count == comb(2*n,n)
    q = Fraction(4**n, count)
    mean_k = q-1
    mean_d2 = Fraction(n*(n+2),3)
    var_k = 4*n+2-q-q*q
    cov = -Fraction(n*(n-1),12)*q
    assert Fraction(sumk,count) == mean_k, (n,'mean k')
    assert Fraction(sumk2,count) - mean_k**2 == var_k, (n,'var k')
    assert Fraction(sumd2,count) == mean_d2, (n,'mean d2')
    assert Fraction(sumkd2,count) - mean_k*mean_d2 == cov,(n,'cov')
    assert len(set(occupancy)) == 1, (n,'Chung-Feller')
    return count, cov


def cat(j): return comb(2*j,j)//(j+1)

def factorial_moments(n):
    # GF: B(z,u)=1/(1-u E(z)), E(z)=sum_{l>=1} 2 Catalan_{l-1} z^l.
    # W_{n,k} counts walks having k excursions.
    W = [[0]*(n+1) for _ in range(n+1)]
    Q = [[0]*(n+1) for _ in range(n+1)] # sum of squared half-lengths
    W[0][0] = 1
    for k in range(1,n+1):
        for s in range(k,n+1):
            for l in range(1,s-k+2):
                w = 2*cat(l-1)
                W[k][s] += w*W[k-1][s-l]
                Q[k][s] += w*(Q[k-1][s-l]+l*l*W[k-1][s-l])
    c = comb(2*n,n)
    assert sum(W[k][n] for k in range(n+1)) == c
    ek = Fraction(sum(k*W[k][n] for k in range(n+1)),c)
    es2 = Fraction(sum(Q[k][n] for k in range(n+1)),c)
    eks2 = Fraction(sum(k*Q[k][n] for k in range(n+1)),c)
    q= Fraction(4**n,c)
    assert ek == q-1,(n,'GF E K')
    assert es2 == Fraction(n*(n+2),3),(n,'GF E S2')
    assert eks2 - ek*es2 == -Fraction(n*(n-1),12)*q,(n,'GF covariance')
    return c


def verify():
    cases=0
    for n in range(1,9):
        enumeration(n)
        cases+=1
    for n in range(1,81):
        factorial_moments(n)
        cases+=1
    for n in (20,100,1000,10000):
        q = 4**n / comb(2*n,n) if n <= 100 else None
        if q is None:
            # Avoid float overflow. Ratio via a logarithmic sum.
            from math import lgamma,exp,log
            q = exp(n*log(4) - (lgamma(2*n+1)-2*lgamma(n+1)))
        vk = 4*n + 2 - q - q*q
        vd2 = 4*n*(n+2)*(n*(n+2)-3)/45
        cv = - n*(n-1)*q/12
        corr = cv/sqrt(vk*vd2)
        assert -1 < corr < 0 and -0.60 < corr < -0.45,(n,corr)
        cases += 1
    print('PASS',cases,'parameter-case checks; exact exhaustive paths up to 16 steps')

if __name__ == '__main__':
    verify()
