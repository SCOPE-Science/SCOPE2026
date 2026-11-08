"""Exact rational checks of additive-projection norming-row masking.

Usage: python verify.py
This is finite corroboration of the analytical theorem, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product
from math import prod


def rows(weights):
    return list(product(*(range(len(w)) for w in weights)))


def row_norm_direct(weights, x):
    d = len(weights)
    total = F(0)
    for y in rows(weights):
        mass = prod(weights[i][y[i]] for i in range(d))
        # direct expression via one-coordinate conditional expectations
        kernel = sum((F(1, 1) / weights[i][x[i]]) if y[i] == x[i]
                     else F(0) for i in range(d)) - (d - 1)
        total += mass * abs(kernel)
    return total


def verify_mask(weights, R, T):
    d = len(weights)
    assert len(R)+len(T)==d and set(R).isdisjoint(T)
    minima = [min(w) for w in weights]
    assert all(minima[i] * (d-1) < 1 for i in R)
    assert sum((1/minima[i] for i in T), F(0)) < d-1
    best = 1 + 2 * (len(R)-1)*prod(1-minima[i] for i in R)
    expected = {x for x in rows(weights) if all(weights[i][x[i]]==minima[i] for i in R)}
    actual = {x for x in rows(weights) if row_norm_direct(weights, x)==best}
    assert actual == expected, (actual,expected)
    # Strict-loss certificate for points disagreeing with mandatory rare atoms.
    for x in rows(weights):
        val = row_norm_direct(weights,x)
        assert val <= best
        for i in R:
            qi = weights[i][x[i]]
            if qi > minima[i]:
                bound = 2*prod(1-weights[j][x[j]] for j in range(d) if j!=i)*min((d-1)*(qi-minima[i]), 1-(d-1)*minima[i])
                assert best - val >= bound > 0, (x,i,best,val,bound)
    return len(actual),best


def binary_example(k):
    d=3*k+2
    R=list(range(2*k+2)); T=list(range(2*k+2,d))
    small=F(1,2*d); common=F(1,3)
    weights=[[1-small,small] for _ in R]+[[1-common,common] for _ in T]
    count, best=verify_mask(weights,R,T)
    assert count==2**k
    assert best==1+2*(2*k+1)*(1-small)**(2*k+2)
    print('BINARY_MASK_FACE_OK',k,'dimension',d,'norming_rows',count,'norm',str(best))


def categorical_example():
    d=5; R=list(range(4));T=[4]
    p=F(1,10)
    # last coordinate has all 3 atom weights distinct, no rare-atom symmetry
    weights=[[p,1-p] for _ in R]+[[F(3,10),F(1,3),F(11,30)]]
    count,best=verify_mask(weights,R,T)
    assert count == 3
    print('CATEGORICAL_MASK_FACE_OK',count,'norm',str(best))


def verify_telescope():
    # Compare one-coordinate strictness with the all-subset crossing criterion.
    examples = [ [F(1,4),F(1,3),F(2,5)],
                 [F(1,6),F(1,3),F(2,5),F(1,4)],
                 [F(1,10),F(1,10),F(1,10),F(1,3),F(1,3)] ]
    n=0
    for minima in examples:
        d=len(minima)
        for bits in product((0,1), repeat=d):
            q=[(1-z if b else z) for z,b in zip(minima,bits)]
            base=row_norm_bernoulli(q)
            for i in range(d):
                if q[i]==minima[i]:continue
                new=q.copy();new[i]=minima[i]
                strict=any(0 < d-1-sum((F(1)/q[j] for j in range(d) if j!=i and ((mask>>j)&1)),F(0)) < 1/minima[i]
                           for mask in range(1<<d))
                assert (row_norm_bernoulli(new)>base)==strict, (minima,bits,i)
                n+=1
    print('EXACT_COORDINATE_CROSSING_CRITERION_OK',n)


def row_norm_bernoulli(q):
    d=len(q)
    v=F(0)
    for y in product([0,1],repeat=d):
        p=prod(q[i] if y[i] else 1-q[i] for i in range(d))
        v+=p*abs(sum((F(y[i])/q[i] for i in range(d)),F(0))-(d-1))
    return v


if __name__=='__main__':
    binary_example(1)
    binary_example(2)
    categorical_example()
    verify_telescope()
    print('ALL_MASKED_ADDITIVE_PROJECTOR_CHECKS_OK')
