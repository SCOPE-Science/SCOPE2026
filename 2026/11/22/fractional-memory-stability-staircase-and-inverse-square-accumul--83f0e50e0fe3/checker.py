#!/usr/bin/env python3
"""Reproduce algebraic identities and diagnostic stability counts for a sine-cubic fractional map.
Only standard Python libraries are needed; this script is finite diagnostics, not the proof."""
import math
import cmath

PI=math.pi

def d_boundary(alpha, D):
    assert 0 < alpha <= 1 and D > .25
    theta=math.acos(-1/(2*math.sqrt(D)))
    return math.sqrt(D)-(2*math.cos((theta-PI)/(2-alpha)))**alpha

def critical(alpha):
    assert 0 < alpha <= 1
    lo=.2500000001; hi=8.0
    assert d_boundary(alpha,lo)<0<d_boundary(alpha,hi)
    for i in range(130):
        mid=(lo+hi)/2
        if d_boundary(alpha,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def stable_scalar(alpha,mu):
    if mu == 0: return False
    ang=abs(cmath.phase(mu))
    if ang<=alpha*PI/2: return False
    return abs(mu)<(2*math.cos((ang-PI)/(2-alpha)))**alpha

def eigenvalues(D):
    disc=cmath.sqrt(1-4*D)
    return ((-1+disc)/2, (-1-disc)/2)

def exact_count(alpha,c):
    h=math.sqrt(c-1)
    delta=math.atan(h)/PI
    x=critical(alpha)/(2*PI*h)-delta
    return 2*max(0,math.ceil(x))

def positive_fixed_point(c,m,sgn=1):
    h=math.sqrt(c-1)
    r=h/math.sqrt(c)
    delta=math.atan(h)/PI
    return sgn*r, sgn*((-1)**m)*(m+delta)

def test():
    for a in (.05,.25,.5,.75,.95,1.0):
        dc=critical(a)
        assert abs(d_boundary(a,dc))<3e-14
        if a<1: assert dc>1
        else: assert abs(dc-1)<1e-12
        for D in (.005,.1,.249, .26, .5, .999, 1.001, dc*.999, dc*1.001,2.0,5.0):
            spectrum_all=all(stable_scalar(a,z) for z in eigenvalues(D))
            assert spectrum_all == (D<dc), (a,D,dc)
        for c in (1.0001,1.01,1.05,1.2,1.7,2.25):
            h=math.sqrt(c-1); delta=math.atan(h)/PI
            t=dc/(2*PI*h)
            brute=0
            for m in range(int(math.ceil(t))+3):
                for sgn in (-1,1):
                    x,y=positive_fixed_point(c,m,sgn)
                    # Fixed point identities of the nonfractional vector field.
                    assert abs(math.sin(PI*y)-x)<2e-12
                    assert abs(c*(1-x*x)*y-y)<3e-12
                    # Linearized Caputo field has trace -1, determinant below.
                    b=PI*math.cos(PI*y); d=-2*c*x*y
                    det=-b*d
                    expected=2*PI*h*(m+delta)
                    assert abs(det-expected)<1e-10*max(1,expected)
                    if all(stable_scalar(a,z) for z in eigenvalues(det)):
                        brute+=1
            assert brute==exact_count(a,c),(a,c,brute,exact_count(a,c))
    # At c=1, every (0,k) with k integer is stationary; Jacobian has a zero eigenvalue.
    for k in range(-25,26):
        assert abs(math.sin(PI*k))<2e-14
    # Fractional-order 1/2 keeps a spectrally stable pair past the order-1 endpoint.
    c=1.7
    assert exact_count(1,c)==0 and exact_count(.5,c)==2
    assert abs(critical(.5)-1.44762298685488)<2e-12
    # The inverse-square transition law follows from the defining scalar equation.
    a=.5; D=critical(a)
    for m in (100,1000,10000):
        lo=0.0; hi=D/(2*PI*m)
        for _ in range(100):
            h=(lo+hi)/2
            val=2*PI*h*m+2*h*math.atan(h)
            if val>D: hi=h
            else: lo=h
        h=(lo+hi)/2
        scaled=h*h*m*m
        target=D*D/(4*PI*PI)
        assert abs(scaled-target)<.0015/m
    print('PASS: exact fixed-point identities, Caputo spectral classification, counts, critical order effect, threshold scaling')
    print('D_0.5 = %.15f; D_1 = %.15f'%(critical(.5),critical(1)))
    print('Counts at c=1.01: alpha=0.5 -> %d, alpha=1 -> %d'%(exact_count(.5,1.01),exact_count(1,1.01)))

if __name__=='__main__': test()
