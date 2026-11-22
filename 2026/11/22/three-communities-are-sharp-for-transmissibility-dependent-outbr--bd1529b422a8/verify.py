"""Standalone reproducibility checks for Poisson multitype epidemic source rankings.
Proof is in RESULT.md; this file tests algebraic certificates and numerical fixed points.
"""
from fractions import Fraction as Q
import math
import random

A = [
    [Q(1,10), Q(1,1000), Q(5)],
    [Q(1,1000), Q(2), Q(1,1000)],
    [Q(1,1000), Q(1,1000), Q(1,10)],
]
assert all(x>0 for row in A for x in row)
r = [sum(row) for row in A]
assert r == [Q(5101,1000),Q(1001,500),Q(51,500)]
# Exact algebraic inequalities in proof: at t=1, p3 <= 1/450,
# p1 <= 109/8100 < 1/50 < 1/2 < p2.
p3_bound=Q(1,450)
p1_bound=(Q(1,1000)+Q(5)*p3_bound)/(1-Q(1,10))
assert p1_bound==Q(109,8100) and p1_bound<Q(1,50)
# At t=20, p3>1/2, so p1>1-exp(-50)>1-exp(-40.04)>=p2.
assert Q(20)*Q(5)*Q(1,2)>Q(20)*r[1]


def p_survival(matrix,t=1.0):
    x = [1.0]*len(matrix)
    for k in range(20000):
        y = [-math.expm1(-t*sum(float(a)*v for a,v in zip(row,x))) for row in matrix]
        if max(abs(a-b) for a,b in zip(x,y))<3e-14: return y
        x = y
    raise AssertionError('no convergence')

p1=p_survival(A,1)
p20=p_survival(A,20)
assert p1[0]<.02 and p1[1]>.5
assert all(0<x<1 for x in p1)
# At 20x, double precision rounds both probabilities to 1; compare the
# accurately computed negative log extinction fractions instead.
exponents=[20*sum(float(a)*v for a,v in zip(row,p20)) for row in A]
assert exponents[0]>exponents[1]
assert all(0<x<=1 for x in p20)
print('At unit transmission:',p1)
print('At 20x transmission:',p20)

# Two-type order theorem tested across positive matrices, with independent
# scalar rescaling on each sample. Numerical testing is NOT the infinite proof.
rng=random.Random(1776)
checked=0
for trial in range(1500):
    B=[[10**rng.uniform(-1,1.5) for j in range(2)] for i in range(2)]
    t=10**rng.uniform(-.1,1.25)
    z=p_survival(B,t)
    if min(z)<1e-7: continue
    d=sum(B[0])-sum(B[1]); e=z[0]-z[1]
    if abs(d)>1e-6 and abs(e)>1e-9:
        assert d*e>0,(B,t,z)
        checked+=1
assert checked>500
print('Two-type positive-matrix numerical tests:',checked)
print('All exact certificate checks passed.')
