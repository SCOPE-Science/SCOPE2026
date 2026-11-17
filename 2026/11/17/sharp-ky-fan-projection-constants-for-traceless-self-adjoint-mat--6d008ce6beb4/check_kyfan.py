"""Exact finite diagnostics for the Ky Fan trace-centering theorem.

Only Python's standard library is required.  All comparisons use Fractions.
The universal proof is algebraic; this script independently enumerates
sign-support vertices of the dual Ky Fan ball at small matrix orders.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def kyfan(x, k):
    return sum(sorted((abs(v) for v in x), reverse=True)[:k], Q(0))


def center(x):
    n = len(x)
    avg = sum(x, Q(0)) / n
    return tuple(v-avg for v in x)


def dual_kyfan(x, k):
    return max(max(abs(v) for v in x), sum((abs(v) for v in x), Q(0))/k)


def predicted(n, k):
    return max(Q(2*(n-k), n), Q(n+k-2, n))


def dual_polytope_exhaustion(n, k):
    best = Q(0)
    for supp in combinations(range(n), k):
        for signs in product((-1, 1), repeat=k):
            b=[Q(0)]*n
            for idx, sgn in zip(supp, signs):
                b[idx]=Q(sgn)
            best=max(best, dual_kyfan(center(b),k))
    return best


def check():
    cases=0
    for n in range(2,11):
        for k in range(1,n+1):
            norm=predicted(n,k)
            # Completely independent evaluation over vertices of the dual ball.
            assert dual_polytope_exhaustion(n,k)==norm,(n,k)
            # Explicit primal extremizers in each branch (real diagonal matrices).
            spike=tuple(Q(int(j==0)) for j in range(n))
            assert kyfan(center(spike),k)/kyfan(spike,k)==Q(n+k-2,n)
            if n>=2*k:
                plateau=tuple(Q(1) if j<k else Q(-1) for j in range(n))
                assert kyfan(center(plateau),k)/kyfan(plateau,k)==Q(2*(n-k),n)
            assert norm>=1
            cases+=1
    print('DUAL_POLYTOPE_SIGN_SUPPORT_CASES_PASSED',cases)
    print('EXPLICIT_PRIMAL_EXTREMIZERS_AND_THRESHOLD_CASES_PASSED',cases)
    for n in range(2,16):
        nonexp=[k for k in range(1,n+1) if predicted(n,k)==1]
        expected={2:[1,2],3:[2],4:[2]}.get(n,[])
        assert nonexp==expected,(n,nonexp,expected)
    print('COMPLETE_NONEXPANSIVITY_CLASSIFICATION_PASSED',14)
    print('ALL_EXACT_KY_FAN_CENTERING_DIAGNOSTICS_PASSED')


if __name__ == '__main__':
    check()
