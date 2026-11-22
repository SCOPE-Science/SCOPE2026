"""Reproducible numerical diagnostics for invariant-line chords of a circular segment."""
import math
import numpy as np

def length(alpha,t,h):
    alpha,t=np.broadcast_arrays(np.asarray(alpha),np.asarray(t))
    u=np.sqrt(np.maximum(0.,1-t*t))
    sn=np.abs(np.sin(alpha)); cs=np.cos(alpha)
    q=np.divide(h-t*cs,sn,out=np.full_like(u,np.inf),where=sn>1e-15)
    value=np.where(sn>1e-15,np.maximum(0.,u-np.maximum(-u,q)),np.where(t>=h,2*u,0.))
    return np.where(abs(t)<=1,value,0.)

def quad(h,eps,n=1050):
    sc=math.sqrt(eps)
    if abs(h)<=2*sc:
        angles=np.linspace(-4*sc,4*sc,n)
        offsets=np.linspace(-6*sc,6*sc,n)
    elif h>0:
        angles=np.linspace(-3*eps/h,3*eps/h,n)
        offsets=h+np.linspace(-2*eps,3*eps/h,n)
    else:
        angles=np.linspace(-math.pi/2,math.pi/2,n)
        offsets=np.linspace(-2*sc,2*sc,n)
    aa,tt=np.meshgrid(angles,offsets,indexing='ij')
    D=2. if h<=0 else 2*math.sqrt(1-h*h)
    good=(length(aa,tt,h)>=D-eps).astype(float)
    area=np.trapezoid(np.trapezoid(good,offsets,axis=1),angles)
    return area/(2*math.acos(h)+2*math.sqrt(1-h*h))

def fixed_coeff(h):
    perimeter=2*math.acos(h)+2*math.sqrt(1-h*h)
    if h<0: return 4*math.asin(-h)/perimeter,0.5
    if h==0: return 1/perimeter,1.
    return math.sqrt(1-h*h)/(4*h*h*perimeter),2.

def phi(lam):
    if lam<=-1: return -4*lam
    if lam<=0: return (1-lam)**2
    return (math.sqrt(1+lam*lam)-lam)**2

def main():
    diagnostics=0
    for h,eps in [(-.5,.001),(-.1,.001),(0.,.001),(.2,.0003),(.5,.001)]:
        c,p=fixed_coeff(h)
        ratio=quad(h,eps)/(c*eps**p)
        assert abs(ratio-1)<0.09,(h,ratio)
        diagnostics+=1
    for lam in [-2.,-1.,-.5,0.,.5,2.]:
        eps=.0003;h=lam*math.sqrt(eps)
        ratio=quad(h,eps)/(eps*phi(lam)/(math.pi+2))
        assert abs(ratio-1)<0.11,(lam,ratio)
        diagnostics+=1
    # Boundary/normalization and a symmetry check.
    assert abs(phi(-1)-4)<1e-12
    assert abs(phi(0)-1)<1e-12
    assert np.allclose(length(.08,np.array([0.,.1,.2]),-.2),length(-.08,np.array([0.,.1,.2]),-.2))
    diagnostics+=3
    print('PASS:',diagnostics,'deterministic numerical diagnostics (finite evidence only)')
if __name__=='__main__':main()
