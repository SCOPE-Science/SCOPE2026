"""Reproduce exact identities and auxiliary numerical checks for OU quadratic-energy sampling.

The finite numerical tests illustrate but do not prove the global analytical results.
Dependencies: sympy, numpy, scipy, mpmath.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar
import mpmath as mp

def exact_checks():
    d,r,z,w=sp.symbols('d r z w',real=True,positive=True)
    K=sp.Matrix([[1,r],[r,1]])
    B=sp.Matrix([[1-(z+r*r*w)/2,r*(d+1-(z+w)/2)],
                 [r*(d+1-(z+w)/2),1-(r*r*z+w)/2]])
    F=sp.factor(sp.trace(K.inv()*B*K.inv()*B))
    const=sp.factor(F.subs({z:0,w:0}))
    reduced=sp.expand((z+w)**2/4-(z+w)-(1-r*r)*z*w/2)
    assert sp.simplify(F-const-reduced)==0
    e=sp.symbols('e',positive=True)
    mu_p=1+d/(1+sp.exp(d))-e*(1+sp.exp(-d))/2
    mu_m=1-d/(sp.exp(d)-1)-e*(1-sp.exp(-d))/2
    centered=sp.factor(F.subs({z:e,w:e,r:sp.exp(-d)}))
    assert sp.simplify(centered-mu_p**2-mu_m**2)==0
    L=sp.symbols('L',positive=True)
    phi=mu_p.subs(e,sp.exp(d-L))**2+mu_m.subs(e,sp.exp(d-L))**2
    assert sp.simplify(sp.limit(phi,d,0,dir='+')-(1-sp.exp(-L))**2)==0
    assert sp.simplify(sp.limit(sp.diff(phi,d),d,0,dir='+')-(1-sp.exp(-L))**2)==0
    assert sp.simplify(sp.diff(mu_p.subs(e,sp.exp(d-L)),d).subs(d,L)-(
        (-sp.exp(2*L)-2*L*sp.exp(L)+1)/(2*(sp.exp(L)+1)**2)))==0
    assert sp.simplify(sp.diff(mu_m.subs(e,sp.exp(d-L)),d).subs(d,L)-(
        (-sp.exp(2*L)+2*L*sp.exp(L)+1)/(2*(sp.exp(L)-1)**2)))==0
    h=d/sp.tanh(d)-2
    DD=sp.factor(sp.diff(h,d)**2*sp.sinh(d)**4-h*sp.diff(h,d,2)*sp.sinh(d)**4)
    from_series=sp.series(DD,d,0,18).removeO()
    target=sum(sp.Rational(2)**(2*n-2)*(2**(2*n-1)-4*n*n+10*n-8)*d**(2*n)/sp.factorial(2*n) for n in range(2,9))
    assert sp.expand(from_series-target)==0
    print('PASS symbolic matrix identity, centered spectrum, endpoint derivatives, positive-series coefficients')

def phi(L,d):
    r=np.exp(-d)
    e=np.exp(d-L)
    plus=1+d*r/(1+r)-e*(1+r)/2
    minus=1-d*r/(1-r)-e*(1-r)/2
    return plus**2+minus**2

def direct(L,u,v):
    s,t=sorted((float(u),float(v)))
    dd=t-s
    r=np.exp(-dd)
    z=np.exp(-2*s)
    w=np.exp(-2*(L-t))
    K=np.array([[1,r],[r,1.]])
    B=np.array([[1-(z+r*r*w)/2,r*(dd+1-(z+w)/2)],
                [r*(dd+1-(z+w)/2),1-(r*r*z+w)/2]])
    C=np.linalg.solve(K,B)
    return np.trace(C@C)

def numerical_checks():
    rng=np.random.default_rng(1729)
    count=0
    for L in [0.2,0.5,1.,2.,3.,5.,10.,20.]:
        opt=minimize_scalar(lambda x:-phi(L,x),bounds=(1e-5,L),method='bounded',options={'xatol':1e-12})
        assert -opt.fun > (1-np.exp(-L))**2
        assert 0<opt.x<L
        assert abs(direct(L,(L-opt.x)/2,(L+opt.x)/2)-(-opt.fun))<1e-8
        for i in range(1000):
            u,v=sorted(rng.uniform(0,L,size=2))
            if v-u<0.002: continue
            centered=direct(L,(L-(v-u))/2,(L+(v-u))/2)
            assert centered+1e-9 >= direct(L,u,v)
            assert abs(centered-phi(L,v-u))<1e-8
            count+=1
    mp.mp.dps=50
    h=lambda d:d*mp.coth(d)-2
    g=lambda d:2*d*h(d)/mp.expm1(2*d)
    root=mp.findroot(lambda x:mp.diff(g,x), (mp.mpf('2.4'),mp.mpf('2.8')))
    assert abs(float(root)-2.554928950095267)<2e-13
    assert abs(float(2+g(root))-2.0181855560856615)<2e-13
    for L in [20.,35.,60.]:
        best=minimize_scalar(lambda d:-phi(L,d),bounds=(0.01,min(L,6.)),method='bounded',options={'xatol':1e-13})
        assert abs(best.x-float(root)) < 0.04
    print(f'PASS {count} independent centered-vs-unrestricted placements and finite-horizon checks')
    print('Asymptotic gap:',mp.nstr(root,22),'limiting score:',mp.nstr(2+g(root),22))

if __name__=='__main__':
    exact_checks()
    numerical_checks()
