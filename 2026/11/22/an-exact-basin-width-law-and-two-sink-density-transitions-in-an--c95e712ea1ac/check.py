"""Independent finite diagnostics for fixed-point stability density of a product-sine map.

These checks are not proofs of the infinite asymptotic statements.
"""
import math
import numpy as np

PI = math.pi

def predicted(kappa):
    return (2/PI)*math.asin(min(1.0,1.0/(PI*kappa))) + (2/PI**2)*math.asin(min(1.0,1.0/kappa))

def count(R,kappa):
    ks=np.arange(-int(math.floor(2*R)),int(math.floor(2*R))+1,dtype=np.int64)
    js=np.arange(-int(math.floor(2*R/PI)),int(math.floor(2*R/PI))+1,dtype=np.int64)
    # At the common zero, the multiplier is +1 and is not a sink.
    ks=ks[ks!=0];js=js[js!=0]
    d_k=1+2*PI*kappa*np.sin((1+PI)*ks)
    d_j=1+2*kappa*np.sin((PI**2+PI)*js)
    return int(np.count_nonzero(np.abs(d_k)<1)+np.count_nonzero(np.abs(d_j)<1))

def f(x,k):return x+k*math.sin(2*PI*x)*math.sin(2*x)

def df(x,k):return 1+k*(2*PI*math.cos(2*PI*x)*math.sin(2*x)+2*math.sin(2*PI*x)*math.cos(2*x))

# Test exact branch derivative identities numerically across multiple lattice nodes.
for k in range(-25,26):
    if k:
        lhs=df(k/2,.7);rhs=1+2*PI*.7*math.sin((PI+1)*k)
        assert abs(lhs-rhs)<1e-12,(k,lhs,rhs)
for j in range(-25,26):
    if j:
        lhs=df(j*PI/2,.7);rhs=1+2*.7*math.sin((PI*PI+PI)*j)
        assert abs(lhs-rhs)<2e-12,(j,lhs,rhs)

# Compare independent finite spatial counts with the equidistribution prediction.
for kappa in (.05,1/(2*PI),.25,.7,1,1.3,5):
    R=50000
    obs=count(R,kappa)/(2*R)
    theo=predicted(kappa)
    assert abs(obs-theo)<.006,(kappa,obs,theo)
    print('spatial density',round(kappa,9), round(obs,7),round(theo,7),'diff',round(obs-theo,7))

# Test the exact two threshold expansions at small eps.
for eps in (.0001,.00001):
    k1=(1+eps)/PI
    actual=(1+1/PI)-predicted(k1)
    expected=2*math.sqrt(2*eps)/PI
    assert abs(actual/expected-1)<.003
    k2=1+eps
    delta=predicted(1)-predicted(k2)
    expected2=2*math.sqrt(2*eps)/(PI**2)
    # Smooth drift from first family contributes O(eps) relative to sqrt(eps).
    assert abs(delta/expected2-1)<.035,(eps,delta/expected2)

# Check no nonmonotonicity below threshold, and that negative derivatives appear above.
xs=np.linspace(-50,50,700001)
for kappa in (.08,1/(2*PI)):
    slopes=1+kappa*(2*PI*np.cos(2*PI*xs)*np.sin(2*xs)+2*np.sin(2*PI*xs)*np.cos(2*xs))
    assert slopes.min()>=-1e-11
kappa=.2
slopes=1+kappa*(2*PI*np.cos(2*PI*xs)*np.sin(2*xs)+2*np.sin(2*PI*xs)*np.cos(2*xs))
assert slopes.min()<-.1

# Exact basin-width mixture at a low gain, using all fixed-point locations.
R=25000
ks=np.arange(-int(2*R),int(2*R)+1,dtype=np.int64)
js=np.arange(-int(2*R/PI),int(2*R/PI)+1,dtype=np.int64)
zeros=np.sort(np.concatenate((ks/2.0,js[js!=0]*PI/2.0)))
gprime=2*PI*np.cos(2*PI*zeros)*np.sin(2*zeros)+2*np.sin(2*PI*zeros)*np.cos(2*zeros)
sink_ids=np.where(gprime < -1e-10)[0]
sink_ids=sink_ids[(sink_ids>0)&(sink_ids<len(zeros)-1)]
widths=zeros[sink_ids+1]-zeros[sink_ids-1]
atom_half=np.mean(np.abs(widths-.5)<1e-6)
atom_one=np.mean(np.abs(widths-1)<1e-6)
continuous=1-atom_half-atom_one
assert abs(atom_half-1/(PI+1))<.001
assert abs(atom_one-(PI-2)/(PI+1))<.001
assert abs(continuous-2/(PI+1))<.001
assert np.all((widths>.499999)&(widths<1.000001))
# The nonatomic widths are uniformly distributed on (1/2,1).
nonatom=widths[(widths>.500001)&(widths<.999999)]
assert abs(nonatom.mean()-.75)<.002
print('basin weights',round(atom_half,7),round(atom_one,7),round(continuous,7))

# Monotone basin diagnostic for low gain.
for kappa in (.05,.15):
    for x0 in (-15.3,-2.4,-.3,.001,.1,1.14,5.123,20.3):
        x=x0
        for _ in range(2500):x=f(x,kappa)
        assert abs(f(x,kappa)-x)<1e-5,(kappa,x0,x)
print('all finite diagnostics passed')
