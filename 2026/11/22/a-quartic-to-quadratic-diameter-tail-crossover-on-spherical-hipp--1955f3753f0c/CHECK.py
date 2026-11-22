#!/usr/bin/env python3
"""Deterministic checks for antipodal distance tails on sphere/cylinder curves."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipe, beta
from numpy.polynomial.legendre import leggauss

def gamma(t,a=1.):
    return np.array((a*(1+np.cos(t)),a*np.sin(t),2*a*np.sin(t/2))).T

def length_viviani():
    return 8*np.sqrt(2)*ellipe(.5)

def critical_constant():
    return 2**(-15/4)*beta(.25,1.5)/ellipe(.5)**2

def exact_tail_viviani(delta,n=140):
    # Event is restricted to two ordered pole pairs for small delta.
    c=2*delta-delta**2/4
    vmax=math.acos(1-math.sqrt(c))
    nodes, weights=leggauss(n)
    result=0.
    for V,Wv in zip(nodes,weights):
        v=vmax*V
        excess=c-(1-math.cos(v))**2
        umax=math.acos(min(1.,max(-1.,1-excess/(1+math.cos(v))))) if excess>0 else 0.
        u=umax*nodes
        ws=np.sqrt(1+np.sin((u+v)/2)**2)*np.sqrt(1+np.sin((u-v)/2)**2)
        result+=Wv*vmax*umax*np.dot(weights,ws)
    return 4*result/length_viviani()**2

def generalized_length(b):
    xlo=2*b-2
    def curve_integrand(theta):
        # transformation x=xlo+(2-xlo)*sin(theta)^2
        s=math.sin(theta); c=math.cos(theta)
        x=xlo+(2-xlo)*s*s
        dx=2*(2-xlo)*s*c
        if s==0 or c==0:
            return 0.0
        yy=(2-x)*(x-xlo)
        w=math.sqrt(1+(b-x)**2/yy+b/(2*(2-x)))
        return dx*w
    return 4*quad(curve_integrand,0,math.pi/2,epsabs=1e-10,limit=200)[0]

def generic_coefficient(b):
    h=4*(1-b); k=b*b/h+b/4
    L=generalized_length(b)
    return 16*math.pi*(1+k)/(L*L*math.sqrt(k))

def test():
    print('L_1',length_viviani(),'C_critical',critical_constant())
    for delta in [0.1,0.03,0.01,0.003,0.001,0.0003]:
        tail=exact_tail_viviani(delta)
        print('delta',delta,'exact',tail,'tail/delta^.75',tail/delta**.75,'ratio_to_limit',tail/(critical_constant()*delta**.75))
    for b in [.25,.5,.75,.95,.99]:
        print('offset',b,'L',generalized_length(b),'C_linear',generic_coefficient(b))
    # Algebraic identity: sum-of-antipodes exact formula for Viviani C near poles
    rng=np.random.default_rng(235)
    for _ in range(1000):
        u,v=rng.uniform(-.5,.5,2)
        s=u+v;q=u-v
        p=gamma(math.pi+s); z=gamma(3*math.pi+q)
        exact=np.sum((p+z)**2)
        rhs=4*((1-math.cos(v))**2+(1+math.cos(v))*(1-math.cos(u)))
        assert np.isclose(exact,rhs,rtol=1e-11,atol=1e-12), (exact,rhs)
    assert abs(critical_constant()-.14244157343155)<1e-12
    print('pass: 1000 independent exact-identity checks; quadrature table')

if __name__=='__main__': test()

def crossover_area(kappa):
    a=np.sqrt(2)*kappa
    lo=np.sqrt(max(0.,a-1.)); hi=np.sqrt(a+1.)
    area=4*quad(lambda v: np.sqrt(max(0.,1-(v*v-a)**2)),lo,hi,epsabs=1e-12,limit=300)[0]
    return area

def direct_crossover(delta,kappa,n=900):
    # Composite midpoint quadrature on a fixed scaled box with exact geometric predicates.
    b=1-kappa*np.sqrt(delta)
    assert 0<b<=1
    A=np.sqrt(2)*kappa
    vmax=np.sqrt(A+1)+.25
    umax=1.25
    U=(np.arange(n)+.5)*(2*umax/n)-umax
    V=(np.arange(n)+.5)*(2*vmax/n)-vmax
    UU,VV=np.meshgrid(U,V,indexing='ij')
    u=np.sqrt(2*delta)*UU;v=(8*delta)**.25*VV
    y1=u+v;y2=u-v
    r=2-b
    x1=b-np.sqrt(r*r-y1*y1)
    x2=b-np.sqrt(r*r-y2*y2)
    z1=np.sqrt(4-x1*x1-y1*y1)
    z2=np.sqrt(4-x2*x2-y2*y2)
    gap=(x1+x2)**2+(y1+y2)**2+(z1-z2)**2
    flag=gap<(8*delta-delta*delta)
    dx1=y1/np.sqrt(r*r-y1*y1)
    dx2=y2/np.sqrt(r*r-y2*y2)
    dz1=-(x1*dx1+y1)/z1
    dz2=-(x2*dx2+y2)/z2
    w1=np.sqrt(1+dx1*dx1+dz1*dz1)
    w2=np.sqrt(1+dx2*dx2+dz2*dz2)
    area_weighted=np.mean(flag*w1*w2)*4*umax*vmax
    ratio=2**(13/4)*area_weighted/generalized_length(b)**2
    predicted=2**(-15/4)*crossover_area(kappa)/ellipe(.5)**2
    return ratio,predicted

if __name__=='__main__':
    print('CROSSOVER')
    for k in [0.,.2,1/np.sqrt(2),1.,2.]:
        print('kappa',k,'area',crossover_area(k),'predicted',2**(-15/4)*crossover_area(k)/ellipe(.5)**2)
        for d in [0.003,0.0003]:
            print(' ',d,'direct,pred',direct_crossover(d,k,n=700))
