"""Reproducibility checks for the directed circular heat-to-Poisson projection."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def root_constant():
    def moment(c):
        return quad(lambda u: math.exp(-u-(u/c)**2), 0, 45, epsabs=2e-13)[0]
    return brentq(lambda c: moment(c)-0.5, 0.1, 5, xtol=5e-15)


def limiting_K(c):
    def e_log():
        return quad(lambda x: math.exp(-x*x/4)*math.log(c*c+x*x)/math.sqrt(math.pi), 0, 30, epsabs=2e-13)[0]
    return math.log(math.pi/c)-0.5*math.log(4*math.pi*math.e)+e_log()


def solve_s(t):
    nn=np.arange(1, max(40, int(math.sqrt(40/t))+1), dtype=float)
    a=np.exp(-t*nn*nn)
    def gap(s):
        return np.dot(a, np.exp(-s*nn))-1/math.expm1(2*s)
    return brentq(gap, 1e-8, max(t+1,4), xtol=3e-15)


def heat_on_grid(t, N=32768):
    theta=2*math.pi*np.arange(N)/N
    theta=np.where(theta>math.pi,theta-2*math.pi,theta)
    H=np.zeros(N)
    for k in range(-6,7):
        H+=np.exp(-(theta+2*math.pi*k)**2/(4*t))
    return theta, math.sqrt(math.pi/t)*H


def kl_grid(t,s,phi=0):
    theta,H=heat_on_grid(t)
    r=math.exp(-s)
    P=(1-r*r)/(1+r*r-2*r*np.cos(theta-phi))
    entr=np.zeros_like(H)
    good=H>0
    entr[good]=H[good]*(np.log(H[good])-np.log(P[good]))
    return float(np.mean(entr))


def stationary_residual(t,s):
    n=np.arange(1, max(40,int(math.sqrt(40/t))+1), dtype=float)
    return float(np.dot(np.exp(-t*n*n),np.exp(-s*n))-1/math.expm1(2*s))


def run():
    checks=0
    c=root_constant(); K=limiting_K(c)
    assert abs(c-0.86550319873261586)<5e-13
    assert abs(K-0.18275830866970635)<5e-12
    checks+=2
    for t in [0.0005,0.001,0.01,0.05,0.2,0.7,2,4]:
        s=solve_s(t)
        assert s>t and abs(stationary_residual(t,s))<2e-9
        checks+=2
        for factor in [0.85,1.0,1.2]:
            kval=kl_grid(t,s*factor)
            assert kval>=-1e-8
            checks+=1
        opt=kl_grid(t,s)
        for factor in [0.6,0.85,1.2,1.7]:
            assert opt<kl_grid(t,s*factor)+3e-8
            checks+=1
        assert opt<kl_grid(t,s,0.6)+3e-8
        checks+=1
    for t in [0.0005,0.001,0.01]:
        s=solve_s(t)
        assert abs(s/math.sqrt(t)-c)<0.02
        assert abs(kl_grid(t,s)-K)<0.008
        checks+=2
    t=0.0005
    assert kl_grid(t,t)>kl_grid(t,solve_s(t))+1.0
    checks+=1
    # Verify long-time asymptotics against an independently solved scalar stationarity equation.
    for t in [3,4,5]:
        s=solve_s(t); q=math.exp(-t); r=math.exp(-s)
        assert abs(r-(q-q**3+3*q**5))<30*q**7
        checks+=1
    print({'status':'PASS','checks':checks,'c_star':c,'K_star':K,
           'numerical_qualifier':'Finite diagnostics only; proofs are analytic.'})

if __name__=='__main__':run()
