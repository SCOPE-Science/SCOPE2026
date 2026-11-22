"""Exact checks for a three-coordinate two-grid Jordan-smoother example.
Requires Python 3 standard library only. Mathematical proof is in RESULT.md.
"""
from fractions import Fraction as F
from random import Random

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def sub(a,b):
    return [[x-y for x,y in zip(row1,row2)] for row1,row2 in zip(a,b)]

def scale(a,z):
    return [[z*x for x in row] for row in a]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def add(a,b):
    return [[x+y for x,y in zip(row1,row2)] for row1,row2 in zip(a,b)]

def trace(a):
    return sum(a[i][i] for i in range(len(a)))

rng = Random(261105837)
checks=0
# Exact rational cosine/sine pairs: axes, 3-4-5, 5-12-13, 8-15-17, 7-24-25.
pairs = [(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(4,5),F(3,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17)),(F(7,25),F(24,25))]
for _ in range(800):
    rho=F(rng.randint(1,12),rng.randint(25,40))
    t=F(rng.randint(1,20),rng.randint(25,40))
    c,s=pairs[rng.randrange(len(pairs))]
    S=[[F(0),F(0),F(0)],[F(0),rho,t],[F(0),F(0),rho]]
    Pu=[[F(1),F(0),F(0)],[F(0),F(0),F(0)],[F(0),F(0),F(0)]]
    Pv=[[F(1),F(0),F(0)],[F(0),c*c,c*s],[F(0),c*s,s*s]]
    Eu=matmul(matmul(S,sub(eye(3),Pu)),S)
    Ev=matmul(matmul(S,sub(eye(3),Pv)),S)
    expected_u=[[F(0),F(0),F(0)],[F(0),rho*rho,2*rho*t],[F(0),F(0),rho*rho]]
    eig=rho*rho-2*rho*t*c*s
    assert Eu==expected_u
    assert trace(Ev)==eig
    assert matmul(Ev,Ev)==scale(Ev,eig)
    assert Ev[0]==[F(0)]*3
    # Frobenius and spectral norm coincide for rank-one Ev; exact squared norm.
    evnormsq=sum(v*v for row in Ev for v in row)
    expected_normsq=(rho*rho+t*t*c*c-2*rho*t*c*s)*(rho*rho+t*t*s*s-2*rho*t*c*s)
    assert evnormsq==expected_normsq
    checks+=5
# Sharp equal-angle case with a strictly contractive smoother.
rho,t=F(1,20),F(1,2)
sqrt_cond=rho*rho+t < 1
lambda_u=rho*rho
lambda_v=rho*(t-rho)
norm_v=(rho*rho+(rho-t)**2)/2
assert sqrt_cond and lambda_v/lambda_u == 9 and norm_v==F(41,400)
checks+=3
print('VERIFY_OK',checks)
