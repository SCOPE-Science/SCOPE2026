"""Exact Fourier and numerical asymptotic checks for capped Hamming metrics.
Run: python check.py (Python 3 standard library)."""
from itertools import product
from math import comb, cos, pi, log, expm1, exp, isclose

def kraw(n,q,k,j):
    return sum((-1)**a*comb(k,a)*comb(n-k,j-a)*(q-1)**(j-a)
               for a in range(max(0,j-(n-k)), min(k,j)+1))

def eig(n,q,k,p):
    v=-1.
    for j in range(1,4):
        v+=expm1(p*log(j/4))*kraw(n,q,k,j)
    return v*exp(p*log(4))

def critical(n,q):
    # β in (0,1] unless cap 4 coincides with ordinary Hamming at n=4.
    if max(eig(n,q,k,1) for k in range(1,n+1))<=1e-9: return 1., tuple(k for k in range(1,n+1) if abs(eig(n,q,k,1))<1e-8)
    lo,hi=0.,1.
    for _ in range(72):
        mid=(lo+hi)/2
        if max(eig(n,q,k,mid) for k in range(1,n+1))<=0:lo=mid
        else:hi=mid
    b=(lo+hi)/2
    m=max(eig(n,q,k,b) for k in range(1,n+1))
    modes=tuple(k for k in range(1,n+1) if abs(eig(n,q,k,b)-m)<1e-6)
    return b,modes

def P(c,s):
    return -1/6+c*s/2-c*c*s*(s-1)/2+c*c*c*s*(s-1)*(s-2)/6

def mu(c):
    vals=[P(c,s) for s in range(250)]
    m=min(vals)
    return -m,tuple(s for s,v in enumerate(vals) if abs(v-m)<1e-8)

# Direct additive characters and exact Krawtchouk multiplicities.
for q,n in [(2,4),(3,4),(4,4),(3,5)]:
    elems=list(product(range(q),repeat=n))
    for k in range(1,n+1):
        a=(1,)*k+(0,)*(n-k)
        for p in (.375,1.,1.25):
            direct=sum(min(sum(x!=0 for x in v),4)**p * cos(2*pi*sum(x*y for x,y in zip(a,v))/q) for v in elems)
            formula=eig(n,q,k,p)
            assert abs(direct-formula)<2e-7,(q,n,k,p,direct,formula)
print('FOURIER_CHECKS_PASSED direct_cases=51')

# Verify limiting Charlier polynomial and its sharp half-ratio transition.
for c in (.1,.3,.49,.5,.51,.6,.8,1.,1.3,2.,3.):
    v,s=mu(c)
    if c<=.5: assert abs(v-1/6)<1e-10, (c,v,s)
    else: assert v>1/6, (c,v,s)
    print('CHARLIER',c,'min',round(v,8),'critical_codim',s)

# Check finite-n transition and independent fixed n/q asymptotics.
for c in (.3,.5,.6,1.,2.):
    for n in (100,300,1000):
        q=max(3,round(c*n))
        b,modes=critical(n,q)
        asym,_=mu(c)
        target=1/(asym*log(4/3))
        measured=b*n**3
        assert abs(measured/target-1)<.22,(c,n,measured,target,modes)
        if n==1000:
            print('CROSSOVER',c,n,q,round(measured,7),round(target,7),'critical_codim',tuple(n-k for k in modes))
# Exact stabilization is a finite-q equality once the full frequency is critical.
for n in (100,300,1000):
    universal, modes=critical(n,2)
    assert modes==(n,)
    for q in (3, max(3, round(.3*n)), max(3, round(.45*n))):
        v, crit=critical(n,q)
        assert abs(v-universal)<5e-14 and crit==(n,), (n,q,v,universal,crit)
print('LOW_RATIO_EXACT_STABILIZATION_CHECKS_PASS')
for n in (5,6,10):
    c=(n-2)*log(4/3)-log(2)
    for q in (200,1000):
        b,modes=critical(n,q)
        assert modes==(n-2,), (n,q,modes)
        assert abs(b*q*q*c-1)<.12,(n,q,b*q*q*c)
    print('LARGE_ALPHABET',n,'observed',round(b*q*q,8),'target',round(1/c,8))
for q in (2,3,5):
    for n in (80,300,1000):
        b,modes=critical(n,q)
        target=6/log(4/3)
        assert abs(b*n**3/target-1)<.25,(q,n,b*n**3,target)
print('CAPPED_HAMMING_CHARLIER_CHECKS_PASS')
