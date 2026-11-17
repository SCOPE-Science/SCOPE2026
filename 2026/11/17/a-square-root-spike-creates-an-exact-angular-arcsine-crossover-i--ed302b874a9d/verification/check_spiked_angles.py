import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import norm

def origin(tau): return math.atan(tau)/math.pi

def pdf(t,tau):
    if not 0<t<1: return 0.
    f=1 + math.sqrt(t/(t+tau*tau))
    return f/(2*math.pi*math.sqrt(t*(1-t)))

def mean_width(tau): return math.sqrt(2/math.pi)*(1+math.sqrt(1+tau*tau))
for tau in [0,0.2,0.5,1,2,5,100]:
    total=quad(lambda t: pdf(t,tau),0,1,epsabs=1e-11)[0]+origin(tau)
    assert abs(total-1)<2e-9,(tau,total)
    print(tau,'mass',origin(tau),'density mass',total-origin(tau),'meanwidth',mean_width(tau))
# sanity 1: explicit vertex inner products match random walk formula, in actual coordinates
rng=np.random.default_rng(160423)
for n in range(3,15):
    for a in (1,3,11):
        for repeat in range(20):
            G=rng.normal(size=n)
            vertices=np.zeros((n+1,n))
            for k in range(n):
                vertices[k,k:n-1]=1.
                vertices[k,-1]=a
            expected=np.max(vertices@G)
            bm=np.max(np.r_[0,np.cumsum(G[n-2::-1])])
            assert np.isclose(expected,max(0.,a*G[-1]+bm))
print('finite support identities passed 720')
# sanity 2: actual step argmax law and origin mass vs limit
for tau in [0.,0.5,1.,2.]:
    n=700
    a=1 if tau==0 else round(tau*math.sqrt(n))
    N=60000
    ang=[]; vals=[]
    hit=0
    batch=2500
    for i in range(0,N,batch):
        q=min(batch,N-i)
        increments=rng.standard_normal((q,n-1))
        partial=np.c_[np.zeros(q),np.cumsum(increments,axis=1)]
        j=np.argmax(partial,axis=1)
        m=partial[np.arange(q),j]
        g0=rng.normal(size=q)
        keep=m+a*g0>0
        hit+=(~keep).sum()
        ang.extend(j[keep]/n)
    exp=origin(tau)
    obs=hit/N
    # nonzero probability on j/n < 0.5, via analytical integration
    target=quad(lambda t: pdf(t,tau),0,.5,epsabs=1e-9)[0]
    empirical=len([x for x in ang if x<.5])/N
    print('sim',tau,n,a,'origin',round(obs,5),round(exp,5),'t<.5',round(empirical,5),round(target,5))
    assert abs(obs-exp)<.035
    assert abs(empirical-target)<.035
print('SPIKED_LECTURE_HALL_PASS analytic_norms=7 finite_vertex_tests=720 stochastic=240000')
