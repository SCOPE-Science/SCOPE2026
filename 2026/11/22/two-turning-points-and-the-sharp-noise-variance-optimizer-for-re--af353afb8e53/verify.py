"""Standalone finite checks for the reflection-symmetric three-bin statistic.

Uses only Python's standard library. The analytical proof of the global
shape theorem is contained in RESULT.md; this code checks its arithmetic.
"""
from math import pi, sqrt, asin, comb, factorial
from fractions import Fraction

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def v(a):
    return a*(5-9*a)

def cov(a):
    return a*(9*a-4)

def rho(a):
    return (9*a-4)/(5-9*a)

def G(r):
    return pi/2 - 2 + sqrt(max(0.,1-r*r)) + r*asin(max(-1.,min(1.,r)))

def H(r):
    return (5*r+4)*(1+r)*asin(r) - (5*r+3)*G(r)

def V(a):
    if a == 0:
        return 0.
    if a == .5:
        return 1-2/pi
    r=rho(a)
    return 2*v(a)*(1-4/pi + 2/pi*(sqrt(1-r*r)+r*asin(r)))

def bisect_root(lo,hi):
    flo=H(lo)
    check(flo*H(hi)<0, 'root not bracketed')
    for _ in range(110):
        mid=(lo+hi)/2
        if H(mid)*flo >0:
            lo=mid;flo=H(lo)
        else:
            hi=mid
    return (lo+hi)/2

# Direct categorical one-step covariance, independently of the closed form.
for num in range(1,20):
    a=Fraction(num,40); ps=(a,1-2*a,a)
    d1=(-1,1,0);d2=(0,-1,1)
    m1=sum(p*x for p,x in zip(ps,d1))
    m2=sum(p*x for p,x in zip(ps,d2))
    vv1=sum(p*(x-m1)**2 for p,x in zip(ps,d1))
    vv2=sum(p*(x-m2)**2 for p,x in zip(ps,d2))
    cc=sum(p*(x-m1)*(y-m2) for p,x,y in zip(ps,d1,d2))
    check(vv1==a*(5-9*a), 'edge variance 1')
    check(vv2==a*(5-9*a), 'edge variance 2')
    check(cc==a*(9*a-4), 'edge covariance')
    check(vv1**2-cc**2==9*a*a*(1-2*a), 'covariance determinant')

for k in range(1,100):
    rr=-.8+1.8*k/100
    quadratic=15+4*rr-10*rr*rr
    check(quadratic>0,'convexity numerator')
    actual_hpp=(1+rr)*quadratic/(1-rr*rr)**1.5
    check(actual_hpp>0,'convexity second derivative')

r1=bisect_root(-.65,-.64)
r2=bisect_root(.37,.39)
a1=(5*r1+4)/(9*(1+r1))
a2=(5*r2+4)/(9*(1+r2))
check(abs(a1-0.240033242514835856)<2e-14,'global maximizing mass')
check(abs(a2-0.474914471760339773)<2e-14,'local minimizing mass')
check(abs(V(a1)-0.684872023385757119)<2e-14,'peak variance')
check(abs(V(a2)-0.282216149055267041)<2e-14,'valley variance')
check(V(.25)>V(.5)>V(0),'global endpoint comparison')
check(V(a1)>V(.25),'interior maximum vs trial')
for a,b in [(0.,a1),(a1,a2),(a2,.5)]:
    mids=[a+(b-a)*i/10 for i in range(1,10)]
    vals=[V(x) for x in mids]
    if a==0.:check(all(vals[i+1]>vals[i] for i in range(8)),'first increasing interval')
    elif b==.5:check(all(vals[i+1]>vals[i] for i in range(8)),'last increasing interval')
    else:check(all(vals[i+1]<vals[i] for i in range(8)),'middle decreasing interval')

# Exact (not Monte Carlo) finite-multinomial sums at rational profiles.
def exact_variance(N, numerator, denominator):
    a=Fraction(numerator,denominator)
    p=(a,1-2*a,a)
    m1=N*(p[1]-p[0]);m2=N*(p[2]-p[1])
    EX=Fraction(0);EX2=Fraction(0);prob_sum=Fraction(0)
    # multinomial coefficient in integers and probability weight in rationals
    denom_power=denominator**N
    w=(numerator,denominator-2*numerator,numerator)
    for i in range(N+1):
      for j in range(N-i+1):
        k=N-i-j
        wt=Fraction(comb(N,i)*comb(N-i,j)*w[0]**i*w[1]**j*w[2]**k,denom_power)
        T=abs(j-i-m1)+abs(k-j-m2)
        EX+=wt*T
        EX2+=wt*T*T
        prob_sum+=wt
    check(prob_sum==1,'exact probability normalization')
    return EX2-EX**2

for n in [8,16,32,64,96]:
    variance=exact_variance(n,1,4)
    check(variance>0,'positive finite variance')
    if n==96:
        check(abs(float(variance/n)-V(.25))<.03,'finite moments approach Gaussian asymptotic')
print('PASS:',checks,'deterministic assertions; peaks',format(a1,'.15f'),format(a2,'.15f'))
