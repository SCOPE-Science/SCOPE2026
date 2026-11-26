"""Reproducible rational and quadrature checks for reset-age Fourier-energy covariance.
Python standard library only. Analytic proofs, not the numerical checks, establish
statements for arbitrary mode sets.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import sqrt

R=F(3,2)
B=[F(1),F(2),F(5),F(11),F(17)]
D=[F(1),F(3,2),F(2),F(5,4),F(7,3)]

def k(i,j):
    return 4*R*D[i]*D[j]/((R+B[i])*(R+B[j])*(R+B[i]+B[j]))

def covariance_by_laplace(i,j):
    bi,bj=B[i],B[j]
    pref=4*D[i]*D[j]/(bi*bj)
    eij=1-R/(R+bi)-R/(R+bj)+R/(R+bi+bj)
    ei=bi/(R+bi)
    ej=bj/(R+bj)
    return pref*(eij-ei*ej)

def det(mat):
    n=len(mat)
    ans=F(0)
    for p in permutations(range(n)):
        s=1
        for i in range(n):
            for j in range(i+1,n):
                if p[i]>p[j]:s=-s
        product=F(s)
        for i in range(n):product*=mat[i][p[i]]
        ans+=product
    return ans

def cauchy_minor(I,J):
    n=len(I)
    v=(4*R)**n
    for i in I:v*=D[i]/(R+B[i])
    for j in J:v*=D[j]/(R+B[j])
    for m in range(n):
        for t in range(m+1,n):
            v*=(B[I[t]]-B[I[m]])*(B[J[t]]-B[J[m]])
    for i in I:
        for j in J:v/=R+B[i]+B[j]
    return v

checks=0
for i in range(len(B)):
    for j in range(len(B)):
        assert k(i,j)==covariance_by_laplace(i,j)
        assert k(i,j)>0
        expected_rho_squared=(R+2*B[i])*(R+2*B[j])/(R+B[i]+B[j])**2
        assert k(i,j)**2/(k(i,i)*k(j,j))==expected_rho_squared
        if i!=j:
            assert (B[i]-B[j])**2/(1-expected_rho_squared)==(R+B[i]+B[j])**2
        checks+=4

for m in range(1,len(B)+1):
    for I in combinations(range(len(B)),m):
        for J in combinations(range(len(B)),m):
            value=det([[k(i,j) for j in J] for i in I])
            target=cauchy_minor(I,J)
            assert value==target,(I,J,value,target)
            assert value>0,(I,J,value)
            checks+=2

# Independent numeric integral under z=exp(-r*A), z uniform on (0,1).
# This does not reuse the rational exponential-age identity.
from math import fsum
N=12000
z=[(j+0.5)/N for j in range(N)]
for i,j in [(0,1),(1,3),(0,4),(2,4)]:
    vi=[(2*float(D[i])/float(B[i]))*(1-zv**(float(B[i])/float(R))) for zv in z]
    vj=[(2*float(D[j])/float(B[j]))*(1-zv**(float(B[j])/float(R))) for zv in z]
    cov=fsum(a*b for a,b in zip(vi,vj))/N - (fsum(vi)/N)*(fsum(vj)/N)
    assert abs(cov-float(k(i,j)))<1e-6,(i,j,cov,float(k(i,j)))
    checks+=1

# Interface example: R=1, decay rates b1=2,b2=8, diffusivities=1.
assert F(85,121)==(F(1)+2*F(2))*(F(1)+2*F(8))/(F(1)+F(2)+F(8))**2
assert (F(8)-F(2))**2/(1-F(85,121)) == 11**2
checks+=2
print(f"PASS: {checks} exact rational/determinant and independent quadrature assertions")
