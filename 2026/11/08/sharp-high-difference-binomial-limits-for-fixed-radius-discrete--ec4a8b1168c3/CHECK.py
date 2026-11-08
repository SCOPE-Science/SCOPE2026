#!/usr/bin/env python3
"""Reproducible finite checks for the sharp high-difference smoothing laws."""
import math
import numpy as np
from scipy.optimize import brentq, linprog
from scipy.special import lambertw


def q2_data():
    d = brentq(lambda v: math.exp(v) * (v - 2) - v - 2, 2.01, 3.0, xtol=2e-14)
    t = brentq(lambda x: x*x+(d-2)*x+2-d-(d+2)*math.exp(-x-d), .1, 1.5, xtol=2e-14)
    a = 2 - 2*t - d
    b = t*t + (d-2)*t + 2-d
    return d,t,a,b


def signed_finite(K):
    zs = np.linspace(0, min(K, 24), 5001)
    w = np.maximum(0,1-zs/K)**K
    h1, h0 = zs-zs*zs/K, 1-zs*zs/(K*K)
    z2 = zs*zs
    A = np.vstack((np.column_stack((w*h1,w*h0,-np.ones_like(zs))),
                   np.column_stack((-w*h1,-w*h0,-np.ones_like(zs)))))
    rhs = np.r_[-w*z2,w*z2]
    r=linprog([0,0,1], A_ub=A, b_ub=rhs, bounds=[(None,None),(None,None),(0,None)], method='highs')
    assert r.success,r.message
    b,c,upper=r.x
    aa=1-b/K-c/(K*K)
    # Exact extrema of (1-z/K)^K Q(z): derivative is quadratic.
    # (K-z)Q'(z)-KQ(z) = 0
    coeff=[-(K+2)*aa, (2*K*aa-(K+1)*b), K*b-K*c]
    roots=np.roots(coeff)
    tests=[0.,float(K)]
    tests.extend(float(x.real) for x in roots if abs(x.imag)<1e-8 and 0<=x.real<=K)
    exact=max((max(0,1-z/K)**K)*abs(aa*z*z+b*z+c) for z in tests)
    assert abs(exact-upper)<3e-4,(K,exact,upper)
    return exact,aa,b,c


def main():
    d,t,a,b = q2_data()
    assert 2<d<3 and 0<t<t+d
    assert abs(math.exp(d)*(d-2)-(d+2))<1e-12
    q=lambda z: z*z+a*z+b
    assert abs(q(t)-(2-d))<1e-12
    assert abs(q(t+d)-(2+d))<1e-12
    assert abs(q(t)-(2*t+a))<1e-12 # critical-point identity
    for z in [t,t+d]:
        assert abs((2*z+a)-q(z))<1e-12
    assert abs(b+math.exp(-t)*q(t))<1e-12
    assert abs(b-math.exp(-t-d)*q(t+d))<1e-12
    x=np.linspace(0,40,20001)
    vals=np.exp(-x)*abs(x*x+a*x+b)
    assert vals.max() < b+1e-9
    assert b==max(b, math.exp(-t)*abs(q(t)),math.exp(-t-d)*q(t+d)) or abs(b-math.exp(-t)*abs(q(t)))<1e-13
    s=2*lambertw(math.exp(-1)).real
    bp=s*s
    assert abs(bp-4*math.exp(-s-2))<2e-14
    vals2=np.exp(-x)*(x-s)**2
    assert vals2.max() < bp+1e-9
    assert abs(b-0.21691547125616747)<3e-14
    assert abs(bp-0.3101700063005356)<3e-14
    # High-order finite-radius minimax values approach the proven limit.
    vals=[]
    for K in (8,16,32,64,128):
        v,aa,bb,cc=signed_finite(K)
        vals.append(v)
        assert 0<v<b+.003,(K,v)
        # Polynomial coefficients correspond exactly to an even 5-tap Fourier kernel.
        yy=np.array([0.,.5,1.])
        rr=np.array([(aa*(K*(1-y))**2+bb*K*(1-y)+cc)/(K*K) for y in yy])
        assert abs(rr[0]-1.)<2e-12
        u0=(rr[0]+rr[2]+2*rr[1])/4
        u1=(rr[0]-rr[2])/4
        u2=(rr[0]+rr[2]-2*rr[1])/8
        assert abs(u0+2*u1+2*u2-1)<2e-12
        theta=np.linspace(-math.pi,math.pi,10001)
        symbol=u0+2*u1*np.cos(theta)+2*u2*np.cos(2*theta)
        y=(1-np.cos(theta))/2
        assert np.max(np.abs(symbol-(aa*(K*(1-y))**2+bb*K*(1-y)+cc)/(K*K)))<1e-10
        opnorm=(2**(2*K))*np.max((y**K)*abs(symbol))
        assert abs(opnorm/(2**(2*K))*K*K-v)<3e-4
    assert all(vals[i]<vals[i+1] for i in range(len(vals)-1)),vals
    assert abs(vals[-1]-b)<.0021,vals
    print('HIGH_DIFFERENCE_CHECKS_PASSED',len(x)*2+5*10001)
    print('radius_two_signed',format(b,'.16g'),'positive',format(bp,'.16g'))
    print('finite_K_scaled_values',[(k,round(v,10)) for k,v in zip((8,16,32,64,128),vals)])

if __name__=='__main__':
    main()
