import numpy as np
from scipy.special import betainc,beta

def theoretical(n,a):
    pbound=1-n*(1-betainc(a,(n-1)*a,0.5))
    const=n*2**(2-n*a)/(np.pi*beta(a,(n-1)*a)*pbound)
    return pbound,const

def trial(n,a,N=1800000):
    rng=np.random.default_rng(3192+int(100*a)+n)
    pb,c=theoretical(n,a)
    nb=0;hit={120:0,240:0,480:0}
    for i in range(0,N,120000):
        x=rng.gamma(a,1,size=(min(120000,N-i),n));x/=x.sum(axis=1,keepdims=True)
        keep=np.max(x,axis=1)<0.5
        xx=x[keep];nb+=len(xx)
        area=np.tan(np.pi*xx).sum(axis=1)
        for threshold in hit:hit[threshold]+=np.count_nonzero(area>threshold)
    ratios={z:(hit[z]/nb)*z/c for z in hit}
    print('n,a',n,a,'Pbound',pb,'estimate',nb/N,'C',c,'ratios',ratios,'hits',hit)
    assert abs(nb/N-pb)<0.004
    assert 0.85<ratios[120]<1.15 and 0.80<ratios[240]<1.2 and 0.75<ratios[480]<1.25

for n,a in [(3,0.5),(3,1.0),(4,1.0),(4,2.0)]:trial(n,a)
print('DIRICHLET_TANGENT_PARETO_CHECKS_OK')
