"""Reproducibility checks for a fixed-three-observation sphere-ECF statistic.

Requires numpy and scipy. These numerical checks supplement the analytic proof;
they do not certify any asymptotic assertion by finite computation.
"""
import math
import numpy as np
from scipy.special import hyp0f1, roots_jacobi, j0

N = 3
c = math.exp(-0.5)
h = math.exp(-1.0 / 3)
C = 3 * (((1 + 2*c)/3)**2 - 2*c*h + c*c)
beta = c*(-1/6 - 2*c/3 + h/3)
gamma = c*(1+2*c-h)/24
assert gamma > 0

def H(m, x, nodes=None, weights=None):
    """Spherical character integral at squared argument m*x."""
    x = np.asarray(x, dtype=float)
    if nodes is None:
        nodes, weights = roots_jacobi(72, m-1.5, m-1.5)
        weights = weights / np.sum(weights)
    return np.sum(np.cos(np.sqrt(m*np.maximum(x, 0))[..., None]*nodes)*weights, axis=-1)

def normalized_stat_from_gram(G, m):
    diag = np.diag(G)
    D = np.maximum(0.0, diag[:,None]+diag[None,:]-2*G)
    x1 = D[:,:,None,None]+D[None,None,:,:]
    x2 = diag[:,None]+diag[None,:]
    nodes, weights = roots_jacobi(72, m-1.5, m-1.5)
    weights = weights / weights.sum()
    return N*(H(m, x1, nodes, weights).mean() - 2*c*H(m, x2, nodes, weights).mean()+c*c)

def sample_gram(X):
    n, m = X.shape
    assert n==3
    z = X-X.mean(axis=0)
    z = z / np.sqrt(np.sum(z*z,axis=0)/(n-1))
    G = z@z.T/m
    assert np.max(np.abs(G@np.ones(n))) < 1e-9
    assert abs(np.trace(G)-2) < 1e-9
    return G,z

P=np.eye(3)-np.ones((3,3))/3
rng=np.random.default_rng(1289)
count=0
# Two independent implementations of the spherical integral: generalized hypergeometric
# function (through m=60) versus Jacobi quadrature.
for m in (1,2,3,5,10,20,50):
    for x in np.linspace(0, 8, 21):
        ref=float(hyp0f1(m, -m*x/4))
        got=float(H(m,x))
        assert abs(got-ref) < 2e-12, (m,x,got,ref)
        count+=1
# The m=1 formula agrees with the published Bessel representation.
for _ in range(15):
    data=rng.normal(size=(3,1))
    G,z=sample_gram(data)
    d2=np.maximum(0,np.diag(G)[:,None]+np.diag(G)[None,:]-2*G)
    x1=d2[:,:,None,None]+d2[None,None,:,:]
    x2=np.diag(G)[:,None]+np.diag(G)[None,:]
    bessel=3*(j0(np.sqrt(x1)).mean()-2*c*j0(np.sqrt(x2)).mean()+c*c)
    assert abs(normalized_stat_from_gram(G,1)-bessel) < 2e-12
    count+=1
# Three-row tangent space: trace, row sums and exact quadratic form.
def tangent(a,b):
    d=-a-b
    return np.array([[a,d,b],[d,b,a],[b,a,d]])
for _ in range(25):
    a,b=rng.uniform(-.5,.5,size=2)
    T=tangent(a,b)
    assert np.max(abs(T@np.ones(3))) < 1e-12
    assert abs(np.trace(T))<1e-12
    S=a*a+b*b+(-a-b)**2
    assert abs(np.sum(T*T)-3*S)<1e-12
    count+=3
# Check the explicit second-order expansion against exact sphere quadrature.
T=tangent(.4,-.15)
limit=beta+gamma*np.sum(T*T)
err=[]
for m in (100,200,500,1000,2000,4000):
    G=P+T/math.sqrt(m)
    assert np.min(np.linalg.eigvalsh(G)[1:]) > 0
    value=m*(normalized_stat_from_gram(G,m)-C)
    err.append(abs(value-limit))
    count+=2
assert err[-1]<err[0]*.12, err
assert err[-1]<0.0005, err
count+=2
# Normalized sample shapes generate the same 2-dimensional covariance under
# Gaussian, uniform and Laplace marginal distributions.
E1=tangent(1/math.sqrt(6),-1/math.sqrt(6))
E2=tangent(1/math.sqrt(18),1/math.sqrt(18))
for kind in ('normal','uniform','laplace'):
    X=getattr(rng,kind)(size=(3,30000))
    G,Z=sample_gram(X)
    y1=np.einsum('ik,ij,jk->k',Z,E1,Z)
    y2=np.einsum('ik,ij,jk->k',Z,E2,Z)
    Y=np.vstack((y1,y2))
    assert np.max(abs(Y.mean(axis=1)))<.025, (kind,Y.mean(axis=1))
    cov=Y@Y.T/Y.shape[1]-np.outer(Y.mean(axis=1),Y.mean(axis=1))
    assert np.max(abs(cov-np.eye(2)))<.035, (kind,cov)
    norms=np.sum(Y*Y,axis=0)
    assert np.max(abs(norms-2))<2e-12
    count+=5
rho=2*math.sqrt(math.pi)*math.erf(math.sqrt(3)/2)/math.sqrt(2*math.sqrt(3)*math.sqrt(2*math.pi))
assert 0<rho<1
count+=1
print('CHECKS PASSED:', count)
print('C =',format(C,'.15g'))
print('beta =',format(beta,'.15g'))
print('gamma =',format(gamma,'.15g'))
print('limit expected mean =',format(beta+2*gamma,'.15g'))
print('limit 95th percentile =',format(beta-2*gamma*math.log(.05),'.15g'))
print('uniform-vs-Gaussian one-coordinate affinity =',format(rho,'.15g'))
print('finite-dimension expansion errors =',err)
