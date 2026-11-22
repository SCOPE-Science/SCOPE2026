#!/usr/bin/env python3
"""Standalone deterministic numerical checks of the stated torus-knot curvature limit.
No external packages or data required. Numerical checks do not replace the analytic proof.
"""
import math

def exact_density(p,q,r,u):
    c,s=math.cos(u),math.sin(u)
    v=(-r*q*s,p*(1+r*c),r*q*c)
    a=(-p*p-r*(p*p+q*q)*c,-2*p*r*q*s,-r*q*q*s)
    cross=(v[1]*a[2]-v[2]*a[1],v[2]*a[0]-v[0]*a[2],v[0]*a[1]-v[1]*a[0])
    vv=sum(x*x for x in v)
    return math.sqrt(sum(x*x for x in cross))/vv

def average(f,n=8192):
    return (2*math.pi/n)*sum(f((j+.5)*2*math.pi/n) for j in range(n))

def torus_curvature(p,q,lam,n=8192):
    r=lam*p*p/(q*q)
    assert r<1
    return average(lambda u: exact_density(p,q,r,u),n)

def profile(lam,n=8192):
    return average(lambda u: math.hypot(1+lam*math.cos(u),lam*math.sin(u)),n)

def check():
    tests=0
    # Positive exact density, agreement with Cartesian derivatives
    for p,q in [(2,3),(2,7),(3,4),(3,10)]:
        for r in [.001,.08,.34]:
            for u in [0,.1,.5,1.1,2.0,3.1,4.2,5.9]:
                assert exact_density(p,q,r,u)>0;tests+=1
    # Scaling limit and sharp convergence for fixed p, exact arclength quadrature
    for p,q in [(2,41),(2,101),(2,401),(3,41),(3,101),(3,401),(4,101),(4,401)]:
        for lam in [0,.1,.5,.9,1.,1.1,1.6,3.0]:
            T=torus_curvature(p,q,lam)
            F=profile(lam)
            assert abs(T-p*F)<100*p**3*(1+lam)**2/q, (p,q,lam,T,p*F)
            tests+=1
    for lam in [.1,.2,.5,.9,1.1,1.7,3.0]:
        assert profile(lam)>profile(0)
        assert abs(profile(lam)-lam*profile(1/lam))<3e-13
        tests+=2
    assert abs(profile(1,32768)-8)<1e-7;tests+=1
    # Cusp expansion, quadrature may require refinement close to its integrable corner
    for delta in [-.02,-.01,.01,.02]:
        pred=8+4*delta+delta*delta*(math.log(8/abs(delta))-.5)
        obs=profile(1+delta,32768)
        assert abs(obs-pred)<.8*abs(delta)**3*(1+abs(math.log(abs(delta)))),(delta,obs,pred)
        tests+=1
    # Critical layer robust to coprimality; q*r ->0 in both outer regimes
    for p,q,lam in [(2,1001,1e-3),(3,2003,1e-2),(2,10001,100),(3,10003,50)]:
        T=torus_curvature(p,q,lam)
        if lam<1:
            assert abs(T/(2*math.pi*p)-1)<.01
        else:
            assert abs(T/(2*math.pi*p*lam)-1)<.03
        tests+=1
    print('PASS',tests,'deterministic checks')

if __name__=='__main__':check()

# Supplementary checks of the exact local normal form at the critical radius.
def local_cross_vector(p,q,r,u):
    c,s=math.cos(u),math.sin(u)
    v=(-r*q*s,p*(1+r*c),r*q*c)
    a=(-p*p-r*(p*p+q*q)*c,-2*p*r*q*s,-r*q*q*s)
    return (v[1]*a[2]-v[2]*a[1],v[2]*a[0]-v[0]*a[2],v[0]*a[1]-v[1]*a[0])

def local_check():
    checks=0
    for p,q in [(2,3),(2,5),(3,4),(4,7),(5,8)]:
        D=p*p+q*q;r=p*p/D
        V=math.hypot(p*(1-r),r*q)
        A=D*V
        B=p*r*q*q*(1+r)
        coefficient=D**4/(p**3*q*q*(2*p*p+q*q))
        assert math.isclose(coefficient,A*A/(B*V*V),rel_tol=2e-14);checks+=1
        assert math.hypot(*local_cross_vector(p,q,r,math.pi))<1e-11;checks+=1
        h=1e-5
        ddelta=tuple((x-y)/(2*h) for x,y in zip(local_cross_vector(p,q,r+h,math.pi),local_cross_vector(p,q,r-h,math.pi)))
        dx=tuple((x-y)/(2*h) for x,y in zip(local_cross_vector(p,q,r,math.pi+h),local_cross_vector(p,q,r,math.pi-h)))
        assert math.isclose(math.hypot(*ddelta),A,rel_tol=1e-8);checks+=1
        assert math.isclose(math.hypot(*dx),B,rel_tol=1e-8);checks+=1
        assert abs(sum(x*y for x,y in zip(ddelta,dx)))<1e-6*A*B;checks+=1
    print('PASS',checks,'local normal-form diagnostics')
if __name__=='__main__':local_check()
