"""Standalone verification of the two-level hysteresis return tower.
Run: python3 check.py (Python standard library only).
Finite checks supplement, but do not replace, the analytical proof.
"""
from fractions import Fraction as Q
from math import log, isclose

def setup(a,b):
    assert Q(0)<a<Q(1) and b>1 and a*(b+1)>1
    mu=a/(1+a)
    q=1/(1+a)
    c=(1+a)*b+a
    U=c/(1+a)
    assert mu<q<U and c*mu==a*U and c*q==U and a*q==mu
    return mu,q,U,c

def F(z,s,a,b):
    lam=-a
    alpha=b+a
    z1=lam*z+alpha*s
    r=s+z1-z
    return z1, (r if abs(r)<=1 else Q(0))

def check_exact(a,b):
    mu,q,U,c=setup(a,b)
    grid=lambda l,r,k:[l+(r-l)*Q(i,k) for i in range(1,k)]
    for sign in [1,-1]:
        for x in [mu,q]+grid(mu,q,313):
            z1,s1=F(sign*x,Q(0),a,b)
            assert (z1,s1)==(-sign*a*x,-sign*(1+a)*x)
            z2,s2=F(z1,s1,a,b)
            assert (z2,s2)==(-sign*c*x,Q(0))
        for x in [U]+grid(q,U,313):
            assert F(sign*x,Q(0),a,b)==(-sign*a*x,Q(0))
    print('PASS exact two-stage and one-stage transitions for',a,b)

for a,b in [(Q(1,2),Q(5,3)),(Q(2,3),Q(4,3)),(Q(4,5),Q(5,4)),(Q(3,5),Q(3,2))]:
    check_exact(a,b)

a,b=Q(1,2),Q(5,3)
mu,q,U,c=setup(a,b)
assert (mu,q,U,c)==(Q(1,3),Q(2,3),Q(2),Q(3))
ell=log(float(1/a)); h=log(float(c)); K=h+2*ell
prob0=(h+ell)/K
mean_abs=(1-float(a))/K
moment2=(1-float(a*a))/(2*K)
assert isclose(prob0+ell/K,1,abs_tol=1e-14)
print('PASS normalizer, atom probability, moments, parameter inversion')
a_recovered=.5
K_recovered=(1-a_recovered)/mean_abs
b_recovered=(__import__('math').exp(K_recovered-2*log(1/a_recovered))-a_recovered)/(1+a_recovered)
assert isclose(b_recovered,float(b),rel_tol=1e-14)

# The section orbit is an irrational circle rotation (angle log 3, length log 6).
# Iterate the *two-dimensional original system* and compare the physical-time law.
z,s=.5,0.0
n=150_000
zcount=0
maximum_discrepancy=0.
abssum=0.
squaresum=0.
for j in range(n):
    maximum_discrepancy=max(maximum_discrepancy,abs(zcount-j*prob0))
    zcount+=abs(s)<1e-13
    abssum+=abs(s)
    squaresum+=s*s
    z1=-.5*z+(13/6)*s
    t=s+z1-z
    z,s=z1,(t if abs(t)<=1 else 0.)
assert abs(zcount/n-prob0)<.002,(zcount/n,prob0)
assert abs(abssum/n-mean_abs)<.002,(abssum/n,mean_abs)
assert abs(squaresum/n-moment2)<.002,(squaresum/n,moment2)
assert maximum_discrepancy<1,maximum_discrepancy
print('PASS bounded original-time reset discrepancy:',maximum_discrepancy)
print('PASS time-average observable numerical check:',zcount/n,abssum/n,squaresum/n)
# Independent quadrature of the proposed stationary integral against F.
# Integrating in logarithmic coordinates avoids ill-conditioned 1/x weights.
from math import exp
samples=5000
lm,lq,lU=map(lambda z:log(float(z)),(mu,q,U))
def fl(x,s):
    zz=-float(a)*x+(float(b)+float(a))*s
    rr=s+zz-x
    return zz,rr if abs(rr)<=1 else 0.
def quad_inv(test):
    lhs=rhs=0.
    for sig in (-1.,1.):
        for left,right,stage in ((lm,lq,0),(lq,lU,0),(lm,lq,1)):
            step=(right-left)/samples
            for j in range(samples):
                xx=exp(left+(j+.5)*step)
                if stage==0: pos=(sig*xx,0.)
                else: pos=(-sig*float(a)*xx,-sig*(1+float(a))*xx)
                lhs+=step*test(*pos)
                rhs+=step*test(*fl(*pos))
    return lhs/(2*K),rhs/(2*K)
for g in (lambda x,s: x*x+2*x*s+s*s,lambda x,s:x**3+s**3,
          lambda x,s: x*x*s+3*s*x+7*s*s):
    aa,bb=quad_inv(g)
    assert abs(aa-bb)<.0002,(aa,bb)
print('PASS quadrature invariance for three independent test observables')
