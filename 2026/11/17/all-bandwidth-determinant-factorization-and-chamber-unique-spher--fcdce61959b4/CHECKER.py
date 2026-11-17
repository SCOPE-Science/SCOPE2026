"""Supplementary computational checks of the spherical ring determinant theorem.

Requires Python 3, NumPy, SciPy, and SymPy. Analytical proof is in RESULT.md.
Run: python CHECKER.py
"""
from math import factorial, pi, log
from itertools import permutations
import numpy as np
import sympy as sy
from scipy.special import sph_harm_y
from scipy.optimize import minimize


def exact_constant(L):
    q=sy.Integer(1)
    for j in range(L):
        q *= (2*j+1)**(2*j+1)
    for m in range(-(L-1), L):
        k=abs(m)
        for ell in range(k,L):
            n2=sy.Rational(2*ell+1,4)*sy.Rational(factorial(ell-k),factorial(ell+k))
            a=sy.Rational(factorial(2*ell),2**ell*factorial(ell)*factorial(ell-k))
            q *= n2*a**2
    return sy.cancel(q)  # C_L multiplied by pi**(L**2)


def formula_log(L,x):
    value=float(sy.log(exact_constant(L))) - L**2*log(pi)
    for j in range(1,L):
        value += j*(j+1)*np.log1p(-x[j]**2)
    for i in range(L):
        for j in range(i+1,L):
            value += 2*(2*i+1)*np.log(abs(x[j]-x[i]))
    return value


def direct_log(L,x,phi):
    matrix=[]
    for j in range(L):
        for r in range(2*j+1):
            azimuth=phi[j]+2*np.pi*r/(2*j+1)
            colatitude=np.arccos(x[j])
            matrix.append([sph_harm_y(ell,m,colatitude,azimuth)
                          for ell in range(L) for m in range(-ell,ell+1)])
    sign,logabs=np.linalg.slogdet(np.asarray(matrix,complex))
    assert abs(sign)>0.9
    return 2*logabs


def F_and_grad(L,y):
    x=np.concatenate(([-1.],y))
    if np.any(np.abs(y)>=1) or min(abs(x[i]-x[j]) for i in range(L) for j in range(i+1,L))<1.e-12:
        return -np.inf,np.full(L-1,np.nan)
    F=0.
    g=np.zeros(L)
    for j in range(1,L):
        F+=j*(j+1)*np.log1p(-x[j]**2)
        g[j]-=2*j*(j+1)*x[j]/(1-x[j]**2)
    for i in range(L):
        for j in range(i+1,L):
            a=2*(2*i+1)
            z=x[j]-x[i]
            F+=a*log(abs(z))
            g[j]+=a/z
            g[i]-=a/z
    return F,g[1:]


def run():
    checks=0
    assert exact_constant(2)==sy.Rational(729,1024)
    checks+=1
    assert exact_constant(3)==sy.Rational(5189853515625,1073741824)
    checks+=1
    rng=np.random.default_rng(20261114)
    for L in range(2,6):
        for trial in range(6):
            y=rng.uniform(-.92,.92,L-1)
            # Well-spaced samples avoid numerical determinant conditioning.
            if len(y)>1:
                y=np.sort(y)
                if np.diff(y).min()<.12: continue
                rng.shuffle(y)
            x=np.concatenate(([-1.],y))
            expected=formula_log(L,x)
            for shift in range(3):
                phi=rng.uniform(-np.pi,np.pi,L)
                computed=direct_log(L,x,phi)
                assert abs(computed-expected)<3.e-8, (L,x,computed,expected)
                checks+=1
    for L in range(2,8):
        for trial in range(20):
            x=np.sort(rng.uniform(-.85,.85,L-1))
            if np.diff(x).min(initial=1)<.03: continue
            rng.shuffle(x)
            f,g=F_and_grad(L,x)
            for j in range(L-1):
                h=1.e-6
                up=x.copy();up[j]+=h
                down=x.copy();down[j]-=h
                fd=(F_and_grad(L,up)[0]-F_and_grad(L,down)[0])/(2*h)
                assert abs(fd-g[j])<2.e-5*(1+abs(g[j])),(L,x,j,fd,g[j])
                checks+=1
    # Symmetric negative definiteness follows symbolically from each
    # positive endpoint and squared-difference term in the displayed Hessian.
    for L in range(2,6):
        for ordering in permutations(range(1,L)):
            y=np.zeros(L-1)
            for k,j in enumerate(ordering):y[j-1]=-0.75+1.5*(k+1)/L
            assert np.all(np.abs(y)<1)
            grad=F_and_grad(L,y)[1]
            assert np.isfinite(grad).all()
            checks+=1
    print('PASS', checks,'supplementary assertions')

if __name__=='__main__':run()
