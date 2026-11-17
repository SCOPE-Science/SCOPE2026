#!/usr/bin/env python3
"""Exact rational checks for the five-coordinate projection constant."""
from fractions import Fraction as F

u = (F(1), F(4,5), F(1,4), F(-1,4), F(-4,5))
v = (F(0), F(3,5), F(1), F(1), F(3,5))
f = (F(520,659),F(105,1318),F(110,659),F(-110,659),F(-105,1318))
g = (F(0),F(70,659),F(575,1318),F(575,1318),F(70,659))
assert sum(x*y for x,y in zip(f,u))==1
assert sum(x*y for x,y in zip(f,v))==0
assert sum(x*y for x,y in zip(g,u))==0
assert sum(x*y for x,y in zip(g,v))==1
P = [[ui*fj+vi*gj for fj,gj in zip(f,g)] for ui,vi in zip(u,v)]
c = F(845,659)
assert [sum(map(abs,row)) for row in P] == [c]*5
assert c < F(13,10) < F(4,3)
# Certificate is an identity of coefficient vectors, not a numerical sample.
L1   = (F(1),F(2),F(2),F(0),F(0))
L2a  = (F(4,5),F(0),F(0),F(6,5),F(6,5))
L2b  = (F(4,5),F(8,5),F(0),F(0),F(6,5))
L3   = (F(1,4),F(0),F(0),F(2),F(2))
A    = (F(1),F(8,5),F(1,2),F(0),F(0))
B    = (F(0),F(0),F(0),F(6,5),F(2))
assert [104*x+29*y+286*z+240*w for x,y,z,w in zip(L1,L2a,L2b,L3)] == [416*x+429*y for x,y in zip(A,B)]
assert 104+29+286+240 == 659
# The symmetry has the stated effect on both spanning vectors.
def S(x):return (-x[0],x[4],x[3],x[2],x[1])
assert S(u) == tuple(-x for x in u)
assert S(v) == v
# Every finite direct sum has the claimed projection norm and is idempotent.
for n in (3,4,5,9,17):
    size = 2*n
    M = [[F(0) for _ in range(size)] for _ in range(size)]
    for i in range(5):
        for j in range(5): M[i][j]=P[i][j]
    M[5][5]=1
    for k in range(n-3):
        i=6+2*k
        for ii in (i,i+1):
            for jj in (i,i+1):M[ii][jj]=F(1,2)
    assert max(sum(map(abs,row)) for row in M) == c
    # Idempotence on each scalar and pair block follows from multiplication.
    assert all(sum(M[i][k]*M[k][j] for k in range(size))==M[i][j]
               for i in range(size) for j in range(size))
print('RATIONAL_PROJECTION_CONSTANT_OK', c)
