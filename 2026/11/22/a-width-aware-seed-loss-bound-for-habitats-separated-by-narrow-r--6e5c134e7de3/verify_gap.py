#!/usr/bin/env python3
"""Numerical checks of rectangular slit seed-loss identities.
Only mathematical inputs and tests; no external data.
"""
from math import erf, exp, sqrt, pi, erfc
import random
from scipy.integrate import quad

SQRT2PI=sqrt(2*pi)
alpha=sqrt(2/pi)

def phi(z): return exp(-z*z/2)/SQRT2PI

def Phi(z): return (1+erf(z/sqrt(2)))/2

def primitive(t,s):
    return t*Phi(t/s)+s*phi(t/s)

def block(a,b,c,d,s):
    return (primitive(d-a,s)-primitive(d-b,s)
          - primitive(c-a,s)+primitive(c-b,s))

def gaussian_exact(L,H,roads,s):
    endpoints=[0.0]
    for a,w in roads:
        endpoints.extend([a,a+w])
    endpoints.append(L)
    intervals=[(endpoints[2*i],endpoints[2*i+1]) for i in range(len(endpoints)//2)]
    W=sum(b-a for a,b in intervals)
    # Numeric cancellation at very small s: only test s>=0.008.
    kx=sum(block(a,b,c,d,s) for a,b in intervals for c,d in intervals)
    ky=block(0,H,0,H,s)
    return 1-(kx/W)*(ky/H)

def psi(lam):
    return alpha*(-__import__('math').expm1(-lam*lam/2)) + lam*erfc(lam/sqrt(2))

def improved(L,H,roads,s):
    W=L-sum(w for _,w in roads)
    return s*alpha*(1/W+1/H)+s*sum(psi(w/s) for _,w in roads)/W

def perimeter(L,H,roads,s):
    m=len(roads); W=L-sum(w for _,w in roads)
    return s*alpha*( (m+1)/W+1/H)

def asymptotic(L,H,lams,s):
    return s*(alpha*(1/L+1/H)+sum(psi(x) for x in lams)/L)

def check():
    random.seed(44)
    for m in [1,2,3]:
      for j in range(200):
        L=1.; H=random.uniform(.8,4.)
        s=random.uniform(.008,.065)
        road_locations=[(i+1)*L/(m+1) for i in range(m)]
        widths=[random.uniform(0,.5)*s for _ in range(m)]
        roads=list(zip(road_locations,widths))
        val=gaussian_exact(L,H,roads,s)
        up=improved(L,H,roads,s)
        old=perimeter(L,H,roads,s)
        if not (0<=val<=up+2e-12 and up<=old+2e-12):
          raise AssertionError((m,j,L,H,s,roads,val,up,old))
    print('600 finite-width Gaussian cases: exact <= road-aware bound <= perimeter bound: PASS')
    for lams in [[.25],[.1,.5],[.2,1.1,.8]]:
      m=len(lams)
      for s in [.01,.005,.0025]:
        roads=[((i+1)/(m+1),s*lam) for i,lam in enumerate(lams)]
        exact=gaussian_exact(1.,4.,roads,s)
        approx=asymptotic(1.,4.,lams,s)
        if abs(exact-approx)>20*s*s: raise AssertionError((lams,s,exact,approx))
    print('9 small-width asymptotic second-order tests: PASS')
    L,H,s,lam=1.,4.,.02,.25
    road=[(.5,s*lam)]
    v=gaussian_exact(L,H,road,s)
    b=improved(L,H,road,s)
    old=perimeter(L,H,road,s)
    print('Example L=1, H=4, Gaussian sd=.02, gap=.005')
    print('exact',format(v,'.12f'),'new upper bound',format(b,'.12f'),'old upper bound',format(old,'.12f'))
    print('bound improvement',format(100*(old-b)/old,'.6f'),'%')
    for z in [0,.1,.25,1,3,10]:
      lhs=quad(lambda x: 2*x*phi(x),0,z,epsabs=1e-13)[0]+2*z*quad(phi,z,12,epsabs=1e-13)[0]
      assert abs(lhs-psi(z))<2e-12,(z,lhs,psi(z))
    print('Gaussian crossover integral at six widths: PASS')

if __name__=='__main__': check()

def radial_mean_bound(L,H,roads,mean_r):
    W=L-sum(w for _,w in roads)
    def F(r,w):
        if w<=0: return 0.0
        if w>=r: return 2*r/pi
        s=w/r
        return (2/pi)*(w*__import__('math').acos(s)+r*(1-sqrt(1-s*s)))
    return (2*mean_r/pi)*(1/W+1/H)+sum(F(mean_r,w) for _,w in roads)/W

def test_radial_bound():
    # Conventional Gaussian: actual displacement radius is Rayleigh with mean sigma*sqrt(pi/2).
    random.seed(2044)
    for m in [1,2,3]:
      for _ in range(200):
        L=1.; H=1.7
        s=random.uniform(.005,.09)
        roads=[((i+1)/(m+1),s*random.uniform(0,1.7)) for i in range(m)]
        exact=gaussian_exact(L,H,roads,s)
        exact_kern=improved(L,H,roads,s)
        meanonly=radial_mean_bound(L,H,roads,s*sqrt(pi/2))
        old=perimeter(L,H,roads,s)
        assert exact<=exact_kern+3e-12<=meanonly+3e-12<=old+4e-12,(exact,exact_kern,meanonly,old)
    print('600 Gaussian instances: exact <= kernel-aware <= sharp mean-only <= perimeter: PASS')
    L,H,s=1,4,.02
    roads=[(.5,.005)]
    print('mean-only example bound', format(radial_mean_bound(L,H,roads,s*sqrt(pi/2)),'.12f'))
    # Test Jensen for two-point radial distributions by numerical angular integration
    from scipy.integrate import quad
    for _ in range(100):
      r1=random.uniform(.01,2.0);r2=random.uniform(.01,2.0)
      t=random.uniform(0,1); w=random.uniform(0,2)
      f=lambda r: (2/pi)*quad(lambda theta:min(r*__import__('math').cos(theta),w),0,pi/2,epsabs=1e-9,points=[__import__('math').acos(w/r)] if 0<w<r else None)[0]
      assert t*f(r1)+(1-t)*f(r2)<=f(t*r1+(1-t)*r2)+2e-10
    print('100 radial-mixture Jensen comparisons: PASS')

if __name__=='__main__':test_radial_bound()

def F_uniform_radius(r,w):
    from math import acos
    if w <= 0: return 0.
    if w>=r: return 2*r/pi
    a=w/r
    return (2/pi)*(w*acos(a)+r*(1-sqrt(1-a*a)))

def fixed_radius_exact(L,H,roads,r):
    W=L-sum(w for _,w in roads)
    theta=[min(w/r,1) for _,w in roads]
    correction=(r*r/(pi*W*H))*(1+sum(2*t-t*t for t in theta))
    upper=((2/pi)*r+sum(F_uniform_radius(r,w) for _,w in roads))/W+(2/pi)*r/H
    return upper-correction,upper,correction

def one_dim_outflow(intervals,u):
    W=sum(b-a for a,b in intervals)
    cross=sum(max(0,min(b+u,d)-max(a+u,c))
              for a,b in intervals for c,d in intervals)
    return W-cross

def integrate_angle_exact(L,H,roads,r):
    stops=[0.]
    for a,w in roads:stops.extend([a,a+w])
    stops.append(L)
    intervals=list(zip(stops[0::2],stops[1::2]))
    W=L-sum(w for _,w in roads)
    def conditional(theta):
        from math import cos,sin
        ux=r*cos(theta);uy=r*sin(theta)
        lx=one_dim_outflow(intervals,ux)
        ly=min(abs(uy),H)
        return lx/W+ly/H-lx*ly/(W*H)
    # Integral quadrants + gap kinks, precision 1e-8.
    return sum(quad(conditional,k*pi/2,(k+1)*pi/2,epsabs=1e-9,limit=80)[0] for k in range(4))/(2*pi)

def test_fixed_radius():
    for m in [1,2,3]:
      for lam in [.05,.3,1.2]:
        L,H,r=1.,2.,.02
        roads=[((i+1)/(m+1),r*lam) for i in range(m)]
        actual=integrate_angle_exact(L,H,roads,r)
        predicted,upper,correction=fixed_radius_exact(L,H,roads,r)
        assert abs(actual-predicted)<1e-10,(actual,predicted,m,lam)
        assert abs(upper-actual-correction)<1e-10
    print('9 direct angular integrations vs exact radius/road second-order formula: PASS')
    L,H,r=1.,4.,.02
    roads=[(.5,.005)]
    actual,upper,correction=fixed_radius_exact(L,H,roads,r)
    print('Fixed-distance example: exact', format(actual,'.12f'),'bound',format(upper,'.12f'),'gap',format(correction,'.12f'))

if __name__=='__main__':test_fixed_radius()
