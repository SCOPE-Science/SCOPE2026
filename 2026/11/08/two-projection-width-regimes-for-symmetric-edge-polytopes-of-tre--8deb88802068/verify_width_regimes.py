"""Finite computational checks for root-polytope directional-width limits.

Run: python verify_width_regimes.py
This program is corroborative, not an infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.special import ndtri, ndtr
from scipy.integrate import quad

rng = np.random.default_rng(250311)


def width_from_gaussian(x, edges):
    x = np.asarray(x, dtype=float)
    u = (x - x.mean())/np.linalg.norm(x-x.mean())
    direct = 2 * max(abs(u[i]-u[j]) for i,j in edges)
    gauss = 2 * max(abs(x[i]-x[j]) for i,j in edges)/np.linalg.norm(x-x.mean())
    assert abs(direct-gauss) < 1e-11
    return direct

# Exact support identity and the fact that every tree's edge roots are a basis.
for n in range(4, 15):
    edges_star = [(0,j) for j in range(1,n)]
    edges_path = [(j,j+1) for j in range(n-1)]
    for edges in (edges_star,edges_path):
        x = rng.normal(size=n)
        width_from_gaussian(x,edges)
        incidence = np.zeros((n,len(edges)))
        for c,(i,j) in enumerate(edges):
            incidence[i,c]=1
            incidence[j,c]=-1
        assert np.linalg.matrix_rank(incidence)==n-1

# Hub-core trees, exact threshold functional in terms of the same Gaussian sample.
def hub_core_edges(leaves):
    k = len(leaves)
    edges=[(j,j+1) for j in range(k-1)]
    pos=k
    for j,num in enumerate(leaves):
        edges.extend((j,u) for u in range(pos,pos+num))
        pos+=num
    return edges,pos

for leaves in ([7], [5,9], [3,4,5]):
    edges,n = hub_core_edges(leaves)
    for _ in range(5):
        g = rng.normal(size=n)
        s1=max(abs(g[i]-g[j]) for i,j in edges)
        h=g[:len(leaves)]
        s2=max([abs(h[j]-h[j+1]) for j in range(len(leaves)-1)] +
               [max(abs(g[sum(leaves[:j])+len(leaves):sum(leaves[:j+1])+len(leaves)]-h[j])) for j in range(len(leaves))])
        assert abs(s1-s2)<1e-12
        width_from_gaussian(g,edges)

# Exact finite-dimensional star-edge maximum CDF, integrated over the hub.
from scipy.stats import norm
m_star=6
threshold=2.1
integral, _=quad(lambda x: norm.pdf(x)*(ndtr(x+threshold)-ndtr(x-threshold))**m_star,-9,9,epsabs=2e-11)
samples=rng.normal(size=(120000,m_star+1))
empirical=np.mean(np.max(np.abs(samples[:,1:]-samples[:,:1]),axis=1)<=threshold)
assert abs(empirical-integral)<0.012,(empirical,integral)

# Distinct first two hub-count laws share the same surprising limit variance.
from scipy.integrate import quad
cdf2=lambda t:(2*ndtr(t)-1)**2
mean2=quad(lambda t:1-cdf2(t),0,10,epsabs=1e-11)[0]
second2=quad(lambda t:2*t*(1-cdf2(t)),0,10,epsabs=1e-11)[0]
assert abs(mean2-2/math.sqrt(math.pi))<1e-8
assert abs(second2-1-2/math.pi)<1e-8
assert abs(second2-mean2**2-(1-2/math.pi))<1e-8

# Numerically verify finite-dimensional scale and limiting distribution shapes.
for k in (1,2,3):
    m=2400
    leaves=[m//k]*k
    leaves[-1]+=m-sum(leaves)
    edge,n=hub_core_edges(leaves)
    reps=2800
    gs=rng.normal(size=(reps,n))
    a=ndtri(1-1/m)
    s=np.zeros(reps)
    pos=k
    for j,l in enumerate(leaves):
        s=np.maximum(s,np.max(np.abs(gs[:,pos:pos+l]-gs[:,j:j+1]),axis=1))
        pos+=l
    if k>1:
        s=np.maximum(s,np.max(np.abs(np.diff(gs[:,:k],axis=1)),axis=1))
    h=np.max(np.abs(gs[:,:k]),axis=1)
    err=np.mean(np.abs((s-a)-h))
    assert err<0.50,(k,err)
    # The normalized radial correction is small at the tested size.
    R=np.linalg.norm(gs-gs.mean(axis=1,keepdims=True),axis=1)
    root_width=(math.sqrt(n-1)/R)*s
    assert np.mean(abs(root_width-s))<0.13
    print('hub',k,'n',n,'mean_abs_coupling_error',round(float(err),3))

m=16000
q=ndtri(1-1/(2*m))
b=math.sqrt(2)*q
reps=2000
batch=100
vals=[]
for _ in range(reps//batch):
    gs=rng.normal(size=(batch,m+1))
    s=np.max(np.abs(np.diff(gs,axis=1)),axis=1)
    vals.extend((0.5*b*(s-b)).tolist())
vals=np.array(vals)
for y in (-1,0,1):
    ecdf=np.mean(vals<=y)
    theoretical=math.exp(-math.exp(-y))
    assert abs(ecdf-theoretical)<0.12,(y,ecdf,theoretical)
print('path','m',m,'Gumbel-quantiles',[(y,round(float(np.mean(vals<=y)),3)) for y in (-1,0,1)])
print('ROOT_POLYTOPE_WIDTH_REGIME_CHECKS_PASSED')
