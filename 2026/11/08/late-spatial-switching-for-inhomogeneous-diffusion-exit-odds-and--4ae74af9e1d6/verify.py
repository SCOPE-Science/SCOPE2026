"""Finite-state and spectral consistency tests for one-dimensional exit-time odds.

Run: python verify.py
Requires Python 3, NumPy and SciPy. These tests do not establish
uniform-in-time or continuum theorems; the proof is analytic.
"""
from fractions import Fraction
from math import exp
import numpy as np
from scipy.linalg import eigh_tridiagonal


def exact_lattice_tests():
    # Non-lazy, spatially inhomogeneous nearest-neighbor chain with absorbing
    # endpoints. Exact rational first-exit masses at finite times.
    # Comparisons require the same starting parity and exit-time parity:
    # this lattice control is not a proof of the diffusion result.
    n = 7
    hold = Fraction(0, 1)
    up = [Fraction(0)] + [
        (1-hold)*Fraction(2*i+3, 2*i+3 + (i+2)**2)
        for i in range(1,n+1)
    ]
    down = [Fraction(0)] + [1-hold-up[i] for i in range(1,n+1)]
    F0 = [[Fraction(0) for _ in range(n+1)] for _ in range(30)]
    Fa = [[Fraction(0) for _ in range(n+1)] for _ in range(30)]
    F0[1][1]=down[1]
    Fa[1][n]=up[n]
    for t in range(2,30):
        for i in range(1,n+1):
            F0[t][i] = hold*F0[t-1][i]
            Fa[t][i] = hold*Fa[t-1][i]
            if i>1:
                F0[t][i] += down[i]*F0[t-1][i-1]
                Fa[t][i] += down[i]*Fa[t-1][i-1]
            if i<n:
                F0[t][i] += up[i]*F0[t-1][i+1]
                Fa[t][i] += up[i]*Fa[t-1][i+1]
    checked = 0
    for s in range(1,29):
        for t in range(s+1,30):
            for i in range(1,n+1):
                for j in range(i+2,n+1,2):
                    if (s-i)%2 or (t-i)%2: continue
                    # The earlier lower exit favours the smaller starting state.
                    assert F0[s][i]*F0[t][j] >= F0[t][i]*F0[s][j], (s,t,i,j,F0[s][i],F0[t][j],F0[t][i],F0[s][j])
                    # The earlier upper exit favours the larger starting state.
                    assert Fa[s][j]*Fa[t][i] >= Fa[t][j]*Fa[s][i]
                    checked += 2
    return checked


def root_linear(x,y):
    inds = np.flatnonzero(y[:-1]*y[1:] < 0)
    assert len(inds)==1
    i=int(inds[0])
    return x[i]-y[i]*(x[i+1]-x[i])/(y[i+1]-y[i])


def spectral_tests():
    checked=0
    details=[]
    for n in (50,90,140):
        h=1/(n+1)
        x=np.arange(1,n+1)*h
        A=.5
        b=2*x*x
        up=A/h**2+b/(2*h)
        down=A/h**2-b/(2*h)
        assert np.all(down>0)
        lam,U=eigh_tridiagonal(up+down,-np.sqrt(up[:-1]*down[1:]))
        for j in range(3):
            if U[0,j]<0: U[:,j]*=-1
        assert np.all(U[:,0]>0)
        assert lam[0]>0 and lam[0]<lam[1]<lam[2]
        star=root_linear(x,U[:,1])
        c0=U[0,:]/U[0,0]
        ca=U[-1,:]/U[-1,0]
        K=(lam-lam[0])*(c0-ca)
        assert K[1]>0
        predconst=-K[2]*np.interp(star,x,U[:,2])/(K[1]*np.interp(star,x,np.gradient(U[:,1],x)))
        for t in (.07,.09,.11,.15,.18,.22,.26):
            E=np.exp(-(lam-lam[0])*t)
            ff0=(U*E).dot(U[0,:]); ffa=(U*E).dot(U[-1,:])
            # Remove the common principal eigenvalue from both log derivatives.
            df0=(U*(E*(lam-lam[0]))).dot(U[0,:])
            dfa=(U*(E*(lam-lam[0]))).dot(U[-1,:])
            D=df0/ff0-dfa/ffa
            assert np.all(np.isfinite(D))
            assert np.max(np.diff(D)) < 5e-7
            ix=np.flatnonzero(D[:-1]*D[1:]<0)
            assert len(ix)==1
            sw=root_linear(x,D)
            assert abs(sw-star)<.02
            checked+=5
            if t>=.18 and t<=.22:
                pred=predconst*exp(-(lam[2]-lam[1])*t)
                assert np.sign(sw-star)==np.sign(pred)
                assert abs((sw-star)/pred-1)<.24
                checked+=2
        details.append((n,tuple(round(v,7) for v in lam[:3]),round(star,7)))
    return checked,details


if __name__=='__main__':
    a=exact_lattice_tests()
    b,details=spectral_tests()
    print('PASS',a,'exact parity-compatible lattice determinant inequalities')
    print('PASS',b,'finite-grid spectral/root consistency assertions')
    print('Discrete-diffusion eigenvalues and approximate switching nodes:')
    for d in details:print(d)
    print('TOTAL',a+b,'assertions')
