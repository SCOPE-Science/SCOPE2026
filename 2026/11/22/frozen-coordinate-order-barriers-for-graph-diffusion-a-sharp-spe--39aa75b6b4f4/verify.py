"""Exact finite checks for a graph-heat coordinate-freeze obstruction.

All graph matrices use rational arithmetic.  The universal result is proved
analytically in RESULT.md; this script provides finite regression checks only.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import exp, factorial


def mm(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def mv(A, x):
    return [sum(a*b for a,b in zip(row,x)) for row in A]


def lap(n, edges):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j,w in edges:
        L[i][i]+=w
        L[j][j]+=w
        L[i][j]-=w
        L[j][i]-=w
    return L


def addk(L,k):
    n=len(L)
    return [[L[i][j]+(k if i==j else 0) for j in range(n)] for i in range(n)]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def delta_squared(Q, i):
    r=Q[i]
    s=mm(Q,Q)[i]
    return dot(s,s)-dot(s,r)**2/dot(r,r)


def is_connected(n, edges):
    reached={0}
    changed=True
    while changed:
        changed=False
        for i,j,_ in edges:
            if (i in reached) != (j in reached):
                reached.update((i,j));changed=True
    return len(reached)==n

checks=0
for n in range(2,6):
    pairs=list(combinations(range(n),2))
    for mask in range(1,1<<len(pairs)):
        E=[(i,j,F(1)) for p,(i,j) in enumerate(pairs) if mask>>p&1]
        if not is_connected(n,E):
            continue
        L=lap(n,E)
        for i in range(n):
            degree=sum((i==a or i==b) for a,b,_ in E)
            d=delta_squared(L,i)
            assert d>=0
            assert (d==0)==(degree==n-1)
            assert delta_squared(addk(L,F(1,2)),i)>0
            checks+=3
        all_zero=all(delta_squared(L,i)==0 for i in range(n))
        assert all_zero==(len(E)==len(pairs))
        checks+=1

for n in range(2,6):
    pairs=list(combinations(range(n),2))
    for weights in (tuple(F(1) for _ in pairs),tuple(F(1+(j%3)) for j in range(len(pairs)))):
        L=lap(n,[(i,j,w) for (i,j),w in zip(pairs,weights)])
        all_zero=all(delta_squared(L,i)==0 for i in range(n))
        assert all_zero==(len(set(weights))==1)
        for k in (F(1,2),F(3)):
            for i in range(n):
                assert delta_squared(addk(L,k),i)>0
                checks+=1
        checks+=1

P=lap(3,[(0,1,F(1)),(1,2,F(1))])
x=[F(1),F(1),F(2)]
assert mv(P,x)[0]==0 and mv(mm(P,P),x)[0]==1
assert delta_squared(P,0)==F(3,2)
assert delta_squared(P,1)==0
checks+=4

Q=addk(lap(2,[(0,1,F(1))]),F(1))
x=[F(1),F(2)]
assert mv(Q,x)==[F(0),F(3)]
assert mv(mm(Q,Q),x)==[F(-3),F(6)]
checks+=2

for n in range(2,10):
    for c,k in ((F(1),F(1,2)),(F(2,3),F(2,5)),(F(4),F(3))):
        L=[[c*((F(1) if i==j else F(0))-F(1,n)) for j in range(n)] for i in range(n)]
        Q=addk(L,k)
        pred=c*c*k*k*(c+k)*(c+k)*(n-1)/(n*(k*k+(n-1)*(c+k)*(c+k)))
        for i in range(n):
            assert delta_squared(Q,i)==pred
            checks+=1

# Positivity of the exact uniform-clique step and a scalar remainder sanity check.
for n in range(2,8):
    for c in (0.2,1.0,2.4):
        for h in (0.02,0.5,4.0):
            psi=-__import__('math').expm1(-c*h)/c
            x=[1.+j/7. for j in range(n)]
            L=[[c*((1. if i==j else 0.)-1/n) for j in range(n)] for i in range(n)]
            y=[x[i]-psi*sum(L[i][j]*x[j] for j in range(n)) for i in range(n)]
            mean=sum(x)/n
            exact=[mean+exp(-c*h)*(a-mean) for a in x]
            assert max(abs(a-b) for a,b in zip(y,exact))<1e-11
            checks+=1

print('VERIFY_OK',checks)
