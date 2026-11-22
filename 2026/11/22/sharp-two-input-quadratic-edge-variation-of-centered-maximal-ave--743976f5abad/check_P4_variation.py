#!/usr/bin/env python3
"""Exact enumeration certificate for the centered path-four maximal averaging inequality."""
from itertools import product, combinations

N=4
balls=[]
for vertex in range(N):
    b=[]
    for radius in range(N):
        points=[j for j in range(N) if abs(vertex-j)<=radius]
        if points not in b:
            b.append(points)
    balls.append(b)
assert list(map(len,balls))==[4,3,3,4]
# Edge difference B and right inverse T, so B*T=I.
B=[[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]]
T=[[1,1,1],[0,1,1],[0,0,1],[0,0,0]]

def mul(a,b):
    return [[sum(x*y for x,y in zip(ar,col)) for col in zip(*b)] for ar in a]

def transpose(a): return [list(x) for x in zip(*a)]
def determinant(a):
    if len(a)==1: return a[0][0]
    if len(a)==2: return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def principal_minors(a):
    return [(ind, determinant([[a[i][j] for j in ind] for i in ind]))
            for r in (1,2,3) for ind in combinations(range(3),r)]

zero_minors=0
saturating=[]
smallest=10**100
for mask in product(*[range(len(x)) for x in balls]):
    a12=[[12//len(balls[i][choice]) if j in balls[i][choice] else 0
          for j in range(N)] for i,choice in enumerate(mask)]
    h12=mul(mul(B,a12),T)
    gram=mul(transpose(h12),h12)
    defect=[[216*(i==j)-gram[i][j] for j in range(3)] for i in range(3)]
    minors=principal_minors(defect)
    assert all(v>=0 for ind,v in minors), (mask,minors)
    smallest=min(smallest,min(v for ind,v in minors))
    if determinant(defect)==0:
        saturating.append(mask)

assert len(saturating)==2 and sorted(saturating)==[(0,2,2,0),(3,0,0,3)],saturating
assert smallest==0
print('PASS: 144 exact branch positive-semidefinite certificates')
print('Equality branch masks:',saturating)

# The strict (0,2,2,0) branch is active at (8,1,1,8), with 0/2-based radii.
base=[8,1,1,8]
for i,r in enumerate((0,2,2,0)):
    averages=[sum(base[j] for j in s)/len(s) for s in balls[i]]
    assert averages[r]>max(v for j,v in enumerate(averages) if j!=r),(i,averages)
# Norming increment direction is (1,1,1), represented by T*(1,1,1)=(3,2,1,0).
# Choose perturbation epsilon = 1/100; both signals stay in same strict region.
from fractions import Fraction as F
pert=[F(3,100),F(2,100),F(1,100),F(0)]
base=[F(x) for x in base]
shifted=[x+y for x,y in zip(base,pert)]
for ff in (base,shifted):
    for i,r in enumerate((0,2,2,0)):
        means=[sum(ff[j] for j in s)/len(s) for s in balls[i]]
        assert means[r]>max(v for j,v in enumerate(means) if j!=r)

def maxima(ff):return [max(sum(ff[j] for j in s)/len(s) for s in balls[i]) for i in range(4)]

def edgenorm2(ff): return sum((ff[i]-ff[i+1])**2 for i in range(3))
assert edgenorm2([a-b for a,b in zip(maxima(shifted),maxima(base))])*2 == edgenorm2(pert)*3
print('PASS: positive rational maximizing pair, exact squared ratio 3/2')
