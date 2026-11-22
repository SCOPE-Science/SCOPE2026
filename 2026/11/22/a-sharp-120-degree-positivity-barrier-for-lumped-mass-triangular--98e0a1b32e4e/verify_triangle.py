"""Exact rational checks for a lumped-mass P1 heat step on a single triangle.

Run with Python 3 (standard library). Finite tests corroborate the algebraic proof.
"""
from fractions import Fraction as F
from itertools import product
import math

def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def inv(a):
    n=len(a)
    x=[list(a[i])+[F(int(j==i)) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if x[i][j])
        x[j],x[p]=x[p],x[j]
        q=x[j][j]
        x[j]=[v/q for v in x[j]]
        for i in range(n):
            if i!=j:
                c=x[i][j]
                x[i]=[x[i][k]-c*x[j][k] for k in range(2*n)]
    return [r[n:] for r in x]

def matrices(h):
    # Vertices (-1,0),(1,0),(0,h); area h; Neumann P1 heat flow.
    # Lumped mass each h/3; K_ij = area * grad(phi_i) dot grad(phi_j).
    K=[[F(0) for j in range(3)] for i in range(3)]
    g=[(F(-1,2),-F(1,2)/h),(F(1,2),-F(1,2)/h),(F(0),F(1)/h)]
    for i in range(3):
        for j in range(3):
            K[i][j]=h*sum(g[i][k]*g[j][k] for k in range(2))
    M=[[h/3 if i==j else F(0) for j in range(3)] for i in range(3)]
    return M,K

def step(h,t,theta):
    M,K=matrices(h)
    A=[[M[i][j]+theta*t*K[i][j] for j in range(3)] for i in range(3)]
    B=[[M[i][j]-(1-theta)*t*K[i][j] for j in range(3)] for i in range(3)]
    return mul(inv(A),B)

def projectors():
    # Eigenvalues 0,b=h²,3 of the normalized stiffness, respectively.
    P0=[[F(1,3)]*3 for _ in range(3)]
    PA=[[F(1,2),-F(1,2),F(0)],[-F(1,2),F(1,2),F(0)],[F(0),F(0),F(0)]]
    PS=[[F(1,6),F(1,6),-F(1,3)],[F(1,6),F(1,6),-F(1,3)],[-F(1,3),-F(1,3),F(2,3)]]
    return P0,PA,PS

def spectral(h,t,theta):
    scale=F(3,2)/h**2
    vals=[F(1), (1-(1-theta)*t*scale*h*h)/(1+theta*t*scale*h*h), (1-(1-theta)*t*scale*3)/(1+theta*t*scale*3)]
    return [[sum(vals[k]*pr[i][j] for k,pr in enumerate(projectors())) for j in range(3)] for i in range(3)]

def predicted(h,t,theta):
    b=h*h
    if t==0:return True
    if theta==1:
        return t>= (1-b)/3
    return b>=F(1,3) and F(2,3)*(1-b)<=t<=F(4,3)*b

n=0
hs=[F(1,9),F(1,4),F(1,2),F(2,3),F(3,4),F(4,5),F(9,10),F(1)]
base=[F(0),F(1,10000),F(1,1000),F(1,100),F(1,10),F(1,5),F(1,4),F(1,3),F(1,2),F(3,4),F(1),F(2),F(10)]
for h in hs:
    b=h*h
    threshold_be=(1-b)/3
    threshold_cn=F(2,3)*(1-b)
    upper_cn=F(4,3)*b
    times=base+[threshold_be,threshold_be+F(1,100),threshold_cn,threshold_cn+F(1,100),upper_cn,upper_cn+F(1,100)]
    for theta in (F(1),F(1,2)):
        for t in times:
            if t<0:continue
            p=step(h,t,theta)
            s=spectral(h,t,theta)
            assert p==s, (h,t,theta,p,s)
            assert all(sum(row)==1 for row in p)
            assert all(p[i][j]==p[j][i] for i in range(3) for j in range(3))
            assert all(p[i][j]>=0 for i in range(3) for j in range(3))==predicted(h,t,theta),(h,t,theta,p)
            n+=1

# Semigroup: unique sign change, locate and check for a representative family.
for h in (0.2,0.5,0.75,0.9,0.99):
    b=h*h
    zcrit=-math.log(b)/(3-b)
    f=lambda z:(2+math.exp(-3*z)-3*math.exp(-b*z))/6
    assert f(zcrit)<0
    assert f(0)==0
    assert f(100/b)>0

print('VERIFY_OK: exact_rational_steps=%d; eigenprojector_identity=all; semigroup_samples=5'%n)

# The angle-120-degree limiting boundary is exactly attainable when b=1/3.
# It has irrational physical altitude h=1/sqrt(3), but the spectral projectors
# and non-dimensional y=1 still allow a rational check with no approximation.
b=F(1,3); y=F(1)
p0,pa,ps=projectors()
a=(1-b*y)/(1+b*y); s=(1-3*y)/(1+3*y)
c=[[p0[i][j]+a*pa[i][j]+s*ps[i][j] for j in range(3)] for i in range(3)]
assert c==[[F(1,2),F(0),F(1,2)],[F(0),F(1,2),F(1,2)],[F(1,2),F(1,2),F(0)]]
print('VERIFY_OK: angle_120_exact_boundary=passed')
