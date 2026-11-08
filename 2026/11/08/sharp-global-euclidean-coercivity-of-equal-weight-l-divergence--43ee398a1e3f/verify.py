#!/usr/bin/env python3
"""Standalone finite checks for a global geometric-mean L-divergence bound.

No external packages. These computations are corroborating checks; the proof
of the universal statement is contained in RESULT.md.
"""
import itertools
import math
import random


def compositions(total, count):
    if count == 1:
        if total > 0:
            yield (total,)
        return
    for i in range(1, total-count+2):
        for suffix in compositions(total-i, count-1):
            yield (i,) + suffix


def divergence(p, q):
    r = [b/a for a, b in zip(p, q)]
    return math.log(math.fsum(r)/len(r)) - math.fsum(math.log(x) for x in r)/len(r)


def distance2(p, q):
    return math.fsum((x-y)**2 for x, y in zip(p,q))


def check(p, q):
    n = len(p)
    gap = divergence(p,q) - 2.0/n * distance2(p,q)
    assert gap > -5.0e-13, (n,p,q,gap)
    return gap


def finite_grid():
    tests = 0
    for n, lo, hi in ((2,2,27),(3,3,16),(4,4,11)):
        for denominator in range(lo, hi + 1):
            ps = [tuple(k/denominator for k in comp)
                  for comp in compositions(denominator,n)]
            for p in ps:
                for q in ps:
                    if p != q:
                        check(p,q)
                        tests += 1
    return tests


def range_and_tv_checks():
    tests = 0
    for n in range(2,7):
        for r in itertools.product(range(1,6),repeat=n):
            mn, mx = min(r), max(r)
            if mn == mx:
                continue
            t = math.log(math.fsum(r)/n) - math.fsum(math.log(z) for z in r)/n
            bound = 2/n * math.log((mn+mx)/(2*math.sqrt(mn*mx)))
            assert t >= bound-1e-13, (r,t,bound)
            # Turn the range values into actual simplex ratios after normalization.
            for weights in ([1.0]*n, [1.0+j for j in range(n)]):
                total=sum(weights)
                p=[w/total for w in weights]
                c=math.fsum(p[i]*r[i] for i in range(n))
                q=[p[i]*r[i]/c for i in range(n)]
                v=math.fsum(abs(p[i]-q[i]) for i in range(n))/2
                cap=(math.sqrt(mx)-math.sqrt(mn))/(math.sqrt(mx)+math.sqrt(mn))
                assert v <= cap + 1e-13
                tests += 1
    return tests


def monte_carlo():
    rng = random.Random(162049)
    tests = 0
    for n in range(2,11):
        for _ in range(2200):
            ps = [rng.expovariate(1.0) for _ in range(n)]
            qs = [rng.expovariate(1.0) for _ in range(n)]
            sp, sq = sum(ps), sum(qs)
            p = [a/sp for a in ps]
            q = [b/sq for b in qs]
            check(p,q)
            mn, mx = min(b/a for a,b in zip(p,q)), max(b/a for a,b in zip(p,q))
            variation = math.fsum(abs(a-b) for a,b in zip(p,q))/2
            range_tv = (math.sqrt(mx)-math.sqrt(mn))/(math.sqrt(mx)+math.sqrt(mn))
            assert variation <= range_tv + 1e-12
            assert distance2(p,q) <= 2*variation**2 + 1e-12
            tests += 1
    return tests


def sharpness_checks():
    tests=0
    for n in range(2,11):
        for epsilon in (1e-3,1e-5,1e-7):
            if n==2:
                p=[0.5,0.5]
            else:
                a=(1-(n-2)*epsilon)/2
                p=[a,a]+[epsilon]*(n-2)
            a=p[0]
            for t in (1e-2*a,1e-3*a,1e-4*a):
                q=list(p)
                q[0]+=t
                q[1]-=t
                # Direct log1p gives numerical stability at small t.
                exact = -math.log1p(-(t/a)**2)/n
                ratio = exact/(2*t*t)
                prediction = 1/(2*n*a*a)
                assert abs(ratio/prediction-1)<1.01e-4
                check(p,q)
                tests+=1
    return tests


def two_cycle_wealth():
    tests=0
    for n in (2,3,5,8):
        p=[(1/n) for _ in range(n)]
        for step in (0.01,0.07,0.3):
            q=list(p)
            delta=step/n
            q[0]+=delta
            q[1]-=delta
            for m in (10,100):
                path=[p if j%2==0 else q for j in range(m+1)]
                t_sum=math.fsum(divergence(path[k],path[k+1]) for k in range(m))
                bound=2/n*math.fsum(distance2(path[k],path[k+1]) for k in range(m))
                assert t_sum>=bound-1e-12
                tests+=1
    return tests


def main():
    g=finite_grid()
    r=range_and_tv_checks()
    m=monte_carlo()
    s=sharpness_checks()
    c=two_cycle_wealth()
    print(f'VERIFY_OK exact_grid_pairs={g} range_enumerations={r} randomized_simplex_pairs={m} boundary_sharpness={s} two_cycle_checks={c}')


if __name__=='__main__':
    main()
