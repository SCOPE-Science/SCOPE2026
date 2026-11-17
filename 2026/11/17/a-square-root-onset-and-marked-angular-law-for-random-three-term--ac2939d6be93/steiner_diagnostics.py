"""Numerical corroboration of a circle-sampled three-terminal Steiner-savings law.
Run: python steiner_diagnostics.py (requires numpy and scipy)."""
import math
import numpy as np
from scipy.integrate import quad

PI=math.pi

def h_boundary(alpha):
    p=2*math.sin(alpha/2)
    q=2*math.sin(PI/3-alpha/2)
    return p*q/(p+q)**2

def coefficient():
    I=quad(lambda a:math.sqrt(2/h_boundary(a)),0,2*PI/3,epsabs=1e-11,limit=300)[0]
    return 3*I/(PI*PI)

def angular_measure(s,t):
    total=2*PI/3+2*s
    big=4*PI/3-2*s
    lo=max(0,total-big)
    hi=min(total,big)
    if hi<=lo: return 0
    hcrit=(2*t-t*t)/(2*(1-math.cos(s))) if s else float('inf')
    if hcrit>=0.25:return hi-lo
    r=2*hcrit/(1-2*hcrit+math.sqrt(1-4*hcrit))
    cut=2*math.atan2(r*math.sin(total/2),1+r*math.cos(total/2))
    return max(0,min(hi,cut)-lo)+max(0,hi-max(lo,total-cut))

def exact(t):
    s0=math.acos(1-2*(2*t-t*t)) if 2*(2*t-t*t)<2 else PI/3
    borders=[0,PI/6,PI/3]
    if 0<s0<PI/3:borders.append(s0)
    borders=sorted(set(borders))
    value=sum(quad(lambda s:angular_measure(s,t),left,right,epsabs=1e-12,limit=300)[0] for left,right in zip(borders,borders[1:]))
    return 3*value/(PI*PI)

def independent_mc(n=1200000,seed=20261110):
    rng=np.random.default_rng(seed)
    a=rng.uniform(0,2*PI,(n,3))
    xy=np.stack([np.cos(a),np.sin(a)],axis=-1)
    u=xy[:,1]-xy[:,0]
    v=xy[:,2]-xy[:,0]
    w=xy[:,2]-xy[:,1]
    ab=np.linalg.norm(u,axis=1)
    ac=np.linalg.norm(v,axis=1)
    bc=np.linalg.norm(w,axis=1)
    sides=np.stack([ab,ac,bc],axis=1)
    ssort=np.sort(sides,axis=1)
    mst=ssort[:,0]+ssort[:,1]
    # Largest angle >= 120 iff cos of angle opposite longest side <= -1/2.
    cosine=(ssort[:,0]**2+ssort[:,1]**2-ssort[:,2]**2)/(2*ssort[:,0]*ssort[:,1])
    no_steiner=cosine<=-0.5
    area=abs(u[:,0]*v[:,1]-u[:,1]*v[:,0])/2
    steiner=np.sqrt((ab*ab+ac*ac+bc*bc+4*math.sqrt(3)*area)/2)
    steiner=np.where(no_steiner,mst,steiner)
    gain=np.maximum(0,1-steiner/mst)
    return np.mean(no_steiner), {t:float(np.mean((gain>0)&(gain<t))) for t in (0.001,0.01)}

if __name__=='__main__':
    c=coefficient()
    assert abs(c-2.700948948484718)<1e-10
    vals={t:exact(t) for t in (1e-2,1e-3,1e-4,1e-6,1e-8)}
    assert abs(exact(0.14)-2/3)<1e-9
    assert abs(vals[1e-8]/math.sqrt(1e-8)/c-1)<0.00035
    atom, observations=independent_mc()
    assert abs(atom-1/3)<0.002
    for t,obs in observations.items():
        predicted=vals[t]
        assert abs(obs-predicted)<0.0015, (t,obs,predicted)
    print('coefficient',c)
    for t,p in vals.items(): print('t',t,'exact_probability',p,'scaled',p/math.sqrt(t))
    print('atom_mc',atom,'observed',observations)
    print('CIRCULAR_STEINER_SAVINGS_ATOM_AND_SQRT_LAW_OK')
