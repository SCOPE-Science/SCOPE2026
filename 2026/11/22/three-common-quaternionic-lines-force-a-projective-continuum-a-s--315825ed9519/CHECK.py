"""Exact rational quaternion multiplication and centralizer checks (stdlib only).
Finite linear checks supplement, but cannot replace, the all-tuple proof.
"""
from fractions import Fraction
ONE=(1,0,0,0)
ZERO=(0,0,0,0)
Q=[ONE,(0,1,0,0),(0,0,1,0),(0,0,0,1)]
def mul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def neg(x):return tuple(-a for a in x)
def rank_by_columns(columns):
    matrix=[list(map(Fraction,row)) for row in zip(*columns)]
    if not matrix:return 0
    m,n=len(matrix),len(matrix[0]);pivot=0
    for j in range(n):
        best=next((i for i in range(pivot,m) if matrix[i][j]),None)
        if best is None:continue
        matrix[pivot],matrix[best]=matrix[best],matrix[pivot]
        c=matrix[pivot][j]
        matrix[pivot]=[v/c for v in matrix[pivot]]
        for i in range(pivot+1,m):
            c=matrix[i][j]
            if c:matrix[i]=[x-c*y for x,y in zip(matrix[i],matrix[pivot])]
        pivot+=1
        if pivot==m:break
    return pivot
assert mul(Q[1],Q[2])==Q[3] and mul(Q[2],Q[1])==neg(Q[3])
for a in Q[1:]:assert mul(a,a)==neg(ONE)
for target,expected in [([Q[1]],2),([Q[1],Q[2]],1),([ONE],4)]:
    columns=[[v for t in target for v in add(mul(t,u),neg(mul(u,t)))] for u in Q]
    assert 4-rank_by_columns(columns)==expected
entries=[]
for i in range(2):
 for j in range(2):
  for unit in Q:
   X=[[ZERO,ZERO],[ZERO,ZERO]]
   X[i][j]=unit
   entries.append(X)
for target,expected in [([Q[1]],8),([Q[1],Q[2]],4),([ONE],16)]:
    columns=[]
    for X in entries:
        col=[]
        for t in target:
            for i in range(2):
                for j in range(2):
                    col.extend(add(mul(t,X[i][j]),neg(mul(X[i][j],t))))
        columns.append(col)
    assert 16-rank_by_columns(columns)==expected
# Repeated diagonals preserve every graph of a real slope.
for a in (Q[1],Q[2],add(ONE,Q[3])):
 for t in (ZERO,ONE,(2,0,0,0)):
  assert mul(a,t)==mul(t,a)
# A third line of diag(0,1) would require 1*t=t*0, impossible for t != 0.
for t in Q:
    assert mul(ONE,t)!=mul(t,ZERO)
print('QUATERNION_THREE_LINE_CHECKS_OK: scalar dimensions 4,2,1; matrix dimensions 16,8,4')
