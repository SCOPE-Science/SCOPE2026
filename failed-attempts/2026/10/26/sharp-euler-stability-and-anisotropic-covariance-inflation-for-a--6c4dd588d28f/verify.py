"""Reproduce exact covariance stability and equilibrium identities for a two-mode stochastic Euler sampler.

Requires Python 3 and numpy; symbolic algebra uses stdlib Fraction only.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt
import numpy as np


def threshold(lam):
    q = 1.0 + lam
    return (q + 2.0 - sqrt(q*q - 4*q + 8))/(2*q)


def exact_solution(lam, h):
    # Fractions on a closed-form covariance recursion.
    q=1+lam
    f=q*(1-h)*(2-q*h)-1
    p=(q*(1-q*h/2)+lam)/f
    t=(1+2*lam*(1-h))/f
    return p,t,f


def covariance_matrix(lam, h):
    q=1+lam
    u=1-2*h
    v=1-q*h
    a=np.diag([u,v])
    b=np.array([[0.0, np.sqrt(lam)],[-1/np.sqrt(lam),0.0]])
    # For symmetric covariance [p,r,s], update is R -> a R a.T+2h b R b.T+2h I.
    cols=[]
    for basis in [np.array([[1.0,0.0],[0.0,0.0]]),
                  np.array([[0.0,1.0],[1.0,0.0]]),
                  np.array([[0.0,0.0],[0.0,1.0]])]:
        new = a@basis@a.T+2*h*b@basis@b.T
        cols.append([new[0,0],new[0,1],new[1,1]])
    return np.array(cols).T


def main():
    rng=Random(839172)
    exact_cases=0
    for _ in range(1500):
        lam=F(rng.randint(1,20),rng.randint(21,50))
        h=F(rng.randint(1,10),rng.randint(30,70))
        p,t,f=exact_solution(lam,h)
        assert f>0
        u=1-2*h;v=1-(1+lam)*h
        s=t/lam
        assert (1-u*u)*p-2*h*lam*s==2*h
        assert (1-v*v)*s-2*h/lam*p==2*h
        assert t-p==h*(1-lam)**2/(2*f)
        assert p>=1 and t>=1
        exact_cases+=1
    numerical_cases=0
    for lam in [0.00001,0.002,0.01,0.1,0.25,0.5,0.7,1.0]:
        hs=threshold(lam)
        for frac in [0.01,0.3,0.7,0.95,0.999,1.001,1.05,1.3,1.9]:
            h=frac*hs
            if h>=1:continue
            M=covariance_matrix(lam,h)
            rho=max(abs(np.linalg.eigvals(M)))
            assert (rho<1)==(h<hs), (lam,h,rho,hs)
            if h<hs:
                P=np.linalg.solve(np.eye(3)-M,np.array([2*h,0,2*h]))
                p,t,f=exact_solution(float(lam),float(h))
                assert np.allclose(P,[p,0,t/lam],atol=2e-6,rtol=2e-8)
            numerical_cases+=1
    print('EXACT_RATIONAL_CASES',exact_cases)
    print('FULL_COVARIANCE_EIGEN_CASES',numerical_cases)
    for lam in [0.001,0.1,0.5,1.0]:
        hs=threshold(lam)
        h=hs/2
        p,t,f=exact_solution(float(lam),float(h))
        print(f'lambda={lam:.5g} hstar={hs:.12f} sample_h={h:.12f} var_x={p:.8f} normalized_var_y={t:.8f} difference={t-p:.8f}')
    print('OK')

if __name__=='__main__':main()
