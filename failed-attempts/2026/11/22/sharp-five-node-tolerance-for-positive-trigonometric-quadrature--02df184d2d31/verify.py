"""Independent finite sanity checks for five-node trigonometric quadrature.

Analytical minimization and the all-configuration theorem are proved in RESULT.md.
This program does not assert finite random tests establish those quantifiers.
"""
from math import pi, acos, sqrt, cos, sin, isclose
from cmath import exp
import random

H=2*pi/5
CRIT=(5/pi*acos(sqrt(cos(pi/5)/2))-1)/2

def solve(M,b):
    M=[[complex(x) for x in row] + [complex(y)] for row,y in zip(M,b)]
    n=len(b)
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(M[i][k]))
        M[pivot],M[k]=M[k],M[pivot]
        assert abs(M[k][k])>1e-8
        c=M[k][k]
        M[k]=[z/c for z in M[k]]
        for i in range(n):
            if i!=k:
                c=M[i][k]
                M[i]=[a-c*z for a,z in zip(M[i],M[k])]
    return [M[i][-1] for i in range(n)]

def weights(deltas):
    theta=[H*(i+v) for i,v in enumerate(deltas)]
    M=[[exp(1j*k*t) for t in theta] for k in (-2,-1,0,1,2)]
    w=solve(M,[0,0,1,0,0])
    assert max(abs(z.imag) for z in w)<2e-11
    assert max(abs(sum(w[j]*exp(1j*k*theta[j]) for j in range(5))-(1 if k==0 else 0)) for k in range(-2,3))<2e-11
    return [z.real for z in w]

def F_for_center(d):
    theta=[H*(i+d[i]) for i in range(5)]
    x=(theta[1]-theta[0])/2
    y=(theta[4]-theta[3])/2
    D=(theta[3]+theta[4]-theta[0]-theta[1])/2
    F=cos(D)+2*cos(x)*cos(y)
    den=8
    for i in (0,1,3,4):
        den*=sin((theta[2]-theta[i])/2)
    return F,den

N=0
assert .2<CRIT<.202
rng=random.Random(32420)
for a in (0,.05,.1,.2,CRIT,.23,.249):
    predicted=2*cos((1+2*a)*pi/5)**2-cos(pi/5)
    extremal=[-a,a,0,-a,a]
    F,den=F_for_center(extremal)
    assert abs(F-predicted)<3e-14
    assert den>0
    w=weights(extremal)
    assert abs(w[2]-F/den)<3e-13
    N+=1
    for t in range(150):
        d=[rng.uniform(-a,a) for _ in range(5)]
        F,den=F_for_center(d)
        assert F>=predicted-2e-13
        assert den>0
        wr=weights(d)
        assert abs(wr[2]-F/den)<3e-12
        if a<CRIT-1e-8:
            assert min(wr)>0
        N+=1
assert abs(weights([-CRIT,CRIT,0,-CRIT,CRIT])[2])<3e-13
assert weights([-.22,.22,0,-.22,.22])[2]<0
N+=2
print('VERIFY_OK',N,'trigonometric_quadrature_checks','alpha_star',format(CRIT,'.15f'))
