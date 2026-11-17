"""Numerical checks for the random parabolic-tangent beta–Jacobi law."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import beta as B, gamma

def area_det(a,b,c):
    ls=[a,b,c]
    v=np.array([[(ls[i]+ls[j])/2,ls[i]*ls[j]] for i,j in ((0,1),(0,2),(1,2))])
    return abs(np.linalg.det(np.column_stack((v[1]-v[0],v[2]-v[0]))))/2

def density(t,p,q):
    return abs(t)**(q-1)*max(0,1-t*t)**(p-1)/B(q/2,p)

def coefficient(p,q):
    d=2*p+q/2
    return (6*2**(2*p-2+q/2)*(4/3)**(2*p)*gamma(p)**2*gamma(q/2)
            /(B(q/2,p)**3*gamma(d+1)))

def prob_tail(eps,p,q):
    # Exact 2D deterministic quadrature over ordered outer nodes; integrate central node analytically.
    target=.5-eps
    threshold=(16*target)**(1/3)
    max_s=2-threshold
    norm=B(q/2,p)
    def inner_y(z):
        # z=distance between outside samples, exactly threshold <= z <= 2
        delta=z-threshold
        a0=-1
        a1=1-z
        midhalf=z/2*math.sqrt(max(0,1-16*target/z**3))
        def g(a):
            bmid=a+z/2
            lo,hi=bmid-midhalf,bmid+midhalf
            if lo>0:
                ib=quad(lambda t:density(t,p,q),lo,hi,epsabs=1e-11)[0]
            elif hi<0:
                ib=quad(lambda t:density(t,p,q),lo,hi,epsabs=1e-11)[0]
            else:
                ib=(quad(lambda t:density(t,p,q),lo,0,epsabs=1e-11)[0]
                   +quad(lambda t:density(t,p,q),0,hi,epsabs=1e-11)[0])
            return 6*density(a,p,q)*density(a+z,p,q)*ib
        return quad(g,a0,a1,epsabs=1e-10)[0]
    return quad(inner_y,threshold,2,epsabs=1e-10)[0]

rng=np.random.default_rng(20261110)
for _ in range(1000):
    a,b,c=np.sort(rng.uniform(-1,1,3))
    assert math.isclose(area_det(a,b,c),.25*(b-a)*(c-b)*(c-a),rel_tol=3e-11,abs_tol=3e-14)
for p,q in [(1,1),(2,2),(1,3)]:
    assert abs(quad(lambda x:density(x,p,q),-1,1,points=[0],epsabs=1e-12)[0]-1)<1e-11
    K=coefficient(p,q)
    for eps in [.025,.007]:
        true=prob_tail(eps,p,q)
        ratio=true/(K*eps**(2*p+q/2))
        print('p,q,eps,actual/predicted:',p,q,eps,ratio)
        assert .72<ratio<1.35
assert abs(coefficient(1,1)-32*math.sqrt(2)/45)<1e-13
print('JACOBI_TANGENT_TWO_SCALE_TAIL_DIAGNOSTICS_OK')
