"""Independent geometric checks for near-concurrent random-line triangles."""
import math
import numpy as np
from scipy.special import roots_legendre, erf
from scipy.integrate import quad
from numba import njit

# Gaussian offsets N(0,1); angles uniform in [0,pi).
def ew_quad(nodes=480):
    x,weights=roots_legendre(nodes)
    a=math.pi*(x+1)/2
    weights=weights/2
    A=a[:,None];B=a[None,:]
    sa=np.sin(A); sb=np.sin(B); sab=np.sin(A-B)
    w=np.sqrt(np.abs(sa*sb*sab))/np.sqrt(sa**2+sb**2+sab**2)
    return float(weights @ w @ weights)

def ew_adaptive():
    def inner(b,a):
        sa=math.sin(a);sb=math.sin(b);sab=math.sin(b-a)
        return math.sqrt(sa*sb*sab)/math.sqrt(sa*sa+sb*sb+sab*sab)
    def outer(a):
        return quad(inner,a,math.pi,args=(a,),epsabs=1e-10,epsrel=1e-9,limit=120)[0]
    return 2*quad(outer,0,math.pi,epsabs=1e-9,epsrel=1e-9,limit=120)[0]/math.pi**2

@njit
def count_small(n,sigthr,theta,h):
    s=np.empty((n,n),dtype=np.float64)
    for i in range(n):
        for j in range(n):
            s[i,j]=math.sin(theta[j]-theta[i])
    count=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            sj=s[i,j]
            for k in range(j+1,n):
                si=s[k,i]; sk=s[j,k]
                z=sj*h[k]+sk*h[i]+si*h[j]
                p=abs(sj*si*sk)
                if z*z < 2*sigthr*p:count+=1
    return count

@njit
def simulate(reps,n,t,seed):
    np.random.seed(seed)
    counts=np.zeros(reps,dtype=np.int32)
    for r in range(reps):
        theta=np.random.uniform(0,math.pi,n)
        h=np.random.normal(0,1,n)
        counts[r]=count_small(n,t/(n**6),theta,h)
    return counts

if __name__=='__main__':
    ew=ew_adaptive()
    kappa=ew/(3*math.sqrt(math.pi))
    print('adaptive_integral_ew',repr(ew),'poisson_kappa',repr(kappa))
    for nodes in (256,512,1024):
        print('gauss_node_estimate',nodes,repr(ew_quad(nodes)))
    rng=np.random.default_rng(9048)
    errs=[]
    for _ in range(5000):
        a,b,c=np.sort(rng.uniform(0,math.pi,3));h=rng.normal(size=3)
        dirs=np.array([[math.cos(z),math.sin(z)] for z in (a,b,c)])
        v1=np.linalg.solve(dirs[[0,1]],h[[0,1]])
        v2=np.linalg.solve(dirs[[1,2]],h[[1,2]])
        v3=np.linalg.solve(dirs[[2,0]],h[[2,0]])
        area_direct=abs(np.linalg.det(np.array([v2-v1,v3-v1])))/2
        s12=math.sin(b-a);s23=math.sin(c-b);s31=math.sin(a-c)
        area_formula=(s23*h[0]+s31*h[1]+s12*h[2])**2/(2*abs(s12*s23*s31))
        errs.append(abs(area_direct-area_formula)/max(1,area_direct))
    print('geometry_formula_5000_max_relative_error',max(errs))
    # First-event probabilities and point counts for fixed t, increasing n
    t=150.0
    print('t',t,'lambda',kappa*math.sqrt(t),'poisson_zero',math.exp(-kappa*math.sqrt(t)))
    for n,reps in ((40,1800),(80,1200)):
        counts=simulate(reps,n,t,9411+n)
        print('n',n,'reps',reps,'mean',float(np.mean(counts)),'zero_fraction',float(np.mean(counts==0)),'var',float(np.var(counts)),'predmean',kappa*math.sqrt(t))
    # Single-event conditional area CDF versus exact Gaussian mixture in finite h
    theta=rng.uniform(0,math.pi,(250000,3))
    h=rng.normal(size=(250000,3))
    s12=np.sin(theta[:,1]-theta[:,0]);s23=np.sin(theta[:,2]-theta[:,1]);s31=np.sin(theta[:,0]-theta[:,2])
    z=s23*h[:,0]+s31*h[:,1]+s12*h[:,2]
    p=np.abs(s12*s23*s31); s2=s12*s12+s23*s23+s31*s31
    w=np.sqrt(p/s2)
    cutoff=0.0004
    empirical=np.mean(z*z/(2*p) < cutoff)
    exact_mixture=np.mean(erf(w*math.sqrt(cutoff)))
    asympt=2/math.sqrt(math.pi)*ew*math.sqrt(cutoff)
    print('single_area_h',cutoff,'observed',float(empirical),'exact_angle_avg',float(exact_mixture),'leading',asympt)
    assert max(errs)<1e-7
    assert abs(ew-ew_adaptive())<1e-9
    print('LINE_TRIANGLE_CHECKS_OK')
