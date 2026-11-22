#!/usr/bin/env python3
"""Reproduce exact cross-covariance/jackknife identities and sparse limits.
Requires Python standard library; optional numpy/scipy for stochastic cross-checks.
"""
import math, itertools, random, statistics
from fractions import Fraction

checks=0
def ck(ok,msg=''):
    global checks
    if not ok: raise AssertionError(msg)
    checks+=1

def exact_counts(n,a,b,c):
    """Return (f,Q,s0,T_base) from exact table counts, where T=sign(f2)*T_base.
    a and b are the respective marginal-one counts, c the joint-one count.
    """
    assert n>=3 and 0<=c<=min(a,b) and a+b-c<=n
    f=Fraction(n*c-a*b,n*(n-1))
    g0=Fraction(c,2*(n-1))
    gx=Fraction(c-b,2*(n-1))
    gy=Fraction(c-a,2*(n-1))
    gxy=Fraction(n+c-a-b,2*(n-1))
    Q=((n-a-b+c)*(g0-f)**2 +(a-c)*(gx-f)**2
       +(b-c)*(gy-f)**2+c*(gxy-f)**2)
    s02=Fraction(4*(n-1),(n-2)**2)*Q
    tb=math.sqrt(n)*float(f)/math.sqrt(float(s02)) if s02>0 else None
    return f,Q,s02,tb

def direct(xs,ys):
    n=len(xs)
    h=lambda i,j: Fraction((xs[i]-xs[j])*(ys[i]-ys[j]),2)
    f=sum((h(i,j) for i in range(n) for j in range(n) if i!=j),Fraction(0))/ (n*(n-1))
    g=[sum((h(i,j) for j in range(n) if j!=i),Fraction(0))/(n-1) for i in range(n)]
    Q=sum(((v-f)**2 for v in g),Fraction(0))
    return f,Q,Fraction(4*(n-1),(n-2)**2)*Q

for n in range(3,7):
    for labels in itertools.product((0,1,2,3),repeat=n):
        xs=[v&1 for v in labels]; ys=[(v>>1)&1 for v in labels]
        a=sum(xs);b=sum(ys);c=sum(x*y for x,y in zip(xs,ys))
        f,Q,s02,t=exact_counts(n,a,b,c)
        f2,Q2,s022=direct(xs,ys)
        ck((f,Q,s02)==(f2,Q2,s022),f'exact n={n} labels={labels}')

# On c=0 the exact closed form of the jackknife quadratic holds.
for n in (10,20,40,100,1000):
    for a in range(1,min(n//2,12)+1):
        for b in range(1,min(n-a,12)+1):
            f,Q,s02,t=exact_counts(n,a,b,0)
            qwant=Fraction(a*b, (n-1)**2)*(Fraction(a+b,4)-Fraction(a*b,n))
            ck(Q==qwant, 'closed Q c=0')
            if Q>0:
                twant=(n-2)*math.sqrt(n*a*b)/(n*math.sqrt(n-1)*math.sqrt(a+b-4*a*b/n))
                ck(math.isclose(-t,twant,rel_tol=1e-12,abs_tol=1e-12), 'closed T c=0')

# The limit law at theta=1/2, alpha=.05, has an atom at +infty with weight exp(-1).
theta=.5
z=1.6448536269514722
kcrit=next(k for k in range(1,50) if (k-theta)/math.sqrt(k)>z)
ck(kcrit==4)
p0=math.exp(-theta)
pgt=1-p0*sum(theta**k/math.factorial(k) for k in range(kcrit))
alpha_limit=math.exp(-2*theta)+(1-p0)*pgt
ck(abs(alpha_limit-0.3685686509430986)<1e-14)
# Finite-n count sequences with k=0 and a,b close to n p: statistic predicts divergent growth.
for n in (10**3,10**4,10**5,10**6):
    p=math.sqrt(theta/n); a=round(n*p);b=a
    _,_,_,tb=exact_counts(n,a,b,0)
    ck(abs((-tb)/math.sqrt(n*p/2)-1)<0.09)

# Conditional critical-scale for positive overlap k: sign(f2)*T_base tends (k-theta)/sqrt(k).
for k in range(1,8):
    for n in (10**5,10**6,10**7):
        a=round(math.sqrt(theta*n)); b=a
        _,_,_,tb=exact_counts(n,a,b,k)
        ck(abs(tb-(k-theta)/math.sqrt(k)) < 0.2 if n==10**5 else abs(tb-(k-theta)/math.sqrt(k))<0.06)

# Light seeded Monte Carlo of finite rejection rates.
try:
 import numpy as np
 rng=np.random.default_rng(8675309)
 for n, reps, theta in [(2000,12000,.5),(20000,10000,.5)]:
    p=math.sqrt(theta/n)
    # Multinomial 2x2 counts; independent samples in two halves
    rows=rng.multinomial(n,[(1-p)**2,p*(1-p),p*(1-p),p*p],size=(reps,2))
    def batch_t(r):
        a=r[:,1]+r[:,3]; b=r[:,2]+r[:,3]; c=r[:,3]
        f=(n*c-a*b)/(n*(n-1))
        g0=c/(2*(n-1)); gx=(c-b)/(2*(n-1)); gy=(c-a)/(2*(n-1)); gxy=(n+c-a-b)/(2*(n-1))
        Q=(n-a-b+c)*(g0-f)**2+(a-c)*(gx-f)**2+(b-c)*(gy-f)**2+c*(gxy-f)**2
        return f, 4*(n-1)/(n-2)**2*Q
    f1,s02=batch_t(rows[:,0,:]); f2,_=batch_t(rows[:,1,:])
    t=np.sign(f2)*np.sqrt(n)*f1/np.sqrt(s02)
    rejection=np.mean(t>z)
    print('Monte Carlo n',n,'reps',reps,'size',rejection,'limit',alpha_limit)
    ck(abs(rejection-alpha_limit)<.065)
except ImportError:
 print('numpy unavailable; optional simulation skipped')

# Exact finite-n rejection size: sum over all four-cell contingency tables in both halves.
# The second half contributes only sign(f2), so its distribution factors from first-half tails.
for n, expected in ((20,0.03031332282645029),(40,0.08109219386009066),(60,0.17443530520706607)):
    p=math.sqrt(.5/n)
    probs=((1-p)**2,p*(1-p),p*(1-p),p*p)
    logs=[math.log(t) for t in probs]
    fac=[math.lgamma(i+1) for i in range(n+1)]
    plus=minus=above=below=0.0
    for n00 in range(n+1):
        for n10 in range(n-n00+1):
            for n01 in range(n-n00-n10+1):
                n11=n-n00-n10-n01
                w=math.exp(fac[n]-fac[n00]-fac[n10]-fac[n01]-fac[n11]
                    +n00*logs[0]+n10*logs[1]+n01*logs[2]+n11*logs[3])
                f,_,_,tb=exact_counts(n,n10+n11,n01+n11,n11)
                if f>0: plus+=w
                if f<0: minus+=w
                if tb is not None and tb>z:above+=w
                if tb is not None and tb<-z:below+=w
    exact_rej=above*plus+below*minus
    ck(abs(exact_rej-expected)<2e-12,'exact multinomial rejection probability')
    print('Exact finite-n size',n,exact_rej)
print('PASS assertions:',checks)
print('critical 5% rejection:',repr(alpha_limit),'theta:',theta,'kcrit:',kcrit)
