#!/usr/bin/env python3
"""Independent floating-point stress test of the flower spectral recovery law."""
import numpy as np
from collections import defaultdict
rng=np.random.default_rng(771199)

def Hbuild(ts,ph):
    m=len(ts);H=np.zeros((2*m+1,2*m+1),dtype=complex)
    for j,(t,p) in enumerate(zip(ts,ph)):
        a=2*j+1;b=a+1
        H[0,a]=H[a,0]=H[0,b]=H[b,0]=1
        H[a,b]=t*np.exp(1j*p);H[b,a]=t*np.exp(-1j*p)
    return H

def formula(z,ts,ph):
    val=z*np.prod([z*z-t*t for t in ts])
    for j,(t,p) in enumerate(zip(ts,ph)):
        val-=(2*z+2*t*np.cos(p))*np.prod([z*z-tt*tt for k,tt in enumerate(ts) if k!=j])
    return val

for m in range(2,10):
    for trial in range(30):
        ts=[int(rng.integers(1,5)) for _ in range(m)]
        ph=rng.uniform(-np.pi,np.pi,m)
        H=Hbuild(ts,ph)
        roots=np.linalg.eigvalsh(H)
        for z in [float(m+6),float(-m-6),0.4+1.3j,2.6+0.9j]:
            predicted=formula(z,ts,ph)
            actual=np.prod(z-roots)
            assert abs(predicted-actual)<1e-7*max(1.,abs(actual),abs(predicted)),(m,ts,z,predicted,actual)
        # Rooted third walk moments independently via dense matrix multiplication.
        cube=H@H@H
        for j,(t,p) in enumerate(zip(ts,ph)):
            assert abs(cube[2*j+1,2*j+1]-2*t*np.cos(p))<1e-10
        # Resolve each known equal-weight class from the spectrum.
        counts=defaultdict(list)
        for j,t in enumerate(ts):counts[t].append(j)
        Q=np.poly(roots) # monic coefficients in descending order
        quotient=Q.copy()
        for t,inds in counts.items():
            for _ in range(len(inds)-1):
                quotient,rem=np.polydiv(quotient,[1,0,-t*t]);assert np.max(abs(rem))<1e-5*max(1,np.max(abs(Q)))
        for t,inds in counts.items():
            d=np.prod([t*t-u*u for u in counts if u!=t]); recovered=-np.polyval(quotient,t)/(2*t*d)-len(inds)
            truth=sum(np.cos(ph[j]) for j in inds)
            assert abs(recovered-truth)<1e-4,(m,ts,t,recovered,truth)
    print('PASS size',m,'30 random phase/weight samples')
print('NUMERICAL AUDIT PASSED')
