"""Reproducibility diagnostics for intersecting-cylinder surface-to-volume laws.

Uses scipy quadrature and mpmath independent elliptic evaluations. Finite
numerical tests are not a proof of monotonicity or asymptotic statements.
"""
import math
from scipy.integrate import quad
from scipy.special import ellipk,ellipe
import mpmath as mp


def direct(t, angle):
    z = math.sin(angle)
    v = 8.0/z * quad(lambda y: math.sqrt((t*t-y*y)*(1-y*y)),0,1,epsabs=2e-11)[0]
    a1 = 8.0/z * quad(lambda y: t*math.sqrt((1-y*y)/(t*t-y*y)),0,1,epsabs=2e-11)[0]
    # y = sin theta removes the removable endpoint singularity
    a2 = 8.0/z * quad(lambda th: math.sqrt(t*t-math.sin(th)**2),0,math.pi/2,epsabs=2e-11)[0]
    return v,a1+a2,a1,a2


def elliptic(t, angle):
    m=1.0/(t*t)
    E,K=ellipe(m),ellipk(m)
    v=(8*t**3/(3*math.sin(angle)))*((1+m)*E-(1-m)*K)
    a=8/math.sin(angle)*(t*E+(E-(1-m)*K)/m)
    return v,a


def high_Q(t):
    with mp.workdps(65):
        t=mp.mpf(str(t))
        v=mp.quad(lambda y: mp.sqrt((t*t-y*y)*(1-y*y)),[0,1])
        v1=mp.quad(lambda y: t*mp.sqrt(1-y*y)/mp.sqrt(t*t-y*y),[0,1])
        return 3-(t-1)*v1/v


def check():
    n=0
    ratios=[]
    for t in [1.0,1.001,1.03,1.15,1.5,2.0,3.5,7.0,19.0]:
        for beta in [0.26,0.71,math.pi/2,2.37]:
            v,s,s1,s2=direct(t,beta)
            assert v>0 and s1>0 and s2>0
            n+=1
            if t>1.001:
                ev,ea=elliptic(t,beta)
                assert abs(ev-v)<2e-9*max(1,v), (t,beta,ev,v)
                assert abs(ea-s)<2e-9*max(1,s), (t,beta,ea,s)
                n+=2
            else:
                if t==1:
                    assert abs(v-16/(3*math.sin(beta)))<3e-10
                    assert abs(s-16/math.sin(beta))<3e-10
                    n+=2
            ratios.append((t,beta,s/v))
    for t in [1.1,1.5,2,4,8]:
        rvals=[v for x,theta,v in ratios if abs(x-t)<1e-8]
        if rvals:
            assert max(rvals)-min(rvals)<3e-10
            n+=1
        v,_,_,_=direct(t,0.9)
        dt=1e-4
        vp=direct(t+dt,0.9)[0]
        vm=direct(t-dt,0.9)[0]
        dv=(vp-vm)/(2*dt)
        q=3-(t-1)*dv/v
        assert abs(q-direct(t,0.9)[1]/v)<1e-6
        n+=1
    vals=[float(high_Q(x)) for x in ['1','1.00001','1.001','1.01','1.1','1.5','2','4','10','50']]
    assert all(3>=a>b>2 for a,b in zip(vals,vals[1:]))
    n+=9
    for eta in [mp.mpf('1e-3'),mp.mpf('1e-4'),mp.mpf('1e-5'),mp.mpf('1e-6')]:
        q=high_Q(1+eta)
        coef=(q-3+mp.mpf('1.5')*eta)/(eta**2*mp.log(1/eta))
        assert mp.mpf('0.75')<coef<mp.mpf('1.2'), (eta,coef)
        n+=1
    for t in [30,80,250]:
        v=float(high_Q(t))
        assert abs(t*(v-2)-1)<0.04
        n+=1
    print('PASS',n,'deterministic diagnostics')
    print('Q(1), Q(2), Q(10):',*[mp.nstr(high_Q(t),17) for t in [1,2,10]])

if __name__ == '__main__':
    check()
