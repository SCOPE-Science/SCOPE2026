"""Exact finite checks for intrinsic random translates of dilated hypersimplices.

No numerical check is used as an infinite-dimensional proof.
Run: python3 checker.py
"""
import itertools
import math
import random


def eulerian_row(m):
    if m < 1:
        raise ValueError('m must be positive')
    row = [1]
    for n in range(2, m + 1):
        row = [(j + 1) * (row[j] if j < len(row) else 0)
               + (n - j) * (row[j - 1] if j else 0)
               for j in range(n)]
    return row


def bounded_compositions(n, t, s):
    if s < 0 or s > n * (t - 1):
        return 0
    return sum((-1)**a * math.comb(n, a)
               * math.comb(s - t*a + n-1, n-1)
               for a in range(min(n, s//t) + 1))


def predicted_count(n, k, t, j):
    return bounded_compositions(n, t, k*t - j)


def direct_translated_count(n, k, t, first_fracs):
    """Translate the sum-kt hyperplane polytope by a sum-zero vector.

    Choose a=(-u_1,...,-u_{n-1},sum u_i). Enumerate all possible
    integer first coordinates, compute the last one using sum=kt.
    """
    s = sum(first_fracs)
    count = 0
    for first in itertools.product(range(t), repeat=n-1):
        z_last = k*t - sum(first)
        if s < z_last < s+t:
            count += 1
    return count


def test_exact():
    cases = 0
    for n in range(2, 11):
        euler = eulerian_row(n - 1)
        assert sum(euler) == math.factorial(n-1)
        assert euler == euler[::-1]
        for k in range(1, n):
            for t in range(1, 6):
                counts = [predicted_count(n,k,t,j) for j in range(1,n)]
                assert all(c>=0 for c in counts)
                # Haar expected count = normalized volume of t*Delta_{k,n}.
                assert sum(euler[j-1]*counts[j-1] for j in range(1,n)) == t**(n-1)*euler[k-1]
                if n<=5 and t<=4:
                    for j in range(1,n):
                        direct=sum(sum(v)==k*t-j for v in itertools.product(range(t),repeat=n))
                        assert direct == counts[j-1]
                cases+=1
    return cases


def test_geometry():
    rng = random.Random(20261118)
    cases = 0
    for n in range(2,7):
        for k in range(1,n):
            for t in range(1,5):
                for _ in range(12):
                    u=[rng.random() for _ in range(n-1)]
                    j=math.ceil(sum(u))
                    assert direct_translated_count(n,k,t,u)==predicted_count(n,k,t,j)
                    cases+=1
    return cases


def test_limit_moments():
    rows=[]
    for n in [40,80,160,320]:
        e=eulerian_row(n-1)
        fac=math.factorial(n-1)
        k=n//2
        baseline=n*math.log(2)-math.log(math.pi*n/2)/2
        errors=[]
        for j in range(1,n):
            s=2*k-j
            if not 0<=s<=n:continue
            val=math.lgamma(n+1)-math.lgamma(s+1)-math.lgamma(n-s+1)
            errors.append((e[j-1]/fac,val-baseline))
        mean=sum(p*v for p,v in errors)
        second=sum(p*v*v for p,v in errors)
        rows.append((n,mean,second-mean*mean))
    # Limits are mean=-1/6, variance=1/18; numerical checks only.
    assert abs(rows[-1][1]+1/6)<0.02,rows
    assert abs(rows[-1][2]-1/18)<0.02,rows
    return rows


def main():
    exact=test_exact()
    geom=test_geometry()
    moments=test_limit_moments()
    print('PASS',exact,'exact finite coefficient/mean cases;',geom,'direct translated-geometry cases')
    print('centering-deficit mean/variance checks (n,mean,var):')
    for record in moments:
        print(record)


if __name__=='__main__':
    main()
