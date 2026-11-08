#!/usr/bin/env python3
"""Exact algebra and finite numerical sanity checks for critical scalar epsilon-outside RMSProp."""
from fractions import Fraction
import math

def step(a, e, b, x, v):
    vp = b*v + (1-b)*a*a*x*x
    xp = x*(math.sqrt(vp)-e)/(math.sqrt(vp)+e)
    return xp,vp

def check_exact():
    # For rational epsilon and square-root memory w, the two formulae agree exactly.
    for a in (Fraction(1,2),Fraction(3,1),Fraction(7,5)):
        for e in (Fraction(1,10),Fraction(7,4)):
            for w in (Fraction(0),Fraction(1,3),Fraction(8,1)):
                for x in (Fraction(-9,7), Fraction(1,4)):
                    h=2*e/a
                    lhs=x-h*a*x/(w+e)
                    rhs=x*(w-e)/(w+e)
                    assert lhs==rhs
    # Construct exact finite-hit states with v_1 = epsilon^2.
    a=e=Fraction(1)
    b=Fraction(1,2)
    x=Fraction(1,2)
    v=(e*e-(1-b)*a*a*x*x)/b
    vp=b*v+(1-b)*a*a*x*x
    assert vp==e*e and x*(e-e)/(e+e)==0
    return 3*2*3*2

def check_numerical():
    # Choose nonresonant initial conditions avoiding extremely tiny transient values.
    scenarios=[
       (1.0,.1,.5,.03,0.0),
       (2.0,.3,.9,.02,0.0),
       (.3,1.0,.1,3.0,0.0),
       (4.0,.7,.99,.005,0.0),
       (1.5,2.0,.75,1.2,1.0),
    ]
    checked=0
    n=750000
    for a,e,b,x,v in scenarios:
        prev=abs(x)
        flips=0
        for k in range(n):
            nx,nv=step(a,e,b,x,v)
            assert nv>=0
            assert abs(nx)<=prev+1e-15
            if k>n-20000 and x*nx<0: flips+=1
            x,v=nx,nv
            prev=abs(x)
        assert flips>19000
        val=n*abs(x)
        vval=n*n*v
        target=e/(2*a)
        vt=e*e/4
        # finite-time effects may be large for some initial conditions; print all values
        print("CASE",a,e,b,"n_abs_x",val,"expected",target,"n2_v",vval,"expected",vt)
        assert abs(val/target-1)<.07,(a,e,b,val,target)
        assert abs(vval/vt-1)<.14,(a,e,b,vval,vt)
        checked+=1
    return checked

if __name__=="__main__":
    print("EXACT_IDENTITIES",check_exact())
    print("NUMERICAL_SCENARIOS",check_numerical())
    print("VERIFY_OK finite_checks_only_analytic_proof_required")
