#!/usr/bin/env python3
"""Exact finite diagnostics for the four-child Hadamard Haar endpoint constant."""
from fractions import Fraction
from itertools import product
from functools import lru_cache

CHILDREN = ((0,0),(0,1),(1,0),(1,1))
CHARS = tuple(tuple((-1)**(a[0]*x[0]+a[1]*x[1]) for x in CHILDREN)
              for a in ((1,0),(0,1),(1,1)))

def contrast_row(x,signs):
    return tuple(sum(signs[a]*CHARS[a][x]*CHARS[a][y] for a in range(3))
                 for y in range(4))

assert all(sum(CHARS[a][x]*CHARS[b][x] for x in range(4)) == (4 if a==b else 0)
           for a in range(3) for b in range(3))
C = sorted(set(contrast_row(0,s) for s in product((-1,1),repeat=3)))
assert len(C)==8
assert C == sorted(set(tuple(sign*(3 if y==target else -1) for y in range(4))
                       for sign in (-1,1) for target in range(4)))
print('LOCAL_HADAMARD_SIGNED_ROW_CLASSIFICATION_PASSED',len(C))

@lru_cache(None)
def bellman(k,u):
    if not k:
        return abs(u)
    return max(Fraction(1,4)*sum(abs(u+c[y]) for y in range(1,4))
               +bellman(k-1,(u+c[0])/4) for c in C)

def formula(k):
    return Fraction(4*k,3)+Fraction(5,9)+Fraction(4,9*4**k)

# Independent brute-force evaluation of the complete row mass: the three sibling
# cylinders at each level and its final distinguished leaf give a disjoint partition.
def brute_row_max(depth):
    best=Fraction(-1)
    patterns=0
    number_maximizers=0
    for blocks in product(C,repeat=depth):
        base=1
        total=Fraction(0)
        for j,c in enumerate(blocks):
            total+=sum(abs(base+4**j*c[y]) for y in range(1,4))*Fraction(1,4**(j+1))
            base+=4**j*c[0]
        total+=abs(base)*Fraction(1,4**depth)
        patterns+=1
        if total>best:
            best=total
            number_maximizers=1
        elif total==best:
            number_maximizers+=1
    return best,patterns,number_maximizers

for d in range(7):
    exact=bellman(d,Fraction(1))
    assert exact==formula(d),(d,exact,formula(d))
    if d<=5:
        separate,n,count=brute_row_max(d)
        assert separate==exact,(d,separate,exact)
        predicted_count=(1 if d==0 else 4 if d==1 else 16*3**(d-2))
        assert count==predicted_count,(d,count,predicted_count)
        print('DEPTH',d,'EXACT',exact,'INDEPENDENT_SIGN_ROWS',n,'SHARP_PATH_SIGNS',count)
    else:
        print('DEPTH',d,'EXACT',exact)

# Separate binary Haar recursion, derived from its own two-child contrast
# (not a lookup of a previously recorded endpoint result).
@lru_cache(None)
def binary_bellman(m,u):
    if not m:
        return abs(u)
    return max(Fraction(1,2)*abs(u-s)+binary_bellman(m-1,(u+s)/2)
               for s in (-1,1))
for d in range(7):
    assert binary_bellman(2*d,Fraction(1)) == formula(d)
print('INDEPENDENT_BINARY_TWO_STAGE_IDENTITY_PASSED',7)

# Check all affine Bellman branches on a rational test mesh (analytical proof
# handles every real parameter, not merely this mesh).
for k in range(1,5):
    A=Fraction(4*k,3)+Fraction(2,9)*(1-Fraction(1,4**k))
    B=(1+2*Fraction(1,4**k))/3
    for t in range(-16,17):
        u=Fraction(t,16)
        predicted=A+B*abs(u)
        assert bellman(k,u)==predicted,(k,u,bellman(k,u),predicted)
print('RATIONAL_AFFINE_BELLMAN_CHECKS_PASSED',4*33)

# Independent full Haar matrix at depth up to three using a deterministic
# finite sample of sign configurations for all local coefficients.
def matrix_row(depth, x, y, signs):
    value=signs[()]
    prefix=()
    for level in range(depth):
        if x[:level]!=y[:level]: break
        xs=x[level];ys=y[level]
        value+=4**level*sum(signs[prefix+(a,)]*CHARS[a][xs]*CHARS[a][ys]
                              for a in range(3))
        prefix=x[:level+1]
    return value

for d in range(1,4):
    words=list(product(range(4),repeat=d))
    nodes=[()] +[prefix+(a,) for level in range(d)
              for prefix in product(range(4),repeat=level) for a in range(3)]
    # Deterministic mixed signings, no dependence on other recorded computations.
    for seed in range(12):
        signs={node:(-1 if (hash((node,seed))%13)<6 else 1) for node in nodes}
        for x in words:
            mass=Fraction(sum(abs(matrix_row(d,x,y,signs)) for y in words),4**d)
            assert mass <=formula(d)
    print('FULL_MATRIX_HAAR_ROW_BOUND_PASSED',d,12*len(words))
print('ALL_FOUR_CHILD_HADAMARD_HAAR_DIAGNOSTICS_PASSED')
