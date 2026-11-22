"""Exact rational finite certificate for the centered P4 maximal BV coefficient."""
from fractions import Fraction as F
from itertools import product
import random

BALLS = [
    [(0,), (0, 1), (0, 1, 2), (0, 1, 2, 3)],
    [(1,), (0, 1, 2), (0, 1, 2, 3)],
    [(2,), (1, 2, 3), (0, 1, 2, 3)],
    [(3,), (2, 3), (1, 2, 3), (0, 1, 2, 3)],
]

def averages(x, i):
    return [sum(x[j] for j in b) / len(b) for b in BALLS[i]]

def maxim(x):
    return [max(averages(x,i)) for i in range(4)]

def variation(x):
    return sum(abs(x[i+1]-x[i]) for i in range(3))

def matrix(mask):
    out=[]
    for i,k in enumerate(mask):
        b=BALLS[i][k]
        out.append(tuple(F(int(j in b),len(b)) for j in range(4)))
    return out

def step_profile(A, j):
    return [sum(row[j+1:]) for row in A]

assert tuple(map(len, BALLS)) == (4,3,3,4)
maxima=[F(0),F(0),F(0)]
maximizers=[[],[],[]]
bad=[]
for mask in product(*[range(len(b)) for b in BALLS]):
    A=matrix(mask)
    vals=[]
    for j in range(3):
        z=variation(step_profile(A,j))
        vals.append(z)
        if z>maxima[j]:
            maxima[j]=z
            maximizers[j]=[mask]
        elif z==maxima[j]:
            maximizers[j].append(mask)
    if max(vals)>F(11,6):
        bad.append((mask,max(vals)))
assert maxima == [F(3,2),F(2),F(3,2)], maxima
assert bad==[((3,0,0,3),F(2))],bad
print('ALL_144_MASKS_RATIONAL_EXHAUSTIVE_PASS', 'step_maxima=',tuple(map(str,maxima)), 'unique_excluded=',bad[0][0])

f=[F(x) for x in (0,26,25,21)]
g=[F(x) for x in (0,26,26,22)]
yf=maxim(f)
yg=maxim(g)
assert yf==list(map(F,(18,26,25,24))),yf
assert yg==[F(37,2),F(26),F(26),F(74,3)],yg
assert variation([x-y for x,y in zip(yf,yg)])==F(11,6)
assert variation([x-y for x,y in zip(f,g)])==1
print('EXPLICIT_NONNEGATIVE_ATTAINING_PAIR_PASS',tuple(map(str,yf)),tuple(map(str,yg)))

rng=random.Random(20261117)
for k in range(10000):
    a=[F(rng.randrange(60),rng.randrange(1,7)) for i in range(4)]
    b=[F(rng.randrange(60),rng.randrange(1,7)) for i in range(4)]
    lhs=variation([p-q for p,q in zip(maxim(a),maxim(b))]); rhs=variation([p-q for p,q in zip(a,b)])
    assert lhs*6<=rhs*11,(k,a,b,lhs,rhs)
print('RANDOM_10000_EXACT_RATIONAL_TWO_INPUT_TESTS_PASS')
print('CENTERED_P4_BV_ALL_CHECKS_PASS')
