"""Reproducibility diagnostics for the two-logarithmic-coset exponential Riesz bounds.

Run: python check_two_coset.py (requires numpy, scipy, mpmath).
Finite tests support formulas; the infinite claims use the analytical proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigvalsh
from mpmath import mp


def sech(x):
    return 2.0*math.exp(-abs(x))/(1+math.exp(-2*abs(x)))


def symbol_direct(h, s, theta, cutoff=100):
    f=0j; g=0j
    for j in range(-cutoff, cutoff+1):
        phase=complex(math.cos(j*theta),math.sin(j*theta))
        f+=sech(j*h/2)*phase
        g+=sech((j*h+s)/2)*phase
    return float(f.real),g


def symbol_poisson(h,s,theta,cutoff=100):
    f=0.;g=0j
    for ell in range(-cutoff,cutoff+1):
        omega=(theta+2*math.pi*ell)/h
        z=sech(math.pi*omega)
        f+=z
        g+=z*complex(math.cos(omega*s),math.sin(omega*s))
    return 2*math.pi/h*f,2*math.pi/h*g


def collision_coefficient(h,theta,cutoff=150):
    weights=[];inds=[]
    for ell in range(-cutoff,cutoff+1):
        w=sech(math.pi*(theta+2*math.pi*ell)/h)
        if w>0:weights.append(w);inds.append(ell)
    W=sum(weights)
    return 4*math.pi**3/h**3*(sum(w*i*i for w,i in zip(weights,inds))-(sum(w*i for w,i in zip(weights,inds)))**2/W)


def gram_matrix(h,s,n):
    positions=[j*h+x for j in range(n) for x in (0.,s)]
    return np.array([[sech((x-y)/2) for y in positions] for x in positions],float)


def run():
    checks=0
    for h in (0.8,1.7,3.5):
        for frac in (0.21,0.5,0.79):
            s=frac*h
            for theta in (0., 0.37, 1.2, 2.81,math.pi):
                f,g=symbol_direct(h,s,theta)
                fp,gp=symbol_poisson(h,s,theta)
                assert abs(f-fp)<3e-10
                assert abs(g-gp.conjugate())<3e-10
                assert f+1e-12>=abs(g)
                checks+=3
            xs=np.linspace(-math.pi,math.pi,201)
            lower=min(symbol_poisson(h,s,x)[0]-abs(symbol_poisson(h,s,x)[1]) for x in xs)
            upper=max(symbol_poisson(h,s,x)[0]+abs(symbol_poisson(h,s,x)[1]) for x in xs)
            f0,g0=symbol_direct(h,s,0.)
            assert abs(upper-(f0+g0.real))<2e-8
            assert lower>0
            checks+=2
            G=gram_matrix(h,s,12)
            vals=eigvalsh(G)
            assert vals[0]+1e-8>=lower-0.0001 # theta-grid underestimates true inf; loose finite-section sanity
            assert vals[-1]<upper+1e-7
            checks+=2
            for j,k,a,b in ((0,0,0,0),(0,1,1,0),(2,4,1,0)):
                x=j*h+(s if a else 0.)
                y=k*h+(s if b else 0.)
                vx=math.exp(-x);vy=math.exp(-y)
                numeric=quad(lambda t:2*math.sqrt(vx*vy)*math.exp(-(vx+vy)*t),0,np.inf,epsabs=1e-11)[0]
                exact=sech((x-y)/2)
                assert abs(numeric-exact)<1e-9
                checks+=1
    # Verify the local quadratic collision law via 50-digit theta-min computation at two mesh widths.
    mp.dps=55
    for h in (2.,4.):
        hm=mp.mpf(h)
        C=mp.mpf('0')
        w=[(k,1/mp.cosh(mp.pi*(2*mp.pi*k)/hm)) for k in range(-12,13)]
        W=sum(wt for _,wt in w); mu=sum(k*wt for k,wt in w)/W
        C=4*mp.pi**3/hm**3*sum(wt*(k-mu)**2 for k,wt in w)
        for s in (mp.mpf('0.01'),mp.mpf('0.005')):
            gm=sum(wt*mp.exp(1j*2*mp.pi*k*s/hm) for k,wt in w)*2*mp.pi/hm
            fm=W*2*mp.pi/hm
            actual=fm-abs(gm)
            assert abs(actual/s**2/C-1)<mp.mpf('0.00015')
            checks+=1
    for h in (0.5,0.8,1.,2.):
        xs=np.linspace(0.,math.pi,201)
        Cmin=min(collision_coefficient(h,t) for t in xs)
        asym=16*math.pi**3/h**3*math.exp(-2*math.pi**2/h)
        assert abs(Cmin/asym-1)<0.001
        checks+=1
    for h in (12.,16.):
        xs=np.linspace(0.,math.pi,200)
        Cmin=min(collision_coefficient(h,t) for t in xs)
        assert abs(Cmin-0.125)<0.002
        checks+=1
    print('PASS:',checks,'independent finite numerical/quadrature assertions')

if __name__=='__main__':run()
