"""Standalone finite checks of a critical multi-defect zero-range stationary law.
Run: python check.py (Python 3.10+, standard library only).
This verifies finite identities and convergence diagnostics; it is not an infinite-size proof.
"""
import math

def compositions(n,k):
    if k==1:
        yield (n,)
        return
    for t in range(n+1):
        for rem in compositions(n-t,k-1):
            yield (t,)+rem

def logbinom(n,k):
    return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)

def lweight(t,M,r,N,q):
    return logbinom(t+r-1,r-1)+logbinom(N-t+M-1,M-1)-t*math.log(q)

def ratio(t,M,r,N,q):
    return (t+r)*(N-t)/((t+1)*q*(N-t+M-1))

def mode(M,r,N,q):
    a=1-q
    b=N-r-q*(N+M-2)
    c=r*N-q*(N+M-1)
    return math.ceil((b+math.sqrt(b*b+4*a*c))/(2*a))

def distribution(M,r,N,q):
    logw=[lweight(t,M,r,N,q) for t in range(N+1)]
    ma=max(logw)
    w=[math.exp(y-ma) for y in logw]
    z=sum(w)
    return [x/z for x in w]

def binomial_ratio(t,r,k):
    if k>t:return 0.
    return math.exp(sum(math.log1p(-k/(t+i)) for i in range(1,r)))

checks=0
def ck(x,label):
    global checks
    assert x,label
    checks+=1

# Direct incoming/outgoing generator-balance checks on small directed rings.
for M,r,N,q in [(2,2,3,0.4),(3,2,2,0.55),(3,3,2,0.3)]:
    rates=[1.]*M+[q]*r
    configs=list(compositions(N,len(rates)))
    w={n:math.prod(a**(-k) for a,k in zip(rates,n)) for n in configs}
    z=sum(w.values()); p={n:y/z for n,y in w.items()}
    for n in configs:
        outgoing=p[n]*sum(a for a,k in zip(rates,n) if k)
        incoming=0.
        for i in range(len(rates)):
            j=(i+1)%len(rates)
            if n[j]>0:
                m=list(n);m[i]+=1;m[j]-=1
                incoming+=p[tuple(m)]*rates[i]
        ck(abs(incoming-outgoing)<1e-12,'stationary master equation')
    ck(abs(sum(p.values())-1.)<1e-12,'probability normalization')
    marginal={t:sum(y for n,y in p.items() if sum(n[M:])==t) for t in range(N+1)}
    law=distribution(M,r,N,q)
    for t in range(N+1):ck(abs(marginal[t]-law[t])<1e-11,'defect-total combinatorics')

# The exact log-concave weight ratio, mode, and finite critical scaling.
for M,r in [(100,4),(350,10),(1400,30),(10000,70),(100000,150)]:
    rho=1.5;q=rho/(1+rho);N=int(rho*M)
    for t in [0,1,3,10,N//4,N//2,N-1]:
        if t<N:
            ck(abs(math.exp(lweight(t+1,M,r,N,q)-lweight(t,M,r,N,q))/ratio(t,M,r,N,q)-1)<1e-9,'adjacent ratio')
    p=distribution(M,r,N,q)
    ck(abs(sum(p)-1)<3e-13,'finite exact law')
    m=mode(M,r,N,q)
    ck(m==max(range(len(p)),key=p.__getitem__),'quadratic modal root')
    mean=sum(t*pr for t,pr in enumerate(p))
    var=sum((t-mean)**2*pr for t,pr in enumerate(p))
    sigma2=rho*(1+rho)
    if M>=10000:
        ck(abs(mean/math.sqrt(sigma2*M*r)-1)<0.12,'subextensive total scale')
        ck(abs(var/(sigma2*M/2)-1)<0.21,'Gaussian fluctuation variance')

# Exact conditional weak-composition tail ratios: exponential-site limit and
# fixed-order factorial moments for the extreme-value Poisson law.
for t,r in [(100000000,2000),(200000000,3000)]:
    scale=t/r
    for a in (0.5,1.,2.):
        k=math.floor(a*scale)
        ck(abs(binomial_ratio(t,r,k)-math.exp(-a))<0.01,'one-site exponential tail')
    for j in (1,2,3):
        x=0.5
        k=math.floor(scale*(math.log(r)+x))
        falling=math.prod(r-h for h in range(j))
        facmom=falling*binomial_ratio(t,r,j*(k+1))
        ck(abs(facmom/math.exp(-j*x)-1)<0.16,'extreme count factorial moment')
print('PASS',checks,'finite and asymptotic diagnostic checks')
