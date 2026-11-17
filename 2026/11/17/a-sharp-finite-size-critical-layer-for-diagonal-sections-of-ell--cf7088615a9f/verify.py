"""Numerical and analytic consistency checks for the finite-dimensional ell_p section crossover.
Run: python3 verify.py. Only Python standard library required.
"""
import math


def g(p):
    return math.sqrt(6 / math.pi * math.exp(3 * math.lgamma(1+1/p) - math.lgamma(1+3/p)))

def b(p):
    return 2 ** (0.5 - 1 / p)

def log_ratio(p):
    return math.log(g(p) / b(p))

def digamma(z):
    acc = 0.0
    for k in range(24):
        acc -= 1.0/(z+k)
    t = z+24
    return (acc + math.log(t)-1/(2*t)-1/(12*t**2)+1/(120*t**4)
            -1/(252*t**6)+1/(240*t**8)-5/(660*t**10))

def kappa(p):
    return math.exp(math.lgamma(5/p)+math.lgamma(1/p)-2*math.lgamma(3/p))-3

def root(a,b):
    fa=log_ratio(a)
    for _ in range(70):
        m=(a+b)/2
        if log_ratio(m)*fa>0: a=m
        else: b=m
    return (a+b)/2


def density(p,n,nx=700,nt=700):
    assert nx%2==nt%2==0
    bta=2*math.exp(math.lgamma(1+1/p))
    xmax=1.55
    dx=xmax/nx
    w=[]
    xs=[]
    for i in range(nx+1):
        x=i*dx
        w.append((1 if i in (0,nx) else 4 if i%2 else 2)*math.exp(-x**p)*dx/3/math.exp(math.lgamma(1+1/p)))
        xs.append(x)
    tmax=18
    dt=tmax/nt
    integral=0.0
    for j in range(nt+1):
        t=j*dt
        u=t/math.sqrt(n)
        phi=sum(w[i]*math.cos(u*xs[i]) for i in range(nx+1))
        integral+=(1 if j in (0,nt) else 4 if j%2 else 2)*phi**n
    return bta / math.pi * integral*dt/3

if __name__=='__main__':
    p0=root(26,27)
    assert abs(log_ratio(p0))<2e-14
    assert 26.2650<p0<26.2651
    ellp=(3*(digamma(1+3/p0)-digamma(1+1/p0))-2*math.log(2))/(2*p0*p0)
    kap=kappa(p0)
    assert -0.000761 <ellp<-0.000758
    assert -1.186<kap<-1.184
    cc=kap/(8*ellp)
    assert 195.00<cc<195.04
    print('p0:',p0,'Lprime:',ellp,'kappa:',kap,'C:',cc)
    for p in [p0-0.20, p0, p0+0.02]:
        for n in [150,600,1200]:
            actual=density(p,n)
            approx=g(p)*(1+kappa(p)/(8*n))
            assert abs(actual-approx)<0.02/n**2, (p,n,actual,approx)
            print(f'p={p:.7f}, n={n}, actual={actual:.11f}, remainder*n^2={(actual-approx)*n*n:.7f}')
    assert density(p0-0.2,1200)>b(p0-0.2)
    assert density(p0,1200)<b(p0)
    print('ALL NUMERICAL CONSISTENCY CHECKS PASSED')
