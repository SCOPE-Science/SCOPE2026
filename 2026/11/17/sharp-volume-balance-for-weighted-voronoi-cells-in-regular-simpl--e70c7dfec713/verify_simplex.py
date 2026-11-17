"""Exact, standalone reproducibility checks for regular-simplex cubical cells.
Requires Python >=3.9 standard library only. Finite tests do not prove the theorem.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb


def algebraic_volume_fraction(b, i):
    d = len(b)-1
    others = [j for j in range(d+1) if j != i]
    answer = Q(0)
    for k in range(d+1):
        for S in combinations(others,k):
            remainder = 1-b[i]-sum((b[j] for j in S), Q(0))
            answer += (-1)**k * remainder**d / (k+1)
    return answer


def determinant(a):
    a = [list(r) for r in a]
    n = len(a)
    ans = Q(1)
    for k in range(n):
        r = next((j for j in range(k,n) if a[j][k]), None)
        if r is None:
            return Q(0)
        if r != k:
            a[r],a[k] = a[k],a[r]
            ans = -ans
        p = a[k][k]
        ans *= p
        for j in range(k+1,n):
            f = a[j][k]/p
            for h in range(k+1,n):
                a[j][h] -= f*a[k][h]
            a[j][k] = Q(0)
    return ans


def chain_volume_fraction(b, i):
    d = len(b)-1
    others = [j for j in range(d+1) if j != i]
    total = Q(0)
    for perm in permutations(others):
        S = {i}
        verts = []
        for j in range(d+1):
            missing = sum((b[k] for k in range(d+1) if k not in S), Q(0))
            p = [b[k]+missing/len(S) if k in S else Q(0) for k in range(d+1)]
            assert sum(p)==1 and all(x>=0 for x in p)
            verts.append(p[:d])
            if j<d: S.add(perm[j])
        mat = [[verts[k+1][r]-verts[0][r] for k in range(d)] for r in range(d)]
        det = determinant(mat)
        assert det != 0
        total += abs(det)    # full simplex has coordinate volume 1/d!
    return total


def check():
    tests = 0
    for d in range(2,7):
        for seed in range(3 if d<=5 else 1):
            nums = [1+((j+3)*(seed+5)+2*j*j)%13 for j in range(d+1)]
            b = [Q(x,sum(nums)) for x in nums]
            probabilities = [algebraic_volume_fraction(b,i) for i in range(d+1)]
            assert sum(probabilities)==1
            for i,p in enumerate(probabilities):
                s=1-b[i]
                assert s**d/d < p <= Q((d+1)**(d-1),d**d)*s**d
                assert chain_volume_fraction(b,i)==p
                tests += 1
    for d in range(2,10):
        s=Q(3,5); t=1-s
        uniform=[t]+[s/d]*d
        corner=[t,s]+[Q(0)]*(d-1)
        assert algebraic_volume_fraction(uniform,0)==Q((d+1)**(d-1),d**d)*s**d
        assert algebraic_volume_fraction(corner,0)==s**d/d
        tests += 2
    for d in range(2,8):
        for seed in range(10):
            nums=[1+((j+3)*(seed+8)+j*j)%19 for j in range(d+1)]
            b=[Q(x,sum(nums)) for x in nums]
            old=algebraic_volume_fraction(b,0)
            j,k = 1+(seed%d), 1+((seed+1)%d)
            avg=(b[j]+b[k])/2
            b[j]=b[k]=avg
            new=algebraic_volume_fraction(b,0)
            assert new>=old
            tests+=1
    print(f'PASS: {tests} exact rational test cases, independent flag-determinant volumes in dimensions 2--6')

if __name__=='__main__':
    check()
