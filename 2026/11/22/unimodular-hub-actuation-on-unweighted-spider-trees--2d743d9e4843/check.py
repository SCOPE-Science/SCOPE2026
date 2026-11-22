"""Exact checks for unimodular hub actuation on unweighted spider trees.

Python 3 and SymPy required. No stochastic or floating-point certification.
Run: python check.py
"""
from itertools import combinations, combinations_with_replacement
from math import gcd
import sympy as sp

x = sp.symbols('x')
P = [sp.Integer(1), x-1]
for length in range(2, 17):
    P.append(sp.expand((x-2)*P[-1]-P[-2]))

checks = 0
for a,b in combinations(range(1,17), 2):
    resultant = sp.resultant(P[a], P[b], x)
    expected = gcd(2*a+1,2*b+1)==1
    assert (abs(resultant)==1 if expected else resultant==0), (a,b,resultant)
    checks += 1


def make_laplacian(arms):
    n=1+sum(arms)
    L=sp.zeros(n)
    cursor=1
    for length in arms:
        previous=0
        for pos in range(length):
            current=cursor+pos
            L[current,current]+=1
            L[previous,previous]+=1
            L[current,previous]-=1
            L[previous,current]-=1
            previous=current
        cursor+=length
    return L


def kalman_det(A):
    n=A.rows
    v=sp.eye(n)[:,0]
    cols=[]
    for _ in range(n):
        cols.append(v)
        v=A*v
    return sp.Matrix.hstack(*cols).det(method='domain-ge')

for number, max_arm in [(3,6),(4,4)]:
    for arms in combinations_with_replacement(range(1,max_arm+1), number):
        L=make_laplacian(arms)
        pairwise_coprime=all(gcd(2*a+1,2*b+1)==1 for a,b in combinations(arms,2))
        det=kalman_det(-L)
        assert (abs(det)==1 if pairwise_coprime else det==0), (arms,det)
        checks+=1

for arms in ((1,2,3),(1,2,4),(1,3,5),(2,3,4),(1,2,3,5)):
    L=make_laplacian(arms)
    assert abs(kalman_det(-L))==abs(kalman_det(sp.eye(L.rows)-L))
    checks+=1

L=make_laplacian((1,2,3))
A=sp.eye(L.rows)-L
n=L.rows
v=sp.eye(n)[:,0]
columns=[]
for _ in range(n):
    columns.append(v)
    v=A*v
K=sp.Matrix.hstack(*columns)
assert abs(K.det())==1
assert all(val.q==1 for val in K.inv())
checks+=2
print(f'PASS: {checks} exact polynomial, graph and integral-reachability assertions')
