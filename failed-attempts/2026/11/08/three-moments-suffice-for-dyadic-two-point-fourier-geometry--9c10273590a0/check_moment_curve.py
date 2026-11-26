#!/usr/bin/env python3
"""Exact integer checker for dyadic moment-curve two-sum theorem.

No external packages, floating-point arithmetic, or network access are used.
The theorem for all exponents relies on the separate algebraic proof.
"""
from collections import Counter
from random import Random


def predicted_fiber(k, s, p2, p3, roots):
    n = 1 << k
    mask = n - 1
    if s & 1:
        w = ((pow(s, 3, n) - p3) * pow(3*s, -1, n)) & mask
        if (w & 1) or ((s*s - 2*w - p2) & mask):
            return 0
        return 2
    q = n >> 1
    if (s*s - p2) & 1:
        return 0
    w = ((s*s - p2) // 2) % q
    if (s*s*s - 3*s*w - p3) & mask:
        return 0
    h = s // 2
    return 2 * roots[(h*h-w) % q]


def theorem_image_size(k):
    n=1<<k
    if k == 1:
        return 2
    return (7*n*n + (20 if k%2==0 else 16)*n)//24


def verify(max_k=10):
    rnd = Random(0x271337)
    for k in range(1, max_k+1):
        n = 1 << k
        q = n >> 1
        mask = n - 1
        roots = [0]*q
        for x in range(q):
            roots[(x*x)%q] += 1
        pairs = Counter()
        # Independently enumerate ordered pairs and their moment sums.
        for x in range(n):
            x2 = (x*x)&mask
            x3 = (x2*x)&mask
            for y in range(n):
                pairs[((x+y)&mask, (x2+y*y)&mask,
                       (x3+y*y*y)&mask)] += 1
        assert sum(pairs.values())==n*n
        assert len(pairs)==theorem_image_size(k), (k, len(pairs))
        assert sum(v*v for v in pairs.values())==max(2,k)*n*n
        for (s,p2,p3), actual in pairs.items():
            pred=predicted_fiber(k,s,p2,p3,roots)
            assert pred==actual, (k,(s,p2,p3),actual,pred)
        if k<=5:
            for s in range(n):
                for p2 in range(n):
                    for p3 in range(n):
                        pred=predicted_fiber(k,s,p2,p3,roots)
                        assert pairs.get((s,p2,p3),0)==pred
        else:
            for _ in range(2500):
                s,p2,p3 = [rnd.randrange(n) for i in range(3)]
                pred=predicted_fiber(k,s,p2,p3,roots)
                assert pairs.get((s,p2,p3),0)==pred
        # Check that the first three power sums determine all higher power sums,
        # using a separate recurrence from the full pair enumeration.
        if k<=8:
            power_sequences={}
            for x in range(n):
                for y in range(n):
                    s = (x+y)&mask
                    p2 = (x*x+y*y)&mask
                    p3 = (x*x*x+y*y*y)&mask
                    series=tuple((pow(x,j,n)+pow(y,j,n))&mask for j in range(4,10))
                    key=(s,p2,p3)
                    if key in power_sequences:
                        assert power_sequences[key]==series, (k,key)
                    else:
                        power_sequences[key]=series
        print(f'k={k} n={n} |C+C|={len(pairs)} E={sum(v*v for v in pairs.values())} '
              f'fiber_hist={dict(sorted(Counter(pairs.values()).items()))}')
        if k>=2:
            half=n//2
            a=(0,1)
            b=(half, (1-half)%n)
            assert sum(a)%n==sum(b)%n
            assert (sum(z*z for z in a)-sum(z*z for z in b))%n==0
            assert (sum(z*z*z for z in a)-sum(z*z*z for z in b))%n==half
    print('DYADIC_THREE_MOMENT_STABILIZATION_AND_FULL_FIBERS_PASS')

if __name__=='__main__':
    verify()
