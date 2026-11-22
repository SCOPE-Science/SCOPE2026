"""Independent numerical checks for renewal-reset sign-persistence formulas."""
from math import gamma,exp,pi
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc,gammaincc

def kernel(mu,a,t):
    return float(betainc(mu,1-mu,a/(a+t))) if a>0 else 0.0

def C_survival(mu,t,mean,survival):
    val,err=quad(lambda a:survival(a+t)*kernel(mu,a,t),0,np.inf,epsabs=1e-11,epsrel=1e-11,limit=300)
    return val/mean

def C_atomic(mu,t,atoms):
    mean=sum(p*w for p,w in atoms)
    return sum(p*quad(lambda a: kernel(mu,a,t),0,w-t,epsabs=2e-12)[0] for p,w in atoms if w>t)/mean

def check():
    cnt=0
    for mu in (0.2, 1/3, 0.5):
        for t in (0.02,0.2,1.,2.5):
            c=C_survival(mu,t,1.,lambda x:np.exp(-x))
            target=float(gammaincc(1-mu,t))
            assert abs(c-target)<2e-9,(mu,t,c,target)
            cnt+=1
    print('poisson_gamma',cnt)
    import numpy.random as npr
    rng=npr.default_rng(1042)
    inequalities=0
    for mu in (0.22,0.5):
        for _ in range(35):
            w=np.exp(rng.uniform(-1.4,1.4,4))
            p=rng.dirichlet(np.ones(4))
            atoms=list(zip(p,w))
            mean=np.dot(p,w)
            for t in (mean*0.08,mean*0.3,mean*0.8,mean,mean*1.2):
                c=C_atomic(mu,t,atoms)
                deterministic=C_atomic(mu,t,[(1.,mean)])
                assert c>=deterministic-3e-12,(mu,t,atoms,c,deterministic)
                if t<=mean:
                    assert c>deterministic+1e-10,(mu,t,c,deterministic)
                inequalities+=1
    print('deterministic_inequalities',inequalities)
    for mu in (0.2,0.5):
        for beta in (1.2,1.6,1.9,2.0,2.6):
            b=beta-1
            mean=b/(beta-1)
            constant=(b**beta/mean)*gamma(beta-mu)/((beta-1)*gamma(1-mu)*gamma(beta))
            for t in (10**3,10**4):
                c=C_survival(mu,t,mean,lambda x: (1+x/b)**(-beta))
                target=constant*t**(1-beta)
                assert abs(c/target-1)<0.03,(mu,beta,t,c/target)
                cnt+=1
    print('power_law',cnt)
    for mu in (0.2,0.5):
        for atoms in [[(1,1)],[(0.4,.5),(.6,1.5)],[(0.1,.1),(.9,4.)]]:
            mean=sum(p*w for p,w in atoms)
            moment2=sum(p*w*w for p,w in atoms)
            integral,_=quad(lambda t:C_atomic(mu,t,atoms),0,max(w for p,w in atoms),epsabs=3e-8)
            target=(1-mu)*moment2/(2*mean)
            assert abs(integral-target)<3e-6,(mu,atoms,integral,target)
    print('integrated_correlation',6)
    # Beta free last-zero identity via integration of Beta density.
    for mu in (0.2,0.5):
        for a,t in ((.2,1.),(1.,.2),(2.,2.)):
            T=a+t
            free,_=quad(lambda g:np.sin(np.pi*mu)/np.pi*g**(mu-1)*(T-g)**(-mu),0,a,epsabs=1e-10)
            assert abs(free-kernel(mu,a,t))<3e-10,(mu,a,t,free,kernel(mu,a,t))
    print('free_last_zero',6)

if __name__=='__main__':
    check()
