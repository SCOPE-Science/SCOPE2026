"""Exact finite equilibrium witnesses and Gaussian-cone numerical cross-checks.
Requires Python 3 standard library only. Finite tests illustrate, not prove, asymptotics.
"""
from fractions import Fraction as F
from itertools import product
from math import atan, pi, sqrt, log, exp

def solve(A,b):
    n=len(b)
    if n==0:return []
    M=[[F(A[i][j]) for j in range(n)]+[F(b[i])] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if M[i][j]); M[j],M[p]=M[p],M[j]
        r=M[j][j]; M[j]=[x/r for x in M[j]]
        for i in range(n):
            if i!=j:
                r=M[i][j]; M[i]=[M[i][k]-r*M[j][k] for k in range(n+1)]
    return [M[i][-1] for i in range(n)]

def enumerate_faces(A,h):
    n=len(A); out=[]
    for face in product((0,1,2),repeat=n): # 2 = free
        free=[i for i in range(n) if face[i]==2]
        rhs=[-h[i] - sum(A[i][j]*(F(face[j])-F(1,2)) for j in range(n) if face[j]!=2) for i in free]
        vals=solve([[A[i][j] for j in free] for i in free],rhs)
        x=[F(face[i]) if face[i]!=2 else vals[free.index(i)]+F(1,2) for i in range(n)]
        if all(0<x[i]<1 for i in free):
            for i in free:
                assert h[i]+sum(A[i][j]*(x[j]-F(1,2)) for j in range(n))==0
            out.append((face,x))
    return out

def run_case(A,h):
    n=len(A)
    assert all(abs(A[i][i])>2*abs(h[i])+sum(abs(A[i][j]) for j in range(n) if j!=i) for i in range(n))
    faces=enumerate_faces(A,h)
    assert len(faces)==3**n
    K=sum(A[i][i]>0 for i in range(n))
    sinks=[]
    for face,x in faces:
        # Gershgorin-sign count along free subspace plus exact normal sign.
        unstable=sum(A[i][i]>0 for i in range(n) if face[i]==2)+sum(A[i][i]<0 for i in range(n) if face[i]!=2)
        if unstable==0:sinks.append(face)
    assert len(sinks)==2**K
    return n,len(faces),len(sinks),sinks

A3=[[F(6),F(1,4),F(-1,3)],[F(-1,5),F(-7),F(1,6)],[F(1,7),F(-1,8),F(8)]]
h3=[F(1,5),F(-1,4),F(1,6)]
A4=[[F(7) if i==j and i%2==1 else F(-6) if i==j else F((-1)**(i+j),7) for j in range(4)] for i in range(4)]
h4=[F(i-2,10) for i in range(4)]
print('witnesses:',run_case(A3,h3),run_case(A4,h4))
# For q_2: positive-octant cone rays u=(1,0,0),v=(1,1,0)/sqrt(2),w=(sqrt(2),0,1)/sqrt(3).
# Exact solid-angle identity 2 atan(1/(2+sqrt(2)+sqrt(3)+sqrt(6))) = pi/12.
Omega=2*atan(1/(2+sqrt(2)+sqrt(3)+sqrt(6)))
assert abs(Omega-pi/12)<1e-14
assert abs(2*Omega/pi-F(1,6))<1e-14
print('q1=1/2 and q2=1/6, all-9 probability=1/36; cone=',Omega)
print('passed deterministic finite tests; asymptotic relies on proof, not these tests')
