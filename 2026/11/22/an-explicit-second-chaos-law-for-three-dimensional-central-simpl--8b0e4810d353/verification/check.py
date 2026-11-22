import itertools, math
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_legendre

def a(m): return math.comb(2*m,m)/4**m

def lam(m): return (a(m+1)**2-a(m)**2)/(8*(4*m+3))

# Funk--Hecke integral: 1/2 int_{-1}^1 (acos(t)-pi/2)/(4pi) P_l(t) dt
for m in range(13):
    l=2*m+1
    v=quad(lambda t: (math.acos(t)-math.pi/2)*eval_legendre(l,t)/(8*math.pi),-1,1,epsabs=1e-12)[0]
    assert abs(v-lam(m)) < 1e-9, (m,v,lam(m))
for l in range(2,18,2):
    v=quad(lambda t: (math.acos(t)-math.pi/2)*eval_legendre(l,t)/(8*math.pi),-1,1,epsabs=1e-12)[0]
    assert abs(v)<1e-9
exact=(math.pi**2-8)/(64*math.pi**2)
series=sum((4*m+3)*lam(m)**2 for m in range(1000))
assert 0 < exact-series <1e-12,(exact,series)
assert abs(lam(0)+1/32)<1e-15
assert abs(lam(1)+1/512)<1e-15
print('spherical spectral checks 13 odd/8 even + tail:',exact,series, 'n² variance constant:',72*exact)

rng=np.random.default_rng(20261120)
X=np.array([1.,0.,0.])
N=180000
for theta in (0.3,0.85,1.55,2.5):
    Y=np.array([math.cos(theta),math.sin(theta),0.])
    Z=rng.normal(size=(N,3));Z/=np.linalg.norm(Z,axis=1)[:,None]
    W=rng.normal(size=(N,3));W/=np.linalg.norm(W,axis=1)[:,None]
    A=np.sum(np.cross(Y,Z)*W,axis=1)
    B=-np.sum(np.cross(X,Z)*W,axis=1)
    C=np.sum(np.cross(X,Y)*W,axis=1)
    D=-np.sum(np.cross(X,Y)*Z,axis=1)
    val=np.mean(((A>0)&(B>0)&(C>0)&(D>0))|((A<0)&(B<0)&(C<0)&(D<0)))
    target=theta/(4*math.pi)
    print('conditional given 2 common vertices',theta,val,target)
    assert abs(val-target)<0.006

# Direct check of the tetrahedron indicator and n-normalized simplicial depth.
def depth(x,ids):
    A,B,C,D=(x[ids[:,i]] for i in range(4))
    l0=np.einsum('ij,ij->i',np.cross(B,C),D)
    l1=-np.einsum('ij,ij->i',np.cross(A,C),D)
    l2=np.einsum('ij,ij->i',np.cross(A,B),D)
    l3=-np.einsum('ij,ij->i',np.cross(A,B),C)
    return np.mean(((l0>0)&(l1>0)&(l2>0)&(l3>0))|((l0<0)&(l1<0)&(l2<0)&(l3<0)))
for n,rep in [(10,1200),(16,1100),(22,550)]:
    idx=np.array(list(itertools.combinations(range(n),4)))
    vals=np.empty(rep)
    for i in range(rep):
        P=rng.normal(size=(n,3));P/=np.linalg.norm(P,axis=1)[:,None]
        vals[i]=depth(P,idx)
    mean=vals.mean(); nv=(n*n)*vals.var(ddof=1)
    print('finite depth',n,rep,'mean',mean,'n² var',nv,'limit',72*exact)
    assert abs(mean-0.125)<0.013
    assert 0<nv<1.5
print('PASS')
