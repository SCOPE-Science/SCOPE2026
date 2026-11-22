#!/usr/bin/env python3
"""Independent finite checks for lacunary Zindler convexity formulas.
The all-degree theorem relies on the analytic proof, not finite sampling.
"""
import math
from fractions import Fraction

def parameter_admissible(beta, alpha):
    return beta >= 7 and beta % 2 == 1 and alpha > beta and beta*beta > alpha*(1+3*math.pi/2)

def critical_radius(beta, alpha, n):
    a = Fraction(alpha)
    return sum((Fraction(beta**(3*k)-beta**k,1)/a**k for k in range(1,n+1)),Fraction(0))

def hderivs(t,beta,alpha,n):
    h = hp = hpp = hppp = 0.0
    for k in range(1,n+1):
        w = beta**k
        a = alpha**(-k)
        st,ct=math.sin(w*t),math.cos(w*t)
        h += a*st
        hp += a*w*ct
        hpp -= a*w*w*st
        hppp -= a*w*w*w*ct
    return h,hp,hpp,hppp

def det_and_bound(t,beta,alpha,n,r):
    h,hp,hpp,hppp=hderivs(t,beta,alpha,n)
    H=h+hpp
    Hp=hp+hppp
    zpx=-r*math.cos(t)-H*math.sin(t)
    zpy=-r*math.sin(t)+H*math.cos(t)
    zppx=-H*math.cos(t)-(Hp-r)*math.sin(t)
    zppy=-H*math.sin(t)+(Hp-r)*math.cos(t)
    det=zpx*zppy-zpy*zppx
    return det, r*(r-Hp)+H*H, Hp, H

def tests():
    assertions=0
    for beta,alpha in [(7,8),(9,10),(11,13)]:
        assert parameter_admissible(beta,alpha)
        for n in (1,2,3):
            R=critical_radius(beta,alpha,n)
            coeffs=[Fraction(beta**(3*k)-beta**k,alpha**k) for k in range(1,n+1)]
            assert R==sum(coeffs)
            assert R>0
            if n>1: assert critical_radius(beta,alpha,n)>critical_radius(beta,alpha,n-1)
            assertions += 3
            # For t=(2j+1)pi/beta, every beta**k t is an odd multiple of pi.
            for j in range(beta):
                assert all((beta**(k-1)*(2*j+1))%2==1 for k in range(1,n+1))
                assertions += 1
            # Test the determinant formula independently from the derivative vectors.
            for r in (float(R)*0.9,float(R),float(R)*1.1):
                for j in range(250):
                    t=(j+.37)*2*math.pi/250
                    det,formula,Hp,H=det_and_bound(t,beta,alpha,n,r)
                    scale=max(1.,abs(det),abs(formula))
                    assert abs(det-formula)<2e-11*scale,(beta,alpha,n,r,t,det,formula)
                    assert float(R)-Hp >= -2e-9*max(1,float(R))
                    if r>float(R): assert det>0
                    assertions+=3
                # At aligned phases the determinant's exact value is r(r-R).
                exact=Fraction(9,10)*R if r<float(R) else (R if r==float(R) else Fraction(11,10)*R)
                assert exact*(exact-R) < 0 if exact<R else exact*(exact-R)>=0
                assertions+=1
    # Exact example from the motivating source: beta=7, alpha=8.
    assert critical_radius(7,8,1)==42
    assert critical_radius(7,8,2)==Fraction(3759,2)
    assertions+=2
    # Finite rational identity for asymptotic q^n leading coefficient.
    for beta,alpha in [(7,8),(9,10)]:
        q=Fraction(beta**3,alpha)
        s=Fraction(beta,alpha)
        for n in (1,3,8):
            R=critical_radius(beta,alpha,n)
            closed=q*(q**n-1)/(q-1)-s*(s**n-1)/(s-1)
            assert R==closed
            assertions+=1
    print(f"PASS: {assertions} exact-arithmetic and floating-point assertions")
    print("Infinite convexity and zero classifications are established by proof, not sampling")

if __name__=='__main__': tests()
