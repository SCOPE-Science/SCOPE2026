import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import cumulative_trapezoid

def prob(q,alpha,N=180,grid=262145):
 x,w=leggauss(N)
 ts=np.linspace(0,2*np.pi,grid)
 raw=(1-q*np.cos(2*ts))**(alpha/2)
 cdf=np.r_[0,cumulative_trapezoid(raw,ts)]; norm=cdf[-1]
 def F(xx):
  return np.floor(xx/(2*np.pi))+np.interp(np.mod(xx,2*np.pi),ts,cdf)/norm
 def d(xx): return (1-q*np.cos(2*xx))**(alpha/2)/norm
 t=np.pi*(1+x); wt=np.pi*w
 s0=np.pi/2+np.arctan2(q*np.sin(2*t),1-q*np.cos(2*t))
 Q=np.zeros_like(t)
 for left,right,side in [(np.zeros_like(t),s0,1),(s0,np.full_like(t,np.pi),-1)]:
  s=(left[:,None]+right[:,None])/2+(right-left)[:,None]/2*x[None,:]
  ws=(right-left)[:,None]/2*w[None,:]
  A=np.cos(s)-q*np.cos(2*t[:,None]+s)
  B=np.sin(s)+q*np.sin(2*t[:,None]+s)
  r0=np.mod(np.arctan2(-A,B),np.pi)
  mass=F(t[:,None]+2*r0)-F(t[:,None])
  h=(1-mass) if side==1 else mass
  Q += np.sum(ws*2*d(t[:,None]+2*s)*h,axis=1)
 return 1-3*np.sum(wt*d(t)*Q)

def verify():
    import math
    # Independent chord-dot identity for the Euclidean ellipse.
    for q in (-0.75,-0.3,0,0.2,0.75):
        a,b=math.sqrt(1+q),math.sqrt(1-q)
        for t in (.12,1.7,3.2):
            for s,r in ((.4,2.1),(.5,1.8),(2.7,.3)):
                p=np.array([a*math.cos(t),b*math.sin(t)])
                v=np.array([a*math.cos(t+2*s),b*math.sin(t+2*s)])-p
                z=np.array([a*math.cos(t+2*r),b*math.sin(t+2*r)])-p
                dot=float(np.dot(v,z))
                geom=np.cos(s-r)-q*np.cos(2*t+s+r)
                assert dot*geom>=-1e-12
    for alpha in (-1.0,0.,0.5,1.,2.):
        zero=prob(0,alpha,N=80)
        assert abs(zero-.25)<2e-10
        vals=[]
        for q in (.04,.08):
            p=prob(q,alpha,N=180)
            pneg=prob(-q,alpha,N=180)
            assert abs(p-pneg)<4e-9
            th=.25-3*(1-alpha)*q*q/(2*np.pi*np.pi)
            assert abs(p-th)<4*q**4
            vals.append((q,p,th))
        print('alpha',alpha,'samples',vals)
    # Numerically corroborate the special Euclidean-arclength cancellation.
    assert abs(prob(.04,1.,N=240)-.25)<1e-6
    print('ELLIPSE_POWER_SAMPLING_SECOND_VARIATION_CHECKS_OK')

if __name__=='__main__':
    verify()
