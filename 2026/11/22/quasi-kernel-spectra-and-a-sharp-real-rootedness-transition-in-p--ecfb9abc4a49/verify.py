#!/usr/bin/env python3
"""Independent finite checks for directed-cycle pendant quasi-kernels.

Requires only Python 3 standard library. Finite checks corroborate, but do not
replace, the unrestricted combinatorial and analytic proof.
"""
from collections import Counter
from math import comb


def predicted(n, k):
    out = Counter()
    for b in range(n // 3 + 1):
        if (n - 3*b) % 2:
            continue
        a = (n - 3*b) // 2
        r = a + b
        # n/r * C(r,b) is integer for these cyclic compositions.
        blocks_numerator = n * comb(r, b)
        assert blocks_numerator % r == 0
        ways = blocks_numerator // r
        baseline = a + (k+1)*b
        for j in range(k*r+1):
            out[baseline + j] += ways * comb(k*r, j)
    return out


def brute(n, k):
    N = n*(k+1)
    assert N <= 20
    adj = [0]*N
    for i in range(n):
        adj[i] |= 1 << ((i+1)%n)
        for j in range(k):
            adj[i] |= 1 << (n + i*k + j)
    reach = []
    for i in range(N):
        neighborhood = adj[i]
        two = neighborhood | (1<<i)
        while neighborhood:
            bit = neighborhood & -neighborhood
            neighborhood -= bit
            two |= adj[bit.bit_length()-1]
        reach.append(two)
    full = (1<<N)-1
    counts = Counter()
    for S in range(1, 1<<N):
        # This uses reachability independently of the cyclic-gap derivation.
        x = S
        coverage = 0
        independent = True
        while x:
            bit = x & -x
            x -= bit
            i = bit.bit_length()-1
            if adj[i] & S:
                independent = False
                break
            coverage |= reach[i]
        if independent and coverage == full:
            counts[S.bit_count()] += 1
    return counts


def F_coeffs(n):
    out = {}
    for b in range(n//3+1):
        if (n-3*b)%2:
            continue
        a=(n-3*b)//2
        r=a+b
        j=b//2
        val=n*comb(r,b)//r
        assert n*comb(r,b)%r==0
        out[j] = val
    return [out[j] for j in sorted(out)]


def check_all():
    cases = []
    for n in range(3, 10):
        cases.append((n,1))
    for n in range(3,7):
        cases.append((n,2))
    for n in range(3,6):
        cases.append((n,3))
    total_seeds=0
    for n,k in cases:
        got=brute(n,k)
        want=predicted(n,k)
        assert got==want, (n,k,got,want)
        total_seeds += (1<<(n*(k+1)))
    print('INDEPENDENT_EXHAUSTIVE_QK_CENSUS_PASS',len(cases),'cases',total_seeds,'subsets_scanned')
    for n in range(3,151):
        co=F_coeffs(n)
        assert co and all(x>0 for x in co)
        if n%2==0:
            h=n//2
            assert len(co)-1==h//3 and co[0]==2
            if len(co)>1:
                assert co[1]*2==h*(h-2)*co[0]
        else:
            h=(n-1)//2
            assert len(co)-1==(h-1)//3 and co[0]==n
            if len(co)>1:
                assert co[1]*6==(h-2)*(h-3)*co[0]
        # Exact log-concavity of the positive coefficients of F follows
        # from negative roots in the proof, but only samples are tested here.
        assert all(co[j]*co[j]>co[j-1]*co[j+1] for j in range(1,len(co)-1))
    print('EXACT_CYCLIC_COMPOSITION_AND_COEFFICIENT_CHECK_PASS n=3..150')
    assert predicted(6,2) == Counter({3:2,4:12,5:30,6:43,7:42,8:30,9:14,10:3})
    # Exact cubic discriminant for 3*z^3+2*z^2+4*z+2
    a,b,c,d=3,2,4,2
    disc=b*b*c*c - 4*a*c**3 - 4*b**3*d - 27*a*a*d*d + 18*a*b*c*d
    assert disc < 0, disc
    print('NEGATIVE_CUBIC_DISCRIMINANT_PASS',disc)
    print('VERIFY_OK')

if __name__ == '__main__':
    check_all()
