"""Independent finite-parameter consistency checks for strong OU return."""
import numpy as np
from scipy.integrate import quad, cumulative_trapezoid
from scipy.special import erfcx, dawsn

def h(x,D=1.,L=1.,r=1.):
    a=np.sqrt(r/D)
    return r/(2*np.sqrt(D*r))*(np.exp(-a*abs(x))-np.exp(-a*(2*L-x))) if x<L else 0.

def p(x,k,D=1.,L=1.):
    if x<=0:return 0.
    if x>=L:return 1.
    t=np.sqrt(k/(2*D))
    return np.exp(-t*t*(L*L-x*x))*dawsn(t*x)/dawsn(t*L)

def make_m(k,D=1.,limit=30.):
    umax=limit*np.sqrt(k/D)
    u=np.concatenate((np.linspace(0,min(100,umax),70000),np.geomspace(100,umax,30000)[1:])) if umax>100 else np.linspace(0,umax,70000)
    F=np.sqrt(np.pi/2)*erfcx(u/np.sqrt(2))
    v=cumulative_trapezoid(F,u,initial=0.)
    return lambda x:np.interp(abs(x)*np.sqrt(k/D),u,v)/k

def run(D=1.,L=1.,r=1.):
    a=np.sqrt(r/D); q=np.exp(-a*L)
    mass=quad(lambda x:h(x,D,L,r),-40*max(L,1/a),0,epsabs=1e-11)[0]+quad(lambda x:h(x,D,L,r),0,L,epsabs=1e-11)[0]
    assert abs(mass-(1-q))<1e-10
    deriv=(h(L-1e-5,D,L,r)-h(L-2e-5,D,L,r))/1e-5
    assert abs(deriv+r*q/D)<1e-4
    print('params',D,L,r,'q',q,'mass',mass,'boundary slope',deriv,'pred slope',-r*q/D)
    for k in (12.,24.,48.,96.,192.,384.):
      m=make_m(k,D,limit=40*max(L,1/a))
      near=quad(lambda x:h(x,D,L,r)*p(x,k,D,L),0,L,epsabs=1e-13,limit=300)[0]
      # compute from original return mean, including target visibility
      a_ret=quad(lambda x:h(x,D,L,r)*m(x),-40*max(L,1/a),0,epsabs=1e-9,limit=300)[0]+quad(lambda x:h(x,D,L,r)*m(x),0,L,epsabs=1e-9,limit=300)[0]-m(L)*near
      M=((1-q)/r+a_ret)/(q+near)
      Mir=(1-q)/(r*q)
      ratio=(M-Mir)*k/np.log(k*L*L/D)
      p_ratio=near*k*k*L*L/(r*q*D)
      print(f'k={k:6.0f}  p_ret={near:.10g}   k² p/(r q)={p_ratio:.6f}  kΔM/logK={ratio:.6f} target={(1-q)/(2*q):.6f}')
      assert near>0 and M>Mir
    return

if __name__=='__main__':
 run()
 run(D=2.,L=1.4,r=0.6)
