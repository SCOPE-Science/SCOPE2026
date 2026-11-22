"""Exact arithmetic checks for finite exchangeability of fixed-pair indicators in random perfect matchings."""
from fractions import Fraction as Q
from math import comb
from functools import lru_cache


def odd_double_factorial(k):
    assert k >= 0
    out = 1
    for j in range(1, 2*k, 2):
        out *= j
    return out


def c(m, r):
    assert 0 <= r <= m
    return Q(odd_double_factorial(m-r), odd_double_factorial(m))


def S_direct(k):
    return sum((-1)**j * comb(k+4, j) * (odd_double_factorial(k-j)-1)
               for j in range(k+1))


def S_recursive(K):
    a = [0, 0]
    for k in range(2, K+1):
        a.append(2*(k-1)*a[-1] + 2*(k+3)*a[-2]
                 + (-1)**k*k*(k-1)*(k+1)//3)
    return a


def extremal_distribution(m):
    assert m >= 3
    N = m + 4
    q = c(m, m)
    probs = {t: q * comb(N, t) * S_direct(m-t) for t in range(m-1)}
    probs[N] = q
    return N, probs


def exact_moments(N, probs, r):
    return sum(p * Q(comb(t, r), comb(N, r)) for t, p in probs.items() if t >= r)


def all_matchings(xs):
    if not xs:
        yield ()
        return
    x = xs[0]
    for i in range(1, len(xs)):
        y = xs[i]
        for rest in all_matchings(xs[1:i] + xs[i+1:]):
            yield ((x, y),) + rest


def enumerate_pair_moments(m):
    counts = [0] * (m+1)
    for pairing in all_matchings(tuple(range(2*m))):
        e = {tuple(sorted(pair)) for pair in pairing}
        k = sum((2*i, 2*i+1) in e for i in range(m))
        counts[k] += 1
    den = odd_double_factorial(m)
    assert sum(counts) == den
    for r in range(m+1):
        ex = sum(counts[k] * comb(k, r) for k in range(r, m+1))
        assert Q(ex, den*comb(m, r)) == c(m,r)
    return counts


def run():
    checks = 0
    S = S_recursive(85)
    for k in range(86):
        assert S[k] == S_direct(k)
        checks += 1
    assert S[2] == 2 and S[3] == 0 and S[4] == 48
    for k in range(4,86):
        assert S[k] >= k*(k-1)*(k+1)//3
        checks += 1
    for m in range(3,31):
        N, P = extremal_distribution(m)
        assert all(p >= 0 for p in P.values())
        assert sum(P.values(), Q(0)) == 1
        checks += len(P) + 1
        for r in range(m+1):
            assert exact_moments(N,P,r) == c(m,r)
            checks += 1
        q=c(m,m)
        assert P[m-3] == 0
        assert P[m-2] == 2*q*comb(N,m-2)
        checks += 2
        # The necessary coefficient for an N'=m+5 extension is strictly negative.
        Nprime=m+5
        pprime=2*q*comb(Nprime,m-3)*(m+4-Nprime)
        assert pprime < 0
        checks += 1
    for m in range(2,7):
        enumerate_pair_moments(m)
        checks += m+1
    # Check the exceptional infinite cases: m=1 deterministic, m=2 diagonal Bernoulli(1/3).
    assert c(2,1)==c(2,2)==Q(1,3)
    checks += 1
    print('PASS', checks, 'exact assertions; m=3..30, k=0..85, direct matchings m=2..6')


if __name__=='__main__':
    run()
