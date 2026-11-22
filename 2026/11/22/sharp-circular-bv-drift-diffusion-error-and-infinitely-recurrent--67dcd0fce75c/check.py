"""Independent finite-grid and high-precision checks for circular drift-diffusion BV error."""
import math
import numpy as np
from scipy.optimize import brentq

TAU=2*math.pi

def formula(t,b,K=301):
    ks=np.arange(1,K,2,dtype=float)
    return math.pi/2 - 4/math.pi * np.sum(np.exp(-ks*ks*t)*np.cos(ks*b*t)/(ks*ks))

def derivative(t,b,K=301):
    ks=np.arange(1,K,2,dtype=float)
    return 4/math.pi * np.sum(np.exp(-ks*ks*t)*(np.cos(ks*b*t)+b/ks*np.sin(ks*b*t)))

def grid_semigroup(x,t,b):
    N=len(x)
    m=np.fft.fftfreq(N,d=1/N)
    return np.fft.ifft(np.fft.fft(x)*np.exp(-t*m*m+1j*m*b*t)).real

def tv(x):
    return np.sum(np.abs(np.roll(x,-1)-x))

count=0
rng=np.random.default_rng(20261119)
N=4096
for b in [0.0,0.7,2.0,-3.3]:
    for t in [0.012,0.1,0.8,2.0]:
        C=formula(t,b)
        half=np.r_[np.ones(N//2),np.zeros(N//2)]
        lhs=TAU/N*np.sum(np.abs(half-grid_semigroup(half,t,b)))/tv(half)
        assert abs(lhs-C)<0.002, (t,b,C,lhs)
        count+=1
        for _ in range(5):
            x=rng.normal(size=N)
            val=TAU/N*np.sum(np.abs(x-grid_semigroup(x,t,b)))/tv(x)
            assert val <= C+5.e-5,(b,t,val,C)
            count+=1
        # For all nonhalf arcs, BV error <= sharp; the half arc should outperform.
        for frac in [.1,.25,.4]:
            arc=np.r_[np.ones(round(N*frac)),np.zeros(N-round(N*frac))]
            val=TAU/N*np.sum(np.abs(arc-grid_semigroup(arc,t,b)))/tv(arc)
            assert val < C + 0.0003, (b,t,frac,val,C)
            count+=1

for b in [.3,1.,3.,9.]:
    for n in [1,2,3,4]:
        t0=(math.pi/2+math.atan(b)+n*math.pi)/b
        width=min(0.08,1.0/(8*b))
        root=brentq(lambda t: derivative(t,b),t0-width,t0+width)
        assert abs(root-t0)< 1000*math.exp(-8*min(t0,root)) + 2.e-13
        # extrema alternate, signed deviation from equilibrium has expected sign
        deviation=formula(root,b)-math.pi/2
        if abs(deviation)>5e-15:
            assert deviation*((-1)**n)>0
        else:
            # Double precision cannot resolve exp(-large t) from pi/2.
            leading=(-1)**n*4*b/(math.pi*math.sqrt(1+b*b))*math.exp(-root)
            assert leading*((-1)**n)>0
        count+=1

print('PASS',count,'independent numerical comparisons')
print('b=1 large-time extrema:')
for n in range(4):
    b=1
    t0=(math.pi/2+math.atan(b)+n*math.pi)/b
    root=brentq(lambda t: derivative(t,b),t0-.05,t0+.05)
    print(n,round(root,12),round(formula(root,b)-math.pi/2,12))
