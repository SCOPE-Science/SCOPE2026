#!/usr/bin/env python3
"""Reproduce mathematical checks for a single-priced-edge Kirchhoff design.
No external services are used. Python 3, SymPy and NumPy required.
"""
import math
import numpy as np
import sympy as sp

checks=0

def params(n,r,B=1.0):
    k=n-2
    rc=n/k
    if r<rc:
        h=math.sqrt((k+2)*(2*(k+1)/r-k))
        t=k+1+0.5*(r*(h-k)+(k-1)*math.sqrt(r)*h)
        a=B*(h-k)/(2*t)
        b=B/t
        c=B*(math.sqrt(r)*h-2)/(k*t)
    else:
        delta=math.sqrt(k*(k+2))
        t=k+1+(k-1)*delta/2
        a=0.0
        b=B/t
        c=B*(delta-2)/(k*t)
    return a,b,c

def mat(n,a,b,c):
    L=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            w=a if (i,j)==(0,1) else b if i<2 else c
            L[i,j]=L[j,i]=-w
            L[i,i]+=w
            L[j,j]+=w
    return L

for n in range(4,31):
    k=n-2
    rc=n/k
    for r in [0.03,0.3,0.7,1., (1+rc)/2,rc*(1-1e-5),rc,rc*(1+1e-5),1.5*rc,4.0]:
        for B in [0.75,1.0,3.0]:
            a,b,c=params(n,r,B)
            assert a>=-1e-10 and b>0 and c>0
            assert abs(r*a+2*k*b+k*(k-1)*c/2-B)<1e-9
            L=mat(n,a,b,c)
            vals=np.linalg.eigvalsh(L)
            assert vals[1]>0
            pos=sorted([2*a+k*b,(k+2)*b]+[2*b+k*c]*(k-1))
            assert np.allclose(vals[1:],pos,rtol=2e-10,atol=2e-10)
            spectral=1/(2*a+k*b)+1/((k+2)*b)+(k-1)/(2*b+k*c)
            inverse=np.trace(np.linalg.inv(L+np.ones((n,n))/n))-1
            assert math.isclose(spectral,inverse,rel_tol=1e-9,abs_tol=1e-7)
            lam=2/(2*b+k*c)**2
            gA=-2/(2*a+k*b)**2 +lam*r
            gB=-k/(2*a+k*b)**2-1/((k+2)*b*b)-2*(k-1)/(2*b+k*c)**2+2*k*lam
            gC=-k*(k-1)/(2*b+k*c)**2+lam*k*(k-1)/2
            assert abs(gB)<1e-7 and abs(gC)<1e-7
            if r<rc-1e-8:assert abs(gA)<1e-7
            else: assert gA>=-1e-7
            # one-dimensional perturbations around stationary symmetry solution
            for da,dc in [(0.005,0),(-0.005,0),(0,0.005),(0,-0.005)]:
                aa=a+da*B
                cc=c+dc*B
                bb=(B-r*aa-k*(k-1)*cc/2)/(2*k)
                if aa>=0 and bb>0 and cc>=0:
                    F=1/(2*aa+k*bb)+1/((k+2)*bb)+(k-1)/(2*bb+k*cc)
                    assert F+1e-7>=spectral
            checks+=1

# Finite exact full Laplacian inversion and characteristic-spectrum checks.
for n in [4,5]:
    k=n-2
    D=sp.sqrt(k*(k+2))
    for r in [sp.Integer(1)]:
        if r < sp.Rational(n,k):
            h=sp.sqrt((k+2)*(2*(k+1)/r-k))
            T=k+1+(r*(h-k)+(k-1)*sp.sqrt(r)*h)/2
            a=(h-k)/(2*T)
            b=1/T
            c=(sp.sqrt(r)*h-2)/(k*T)
        else:
            T=k+1+(k-1)*D/2
            a=sp.Integer(0)
            b=1/T
            c=(D-2)/(k*T)
        matx=sp.zeros(n)
        for i in range(n):
            for j in range(i+1,n):
                w=a if (i,j)==(0,1) else b if i<2 else c
                matx[i,j]=matx[j,i]=-w
                matx[i,i]+=w
                matx[j,j]+=w
        assert sp.simplify(r*a+2*k*b+k*(k-1)*c/2-1)==0
        expected=1/(2*a+k*b)+1/((k+2)*b)+(k-1)/(2*b+k*c)
        actual=sp.trace((matx+sp.ones(n)/n).inv())-1
        assert sp.simplify(actual-expected)==0, (n,r)
        char=sp.factor(matx.charpoly().as_expr())
        eigen=sp.Symbol('lambda')
        p=sp.expand(eigen*(eigen-(2*a+k*b))*(eigen-(k+2)*b)*(eigen-(2*b+k*c))**(k-1))
        assert sp.simplify(char-p)==0
        checks+=1

# Exact threshold comparisons with distinct already-known D and gap designs.
for n in range(4,100):
    rD=sp.Rational(n-1,n-2)
    rA=sp.Rational(n,n-2)
    rE=sp.Rational(2*(n-1),n-2)
    assert rD<rA<rE
    assert sp.simplify(rA-rD-sp.Rational(1,n-2))==0
    checks+=1
print('PASS:', checks, 'parameter sets; exact inversions, Laplacian spectra, KKT and threshold checks.')
