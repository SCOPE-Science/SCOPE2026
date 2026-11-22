"""Standalone exact checks for batch-recursive-tree depth covariances.
Run: python CHECK.py; only the Python standard library is used.
Finite tests supplement, but do not replace, the analytical proof.
"""
from collections import defaultdict
from fractions import Fraction as F


def moments_by_recursion(m, T):
    H = R = V = F(0)
    means, variances, covariances = {}, {}, {}
    for t in range(2, T+1):
        a = F(m, 1+m*(t-1))
        B = H-R
        means[t] = 1+H
        variances[t] = B
        covariances[t] = (1-a)*V+a*B
        V = (1-a*a)*V+a*a*B
        H += a
        R += a*a
    return means, variances, covariances


def full_depth_law(m, T):
    law = {(0,): F(1)}
    for t in range(2, T+1):
        new = defaultdict(F)
        n = 1+m*(t-2)
        for past, p in law.items():
            new[past+(1,)] += p/F(n)
            for depth in past[1:]:
                new[past+(1+depth,)] += p*F(m, n)
        law = dict(new)
        assert sum(law.values()) == 1
    return law


def covariance_sum(m, i):
    c = F(1,m)
    return sum(((r+c-1)/((r+c)**2*(r+c+1)) for r in range(1,i-1)), F(0))


def interval(m, K=30):
    c = F(1,m)
    base = F(2,1)/(1+c) - sum((1/(F(r)+c)**2 for r in range(1,K+1)), F(0))
    return (base-1/(F(K)+c), base-1/(F(K+1)+c))


def run():
    checks = 0
    for m in (1,2,3,4):
        for T in range(3,8):
            if m == 4 and T == 7:
                continue
            law = full_depth_law(m,T)
            mean, variance, cov = moments_by_recursion(m,T)
            for i in range(2,T+1):
                mu = sum((p*depths[i-1] for depths,p in law.items()), F(0))
                assert mu == mean[i]; checks+=1
                v = sum((p*(depths[i-1]-mu)**2 for depths,p in law.items()),F(0))
                assert v == variance[i]; checks+=1
                assert cov[i] == covariance_sum(m,i); checks+=1
                for j in range(i+1,T+1):
                    mj = sum((p*depths[j-1] for depths,p in law.items()), F(0))
                    cv = sum((p*(depths[i-1]-mu)*(depths[j-1]-mj)
                              for depths,p in law.items()),F(0))
                    assert cv == cov[i]; checks+=1
    for m in range(1,21):
        _,_,cov=moments_by_recursion(m,200)
        for i in range(2,201):
            assert cov[i] == covariance_sum(m,i); checks+=1
    ranges={m:interval(m) for m in (1,2,3,4)}
    assert all(lo<hi for lo,hi in ranges.values()); checks+=1
    assert all(ranges[3][0]>ranges[m][1] for m in (1,2,4)); checks+=3
    c=F(1,4)
    derivative_lower = 1/(1+c)**3+1/(2+c)**3+1/(2*(3+c)**2)
    assert derivative_lower > 1/(1+c)**2; checks+=1
    print('exact assertions passed:',checks)
    print('certified intervals for limiting covariances:')
    for m in ranges:
        print(m, tuple(float(v) for v in ranges[m]))
    print('m=3 uniquely maximal among positive integers: analytically and rationally certified')

if __name__ == '__main__':
    run()
