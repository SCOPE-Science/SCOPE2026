#!/usr/bin/env python3
"""Reproduce numerical illustrations of Poisson-quorum relay spacing.
The proof of global optimality and asymptotics is analytical (RESULT.md).
Requires only the Python standard library.
"""
import math
import random


def h(m, u):
    """Elasticity m/sum_{j>=0}m! u^j/(m+j)! via a positive series."""
    term = 1.0
    total = 1.0
    for j in range(1, 1000):
        term *= u / (m + j)
        total += term
        if abs(term) < 5e-17 * total:
            break
    else:
        raise ArithmeticError('series failed to converge')
    return m / total


def Q(m, u):
    """Pr(Poisson(u)>=m), using the positive survival series."""
    term = u**m / math.factorial(m)
    total = term
    for j in range(1, 1000):
        term *= u / (m + j)
        total += term
        if abs(term) < 5e-17 * total:
            break
    return math.exp(-u) * total


def cost(m, a, rate, d):
    return rate * h(m, a * math.exp(-rate * d))


def gap_at_t(m, a, rate, t):
    z = cost(m, a, rate, 0.0)
    if t <= z:
        return 0.0
    assert t < rate * m
    lower = 0.0
    upper = 1.0
    while cost(m, a, rate, upper) <= t:
        upper *= 2
        if upper > 500.0:
            raise ValueError('required gap beyond numerical resolution')
    for _ in range(65):
        mid = (lower + upper) / 2
        if cost(m, a, rate, mid) < t:
            lower = mid
        else:
            upper = mid
    return (lower + upper) / 2


def optimum(ms, amplitudes, rates, length):
    if length == 0.0:
        return [0.0] * len(ms), min(cost(m,a,r,0) for m,a,r in zip(ms,amplitudes,rates))
    b = min(m * r for m, r in zip(ms, rates))
    lo = min(cost(m,a,r,0) for m,a,r in zip(ms,amplitudes,rates))
    hi = b
    # Fixed-resolution bisection adequate before long-distance singularity.
    for _ in range(65):
        t = (lo + hi) / 2
        ds = [gap_at_t(m,a,r,t) if t < m*r else 0.0
              for m,a,r in zip(ms,amplitudes,rates)]
        if sum(ds) < length:
            lo = t
        else:
            hi = t
    t = (lo + hi) / 2
    ds = [gap_at_t(m,a,r,t) if t < m*r else 0.0
          for m,a,r in zip(ms,amplitudes,rates)]
    return ds, t


def log_probability(ms, amplitudes, rates, ds):
    return sum(math.log(Q(m,a * math.exp(-r*d)))
               for m,a,r,d in zip(ms,amplitudes,rates,ds))


def main():
    assertions = 0
    # Positive-series identity and strict decrease of h as a function of u.
    for m in range(1, 7):
        for j in range(1, 501):
            u = j / 50.0
            v = u + .001
            assert 0 < h(m, v) < h(m, u) < m
            assertions += 1
            assert 0 < Q(m,u) < Q(m,v) < 1
            assertions += 1
    e3 = math.exp(3)
    c1, c2, c3 = [h(m,3) for m in (1,2,3)]
    assert 20 < e3 < 21
    assert c1 < c2 < 1 < c3
    assertions += 2
    u_one_lo, u_one_hi = 0.001, 3.0
    for _ in range(65):
        u_mid = (u_one_lo + u_one_hi)/2
        if h(1,u_mid) > c2:
            u_one_lo = u_mid
        else:
            u_one_hi = u_mid
    gap_threshold = math.log(3/((u_one_lo+u_one_hi)/2))
    assert abs(gap_threshold-1.03344058691873)<2e-11
    assertions += 1
    u_two_lo, u_two_hi = .01, 3.0
    for _ in range(65):
        u_mid = (u_two_lo+u_two_hi)/2
        if h(2,u_mid)>1:
            u_two_lo=u_mid
        else:
            u_two_hi=u_mid
    saturated_gap = math.log(3/((u_two_lo+u_two_hi)/2))
    assert abs(saturated_gap-0.514564753997419)<2e-11
    assertions += 1
    for L in (.05,.5,1.0,1.1,1.5,2,4,8,12,20):
        ds,t=optimum([1,2,3],[3.,3.,3.],[1.,1.,1.],L)
        assert abs(sum(ds)-L) < 5e-7
        assert ds[2] == 0
        assert (ds[1] == 0) == (L <= gap_threshold)
        if ds[1]:
            assert abs(cost(1,3,1,ds[0])-cost(2,3,1,ds[1]))<1e-9
        assertions += 4
        if L >= 8:
            assert abs(ds[1]-saturated_gap)<.025
            assertions += 1

    rng = random.Random(391731)
    # Stress-test KKT and global dominance numerically over diverse interiors.
    for case in range(100):
        n = rng.randint(2,5)
        ms = [rng.randint(1,5) for _ in range(n)]
        aa = [rng.uniform(.3, 7.0) for _ in range(n)]
        rr = [rng.uniform(.5, 2.0) for _ in range(n)]
        length = rng.uniform(.01,7.0)
        ds,t = optimum(ms,aa,rr,length)
        assert abs(sum(ds)-length) < 3e-7
        assertions += 1
        vals=[cost(m,a,r,d) for m,a,r,d in zip(ms,aa,rr,ds)]
        for d,v in zip(ds,vals):
            if d>1e-7:
                assert abs(v-t)<1e-7
            else:
                assert v>=t-1e-7
            assertions += 1
        opt = log_probability(ms,aa,rr,ds)
        for k in range(150):
            vec = [rng.expovariate(1.0) for _ in range(n)]
            div=sum(vec)
            trial=[length*x/div for x in vec]
            test=log_probability(ms,aa,rr,trial)
            assert opt+2e-9 >= test, (case,k,opt,test,ds,trial)
            assertions += 1
    # A heterogeneous-rate example with TWO long-range minimizing stages.
    ms, aa, rr = [1,2,3], [3.0,3.0,3.0], [2.0,1.0,1.0]
    b = 2.0
    d3_inf = gap_at_t(3,3.0,1.0,b)
    C = math.exp(b*d3_inf) * 3.0 * 3.0**2/2 * Q(3,3.0*math.exp(-d3_inf))
    d15,_ = optimum(ms,aa,rr,15.0)
    d20,_ = optimum(ms,aa,rr,20.0)
    assert abs((d20[0]-d15[0])/5 - 1/3) < 1e-3
    assert abs((d20[1]-d15[1])/5 - 2/3) < 1e-3
    assert abs(d20[2]-d3_inf) < 1e-5
    p20 = math.exp(log_probability(ms,aa,rr,d20))
    assert abs(p20*math.exp(b*20)/C - 1) < 2e-5
    assertions += 4

    print('PASS', assertions, 'assertions')
    print('example thresholds:',format(gap_threshold,'.15f'),format(saturated_gap,'.15f'))
    for L in (1,2,5,10,20):
        ds,t=optimum([1,2,3],[3.,3.,3.],[1.,1.,1.],L)
        print('L=',L,'gaps=',[round(x,9) for x in ds],'shadow=',round(t,9))

if __name__=='__main__':
    main()
