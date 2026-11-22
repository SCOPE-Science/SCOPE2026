"""Exact rational checks for a size-resolved binary-fragmentation and survival cascade."""
from fractions import Fraction as Q
from itertools import permutations, product
from random import Random


def multiply(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def apply(A, x):
    return [sum((a * b for a, b in zip(row, x)), Q(0)) for row in A]


def transfer(s, p):
    n = len(s)
    T = [[Q(0) for _ in range(n)] for _ in range(n)]
    for j in range(n-1):
        T[j][j] = s[j] * (1-p)
        T[j+1][j] = s[j+1] * p
    T[-1][-1] = s[-1]
    return T


def evolve(s, schedule, x):
    for p in schedule:
        x = apply(transfer(s, p), x)
    return x


def verify_local(s, p, q):
    n = len(s)
    A, B = transfer(s, p), transfer(s, q)
    # Small then large is A @ B, and vice versa B @ A.
    diff = [[a-b for a, b in zip(row1,row2)]
            for row1,row2 in zip(multiply(A,B), multiply(B,A))]
    for j in range(n):
        for i in range(n):
            target = (p-q)*s[i]*(s[j]-s[i]) if i==j+1 else Q(0)
            assert diff[i][j] == target, (n, s, p, q, i, j)


def main():
    tests = 0
    r = Random(22147)
    for n in range(2,8):
        for _ in range(120):
            raw = sorted([r.randint(1,20) for i in range(n)], reverse=True)
            s = [Q(x, 20) for x in raw]
            p = Q(r.randint(0,20),20)
            q = Q(r.randint(0,20),20)
            verify_local(s,p,q)
            tests += n*n
    for n in range(2,6):
        for _ in range(65):
            s = [Q(x,20) for x in sorted([r.randint(1,20) for i in range(n)],reverse=True)]
            schedule = [Q(r.randint(0,4),4) for j in range(4)]
            x = [Q(r.randint(0,10),10) for j in range(n)]
            lo = evolve(s, sorted(schedule), x)
            hi = evolve(s, sorted(schedule,reverse=True), x)
            for z in set(permutations(schedule)):
                v=evolve(s,z,x)
                assert all(a>=b>=c for a,b,c in zip(lo,v,hi))
                tests += n
    # A complete nontrivial exact example and its sign reversal when survival rises.
    s = [Q(1),Q(3,4),Q(1,2),Q(1,4)]
    x=[Q(1),Q(0),Q(0),Q(0)]
    lo=evolve(s,[Q(1,4),Q(3,4)],x)
    hi=evolve(s,[Q(3,4),Q(1,4)],x)
    assert lo == [Q(3,16),Q(117,256),Q(9,128),Q(0)]
    assert hi == [Q(3,16),Q(93,256),Q(9,128),Q(0)]
    s2=[Q(1,4),Q(1,2),Q(3,4)]
    lo2=evolve(s2,[Q(1,4),Q(3,4)],[Q(1),Q(0),Q(0)])
    hi2=evolve(s2,[Q(3,4),Q(1,4)],[Q(1),Q(0),Q(0)])
    assert hi2[1]>lo2[1]
    print('PASS:', tests, 'exact-rational coefficient and permutation assertions')


if __name__ == '__main__':
    main()
