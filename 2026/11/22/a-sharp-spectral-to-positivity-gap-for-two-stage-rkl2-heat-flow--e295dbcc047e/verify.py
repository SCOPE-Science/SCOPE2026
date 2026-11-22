"""Exact-rational finite diagnostics for the two-stage RKL2 graph theorem.

Run: python3 verify.py. Finite diagnostics do not replace the analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import cos, pi

checks=0

def check(b):
    global checks
    checks+=1
    assert b, f'exact test {checks} failed'

def graph_from_edges(n, pairs):
    A=[[0]*n for _ in range(n)]
    for i,j in pairs:
        A[i][j]=A[j][i]=1
    return A

def hypercube(d):
    n=2**d
    return graph_from_edges(n,[(i,i^(1<<k)) for i in range(n) for k in range(d) if i<(i^(1<<k))])

def complete(n):
    return graph_from_edges(n,combinations(range(n),2))

def cycle(n):
    return graph_from_edges(n,[(i,(i+1)%n) for i in range(n)])

def triangular(n):
    vertices=list(combinations(range(n),2))
    return graph_from_edges(len(vertices),[(i,j) for i in range(len(vertices)) for j in range(i+1,len(vertices)) if len(set(vertices[i]) & set(vertices[j]))==1])

def product(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def step(A,h):
    n=len(A);d=sum(A[0]); A2=product(A,A)
    return [[F(i==j)+h*(A[i][j]-d*(i==j))+F(1,2)*h*h*(A2[i][j]-2*d*A[i][j]+d*d*(i==j)) for j in range(n)] for i in range(n)]

def criterion(A,h):
    n=len(A);d=sum(A[0]); A2=product(A,A)
    t=min(A2[i][j] for i in range(n) for j in range(n) if A[i][j])
    return h<=F(2,2*d-t)

cases=[hypercube(d) for d in range(1,6)]+[complete(d+1) for d in range(2,7)]+[cycle(k) for k in (5,7)]+[triangular(k) for k in range(4,9)]
for A in cases:
    n=len(A);d=sum(A[0]);A2=product(A,A)
    check(all(sum(row)==d for row in A))
    check(all(A[i][j]==A[j][i] for i in range(n) for j in range(n)))
    check(all(A2[i][i]==d for i in range(n)))
    for h in [F(i,24) for i in range(73)]:
        T=step(A,h)
        check(all(sum(row)==1 for row in T))
        check(all(T[i][j]==T[j][i] for i in range(n) for j in range(n)))
        check((min(min(row) for row in T)>=0)==criterion(A,h))
        check(all(T[i][i]==1-d*h+F(d*(d+1),2)*h*h for i in range(n)))

T5=triangular(5)
check(len(T5)==10)
check(step(T5,F(7,30))[0][1]==F(-7,600))
check(F(7,30)<F(1,4))
check(all(min(row)>=0 for row in step(triangular(4),F(1,3))))
check(all(min(row)>=0 for row in step(hypercube(4),F(1,4))))
check(step(cycle(5),F(8,15))[0][1]<0)
check(float(F(8,15))<2/(2+2*cos(pi/5)))
print(f'VERIFY_OK: {checks} exact assertions across {len(cases)} finite regular graphs; one spectral inequality')
