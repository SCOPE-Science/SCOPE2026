"""Standalone numerical checks for a flat rectangular pillowcase's geodesic-distance law.
Requires Python 3 and NumPy. Research computations are independent of any external ledger.
"""
import math
import numpy as np

def torus_cdf(r, a, b):
    A, B = sorted((a / 2., b / 2.), reverse=True)
    if r <= 0: return 0.
    if r <= B:
        J = math.pi*r*r/4.
    elif r <= A:
        J = (B*math.sqrt(max(r*r-B*B, 0.)) + r*r*math.asin(B/r))/2.
    elif r < math.hypot(A,B):
        J = (A*math.sqrt(max(r*r-A*A,0.)) + B*math.sqrt(max(r*r-B*B,0.))
              +r*r*(math.asin(A/r)+math.asin(B/r)-math.pi/2))/2.
    else: J=A*B
    return max(0., min(1., J/(A*B)))

def pillow_cdf(r,a,b):
    f=torus_cdf(r,a,b)
    return 1-(1-f)**2

def main():
    rng=np.random.default_rng(72659)
    trials=450_000
    for a,b in [(1.,1.),(math.sqrt(2),1/math.sqrt(2)),(2.,.5),(.7,1.7)]:
        X=rng.random((trials,2))*np.array([a,b])
        Y=rng.random((trials,2))*np.array([a,b])
        z=np.abs(X-Y)
        w=np.mod(X+Y,np.array([a,b]))
        z=np.minimum(z,np.array([a,b])-z)
        w=np.minimum(w,np.array([a,b])-w)
        d=np.minimum(np.linalg.norm(z,axis=1),np.linalg.norm(w,axis=1))
        radii=np.linspace(.1*min(a,b),.98*math.hypot(a,b)/2,9)
        for r in radii:
            pred=pillow_cdf(r,a,b)
            actual=np.mean(d<=r)
            sigma=math.sqrt(max(pred*(1-pred),.0001)/trials)
            assert abs(pred-actual)<5.5*sigma+.0015, (a,b,r,actual,pred)
        print('CDF_SAMPLE_OK',a,b,9)
    for ab in [.3,1.,7.]:
        side=math.sqrt(ab)
        for ratio in [1.1,1.4,2.,5.,20.]:
            a=side*math.sqrt(ratio); b=side/math.sqrt(ratio)
            for r in np.linspace(0,math.hypot(a,b)/2,300):
                assert pillow_cdf(r,side,side)+3e-14>=pillow_cdf(r,a,b)
            print('STOCHASTIC_SQUARE_OK',ab,ratio)
    for a,b in [(1.,1.),(2.,.5),(1.7,.7)]:
        R=math.hypot(a,b)/2
        coef=(2*(a*a+b*b)/(a*a*b*b))**2
        for eps in [1e-2, 3e-3,1e-3]:
            surv=1-pillow_cdf(R-eps,a,b)
            err=abs(surv/eps**4/coef-1)
            assert err<.13, (a,b,eps,surv,coef,err)
        print('QUARTIC_UPPER_TAIL_OK',a,b,coef)
    print('PILLOWCASE_GEODESIC_LAW_OK')
if __name__=='__main__': main()
