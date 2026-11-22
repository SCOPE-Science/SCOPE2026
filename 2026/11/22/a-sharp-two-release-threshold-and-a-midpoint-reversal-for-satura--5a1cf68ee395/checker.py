"""Standalone supplementary checks for a finite-horizon two-release mating-pressure theorem.

Uses only the Python standard library; the proof is analytic and is not replaced
by finite sampling.
"""
import math
import random


def score(a, b, mu, T, tau):
    """Exact integrated sterile-mating fraction (dimension of time)."""
    q = math.exp(-mu * T)
    y = math.exp(-mu * tau)
    return (math.log1p(a) - math.log1p(a*y)
            + math.log1p(b+a*y)
            - math.log1p(q*(a+b/y))) / mu


def optimizer(a, b, mu, T):
    q = math.exp(-mu*T)
    critical = math.log(2+(b+1)/a)/mu
    if T <= critical:
        return 0.0
    y = q + math.sqrt(q*q+q*(b+1)/a)
    return -math.log(y)/mu


def numerical_quadrature(a,b,mu,T,tau,n=1000):
    """An independent Simpson quadrature, split at the impulse time."""
    def integrate(l,r,after):
        if r<=l: return 0.0
        h=(r-l)/n
        def f(t):
            s=a*math.exp(-mu*t)
            if after: s+=b*math.exp(-mu*(t-tau))
            return s/(1+s)
        return h/3*(f(l)+f(r)+4*sum(f(l+(2*k+1)*h) for k in range(n//2))
                         +2*sum(f(l+2*k*h) for k in range(1,n//2)))
    return integrate(0,tau,False)+integrate(tau,T,True)


def golden_argmax(fun,l,r):
    phi=(math.sqrt(5)-1)/2
    c=r-phi*(r-l); d=l+phi*(r-l)
    fc=fun(c);fd=fun(d)
    for _ in range(115):
        if fc<fd:
            l=c;c=d;fc=fd;d=l+phi*(r-l);fd=fun(d)
        else:
            r=d;d=c;fd=fc;c=r-phi*(r-l);fc=fun(c)
    return (l+r)/2


def run():
    random.seed(440044)
    count=0
    for _ in range(1200):
        a=math.exp(random.uniform(-2.2,2.2))
        b=math.exp(random.uniform(-2.2,2.2))
        mu=math.exp(random.uniform(-1.2,1.2))
        T=random.uniform(0.2,9)/mu
        t=optimizer(a,b,mu,T)
        critical=math.log(2+(b+1)/a)/mu
        assert 0<=t<T+1e-12
        assert (t>0)==(T>critical)
        count+=2
        # independent direct quadrature, away from underflow/small intervals
        if _<70:
            for test_t in (0.0, T/3, t, T):
                assert abs(score(a,b,mu,T,test_t)-numerical_quadrature(a,b,mu,T,test_t))<2e-8*max(1,T)
                count+=1
        # global maximum on a finite interval and against an independent 1D optimizer
        st=score(a,b,mu,T,t)
        for k in range(151):
            tau=T*k/150
            assert st+1e-10*max(1,T)>=score(a,b,mu,T,tau)
            count+=1
        num=golden_argmax(lambda z:score(a,b,mu,T,z),0.0,T)
        assert st+1e-9*max(1,T)>=score(a,b,mu,T,num)
        count+=1
        q=math.exp(-mu*T)
        y=math.exp(-mu*t)
        if T>critical:
            assert abs(a*y*y-2*a*q*y-q*(b+1)) < 1e-11*max(1,a,b)
            count+=1
            if a<=b+1:
                assert t<T/2+1e-11
            else:
                Tm=2*math.log(2*a/(a-b-1))/mu
                assert Tm>critical
                if T<Tm-1e-8/mu:
                    assert t<T/2
                elif T>Tm+1e-8/mu:
                    assert t>T/2
            count+=1
    a=4.;b=1.;mu=1.
    Tc=math.log(5/2); Tm=math.log(16)
    assert abs(optimizer(a,b,mu,Tm)-math.log(4))<1e-13
    assert abs(optimizer(a,b,mu,math.log(64))-math.log(64/(1+math.sqrt(33))))<1e-13
    assert abs(Tc-math.log(2+(b+1)/a))<1e-13
    count+=3
    # Verify derivative predicted for optimal timing from both sides of a horizon perturbation.
    for _ in range(200):
        a=math.exp(random.uniform(-1.5,1.5));b=math.exp(random.uniform(-1.5,1.5));mu=1.
        T=math.log(2+(b+1)/a)+random.uniform(0.1,8)
        t=optimizer(a,b,mu,T)
        y=math.exp(-t); r=(b+1)/a
        predicted=(2*y+r)/(2*(y+r))
        eps=1e-5
        observed=(optimizer(a,b,mu,T+eps)-optimizer(a,b,mu,T-eps))/(2*eps)
        assert 0.5<predicted<1 and abs(predicted-observed)<5e-8
        count+=2
    print('PASS:',count,'supplementary assertions; analytic proof remains necessary')


if __name__=='__main__':
    run()
