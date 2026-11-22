"""Exact three-state generator certificate and supplementary finite tests.
Run with Python 3.10 or later; no external packages required.
"""
from fractions import Fraction as F
from math import sqrt, exp, log
from random import Random

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def norm1(A):
    return max(sum(abs(A[i][j]) for i in range(len(A))) for j in range(len(A[0])))

Z=F(0); U=F(1)
I=[[U if i==j else Z for j in range(3)] for i in range(3)]
Q=[[-U,Z,F(1,4)],[U,-F(1,4),Z],[Z,F(1,4),-F(1,4)]]
P=[[F(v,9) for j in range(3)] for v in (1,4,4)]
N=add(scale(-U,Q),scale(-F(3,4),add(I,scale(-U,P))))
assert N==[[F(1,3),F(1,12),-F(1,6)],[-F(2,3),-F(1,6),F(1,3)],[F(1,3),F(1,12),-F(1,6)]]
assert norm1(Q)==2 and norm1(N)==F(4,3)
assert mm(P,P)==P and mm(P,N)==[[Z]*3 for _ in range(3)]
assert mm(N,P)==[[Z]*3 for _ in range(3)] and mm(N,N)==[[Z]*3 for _ in range(3)]
assert mm(Q,P)==[[Z]*3 for _ in range(3)]
# (-Q) has characteristic polynomial lambda*(lambda-3/4)^2:
assert sum(-Q[j][j] for j in range(3))==F(3,2)
prod=sum((-Q[i][i])*(-Q[j][j])-Q[i][j]*Q[j][i] for i in range(3) for j in range(i+1,3))
assert prod==F(9,16)

# Check the exact discriminant envelope and its sharp threshold at b=c=1/4.
checks=0
for bi in range(41):
    for ci in range(41):
        b=F(bi,40);c=F(ci,40);t=b+c
        pmax=t+b*c
        disc=(U+t)**2-4*pmax
        assert disc>=U-2*t
        if t<=F(1,2):
            assert disc>=0
            r=(float(U+t)+sqrt(float(disc)))/2
            assert r>=0.75-1e-12
        else:
            assert float(U+t)/2>=0.75
        checks+=1
# Real generator sampling checks off-diagonal contributions to p and spectral bound.
rng=Random(12345)
for k in range(12000):
    d=[[0.0]*3 for _ in range(3)]
    for j in range(3):
        a=rng.random(); b=rng.random(); total=a+b
        other=[i for i in range(3) if i!=j]
        d[other[0]][j]=a;d[other[1]][j]=b
        d[j][j]=-total
    q=[-d[i][i] for i in range(3)]
    s=sum(q)
    p=sum(q[i]*q[j]-d[i][j]*d[j][i] for i in range(3) for j in range(i+1,3))
    delta=s*s-4*p
    r=(s+(sqrt(delta) if delta>=0 else 0.0))/2
    assert r >= 0.75*max(q)-1e-10
    checks+=1
# Exact-Jordan formula gives e^{-tQ} = P+exp(3t/4)(I-P+tN)
for t in (5.0,12.0,30.0,60.0):
    A=add(P,scale(exp(3*t/4),add(add(I,scale(-U,P)),scale(t,N))))
    n=norm1(A)
    ratio=(2*t)/log(n)
    assert ratio<8/3+1e-12
    if t>=30: assert ratio>2.0
    checks+=1
print('PASS', checks, 'supplementary tests; exact projection/nilpotent certificate holds')
