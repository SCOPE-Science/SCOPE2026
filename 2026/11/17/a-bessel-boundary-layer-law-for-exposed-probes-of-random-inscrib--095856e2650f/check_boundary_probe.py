"""Standalone checks for the local boundary-probe limit; not a substitute for proof."""
import numpy as np
from scipy.integrate import quad
from scipy.special import k1

def survival(x):
    return 2*np.sqrt(x)*k1(2*np.sqrt(x))

rng=np.random.default_rng(26061110)
N=260_000
for t in [0.2, 2.0, 12.0]:
    x=t/(2*np.pi*np.pi)
    exact=quad(lambda u:np.exp(-u-x/u),0,np.inf,epsabs=1e-11)[0]
    theory=survival(x)
    assert abs(exact-theory)<2e-10, (t,exact,theory)
    for n in [60,300]:
        # Gaps from the fixed site to neighboring samples, in normalized arclength.
        a=rng.gamma(1.,1.,N)
        b=rng.gamma(1.,1.,N)
        rest=rng.gamma(n-1.,1.,N)
        aa=2*np.pi*a/(a+b+rest)
        bb=2*np.pi*b/(a+b+rest)
        # Exact chord crossing near the base point; large circular gaps have negligible probability.
        depth=1-np.cos((aa+bb)/2)/np.cos((aa-bb)/2)
        event=(depth>t/n**2)
        err=abs(event.mean()-theory)
        tol=0.042 if n==60 else 0.016
        print(f't={t:g} n={n} observed={event.mean():.6f} limit={theory:.6f} error={err:.6f}')
        assert err<tol, (t,n,err)
# Independent hull-halfplane classification for full randomly sampled point sets.
n, samples, t = 35, 18_000, 4.0
angles=np.sort(rng.random((samples,n))*2*np.pi,axis=1)
xp=np.cos(angles); yp=np.sin(angles)
xd=np.roll(xp,-1,axis=1)-xp
yd=np.roll(yp,-1,axis=1)-yp
ptx=1-t/n**2
cross=xd*(-yp)-yd*(ptx-xp)
hull_miss=np.any(cross < -1e-13,axis=1)
a=angles[:,0]; b=2*np.pi-angles[:,-1]
local_cross=1-np.cos((a+b)/2)/np.cos((a-b)/2)
near_miss=local_cross>t/n**2
assert np.array_equal(hull_miss,near_miss), (np.sum(hull_miss!=near_miss),samples)
print(f'direct_hull_samples={samples} exact_local_edge_agreement={np.mean(hull_miss==near_miss):.6f}')
print('BOUNDARY_PROBE_BESSEL_AND_CHORD_OK')
