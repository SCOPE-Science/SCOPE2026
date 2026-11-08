"""Deterministic diagnostics for the Luce variational interpolation.
Run with Python 3 and NumPy; all analytic inequalities are proved in RESULT.md.
"""
import math
import numpy as np

def H(v):
    return -(1.0-v)*np.log1p(-v)

def test_case(beta, a, b, theta):
    t=np.linspace(0.,1.,10001)
    f=np.exp(-beta*t)
    k=np.full_like(t,beta)
    u1=a*t/(1.-0.3*t)
    u2=b*t*(1.+0.2*t)
    du1=a/(1.-0.3*t)**2
    du2=b*(1.+0.4*t)
    v1=-np.expm1(-f*u1)
    v2=-np.expm1(-f*u2)
    q1=f*du1*np.exp(-f*u1)
    q2=f*du2*np.exp(-f*u2)
    v=theta*v1+(1-theta)*v2
    delta=H(v)-theta*H(v1)-(1-theta)*H(v2)
    assert np.min(delta+1e-13)>=0
    assert np.min(delta+1e-13-0.5*theta*(1-theta)*(v1-v2)**2)>=0
    qtheta=theta*q1+(1-theta)*q2+k*delta
    umix=-np.log1p(-v)/f
    assert np.min(qtheta)>=0
    assert np.min(umix)>=-1e-12
    # Chain-rule numerical derivative tested on interior nodes.
    pred=qtheta/(f*(1-v))
    deriv=np.gradient(umix,t)
    assert np.max(np.abs(deriv[1:-1]-pred[1:-1]))<0.002
    A1=np.trapezoid(np.sqrt(q1),t)
    A2=np.trapezoid(np.sqrt(q2),t)
    Amix=np.trapezoid(np.sqrt(qtheta),t)
    assert Amix>=theta*A1+(1-theta)*A2-1e-10
    if beta>0 or abs(a-b)>1e-9:
        assert Amix>theta*A1+(1-theta)*A2+1e-9
    return Amix-theta*A1-(1-theta)*A2

if __name__=='__main__':
    n=0; mindelta=float('inf')
    for beta in (0.0,0.2,0.8,3.0,6.0):
        for a in (0.1,0.3,0.9,2.0):
            for b in (0.15,0.4,1.2,2.5):
                for theta in (0.15,0.5,0.85):
                    mindelta=min(mindelta,test_case(beta,a,b,theta));n+=1
    print(f'PASS: {n} parameter configurations; smallest Jensen gap {mindelta:.9g}')
