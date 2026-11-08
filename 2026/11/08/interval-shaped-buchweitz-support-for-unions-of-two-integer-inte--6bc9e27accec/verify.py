"""Exact reproducibility checks for the two-interval Buchweitz theorem.

The theorem for infinitely many parameters and n is proved symbolically
in RESULT.md; these finite comparisons are diagnostic only.
"""
from itertools import product


def beta_gap(a, b, q, n):
    # Direct adjacent-gap formula, valid for all a,q >=1, b>=a+2, n>=2.
    gaps = sum(max(0, b - 1 - n*a + k*(a-q)) for k in range(n))
    return n*(b+q-2*(a+q+1))+(a+q+2)-gaps


def beta_intervals(a, b, q, n):
    # Independently count the union of the n+1 integer intervals.
    intervals = [(k*b, k*(b+q)+(n-k)*a) for k in range(n+1)]
    total = 0
    right = -1
    for start, end in intervals:
        total += max(0, end-max(start, right+1)+1)
        right = max(right, end)
    return total-(2*n-1)*(a+q+1)


def beta_direct(a, b, q, n):
    # Distinct integer sums by direct bitset recurrence, independent of
    # the sumset interval decomposition.
    A = list(range(a+1))+list(range(b,b+q+1))
    bits = 1
    for _ in range(n):
        nxt=0
        for x in A:
            nxt |= bits << x
        bits=nxt
    return bits.bit_count()-(2*n-1)*(len(A)-1)


if __name__ == '__main__':
    checked_full = 0
    for a, q in product(range(1,7), repeat=2):
        for b in range(a+2, a+17):
            for n in range(2,13):
                one = beta_gap(a,b,q,n)
                assert one == beta_intervals(a,b,q,n)
                assert one == beta_direct(a,b,q,n)
                checked_full += 1
    checked_interval = 0
    checked_boundary = 0
    for a, q in product(range(1,13), repeat=2):
        for b in range(a+2, a+82):
            vals = [beta_gap(a,b,q,n) for n in range(2,82)]
            indices = [n for n, v in enumerate(vals,2) if v > 0]
            assert all(y == x+1 for x,y in zip(indices,indices[1:]))
            assert beta_gap(a,b,q,2) <= 0
            checked_interval += 1
            if a >= q:
                n0 = max(2, (b-1+a-1)//a)
                if n0 >= 4:
                    assert beta_gap(a,b,q,n0)>0
                    checked_boundary += 1
    print(f'DIRECT_EXACT_CASES={checked_full}')
    print(f'INTERVAL_SUPPORT_PARAMETER_CASES={checked_interval}')
    print(f'BOUNDARY_POSITIVITY_PARAMETER_CASES={checked_boundary}')
    print('EXAMPLE_A_[0,1]_U_[4,5]=B={3}:', [n for n in range(2,20) if beta_gap(1,4,1,n)>0])
    print('ALL_FINITE_CHECKS_PASSED')
