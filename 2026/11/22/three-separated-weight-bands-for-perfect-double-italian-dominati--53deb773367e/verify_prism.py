"""Independent exact counting by fixed layer totals and two-variable convolution.
Run: python3 verify_prism.py. No third-party dependencies.
"""
from collections import defaultdict
from math import comb


def prediction(n):
    p = defaultdict(int)
    p[6] += comb(n, 3)**2 + n**3
    p[7] += n**2*(n-1)
    p[8] += comb(n, 2)
    for k in range(n+1):
        p[2*n+1+k] += 2*n*comb(n,k)
    p[2*n+2] += n*(n+1)
    p[2*n+3] += 2*n
    p[3*n] += 2
    for k in range(2*n+1):
        p[4*n+k] += comb(2*n,k)
    return {w:v for w,v in p.items() if v}


def independent_sum_convolution(n):
    # Enumerate target row totals A,B. Allowed (a,b) columns depend on them.
    # This is not the case-based proof: it counts all 16 column digit pairs.
    found = defaultdict(int)
    for A in range(3*n+1):
        for B in range(3*n+1):
            states = [(a,b) for a in range(4) for b in range(4)
                if (a >= 2 or 3 <= A+b <= 4)
                and (b >= 2 or 3 <= B+a <= 4)]
            if not states:
                continue
            dp = {(0,0): 1}
            for _ in range(n):
                ndp = defaultdict(int)
                for (p,q),c in dp.items():
                    for a,b in states:
                        if p+a <= A and q+b <= B:
                            ndp[p+a,q+b] += c
                dp = ndp
                if not dp:
                    break
            found[A+B] += dp.get((A,B),0)
    return {w:v for w,v in found.items() if v}


if __name__ == '__main__':
    for n in range(4, 10):
        got = independent_sum_convolution(n)
        expected = prediction(n)
        assert got == expected, (n,got,expected)
        print('n={} nonzero_weights={} min_count={} total={}'.format(
            n,sorted(got), got[6],sum(got.values())))
    print('LAYER_SUM_CONVOLUTION_CERTIFICATE_OK')
