#!/usr/bin/env python3
"""Standalone floating-point diagnostics for a finite-dimensional fractional propagator.
Run with Python 3.10+; standard library only. Analytical proof is in RESULT.md.
"""
from math import sin, cos, tan, pi, gamma, sqrt, isfinite


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def identity(n):
    return [[float(i == j) for j in range(n)] for i in range(n)]


def norm2(a):
    n = len(a)
    gram = [[sum(a[k][i]*a[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    # Symmetric Jacobi diagonalization: square roots of nonnegative eigenvalues.
    for _ in range(100*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda z:abs(gram[z[0]][z[1]]))
        if abs(gram[p][q])<2e-15: break
        tau=(gram[q][q]-gram[p][p])/(2*gram[p][q])
        t=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t); s=t*c
        app,aqq,apq=gram[p][p],gram[q][q],gram[p][q]
        gram[p][p]=app-t*apq
        gram[q][q]=aqq+t*apq
        gram[p][q]=gram[q][p]=0.
        for k in range(n):
            if k==p or k==q:continue
            gkp,gkq=gram[k][p],gram[k][q]
            gram[k][p]=gram[p][k]=c*gkp-s*gkq
            gram[k][q]=gram[q][k]=s*gkp+c*gkq
    else: raise AssertionError('Jacobi failed')
    return sqrt(max(gram[i][i] for i in range(n)))


def propagator(n,a,alpha,s):
    theta=pi/(n+1)
    coupling=a/cos(theta)
    g=[[-a*(i==j)+coupling*(j==i+1) for j in range(n)] for i in range(n)]
    power=identity(n)
    out=[[0.]*n for _ in range(n)]
    for k in range(34):
        coef=s**k/gamma(1+alpha*k)
        for i in range(n):
            for j in range(n):out[i][j]+=coef*power[i][j]
        power=multiply(power,g)
    return out


def coefficients(n,a,alpha):
    theta=pi/(n+1)
    q=a*a*tan(theta)**2*(n-1)/(n+1)
    chi=a**3*tan(theta)**2/(6*(n+1))
    variance=2/gamma(1+2*alpha)-1/gamma(1+alpha)**2
    return q,chi,variance


def check():
    checks=0
    for n in range(2,10):
        for a in (0.7,1.0,1.4):
            q,chi,_=coefficients(n,a,1.)
            assert q>0 and chi>0; checks+=1
            for s in (0.12,0.06,0.03):
                observed=1-norm2(propagator(n,a,1.,s))
                # Cubic leading coefficient; remainder is fourth order or better.
                assert abs(observed/s**3-chi) < 0.25*chi + 4e-8
                checks+=1
            for alpha in (0.6,0.8,0.95,0.99):
                q,chi,v=coefficients(n,a,alpha)
                assert v>0; checks+=1
                for s in (0.08,0.04):
                    observed=1-norm2(propagator(n,a,alpha,s))
                    pred=0.5*v*q*s*s+chi*s**3
                    assert observed>0 and abs(observed-pred)<max(0.04*pred,2e-9)
                    checks+=1
            for alpha in (0.95,0.99,0.999):
                q,chi,v=coefficients(n,a,alpha)
                assert abs(v/(1-alpha)-1.)<0.08
                checks+=1
    # The two-dimensional exponential case has the independent exact norm.
    for a in (0.6,1.,1.5):
        from math import exp, asinh
        for s in (0.1,0.2,0.5):
            exact=exp(-a*s+asinh(a*s))
            got=norm2(propagator(2,a,1,s))
            assert abs(exact-got)<4e-12
            checks+=1
    print(f'FRACTIONAL_JORDAN_BOUNDARY_DIAGNOSTIC_OK {checks}')

if __name__=='__main__':check()
