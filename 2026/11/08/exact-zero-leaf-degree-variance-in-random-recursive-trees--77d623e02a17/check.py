"""Finite exact checks for zero-leaf-degree recursive-tree variance.

Only Python standard library; finite tests do not establish the asymptotic proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, e


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def falling(n, k):
    if k < 0 or k > n:
        return 0
    ans = 1
    for j in range(k):
        ans *= n-j
    return ans


def single(n, i):
    return sum(((-1)**r*Fraction(choose(n-i,r),falling(n-1,r))
                for r in range(n-i+1)), Fraction(0))


def joint(n, i, h):
    assert 1 <= i < h <= n
    ans = Fraction(0)
    for r in range(n-i+1):
        for s in range(n-h+1):
            count = choose(n-i,r) if s == 0 else (
                choose(n-h,s)*choose(n-i-1-s,r))
            if count:
                assert r+s <= n-1
                ans += (-1)**(r+s)*Fraction(count, falling(n-1,r+s))
    return ans


def verify(n):
    sum_i = [0]*(n+1)
    sum_ih = {(i,h):0 for i in range(1,n+1) for h in range(i+1,n+1)}
    number = 0
    for parents in product(*(range(1,k) for k in range(2,n+1))):
        children = [[] for _ in range(n+1)]
        for j,parent in enumerate(parents, 2):
            children[parent].append(j)
        z = [int(not any(not children[c] for c in children[i]))
             for i in range(n+1)]
        parent = [0,0]+list(parents)
        degree = [0]+[len(children[i])+(i != 1) for i in range(1,n+1)]
        actual_zero = sum(not any(degree[c]==1 for c in children[i])
                          and (i==1 or degree[parent[i]] != 1)
                          for i in range(1,n+1))
        delta = sum(z[1:])-actual_zero
        assert 0<=delta<=int(degree[1]==1), (n, parents, delta)
        for i in range(1,n+1):
            sum_i[i] += z[i]
        for i,h in sum_ih:
            sum_ih[i,h] += z[i]*z[h]
        number += 1
    for i in range(1,n+1):
        assert single(n,i) == Fraction(sum_i[i],number)
    for i,h in sum_ih:
        assert joint(n,i,h) == Fraction(sum_ih[i,h],number)
    mu = sum((Fraction(v,number) for v in sum_i[1:]),Fraction(0))
    second = mu + 2*sum((Fraction(v,number) for v in sum_ih.values()),Fraction(0))
    variance = second-mu**2
    print(f'n={n}: {number} trees; mean={mu}; variance={variance}')
    return variance


def verify_constant():
    diagonal = .5-1/e+.5/e**2
    ordered_pair = (5-e**2)/(4*e**2)
    total = diagonal+2*ordered_pair
    target = (3-e)/e**2
    assert abs(total-target)<1e-14 and 0<target<.04
    # Independent numerical midpoint integration of the two-point kernel.
    from math import exp
    grid=800
    step=1/grid
    midpoint_sum=0.0
    for ia in range(grid):
        a=(ia+.5)*step
        for ib in range(ia):
            b=(ib+.5)*step
            midpoint_sum += exp(-a)*((1+(a-1)*b)*exp(-b)-1)
    integrated=midpoint_sum*step*step
    assert abs(integrated-ordered_pair)<.0004, (integrated,ordered_pair)
    print('constant=',repr(target),'pair numerical=',integrated)


if __name__=='__main__':
    for n in range(3,9):
        verify(n)
    verify_constant()
    print('PASS: all exhaustive rational and numerical consistency checks')
