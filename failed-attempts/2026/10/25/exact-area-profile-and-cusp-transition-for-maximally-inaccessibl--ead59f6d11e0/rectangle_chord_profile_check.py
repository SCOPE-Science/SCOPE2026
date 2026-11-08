"""Reproducibility checks for maximal shortest-chord regions of rectangles.

Requires NumPy and SciPy; the proof is analytical, not computational.
"""
import math
import numpy as np
from scipy.integrate import quad

Q = 2.0/3.0
T = 2.0**(-1.0/3.0)
A = (1.0 - T*T)**1.5
THETA = math.asin(T)

def primitive(theta):
    return (3*theta/16 - 3*math.sin(2*theta)/64
            - 3*math.sin(4*theta)/64 + math.sin(6*theta)/64)

def bow(x):
    return max(0.0, 1.0 - x**Q)**1.5

def exact_area(h):
    assert h >= 1
    if h < 2:
        angle = math.acos((h/2)**(1/3))
        return h - 2*A - 4*(primitive(THETA)-primitive(angle))
    return h - 2*A - 4*primitive(THETA)

def quadrature_area(h):
    t = min(h/2, 1.)
    return 4*quad(lambda x: .5-bow(x), A, t, epsabs=1e-12)[0] + max(0., h-2)

def exact_region(x,y,h):
    return min((xx**Q+yy**Q for xx in (x,h-x) for yy in (y,1-y))) >= 1

def sampled_min_chord(x,y,h,angles):
    u,v = np.cos(angles), np.sin(angles)
    # lengths from p along positive and negative directions to the rectangle boundary.
    txf = np.where(u>0, (h-x)/np.maximum(u,1e-30), x/np.maximum(-u,1e-30))
    tyf = np.where(v>0, (1-y)/np.maximum(v,1e-30), y/np.maximum(-v,1e-30))
    txb = np.where(u>0, x/np.maximum(u,1e-30), (h-x)/np.maximum(-u,1e-30))
    tyb = np.where(v>0, y/np.maximum(v,1e-30), (1-y)/np.maximum(-v,1e-30))
    return float((np.minimum(txf,tyf)+np.minimum(txb,tyb)).min())

def main():
    rng=np.random.default_rng(32711)
    angles=np.arange(16384)*(math.pi/16384)
    for h in [1.,1.01,1.25,1.5,1.8,1.99,2.,2.1,3.,5.]:
        formula=exact_area(h)
        integ=quadrature_area(h)
        assert abs(formula-integ)<3e-10, (h,formula,integ)
        X=rng.random((120000,2))*[h,1.]
        is_in=np.ones(len(X),dtype=bool)
        for x in (X[:,0],h-X[:,0]):
            for y in (X[:,1],1-X[:,1]):
                is_in &= x**Q+y**Q>=1
        freq=is_in.mean()
        std=math.sqrt(max(freq*(1-freq),1e-10)/len(X))
        assert abs(freq-formula/h)<6*std+1e-3, (h,freq,formula/h)
        print('h=',h,'area=',round(formula,12),'fraction=',round(formula/h,12), 'MC=',round(freq,5))
    nchecked=0
    for h in [1.,1.5,2.,3.]:
        pts=rng.random((36,2))*[h,1]
        for x,y in pts:
            low=sampled_min_chord(x,y,h,angles)
            good=exact_region(x,y,h)
            # A sampled minimum cannot certify greater-than-one for nearly critical points.
            if abs(low-1)>.003:
                assert (low>1)==good, (h,x,y,low,good)
                nchecked+=1
    print('passed sampled chord consistency on',nchecked,'noncritical points')
    C=2*A+4*primitive(THETA)
    print('constant=',C,'square_area=',exact_area(1.))
    for eps in [.1,.03,.01]:
        ratio=(exact_area(2-eps)-(2-eps-C))/eps**2.5
        print('transition coeff at',eps,'=',ratio)
    print('leading coefficient',4/(15*math.sqrt(3)))

if __name__=='__main__':
    main()
