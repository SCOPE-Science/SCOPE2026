"""Finite exact and numerical consistency tests for mode-locking period statistics.
Scientific justification of the infinite law is the analytical proof; this code
checks selected rational plateau formulas and the arithmetic normalization.
"""
from fractions import Fraction
from math import floor, gcd, expm1, exp, cosh, pi

def phi(n):
    return sum(gcd(a,n)==1 for a in range(1,n+1))

def plateau(lam,p,q):
    if q==1:
        return Fraction(0),1-lam
    c=1+sum((floor(k*p/q)-floor((k-1)*p/q))*lam**(k-1) for k in range(2,q))
    base=(1-lam)*c/(1-lam**q)
    return base,base+(1-lam)**2*lam**(q-1)/(1-lam**q)

def rational_cycle(lam,delta,q):
    # Exact contraction itinerary on a periodic orbit approximated by 90 iterates.
    x=Fraction(0)
    for _ in range(90):
        raw=lam*x+delta
        x=raw-floor(raw)
    # Get q symbolic digits and algebraically solve the affine return equation.
    start=x
    digits=[]
    for _ in range(q):
        raw=lam*x+delta
        d=floor(raw);digits.append(d)
        x=raw-d
    intercept=sum((delta-d)*lam**(q-1-j) for j,d in enumerate(digits))
    root=intercept/(1-lam**q)
    assert 0<=root<1,('root',q,root)
    x=root
    for d in digits:
        raw=lam*x+delta
        assert floor(raw)==d
        x=raw-d
    assert x==root
    for r in range(1,q):
        if q%r==0:
            x=root
            for _ in range(r): x=(lam*x+delta)%1
            assert x!=root,('nonprimitive',q,r)

for denominator in range(2,13):
    widths=set()
    for p in range(1,denominator):
        if gcd(p,denominator)!=1:continue
        l,r=plateau(Fraction(1,2),p,denominator)
        assert 0<=l<r<=1,(p,denominator,l,r)
        widths.add(r-l)
        rational_cycle(Fraction(1,2),(l+r)/2,denominator)
    assert len(widths)==1
    assert widths.pop()==Fraction(1,4)*Fraction(1,2)**(denominator-1)/(1-Fraction(1,2)**denominator)

# Lambert series coefficient identity (formal power series through degree 120).
for m in range(1,121):
    assert sum(phi(d) for d in range(1,m+1) if m%d==0)==m

# Prove a rational truncation of the phi-weighted plateau probabilities.
L=Fraction(1,2)
partial=sum(phi(q)*(1-L)**2*L**(q-1)/(1-L**q) for q in range(1,42))
assert partial<1
assert Fraction(0)<1-partial<Fraction(1,2**35)

# Numerically check the predicted scaled-period weak law and limiting mean.
def lim_cdf(z):
    n=4096
    step=z/n
    def f(t): return 1.0 if t==0 else t/expm1(t)
    total=f(0)+f(z)
    for j in range(1,n): total+=(4 if j%2 else 2)*f(j*step)
    return 6/pi**2*total*step/3

zeta3=sum(m**(-3) for m in range(1,50001)) + 1/(2*50000**2)
lim_mean=12*zeta3/pi**2
for h in [0.08,0.04,0.02,0.01]:
    N=int(22/h)
    vals=[0.0]+[float(phi(q))*(2*(cosh(h)-1))/expm1(h*q) for q in range(1,N+1)]
    assert abs(sum(vals)-1)<1e-8,(h,sum(vals))
    mean=sum(h*q*vals[q] for q in range(1,N+1))
    assert abs(mean-float(lim_mean))<0.3,(h,mean)
    for z in [0.5,1.0,2.0]:
        F=sum(vals[:int(z/h)+1])
        assert abs(F-lim_cdf(z))<0.11,(h,z,F)
print('VERIFY_OK exact plateau checks q=2..12, cycle periods, totient identity m<=120, rational tails and numerical weak-limit consistency')
