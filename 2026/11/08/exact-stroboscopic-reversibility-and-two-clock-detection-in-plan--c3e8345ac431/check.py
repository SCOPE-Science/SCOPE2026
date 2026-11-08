"""Numerical diagnostics for planar stationary OU sampling identities.

Run with python check.py (requires numpy and scipy). Finite checks supplement,
but do not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov


def cov_stationary(B,D):
    return solve_continuous_lyapunov(B, -2*D)


def paired_kl(B,D,t):
    S=cov_stationary(B,D)
    E=expm(t*B)
    V=E@S
    C=np.block([[S,V.T],[V,S]])
    Crev=np.block([[S,V],[V.T,S]])
    return (np.trace(np.linalg.solve(Crev,C))-4)/2


def ep_continuous(B,D):
    S=cov_stationary(B,D)
    J=B@S-S@B.T
    return np.trace(np.linalg.solve(S,J.T)@np.linalg.solve(D,J))/4


def predicate(B,D,t):
    S=cov_stationary(B,D)
    E=expm(B*t)
    return np.linalg.norm(E@S-S@E.T,ord='fro')


def phase_frequency(B):
    delta=(np.trace(B)**2)/4-np.linalg.det(B)
    return math.sqrt(-delta) if delta<0 else 0.


def analytic_kl(gamma,omega,t):
    return 4*math.sin(omega*t)**2/math.expm1(2*gamma*t)


def main():
    checks=0
    # A rotating OU has exact aliases, regardless of anisotropic noise.
    for gamma in (0.3, 0.9, 2.0):
        for omega in (0.65, 1.8, 3.1):
            B=np.array([[-gamma,-omega],[omega,-gamma]])
            for D in (np.diag([0.7,2.2]),np.array([[1.5,0.4],[0.4,1.0]]),np.eye(2)):
                S=cov_stationary(B,D)
                assert np.linalg.eigvalsh(S).min()>0; checks+=1
                assert ep_continuous(B,D)>0; checks+=1
                for n in (1,2,3):
                    t=n*math.pi/omega
                    assert predicate(B,D,t)<1e-11;checks+=1
                    assert abs(paired_kl(B,D,t))<1e-9;checks+=1
                t=0.37*math.pi/omega
                assert predicate(B,D,t)>1e-5;checks+=1
                assert paired_kl(B,D,t)>1e-9;checks+=1
            # isotropic closed form and its continuum limit
            D=np.eye(2)
            for t in (0.01,0.2,0.7,1.3,2.1):
                assert abs(paired_kl(B,D,t)-analytic_kl(gamma,omega,t))<1e-9;checks+=1
            assert abs(ep_continuous(B,D)-(2*omega**2/gamma))<1e-10;checks+=1
            assert abs(analytic_kl(gamma,omega,1e-5)/1e-5-2*omega**2/gamma)<0.003;checks+=1
    # Nonnormal, non-reversible real and repeated-real spectra: never alias.
    real_drifts=[np.array([[-0.8,0.7],[0.2,-1.2]]),
                 np.array([[-1.3,2.0],[0.,-1.3]]),
                 np.array([[-0.6,0.1],[0.,-1.8]])]
    for B in real_drifts:
        for D in (np.eye(2),np.diag([1.0,2.0])):
            S=cov_stationary(B,D)
            J=B@S-S@B.T
            if np.linalg.norm(J)<1e-10:
                for t in (0.1,0.3,1.1):
                    assert predicate(B,D,t)<1e-11;checks+=1
            else:
                for t in (0.1,0.3,1.1,2.0,3.2):
                    assert predicate(B,D,t)>1e-8;checks+=1
                    assert paired_kl(B,D,t)>1e-10;checks+=1
    # General complex-spectrum, nonnormal drift, anisotropic diffusion.
    B=np.array([[-1.2,3.0],[-0.4,-0.6]])
    D=np.array([[2.0,0.3],[0.3,0.7]])
    assert max(np.real(np.linalg.eigvals(B)))<0;checks+=1
    w=phase_frequency(B)
    assert w>0;checks+=1
    for k in (1,2,3):
        assert predicate(B,D,k*math.pi/w)<1e-10;checks+=1
    for t in (0.3,1.,2.):
        if abs(math.sin(w*t))>0.01:
            assert predicate(B,D,t)>1e-5;checks+=1
    # Two incommensurable lags cannot simultaneously hit an exact alias.
    t1,t2=1.0,math.sqrt(2)
    B=np.array([[-0.4,-math.pi],[math.pi,-0.4]])
    D=np.eye(2)
    assert predicate(B,D,t1)<1e-12;checks+=1
    assert predicate(B,D,t2)>1e-3;checks+=1
    print(f"PASS {checks} deterministic assertions")

if __name__=='__main__':main()
