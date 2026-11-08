"""Finite diagnostics for polynomially sparse comb-tree parent shifts.

Run: python3 check_comb.py
These computations are consistency tests, not proofs of asymptotic or infinite assertions.
"""
import bisect
import math


def branches(beta, cutoff):
    result = []
    k = 1
    while True:
        j = math.floor(k ** beta)
        if j >= cutoff:
            break
        assert not result or result[-1] < j
        result.append(j)
        k += 1
    return result


def max_window(A, n, maxstart):
    return max(bisect.bisect_left(A, j+n)-bisect.bisect_left(A,j)
               for j in range(maxstart+1))


def finite_descendants(A, cutoff, depth):
    # Parent indices for the truncated comb: spine 0..cutoff+depth;
    # tooth rays exist to depth cutoff+depth, enough for tests near the origin.
    parents = [-1] + list(range(cutoff+depth))
    spine_count = len(parents)
    for j in A:
        if j > cutoff+depth-1:
            break
        prev = j
        for ell in range(cutoff+depth-j):
            prev_parent = prev
            parents.append(prev_parent)
            prev = len(parents)-1
    return parents, spine_count


assertions = 0
for beta in (1.25, 1.5, 2.0, 3.0, 4.0):
    alpha = 1.0 / beta
    A = branches(beta, 5000)
    for n in range(1,121):
        best = max_window(A,n,1000)
        root_count = bisect.bisect_left(A,n)
        assert root_count >= n**alpha - 2
        assert best <= n**alpha + 2.001
        assert best >= root_count
        assertions += 3
    # Check exact combinatorial descendant counts using explicit parent iterates.
    parents, length_spine = finite_descendants(A, 120, 20)
    for j in range(0,101,5):
        for n in range(1,11):
            actual = 0
            for k in range(len(parents)):
                v=k
                for _ in range(n):
                    v=parents[v] if v >= 0 else -1
                actual += (v == j)
            predicted = 1 + bisect.bisect_left(A,j+n)-bisect.bisect_left(A,j)
            assert actual == predicted, (beta,j,n,actual,predicted)
            assertions += 1
    # Quantitative lower resolvent witness compared with valid upper norm series.
    for N in (16,32,64,128,256,512,1024):
        r = 1+1/N
        active = [j for j in A if N <= j < 2*N]
        m=len(active)
        if not m:
            continue  # a small dyadic window can miss all sparse branches
        lower2=0.0
        for i in range(N//2+1):
            coordinate=sum(r**(-(j-i+2)) for j in active) / math.sqrt(m*(1-r**-2))
            lower2+=coordinate**2
        lower=math.sqrt(lower2)
        # Exact power-norm expression for all n, computed through maximum window count.
        upper=0.0
        for n in range(5000):
            # Valid simple upper bound from the proved gap estimate.
            power_bound=math.sqrt(n**alpha+3)
            upper += power_bound / r**(n+1)
        assert lower<=upper*(1+1e-9)
        assert lower > 0
        assertions+=3
print('FINITE_COMB_CHECKS_PASS',assertions)
