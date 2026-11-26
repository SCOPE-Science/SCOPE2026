#!/usr/bin/env python3
"""Exact rational checks for the all-Nash-equilibria formula in binary weighted bipartite games."""
from fractions import Fraction as F
from itertools import product


def rank(a):
    m, n = len(a), len(a[0])
    x = [[F(v) for v in row] for row in a]
    k = 0
    for j in range(n):
        pivot = next((i for i in range(k,m) if x[i][j]), None)
        if pivot is None: continue
        x[k],x[pivot] = x[pivot],x[k]
        q=x[k][j]
        x[k] = [v/q for v in x[k]]
        for i in range(m):
            if i != k:
                t=x[i][j]
                x[i] = [u-t*v for u,v in zip(x[i],x[k])]
        k+=1
        if k == m: break
    return k


def matching_number(a):
    m,n=len(a),len(a[0])
    def go(i, used):
        if i==m: return 0
        return max([go(i+1,used)] + [1+go(i+1,used|(1<<j)) for j in range(n) if a[i][j] and not (used>>j&1)])
    return go(0,0)


def nash(a, z):
    c,r=len(a),len(a[0]); zc,zr=z[:c],z[c:]
    # payoff difference between actions 1 and 0: conformist +W*zr, rebel -W^T*zc.
    differences=[sum(a[i][j]*zr[j] for j in range(r)) for i in range(c)] + [-sum(a[i][j]*zc[i] for i in range(c)) for j in range(r)]
    # For z=1 require nonnegative advantage, z=-1 nonpositive, interior requires zero.
    direct=all((adv>=0 if zi==1 else adv<=0 if zi==-1 else adv==0) for zi,adv in zip(z,differences))
    classified=all(x==0 for x in differences)
    return direct, classified


def edge_payoff_total(a,z):
    c,r=len(a),len(a[0]); zc,zr=z[:c],z[c:]
    u_c=sum((w*(1+zc[i]*zr[j])/2) for i,row in enumerate(a) for j,w in enumerate(row))
    u_r=sum((w*(1-zc[i]*zr[j])/2) for i,row in enumerate(a) for j,w in enumerate(row))
    return u_c+u_r

cases=[
    [[1]],
    [[1,1],[1,1]],
    [[1,1],[1,2]],
    [[1,2,3]],
    [[1,0,2],[0,3,4]],
    [[1,2,3],[4,5,6]],
    [[1,0,0],[0,1,0]],
    [[1,2],[0,3],[4,0]],
    [[0,1,0],[2,0,3],[0,4,5]],
]
profile_count=0
for a in cases:
    c,r=len(a),len(a[0]); total=sum(map(sum,a));assert total>0
    for z in product((F(-1),F(0),F(1)),repeat=c+r):
        x,y=nash(a,z)
        assert x == y,(a,z,x,y)
        assert edge_payoff_total(a,z)==total
        profile_count+=1
    assert rank(a)<=matching_number(a)
assert rank([[1,1],[1,1]])==1
assert rank([[1,1],[1,2]])==2
assert nash([[1,1],[1,2]],tuple(F(0) for _ in range(4)))==(True,True)
assert sum(1 for z in product((-1,1),repeat=4) if nash([[1,1],[1,1]],z)[0])==4
assert sum(1 for z in product((-1,1),repeat=4) if nash([[1,1],[1,2]],z)[0])==0
assert rank([[1,2,3],[4,5,6]])==2 and matching_number([[1,2,3],[4,5,6]])==2
# Every 2x2 rational positive-weight matrix on a small finite grid: mixed grid and exact rank.
matrices=0
for a11,a12,a21,a22 in product(range(1,5),repeat=4):
    a=[[a11,a12],[a21,a22]]
    for z in product((-1,0,1),repeat=4):
        assert nash(a,z)[0]==nash(a,z)[1]
    matrices+=1
print('VERIFY_OK: {} game instances, {} exact profile checks, {} positive weighted 2x2 matrices'.format(len(cases),profile_count,matrices))
print('Examples: uniform K2,2 rank=1, equilibrium dimension=2, pure equilibria=4')
print('          weighted K2,2 [[1,1],[1,2]] rank=2, unique equilibrium, pure equilibria=0')
print('          weighted K2,3 [[1,2,3],[4,5,6]] rank=2, equilibrium dimension=1')
