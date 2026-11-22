"""Reproducibility checks for the rare-zero Poisson Stein ratio theorem.

Run: python3 verify.py
Uses only Python's standard library. Numerical finite checks supplement the proof.
"""
import math
from fractions import Fraction
from statistics import NormalDist

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def ratio_via_means(counts, u):
    n=len(counts)
    sx=sum(counts)
    if sx == 0:
        return None
    mean_x = Fraction(sx,n)
    mean_xf = sum(x*u**x for x in counts)/n
    mean_fplus = sum(u**(x+1) for x in counts)/n
    return mean_xf/(mean_x*mean_fplus)

def ratio_via_low_counts(counts, u):
    sx=sum(counts)
    if sx==0:
        return None
    return sum(x*u**(x-1) if x else 0 for x in counts)/(Fraction(sx,len(counts))*sum(u**x for x in counts))

for u in (Fraction(1,2),Fraction(1,3),Fraction(1,7)):
    for counts in ((0,1,2),(1,1,3),(0,0,1,5),(2,3,5,8),(0,0,0),(0,2,4)):
        a,b=ratio_via_means(counts,u),ratio_via_low_counts(counts,u)
        check(a==b,'finite exact ratio equality')

# Independent covariance-matrix calculation for the influence variance and
# second-order delta-method mean correction: Poisson raw moments obtained from pgf.
def moments(mu,u):
    G=math.exp(mu*(u-1))
    H=math.exp(mu*(u*u-1))
    meanX=mu
    A=mu*u*G
    B=u*G
    vX=mu
    # E[X^2 u^(2X)]=(mu*u^2+mu^2*u^4)*H
    vA=(mu*u*u+mu*mu*u**4)*H-A*A
    vB=u*u*H-B*B
    cXA=(mu*u+mu*mu*u*u)*G-mu*A
    cXB=mu*u*u*G-mu*B
    cAB=mu*u**3*H-A*B
    return (vX,vA,vB,cXA,cXB,cAB,A,B)

def independent_variance_and_bias(mu,u):
    vX,vA,vB,cXA,cXB,cAB,A,B=moments(mu,u)
    V=(vX/mu**2+vA/A**2+vB/B**2-2*cXA/(mu*A)+2*cXB/(mu*B)-2*cAB/(A*B))
    C=(vX/mu**2+vB/B**2-cXA/(mu*A)+cXB/(mu*B)-cAB/(A*B))
    return V,C

def closed(mu,u):
    E=math.exp(mu*(1-u)**2)
    return ((1-u)**2+1/mu)*E-1/mu, (1-u)*E

for mu in (.25,.8,1.7,3.,5.,8.,10.):
    for u in (.12,.33,.52,.82,.96):
        v,b=independent_variance_and_bias(mu,u)
        vc,bc=closed(mu,u)
        check(abs(v-vc)<1e-9*max(1,abs(vc)), 'variance formula')
        check(abs(b-bc)<1e-9*max(1,abs(bc)), 'second-order mean coefficient')

# Independent direct Poisson series for the influence-function variance.
for mu in (.7,1.5,3.5,7.0):
    for u in (.2,.5,.8):
        G=math.exp(mu*(u-1));p=math.exp(-mu)
        vv=0.; mass=0.
        for x in range(120):
            psi=(x*u**(x-1)/mu-u**x)/G-x/mu+1 if x>0 else -1/G+1
            vv+=p*psi*psi;mass+=p
            p*=mu/(x+1)
        check(abs(mass-1)<1e-13,'series mass')
        check(abs(vv-closed(mu,u)[0])<1e-9*max(1,vv),'direct Poisson influence variance')

# Verify exact low-count expected error quantities used in the proof.
# N0 expectation 1, N1 expectation log n; remainder terms are controlled by
# E[R]/mu = exp(mu*u)-1 and E[S]/(mu*u) = (exp(mu*u)-1-mu*u)/(mu*u).
for n in (500,2000,10000,100000,1000000,10**10):
    mu=math.log(n);u=mu**-3
    p0=math.exp(-mu);p1=mu*p0
    check(abs(n*p0-1)<1e-11,'critical zero mean')
    check(abs(n*p1-mu)<1e-10,'critical ones mean')
    er=math.expm1(mu*u)
    es=(math.expm1(mu*u)-mu*u)/(mu*u)
    check(er>0 and es>0,'error terms nonnegative')
    check(er<.06,'numerical illustration of remainder control')
    v,b=closed(mu,u)
    check(v/n>0 and b/n>0,'normal calibration well-defined')

z=NormalDist().inv_cdf(.975)
low=2-z
up=2+z
check(Fraction(1,25)<low<Fraction(1,24),'lower cutoff between reciprocal integers')
check(up>1,'upper cutoff accepts all finite reciprocal atoms')
for k in range(1,1001):
    reject=(abs(1/k-2)>z)
    check(reject==(k>=25),'exact reciprocal-atom rejection classification')
# P(Pois(1)>=25) computed by direct positive series, avoiding cancellation.
p0=math.exp(-1.)
p=p0
sumtail=0.
for k in range(1,125):
    p/=k
    if k>=25:
        sumtail+=p
size=p0+sumtail
check(abs(size-0.36787944117144233)<1e-15,'5 percent asymptotic actual size')
check(0.36<size<0.37,'severe size inflation')
print('PASS:',checks,'assertions')
print('exact critical limit: P(K=0)+P(K>=25) =',format(size,'.16g'))
print('null variance and bias formulas verified independently')
print('finite computations supplement, not replace, the infinite-limit proof')
