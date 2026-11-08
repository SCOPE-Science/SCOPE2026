#!/usr/bin/env python3
"""Standalone finite arithmetic and spectral cross-checks for the stated star-corridor theorem.
The analytic inequalities in RESULT.md, not these finite tests, establish all-parameter claims.
Standard library only.
"""
from fractions import Fraction
from math import sqrt


def poly(m, x):
    return x*x*x-x*x-m*x+(m-2)


def bisect_root(m, left, right, steps=85):
    fa=poly(m,left)
    fb=poly(m,right)
    assert fa*fb < 0, (m,left,right,fa,fb)
    for _ in range(steps):
        mid=(left+right)/2
        fm=poly(m,mid)
        if fa*fm <= 0:
            right=mid
            fb=fm
        else:
            left=mid
            fa=fm
    return (left+right)/2


def jacobi_eigenvalues(matrix, tol=1e-13):
    a=[row[:] for row in matrix]
    n=len(a)
    for _ in range(30*n*n):
        i,j=max(((i,j) for i in range(n) for j in range(i+1,n)),
                key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[i][j])<tol:break
        phi=0.5*__import__('math').atan2(2*a[i][j],a[j][j]-a[i][i])
        # Standard Jacobi rotation with sign convention.
        co=__import__('math').cos(phi)
        si=__import__('math').sin(phi)
        aii,ajj,aij=a[i][i],a[j][j],a[i][j]
        a[i][i]=co*co*aii-2*co*si*aij+si*si*ajj
        a[j][j]=si*si*aii+2*co*si*aij+co*co*ajj
        a[i][j]=a[j][i]=0.0
        for k in range(n):
            if k==i or k==j:continue
            aki,akj=a[k][i],a[k][j]
            a[k][i]=a[i][k]=co*aki-si*akj
            a[k][j]=a[j][k]=si*aki+co*akj
    else:raise AssertionError('Jacobi did not converge')
    return sorted(a[i][i] for i in range(n))


def matrix(m, leaf_edge):
    n=m+1
    a=[[0.0]*n for _ in range(n)]
    for j in range(1,n):a[0][j]=a[j][0]=1.0
    if leaf_edge:a[1][2]=a[2][1]=1.0
    return a


def dr(eigs,c):
    e=sorted(eigs)
    return (c+e[-1])/max(abs(c+x) for x in e[:-1])


checks=0
# Exact rational sign brackets for the exceptional three-leaf star.
assert poly(3,Fraction(217,100))==Fraction(-587,1000000)
assert poly(3,Fraction(39,125))==Fraction(-5806,1953125)
assert poly(3,Fraction(3,10))>0
assert poly(3,Fraction(109,50))>0
assert Fraction(1733,1000)**2>3
checks+=5
# Exact formulas at q=2/5 and at sqrt(m)+q (reduction r^2=m):
# f_m(q)=(75m-262)/125; f_m(r+q)=2(50m-20r-131)/125.
q=Fraction(2,5)
for m in range(4,201):
    assert poly(m,q)==Fraction(75*m-262,125)>0
    r=sqrt(m)
    assert 50*m-20*r-131>0
    checks+=2
# Independent Jacobi diagonalization of actual adjacency arrays; compare roots
# and all claimed damping-ratio signs for many sizes/retentions.
for m in range(2,31):
    pre=jacobi_eigenvalues(matrix(m,False))
    post=jacobi_eigenvalues(matrix(m,True))
    r=sqrt(m)
    assert abs(pre[-1]-r)<1e-8
    assert abs(pre[0]+r)<1e-8
    if m>=3:
        gamma=bisect_root(m,-r,-1.0)
        beta=bisect_root(m,0.0,1.0)
        alpha=bisect_root(m,r,r+1)
        assert abs(post[-1]-alpha)<1e-8
        assert any(abs(e-beta)<1e-8 for e in post)
        assert any(abs(e-gamma)<1e-8 for e in post)
        if m>=4:assert alpha-r < beta
    for cscale in (1,1.02,1.4,2,4,10,100):
        c=cscale*r
        a,b=dr(pre,c),dr(post,c)
        assert b>a if m==2 else (b<a if m>=4 else True)
        if m>=3:
            assert abs(b-(c+alpha)/(c+beta))<1e-9
            assert abs(a-(c+r)/c)<1e-9
        # A common scalar s makes both matrices substochastic.
        s=1/(c+m)
        assert s*(c+m)<=1+1e-12
        assert s*(c+2)<=1+1e-12
        checks+=1
    checks+=5
# Exact crossing of the three-leaf case, and a domain threshold check.
r=sqrt(3)
a=bisect_root(3,r,r+1)
b=bisect_root(3,0,1)
crit=r*b/(a-b-r)
assert 4.2453<crit<4.2455 and crit>r
pre=jacobi_eigenvalues(matrix(3,False))
post=jacobi_eigenvalues(matrix(3,True))
for c,sgn in ((r,-1),(4,-1),(crit,0),(5,1),(100,1)):
    v=dr(post,c)-dr(pre,c)
    assert (v<0 if sgn==-1 else v>0 if sgn==1 else abs(v)<1e-9)
    checks+=1
print('PASS',checks,'finite/exact checks; m=3 crossing=',format(crit,'.12f'))
print('m=4, c=2: rho before/after',2+sqrt(4),2+bisect_root(4,2,3))
print('m=4, c=2: damping before/after',dr(jacobi_eigenvalues(matrix(4,False)),2),dr(jacobi_eigenvalues(matrix(4,True)),2))
