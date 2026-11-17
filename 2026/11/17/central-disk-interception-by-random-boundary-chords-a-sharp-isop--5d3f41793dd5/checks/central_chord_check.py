"""Numerical diagnostics for the sharp central-chord intensity theorem."""
import numpy as np
from scipy.integrate import quad
from math import sqrt,pi,log

def analytic_square():
    integral=4*quad(lambda th: 1/np.cos(th)**3,-pi/4,pi/4,epsabs=1e-12)[0]
    return 4*integral/8**2

def independent_opposite_side_derivative():
    # For endpoints (1,y1) and (-1,y2), use u=(y1+y2)/2,
    # v=(y2-y1)/2. Their density is 1/2 on |u|+|v| <= 1.
    # The center distance is |u|/sqrt(1+v*v), so the conditional
    # derivative of interception probability is int sqrt(1+v*v) dv.
    # The chance of an opposite-side pair of either orientation is 1/4.
    ans=quad(lambda v:sqrt(1+v*v),-1,1,epsabs=1e-12)[0]/4
    assert abs(ans-analytic_square())<1e-12
    print("INDEPENDENT_SQUARE_OPPOSITE_SIDES_OK",ans)

def simulate_square(n=3500000, seed=1126051):
    rng=np.random.default_rng(seed)
    sides=rng.integers(0,4,size=(n,2))
    pos=rng.uniform(-1,1,size=(n,2))
    # side index bottom,right,top,left
    xa=np.where(sides[:,0]==1,1,np.where(sides[:,0]==3,-1,pos[:,0]))
    ya=np.where(sides[:,0]==0,-1,np.where(sides[:,0]==2,1,pos[:,0]))
    xb=np.where(sides[:,1]==1,1,np.where(sides[:,1]==3,-1,pos[:,1]))
    yb=np.where(sides[:,1]==0,-1,np.where(sides[:,1]==2,1,pos[:,1]))
    dx=xb-xa;dy=yb-ya
    denom=dx**2+dy**2
    u=np.clip(-(xa*dx+ya*dy)/(denom+1e-300),0,1)
    d=np.hypot(xa+u*dx,ya+u*dy)
    for e in [.04,.02,.01,.005]:
        obs=(d<e).mean(); pred=analytic_square()*e
        print('square eps=',e,'observed=',obs,'ratio=',obs/pred,'count=',(d<e).sum())
    assert abs(analytic_square()-(sqrt(2)+log(1+sqrt(2)))/4)<1e-12

def radial_energy(eta):
    # r = 1+eta cos(2 theta), smooth positive and convex when eta small
    r=lambda t:1+eta*np.cos(2*t)
    dr=lambda t:-2*eta*np.sin(2*t)
    P=quad(lambda t:np.hypot(r(t),dr(t)),0,2*pi,epsabs=1e-11)[0]
    E=quad(lambda t:dr(t)**2/r(t),0,2*pi,epsabs=1e-11)[0]
    k=4/P**2*quad(lambda t:r(t)+dr(t)**2/r(t),0,2*pi,epsabs=1e-11)[0]
    assert k+1e-13 >=4/P+2*E/P**2
    print('radial eta=',eta,'P=',P,'intensity=',k,'bound=',4/P,'stability ratio=',(k-4/P)/(2*E/P**2))
    return k

if __name__=='__main__':
    print('square coefficient:',analytic_square(),'circle equal perimeter:',.5)
    independent_opposite_side_derivative()
    for eta in [.001,.03,.1]:radial_energy(eta)
    simulate_square()
    print('CENTRAL_CHORD_INTENSITY_DIAGNOSTICS_OK')
