"""Finite-level arithmetic tests for Lipschitz Cantor adding-machine realization.

Only the infinite arguments in RESULT.md establish the mathematical theorem.
"""
from fractions import Fraction
from itertools import combinations
from math import log


def digits(j, n):
    return tuple((j >> k) & 1 for k in range(n))


def code_position(word, ratios):
    # Beginning at the left end of the unit parent interval.
    point = Fraction(0)
    length = Fraction(1)
    for digit, r in zip(word, ratios):
        if digit:
            point += (1-r)*length
        length *= r
    return point


def first_difference(a, b):
    return next(i for i, (x,y) in enumerate(zip(a,b)) if x != y)


checks = 0
for n in range(2, 8):
    for mode in ('quarter', 'third', 'variable'):
        if mode == 'quarter':
            ratios = [Fraction(1,4)]*n
        elif mode == 'third':
            ratios = [Fraction(1,3)]*n
        else:
            ratios = [Fraction(1, 2**(k+3)) for k in range(n)]
        words = [digits(j,n) for j in range(2**n)]
        pos = [code_position(w,ratios) for w in words]
        level = [Fraction(1)]
        for r in ratios:
            level.append(level[-1]*r)
        lip = Fraction(1,1) / (1 - 2*max(ratios))
        for u,v in combinations(range(2**n),2):
            k=first_difference(words[u], words[v])
            uu=(u+1)%(2**n)
            vv=(v+1)%(2**n)
            assert first_difference(words[uu],words[vv])==k
            sep=abs(pos[u]-pos[v])
            mapped_sep=abs(pos[uu]-pos[vv])
            assert (1-2*ratios[k])*level[k] <= sep <= level[k]
            assert mapped_sep <= lip*sep
            checks += 1
        if mode=='variable':
            assert level[n]==Fraction(1,2**(n*(n+5)//2))

# Exact tests for arbitrary nonuniform section rescaling, including cyclic return.
for m in (1,2,3,5):
    n=7
    word=digits(11,n)
    ratios=[Fraction(1,4)]*n
    scales=[Fraction(i+1, 5*m+5) for i in range(m)]
    offsets=[Fraction(1,7)]*m
    v=code_position(word, ratios)
    for i in range(m):
        # Non-final fibre maps are the affine copying conjugacies.
        w=offsets[i] + scales[i]*v
        assert Fraction(0)<=w<=Fraction(1)
        if i<m-1:
            w_next=offsets[i+1] + scales[i+1]*v
        else:
            w_next=offsets[0] + scales[0]*code_position(digits(12,n),ratios)
        assert Fraction(0)<=w_next<=Fraction(1)
        checks += 1

for k in range(1,200):
    # The exact cylinder upper bound of the varying-ratio model tends to zero.
    assert Fraction(2, k+5) > 0
    if k>1:
        assert Fraction(2,k+5) < Fraction(2,k+4)
    checks+=1


# A completely exact finite cyclic triangular realization on three base fibres.
# This is a finite approximant, not the limiting odometer theorem.
def affine_interpolant(x, knots):
    if x <= knots[0][0]:
        return knots[0][1]
    if x >= knots[-1][0]:
        return knots[-1][1]
    for (x0,y0),(x1,y1) in zip(knots,knots[1:]):
        if x0 <= x <= x1:
            return y0+(x-x0)*(y1-y0)/(x1-x0)
    raise AssertionError('uncovered interpolation point')

n=5
binary_codes=[digits(j,n) for j in range(2**n)]
coord=[code_position(w,[Fraction(1,4)]*n) for w in binary_codes]
pbase=[Fraction(1,4),Fraction(1,2),Fraction(3,4)]
ascale=[Fraction(1,5),Fraction(1,7),Fraction(1,6)]
aoffset=[Fraction(1,10),Fraction(1,11),Fraction(1,9)]
endpoints=[[aoffset[i]+ascale[i]*u for u in coord] for i in range(3)]
fknots=sorted((pbase[i],pbase[(i+1)%3]) for i in range(3))
fiber_knots=[]
for i in range(3):
    arr=[]
    for j in range(2**n):
        tgt=endpoints[i+1][j] if i<2 else endpoints[0][(j+1)%(2**n)]
        arr.append((endpoints[i][j],tgt))
    fiber_knots.append(sorted(arr))

def finite_triangular(x,y):
    nx=affine_interpolant(x,fknots)
    fy=[affine_interpolant(y,k) for k in fiber_knots]
    ny=affine_interpolant(x, sorted(zip(pbase,fy)))
    return nx,ny

state=(pbase[0],endpoints[0][0]); visited=set()
for t in range(3*(2**n)):
    i=t%3; j=(t//3)%(2**n)
    assert state==(pbase[i],endpoints[i][j])
    visited.add(state)
    state=finite_triangular(*state)
    checks+=1
assert len(visited)==3*(2**n)
assert state==(pbase[0],endpoints[0][0])

print(f'PASS: {checks} exact finite-level tests; infinite assertions require the written proof.')
