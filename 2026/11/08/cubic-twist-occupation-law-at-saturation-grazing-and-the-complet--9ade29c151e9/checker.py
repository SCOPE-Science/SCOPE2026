#!/usr/bin/env python3
"""Standalone numerical and algebraic sanity checks for an unforced saturated oscillator.
The proof of the infinite statements is in RESULT.md; numerical checks are not proofs.
"""
import math

def period(m,E):
    w=math.sqrt(m*m+1.0)
    ec=w*w/2.0
    if E<=ec:
        return 2*math.pi/w
    s=math.sqrt(2*(E-ec))
    return 4*(math.atan(w/s)/w+math.atan(m*s/(w*w))/m)

def occupation(m,E):
    w=math.sqrt(m*m+1.0)
    ec=w*w/2.0
    if E<=ec: return 0.0
    s=math.sqrt(2*(E-ec))
    tin=math.atan(w/s)/w
    tout=math.atan(m*s/(w*w))/m
    return tout/(tin+tout)

def flow(m,E,h=0.000025):
    # Independent initial-value integration in original physical time, using RK4.
    x,y,t=0.0,math.sqrt(2*E),0.0
    first_cross=None
    def accel(z):return -m*m*z-max(-1.0,min(1.0,z))
    for k in range(150000):
        a1=y; b1=accel(x)
        a2=y+h*b1/2; b2=accel(x+h*a1/2)
        a3=y+h*b2/2; b3=accel(x+h*a2/2)
        a4=y+h*b3; b4=accel(x+h*a3)
        xx=x+h*(a1+2*a2+2*a3+a4)/6
        yy=y+h*(b1+2*b2+2*b3+b4)/6
        if first_cross is None and x<=1<xx:
            first_cross=t+h*(1-x)/(xx-x)
        if yy<=0:
            peak=t+h*y/(y-yy)
            outside=0.0 if first_cross is None else (peak-first_cross)/peak
            return 4*peak,outside
        x,y,t=xx,yy,t+h
    raise AssertionError("peak not reached")

def run():
    count=0
    for m in [1,2,5,9]:
        w=math.sqrt(m*m+1); ec=w*w/2
        for delta in [0.001,0.04,0.8,20.0]:
            e=ec+delta
            p=period(m,e); occ=occupation(m,e)
            observed_p, observed_occ=flow(m,e)
            assert abs(observed_p-p)<2e-5,(m,delta,observed_p,p)
            assert abs(observed_occ-occ)<2e-5,(m,delta,observed_occ,occ)
            assert 2*math.pi/w<p<2*math.pi/m
            assert 0<occ<1
            count+=1
        assert period(m,ec)==2*math.pi/w
        assert period(m,ec*0.5)==2*math.pi/w
        assert period(m,ec+1e-3)<period(m,ec+.05)<period(m,ec+20)
        # Threshold exponents and constants by a stable sequence of small deltas.
        for delta in [1e-3,1e-4,1e-5]:
            s=math.sqrt(2*delta)
            # Use small-s directly to avoid subtractive cancellation of arctan(w/s).
            # arctan(w/s) = pi/2-arctan(s/w).
            dt=4*(-math.atan(s/w)/w+math.atan(m*s/(w*w))/m)
            cubic=4*s**3/(3*w**6)
            assert abs(dt/cubic-1)<0.004
            theta=occupation(m,ec+delta)
            assert abs(theta/(2*s/(math.pi*w))-1)<0.025
        for s in [1000.,2000.]:
            d=2*math.pi/m-period(m,ec+s*s/2)
            assert abs(d*s/(4/(m*m))-1)<0.0001
    print("PASS: ",count,"original-flow quarter-period and occupation comparisons, plus core, threshold, far-energy and strict-monotonicity checks")
if __name__=='__main__':run()
