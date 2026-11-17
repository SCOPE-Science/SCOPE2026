"""Reproducible diagnostics for the checkerboard two-radius covering theorem.
Requires Python 3, NumPy and SciPy. Sampling grids are not infinite proofs.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar

def f(s):
    if s < 0 or s > 1: raise ValueError(s)
    if s <= 1/math.sqrt(2):
        return math.sqrt(1-math.sqrt(2)*s+s*s)
    return (1-math.sqrt(2*s*s-1))/math.sqrt(2)

def cost(w,s): return f(s)**2+w*s*s

def optimized(w):
    c=1+w
    s1=1/(math.sqrt(2)*c)
    s2=math.sqrt((1+c**-2)/2)
    E1=1-1/(2*c)
    E2=(c-c**-1)/2
    return (s1,s2,E1,E2)

def check():
    xx=np.linspace(0,1,700)
    X,Y=np.meshgrid(xx,xx,indexing='ij')
    da=np.minimum(np.hypot(X,Y),np.hypot(1-X,1-Y))
    db=np.minimum(np.hypot(X-1,Y),np.hypot(X,1-Y))
    for s in (0,.15,.3,.5,.7071067811865476,.8,.93,.999):
        r=f(s)
        assert not np.any((da>r+1e-9)&(db>s+1e-9)), ('uncovered',s,r)
        if .01<s<.99 and abs(s-1/math.sqrt(2))>1e-4:
            assert np.any((da>r-0.008)&(db>s+1e-4)), ('unexpected slack',s,r)
    print('CHECKERBOARD_FEASIBILITY_GRID_OK')
    for w in (.05,.4,.9,1.,1.2,3.,50.):
        s1,s2,E1,E2=optimized(w)
        assert abs(cost(w,s1)-E1)<1e-12
        assert abs(cost(w,s2)-E2)<1e-12
        # no grid interpolation near cusp; independently minimize each interval
        a=1/math.sqrt(2)
        m1=minimize_scalar(lambda t:cost(w,t),bounds=(0,a),method='bounded',options={'xatol':1e-13})
        m2=minimize_scalar(lambda t:cost(w,t),bounds=(a,1),method='bounded',options={'xatol':1e-13})
        assert abs(min(m1.fun,m2.fun)-min(E1,E2))<1e-8
        print('weight',w,'s1/s2',s1,s2,'cost1/2',E1,E2)
    assert abs(optimized(1)[2]-optimized(1)[3])<1e-14
    print('CHECKERBOARD_WEIGHTED_TRANSITION_OK')
if __name__=='__main__': check()
