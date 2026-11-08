"""Reproduce ellipse-slit visibility probabilities from disk coordinates."""
import math
import numpy as np
from scipy.integrate import quad

def cross_probability_integral(a,c=0.,h=0.):
    assert a>0 and (abs(c)+a)**2+h**2 <1
    def jf(s):
        k=1-s*s-h*h
        def theta_integrand(th):
            p=h*math.cos(th)-s*math.sin(th)
            return math.sin(th)*math.sqrt(max(0.,1-p*p))
        return k*quad(theta_integrand,0,math.pi,epsabs=2e-11)[0]
    return 2/math.pi**2*quad(jf,c-a,c+a,epsabs=1e-10)[0]

def centered_formula(a):
    def g(s):
        q=math.atanh(s)/s if s>0 else 1.
        return (1-s*s)*(1+(1-s*s)*q)
    return 4/math.pi**2*quad(g,0,a,epsabs=1e-12)[0]

def monte_carlo(a,c=0.,h=0.,n=700000,seed=12026):
    rng=np.random.default_rng(seed)
    r=np.sqrt(rng.random((2,n)))
    th=rng.random((2,n))*2*np.pi
    xs=r*np.cos(th);ys=r*np.sin(th)
    frac=np.divide(h-ys[0],ys[1]-ys[0],out=np.full(n,np.nan),where=np.abs(ys[1]-ys[0])>1e-16)
    cross=(frac>0)&(frac<1)
    xcross=xs[0]+frac*(xs[1]-xs[0])
    return np.mean(cross & (xcross>=c-a)&(xcross<=c+a))

if __name__=='__main__':
  for a,c,h in [(0.1,0.,0.),(0.3,0.,0.),(0.3,0.3,0.),(0.3,0.,0.4),(0.3,0.25,0.25),(0.6,0.,0.)]:
    exact=cross_probability_integral(a,c,h)
    sample=monte_carlo(a,c,h)
    if c==h==0:
        assert abs(exact-centered_formula(a))<1e-10
    assert abs(sample-exact)<5*math.sqrt(exact*(1-exact)/700000)+1e-4, (a,c,h,exact,sample)
    assert exact <= centered_formula(a)+1e-11
    print(f'a={a} c={c} h={h} integral={exact:.10f} simulation={sample:.10f}')
  print('DISK_SLIT_BEER_INDEX_AFFINE_CENTERING_OK')

def ellipse_centered_blocked(A,B,length,angle):
    a=length/2*math.hypot(math.cos(angle)/A,math.sin(angle)/B)
    if not (0<a<1): raise ValueError('Segment does not fit')
    return centered_formula(a)

if __name__=='__main__':
    for A,B,length in [(2.,1.,1.2),(1.2,0.5,0.6),(3.,2.,3.1)]:
        best=ellipse_centered_blocked(A,B,length,math.pi/2)
        vals=[ellipse_centered_blocked(A,B,length,t) for t in np.linspace(0,math.pi,101)]
        assert abs(max(vals)-best)<1e-12
        print('ellipse',A,B,length,'max',best,'major',vals[0])
    print('AFFINE_ELLIPSE_FREE_ORIENTATION_MINIMUM_OK')
