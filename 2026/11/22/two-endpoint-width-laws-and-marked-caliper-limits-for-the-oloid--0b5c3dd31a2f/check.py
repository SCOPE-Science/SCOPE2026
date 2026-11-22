"""Standalone numerical diagnostics for the oloid directional-width endpoint theorem.
Python 3; requires numpy and scipy. Run: python check.py
Numerical tests are evidence, not a substitute for the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

def directional_width(x,y,z):
    a=math.hypot(x,y)
    b=math.hypot(y,z)
    return max(a,y+b)+max(a,-y+b)

def reduced_width(theta,y):
    v=math.sqrt(max(0.0,1-y*y))
    x=v*math.cos(theta)
    z=v*math.sin(theta)
    return directional_width(x,y,z)

def lower_tail(eps):
    T=math.sqrt(2)+eps
    theta0=math.acos(T/2)
    theta1=math.asin(T/2)
    def ymax(theta):
        if reduced_width(theta,0)>T+2e-13: return 0.0
        return brentq(lambda y: reduced_width(theta,y)-T,0.0,0.5,
                      xtol=2e-14)
    area=quad(ymax,theta0,theta1,epsabs=1e-12,epsrel=1e-10,limit=200,points=[math.pi/4])[0]
    return 2*area/math.pi

def upper_tail(eps):
    def cap_area(phi):
        cp=math.cos(phi); sp=math.sin(phi)
        def deficit(s):
            return 3-math.sqrt(1-s*cp*cp)-math.sqrt(1-s*sp*sp)-math.sqrt(1-s)
        s=brentq(lambda s:deficit(s)-eps,0,2*eps,xtol=2e-14)
        return 1-math.sqrt(1-s)
    return quad(cap_area,0,2*math.pi,epsabs=1e-12,epsrel=1e-11,limit=200)[0]/(2*math.pi)

def main():
    rng=np.random.default_rng(947131)
    for _ in range(1000):
        v=rng.standard_normal(3);v/=np.linalg.norm(v)
        x,y,z=map(float,v)
        A=math.hypot(x,y);B=math.hypot(y,z)
        w=directional_width(x,y,z)
        assert abs(w-(A+B+max(abs(A-B),abs(y))))<1e-12
        assert math.sqrt(2)-1e-13<=w<=3+1e-13
    for k in range(4):
        theta=math.pi/4+k*math.pi/2
        assert abs(directional_width(math.cos(theta),0,math.sin(theta))-math.sqrt(2))<1e-12
    for y in [-1,1]:
        assert abs(directional_width(0,y,0)-3)<1e-12
    # Compare exact support values against sampled generators, independent of the closed formula.
    ang=np.linspace(0,2*math.pi,1440,endpoint=False)
    C1=np.stack([np.cos(ang),np.sin(ang),np.zeros_like(ang)],axis=1)
    C2=np.stack([np.zeros_like(ang),1+np.cos(ang),np.sin(ang)],axis=1)
    for _ in range(100):
        v=rng.standard_normal(3);v/=np.linalg.norm(v)
        hd=max(float((C1@v).max()),float((C2@v).max()))
        hm=max(float((C1@(-v)).max()),float((C2@(-v)).max()))
        w=directional_width(*map(float,v))
        assert 0<=w-(hd+hm)<3e-5
    k=2*math.sqrt(2)/math.pi
    lows=[]
    for eps in (0.05,0.025,0.0125,0.00625):
        p=lower_tail(eps)
        lows.append(p/eps**2)
        assert abs(p/eps**2-k)<0.06
    assert abs(lows[-1]-k)<abs(lows[0]-k)
    highs=[]
    for eps in (0.02,0.01,0.005):
        p=upper_tail(eps)
        c=(p-eps/2)/eps**2
        highs.append(c)
        assert abs(c-1/64)<0.00015
    assert abs(highs[-1]-1/64)<abs(highs[0]-1/64)
    print('support identity: 1000 random directions verified')
    print('generator support: 100 independent circle-sampling comparisons verified')
    print('lower tail P/epsilon^2:',lows,'target:',k)
    print('upper second-order coefficient:',highs,'target:',1/64)
    print('All diagnostic assertions passed')

if __name__=='__main__':
    main()
