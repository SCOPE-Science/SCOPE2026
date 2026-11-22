"""Deterministic tests for the two-agent exponential-utility opinion rule."""
import math

def direct(mu,kappa,x=0.,y=1.,steps=100000):
    for _ in range(steps):
        d=y-x
        if abs(d) < 1e-13: break
        # stable logistic formula
        w=1/(1+math.exp(-kappa*d))
        xn=x+2*mu*w*d
        yn=y-2*mu*(1-w)*d
        x,y=xn,yn
    return (x+y)/2,abs(x-y)

def series(mu,kappa,d=1.,tol=1e-14):
    q=abs(1-2*mu)
    a=d
    total=0.
    for i in range(1000000):
        term=mu*a*math.tanh(kappa*a/2)
        total+=term
        if abs(term)<tol: return total,i+1
        a*=q
    raise RuntimeError('exhausted')

def threshold(kappa,d=1.):
    lo,hi=.5,.99999999
    for i in range(65):
        mid=(lo+hi)/2
        s,_=series(mid,kappa,d)
        if s>d/2: hi=mid
        else:lo=mid
    return (lo+hi)/2

if __name__=='__main__':
    for k in [.1,.5,1.,2.,5.,10.]:
        mc=threshold(k)
        print('kappa',k,'mu_c',mc,'weak_asymp',1-k/4,'strong_asymp',.5+math.exp(-k),'mu=.99',series(.99,k)[0]+.5)
    n=0
    for mu in [.01,.1,.2,.49,.5,.51,.55,.7,.9,.99]:
        for kap in [-2.,-.5,.25,1.,2.]:
            shifted,its=series(mu,kap)
            direct_val,gap=direct(mu,kap,steps=150000)
            assert abs(direct_val-(.5+shifted)) < 5e-10,(mu,kap,direct_val,shifted)
            assert gap<2e-12
            n+=1
    print('PASS: direct against series',n,'cases')
    for mu in [.9,.95,.99,.995,.999]:
        sh,_=series(mu,1.)
        print('mu',mu,'shift',sh,'scaled',(1-mu)*sh,'theory',math.log(math.cosh(.5)))
