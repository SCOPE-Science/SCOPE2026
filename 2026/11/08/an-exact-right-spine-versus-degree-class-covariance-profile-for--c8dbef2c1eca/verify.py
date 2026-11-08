"""Independent rational checks of the random-BST right-spine/degree covariance."""
from fractions import Fraction
from itertools import permutations
from math import factorial


def theoretical(n):
    if n <= 2:
        return Fraction(0)
    return Fraction((n - 2)*(n + 1), 12*n*(n - 1))


def moments_by_root_recursion(limit=100):
    # E[L], E[R], E[L R] from conditional independence of split subtrees.
    leaves = [Fraction(0)] * (limit+1)
    spine = [Fraction(0)] * (limit+1)
    product = [Fraction(0)] * (limit+1)
    for n in range(1, limit+1):
        if n == 1:
            leaves[n] = spine[n] = product[n] = Fraction(1)
            continue
        for b in range(n):
            a = n - 1 - b
            leaves[n] += (leaves[a] + leaves[b])/n
            spine[n] += (1 + spine[b])/n
            product[n] += (leaves[a] + leaves[b] +
                           product[b] + leaves[a]*spine[b])/n
        assert leaves[n] == Fraction(n+1,3)
        assert spine[n] == sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))
        cov = product[n] - leaves[n]*spine[n]
        assert cov == theoretical(n), (n, cov, theoretical(n))
    return limit-1


def values_for_permutation(p):
    # Node arrays indexed by sorted keys; root linked by random insertion order.
    n = len(p)
    left = [-1]*n
    right = [-1]*n
    root = p[0]-1
    for key in p[1:]:
        cur = root
        idx = key-1
        while True:
            if idx < cur:
                if left[cur] == -1:
                    left[cur] = idx
                    break
                cur = left[cur]
            else:
                if right[cur] == -1:
                    right[cur] = idx
                    break
                cur = right[cur]
    z0 = sum(left[j] == -1 and right[j] == -1 for j in range(n))
    z2 = sum(left[j] != -1 and right[j] != -1 for j in range(n))
    z1 = n - z0-z2
    spine=1
    node=root
    while right[node] != -1:
        node=right[node]
        spine+=1
    assert z0 == z2+1
    return spine, (z0,z1,z2)


def exhaustive(limit=9):
    checks = 0
    for n in range(1,limit+1):
        sumr=sumz=[0,0,0]  # replaced below
        sumr=0
        sums=[0,0,0]
        cross=[0,0,0]
        count=0
        for p in permutations(range(1,n+1)):
            r,counts=values_for_permutation(p)
            count+=1
            sumr+=r
            for k in range(3):
                sums[k]+=counts[k]
                cross[k]+=r*counts[k]
        assert count==factorial(n)
        if n>=2:
            expected=[theoretical(n),-2*theoretical(n),theoretical(n)]
        else:
            expected=[Fraction(0)]*3
        for k in range(3):
            cov=Fraction(cross[k],count)-Fraction(sumr*sums[k],count*count)
            assert cov==expected[k], (n,k,cov,expected[k])
            checks+=1
    return checks


if __name__ == '__main__':
    nr=moments_by_root_recursion(160)
    ne=exhaustive(9)
    print('PASS:',nr,'exact recursion covariance checks,',ne,
          'exhaustive mixed degree-covariance checks; permutations through n=9.')
