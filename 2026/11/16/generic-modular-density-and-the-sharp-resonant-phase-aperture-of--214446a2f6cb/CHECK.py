#!/usr/bin/env python3
"""Finite reproducibility diagnostics for an exact phase-aperture theorem.
Analytical arguments, not these finite tests, establish the theorem.
"""
import math

def u_min(q,c):
    return (-(2*q-1)*c+math.sqrt((2*q-1)**2*c*c+4*q*(1-q)))/(2*(1-q))

def threshold(q,c):
    u=u_min(q,c)
    return math.hypot(1-u*c,u*math.sqrt(max(0.,1-c*c)))/(u**q)

def kappa_star(q):
    return q**(-q)*(1-q)**(q-1)

def check():
    n=0
    for q in [.15, math.sqrt(2)-1, .5, 1/math.sqrt(2), .83, .95]:
        K=kappa_star(q)
        values=[threshold(q,-1+2*j/256) for j in range(257)]
        assert abs(values[0]-K)<1e-11, (q,K,values[0])
        assert abs(values[-1])<1e-11
        assert all(values[i]>values[i+1]-1e-12 for i in range(256))
        for j in range(257):
            c=-1+2*j/256
            u=u_min(q,c)
            assert u>0
            assert abs((1-q)*u*u+(2*q-1)*c*u-q)<1e-10
            if j%32==0:
                for d in (.35,.8,1.2,2.5):
                    assert threshold(q,c)<=(math.hypot(1-d*c,d*math.sqrt(max(0,1-c*c)))/d**q)+1e-10
            n+=1
        for eps in [1e-3,1e-4,1e-5]:
            left,right=-1.0,1.0
            for _ in range(80):
                c=(left+right)/2
                if threshold(q,c)>K-eps: left=c
                else: right=c
            theta=math.acos((left+right)/2)
            predicted=math.sqrt(2*eps/(K*q*(1-q)))
            ratio=(math.pi-theta)/predicted
            assert abs(ratio-1)<.05,(q,eps,ratio)
    # Exact double-zero normalization at the resonant threshold:
    # U=-q/(1-q), V=1/(1-q), so U+V=1 and U+q V=0.
    from fractions import Fraction
    for q in [Fraction(1,3),Fraction(2,5),Fraction(3,4),Fraction(7,8)]:
        U=-q/(1-q); V=1/(1-q)
        assert U+V==1 and U+q*V==0
    print(f'CHECK_OK q_samples=6 stationary_grid={n} tangency_samples=4 asymptotic_sweeps=18')

if __name__=='__main__': check()
