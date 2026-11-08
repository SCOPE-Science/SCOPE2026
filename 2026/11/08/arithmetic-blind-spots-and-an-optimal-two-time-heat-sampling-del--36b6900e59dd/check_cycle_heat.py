"""Reproducible checks for two-time half-cycle heat sampling."""
from math import pi, sin, cos, exp, sqrt, sinh
import numpy as np
from scipy.optimize import minimize_scalar, brentq

def eigenpair(d,t):
    a=exp(-(2-d)*t)
    b=exp(-(2+d)*t)
    matrix=np.array([[1.,1.],[a,b]])/sqrt(2)
    return np.linalg.eigvalsh(matrix.T@matrix)

def exact_bounds(n,t):
    if n%2 or n<4:
        raise ValueError('even n>=4')
    d=0. if n%4==0 else 2*sin(pi/n)
    q=exp(-4*t)
    c=np.cosh(2*t*d)
    tr=2+2*q*c
    det=2*q*(c-1)
    # for small d use stable determinant formula
    muplus=(tr+sqrt(tr**2-4*det))/2
    lower=det/(2*muplus)
    muplus_edge=(3+q*q+sqrt((3+q*q)**2-4*(1-q)**2))/2
    return lower,muplus_edge/2

def direct_bounds(n,t):
    omega=np.exp(2j*pi/n)
    j=np.arange(n)
    F=omega**np.outer(j,j)/sqrt(n)
    lam=2-2*np.cos(2*pi*j/n)
    H=F@np.diag(np.exp(-t*lam))@F.conj().T
    E=np.zeros((n//2,n)); E[np.arange(n//2),2*np.arange(n//2)]=1
    T=np.vstack((E,E@H))
    gram=T.conj().T@T
    return np.linalg.eigvalsh(gram)[[0,-1]]

if __name__=='__main__':
    tested=0
    for n in range(4,45,2):
        for t in (.07,.3,.5544287764393,1.2,2.5):
            a,b=exact_bounds(n,t)
            ad,bd=direct_bounds(n,t)
            assert abs(a-ad)<3e-12,(n,t,a,ad)
            assert abs(b-bd)<3e-12,(n,t,b,bd)
            if n%4==0: assert abs(a)<1e-13
            else: assert a>0
            tested+=1
    tau=brentq(lambda t:t-(1+exp(-4*t))/2,0.5,0.7)
    constant=4*pi*pi*tau*tau/(1+exp(4*tau))
    print('tau',format(tau,'.14f'),'sharp_N_squared_constant',format(constant,'.14f'))
    for n in (10,22,42,102,202,502):
        opt=minimize_scalar(lambda t:-exact_bounds(n,t)[0],bounds=(.15,2),method='bounded',options={'xatol':1e-12})
        assert opt.success
        ratio=n*n*(-opt.fun)/constant
        print('n',n,'topt',format(opt.x,'.10f'),'scaled_A_ratio',format(ratio,'.9f'))
    print('CYCLE_TWO_TIME_HEAT_PASS', 'direct_bound_comparisons',tested,'asymptotic_scales',6)
