"""Independent exact-identity and numerical checks for noisy coordinate-epoch sampling."""
import math
import numpy as np
import sympy as s


def exact_checks():
    c,u,v,p=s.symbols('c u v p',real=True)
    a=(u+c**2*v)/(1-c**4)
    d=(v+c**2*u)/(1-c**4)
    assert s.factor(a-c**2*d-u)==0
    assert s.factor(d-c**2*a-v)==0
    H=s.Matrix([[1,c],[c,1]])
    M12=s.Matrix([[0,-c],[0,c**2]])
    M21=s.Matrix([[c**2,0],[-c,0]])
    assert (M12.T*H*M12-s.diag(0,c**2*(1-c**2))).applyfunc(s.simplify)==s.zeros(2)
    assert (M21.T*H*M21-s.diag(c**2*(1-c**2),0)).applyfunc(s.simplify)==s.zeros(2)
    C12=s.Matrix([[a,-c*a],[-c*a,d]])
    C21=s.Matrix([[a,-c*d],[-c*d,d]])
    assert s.factor(C12.det()-a*v)==0
    assert s.factor(C21.det()-d*u)==0
    S=p*C12+(1-p)*C21
    risk=s.trace(H*S)/2
    expected=(u+v+2*c**2*((1-p)*u+p*v))/(2*(1+c**2))
    assert s.factor(risk-expected)==0
    assert s.factor(s.diff(expected,p)+c**2*(u-v)/(1+c**2))==0
    cumulant=2*p*(1-p)*c**2*(a-d)**2
    target=2*p*(1-p)*c**2*(u-v)**2/(1+c**2)**2
    assert s.factor(cumulant-target)==0
    assert s.factor(a-d-(u-v)/(1+c**2))==0
    print('Exact symbolic identities: PASS (marginal equations, contraction, covariance, risk, fourth cumulant).')


def simulation_checks():
    c=0.6;u=4.;v=1.;p=0.4
    a=(u+c*c*v)/(1-c**4); d=(v+c*c*u)/(1-c**4)
    cross=-c*(p*a+(1-p)*d)
    expected_risk=(u+v+2*c*c*((1-p)*u+p*v))/(2*(1+c*c))
    k=2*p*(1-p)*c*c*(u-v)**2/(1+c*c)**2
    rng=np.random.default_rng(20261118)
    x=np.zeros(2); N=210000; burn=5000
    xx=np.empty((N,2))
    for j in range(N+burn):
        e1=rng.normal(0,math.sqrt(u));e2=rng.normal(0,math.sqrt(v))
        if rng.random()<p:
            x[0]=-c*x[1]-e1
            x[1]=-c*x[0]-e2
        else:
            x[1]=-c*x[0]-e2
            x[0]=-c*x[1]-e1
        if j>=burn:xx[j-burn]=x
    a0=float(np.mean(xx[:,0]**2)); d0=float(np.mean(xx[:,1]**2));cross0=float(np.mean(xx[:,0]*xx[:,1]))
    risk0=(a0+d0+2*c*cross0)/2
    k0=float(np.mean(xx[:,0]**2*xx[:,1]**2)-a0*d0-2*cross0**2)
    for name,estimate,truth,tol in [('a',a0,a,0.13),('d',d0,d,0.10),('cross',cross0,cross,0.12),('risk',risk0,expected_risk,0.13),('mixed cumulant',k0,k,0.42)]:
        print(f'  {name}: sample={estimate:.6f}; exact={truth:.6f}; abs.diff={abs(estimate-truth):.6f}')
        assert abs(estimate-truth)<tol, name
    print('Independent stochastic chain check: PASS.')

if __name__=='__main__':
    exact_checks();simulation_checks()
