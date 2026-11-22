#!/usr/bin/env python3
"""Deterministic diagnostic checks for a triaxial ellipsoid's area-weighted curvature law.
Analytical proof is in RESULT.md; these finite checks do not replace it.
Requires numpy and scipy. Run: python check_curvature.py
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.stats import qmc


def model(a,b,c):
    assert a>b>c>0
    l1,l2,l3 = (1/a**2,1/b**2,1/c**2)
    C=l1*l2*l3
    x,w=leggauss(110)
    phi=np.pi*(x+1)/4
    z=(x+1)/2
    ell=l1+(l2-l1)*np.sin(phi)**2
    # Z=8 int_0^(pi/2) int_0^1 sqrt(Q) dz dphi
    integrand=np.sqrt(ell[:,None]+(l3-ell[:,None])*z[None,:]**2)
    Z=math.pi * np.einsum('i,j,ij->',w,w,integrand)
    kminus=C/l3**2; kplus=C/l1**2; ks=C/l2**2
    dminus=math.pi*l3**1.5/(Z*kminus*math.sqrt((l3-l1)*(l3-l2)))
    dplus=math.pi*l1**1.5/(Z*kplus*math.sqrt((l2-l1)*(l3-l1)))
    B=l2**1.5/(Z*ks*math.sqrt((l2-l1)*(l3-l2)))
    def fq(q):
        if not l1 < q < l3:
            return 0.
        A=l2-l1
        if q<l2:
            v=(q-l1)/A
            def fn(t):
                ss=math.sin(t)**2
                ell_t=l1+(q-l1)*ss
                return 1./math.sqrt((l3-ell_t)*(1-v*ss))
            I=4/math.sqrt(A)*quad(fn,0,math.pi/2,epsabs=1e-10,epsrel=1e-10,limit=400)[0]
        else:
            def fn(t):
                ell_t=l1+A*math.sin(t)**2
                return 1/math.sqrt((l3-ell_t)*(q-ell_t))
            I=4*quad(fn,0,math.pi/2,epsabs=1e-10,epsrel=1e-10,limit=400)[0]
        return math.sqrt(q)*I/Z
    def fk(k):
        if not kminus<k<kplus:return 0.
        q=math.sqrt(C/k)
        return fq(q)*q/(2*k)
    return locals()


def test_case(a,b,c):
    m=model(a,b,c); tests=0
    C=m['C']; l1,l2,l3=m['l1'],m['l2'],m['l3']
    Z=m['Z']; fk=m['fk']; fq=m['fq']
    lo=m['kminus']; hi=m['kplus']; mid=m['ks']
    assert abs(lo-c*c/(a*a*b*b))<1e-12;tests+=1
    assert abs(hi-a*a/(b*b*c*c))<1e-12;tests+=1
    assert abs(mid-b*b/(a*a*c*c))<1e-12;tests+=1
    # Independent solid-angle Jacobian numerical check by finite difference geometry.
    for theta in [0.33,0.92,1.64,2.47]:
        for phi in [0.23,1.05,2.15]:
            u=np.array([math.sin(theta)*math.cos(phi),math.sin(theta)*math.sin(phi),math.cos(theta)])
            dt=np.array([math.cos(theta)*math.cos(phi),math.cos(theta)*math.sin(phi),-math.sin(theta)])*np.array([a,b,c])
            dp=np.array([-math.sin(theta)*math.sin(phi),math.sin(theta)*math.cos(phi),0])*np.array([a,b,c])
            actual=np.linalg.norm(np.cross(dt,dp));expected=a*b*c*math.sqrt(sum(u*u*np.array([l1,l2,l3])))*math.sin(theta)
            assert abs(actual-expected)<1e-11;tests+=1
    # A weighted spherical sampling check: Sobol quadrature of Q and curvature.
    sob=qmc.Sobol(d=2,scramble=False).random_base2(m=17)
    zz=2*sob[:,0]-1;ph=2*math.pi*sob[:,1]
    xx=np.sqrt(1-zz**2)*np.cos(ph);yy=np.sqrt(1-zz**2)*np.sin(ph)
    Q=l1*xx**2+l2*yy**2+l3*zz**2
    weight=np.sqrt(Q)
    assert abs(4*math.pi*weight.mean()-Z)<2e-3;tests+=1
    for q in [l1+0.2*(l2-l1),l2+0.25*(l3-l2),l2+0.75*(l3-l2)]:
        sampled=(weight*(Q<=q)).sum()/weight.sum()
        # integrate the q pdf, avoiding the saddle via explicit split
        target=quad(fq,l1,q,points=[l2] if l2<q else None,epsabs=1e-7,epsrel=1e-7,limit=180)[0]
        assert abs(sampled-target)<3e-3,(sampled,target);tests+=1
    # Near-endpoint f_K convergence with explicit inverse from density ratio.
    for t in [1e-3,1e-4,1e-5]:
        low=fk(lo+t*(mid-lo));high=fk(hi-t*(hi-mid))
        assert abs(low/m['dminus']-1)<.09,(a,b,c,'low',low,m['dminus'])
        assert abs(high/m['dplus']-1)<.09,(a,b,c,'high',high,m['dplus'])
        tests+=2
    r=math.sqrt(hi/lo); g=(m['dminus']/m['dplus'])**2/r**7
    recovered_l2=math.sqrt(lo*hi)
    recovered_l1=recovered_l2*(1+g)/(1+r*g)
    recovered_l3=r*recovered_l1
    rec=(1/math.sqrt(recovered_l1),1/math.sqrt(recovered_l2),1/math.sqrt(recovered_l3))
    assert max(abs(x-y) for x,y in zip(rec,(a,b,c)))<1e-10,(rec,a,b,c)
    tests+=1
    # Gauss-Bonnet: area-average curvature equals 4pi/area.
    area=a*b*c*Z
    measured=(weight*(C/Q**2)).sum()/weight.sum()
    exact=4*math.pi/area
    assert abs(measured-exact)/exact<1e-3,(measured,exact)
    tests+=1
    # Near saddle density ratio tends to known logarithm coefficient.
    for d in [1e-3,1e-4]:
        for sign in [-1,1]:
            kval=mid*(1+sign*d)
            value=fk(kval)
            assert value>m['B']*math.log(1/d)*.75,(value,m['B'])
            tests+=1
    print(f'axes=({a:g},{b:g},{c:g}) tests={tests}; Z={Z:.12g}; K endpoints=({lo:.12g},{hi:.12g}); B={m["B"]:.12g}; CDF and inversion verified')
    return tests

if __name__=='__main__':
    n=sum(test_case(*v) for v in [(3,2,1),(5,3,1.5),(2,1.6,1),(1.5,1.2,1)])
    print(f'PASS {n} diagnostic assertions; numerical checks do not establish novelty or the continuum proof')
