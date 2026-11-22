"""Numerical and algebraic checks for weighted circle/regular-polygon perimeter deviation.
All statements for infinite parameter ranges require the analytical proof in RESULT.md.
This program checks exact simplifications, independently sampled geometry, and
finite-parameter behavior; it is not a stand-alone infinite proof.
"""
import math
from fractions import Fraction

PI=math.pi
checks=0

def check(cond, message):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(message)

def close(x,y,rtol=1e-8,atol=1e-9):
    return abs(x-y)<=atol+rtol*max(abs(x),abs(y))

def dev_formula(n,p,radius):
    a=PI/n
    q=p/(p-1)
    if radius<=1:
        return p*(2*PI-2*n*radius*math.sin(a))
    if radius>=1/math.cos(a):
        return q*(2*n*radius*math.sin(a)-2*PI)
    beta=math.acos(radius*math.cos(a))
    sd=math.sin(beta)
    A=2*n*(beta-sd)
    B=2*n*(radius*math.sin(a)-sd-a+beta)
    return p*A+q*B

def optimum(n,p):
    a=PI/n
    threshold=1+1/math.cos(a)
    if math.isinf(p): return 1/math.cos(a)
    if p<=threshold: return 1.
    return math.cos(2*math.atan(math.tan(a)/p))/math.cos(a)

def optimum_value(n,p):
    a=PI/n
    if p==1: return 2*n*(a-math.sin(a))
    if math.isinf(p): return 2*n*(math.tan(a)-a)
    if p<=1+1/math.cos(a): return 2*n*p*(a-math.sin(a))
    q=p/(p-1)
    return 2*n*q*(2*p*math.atan(math.tan(a)/p)-math.tan(a)-a)

def sampled_dev(n,p,radius,samples=200000):
    # Sample boundary of the disk and each actual polygon edge independently.
    q=p/(p-1)
    a=PI/n
    d=radius*math.cos(a)
    h=radius*math.sin(a)
    ns=[(math.cos(2*PI*j/n),math.sin(2*PI*j/n)) for j in range(n)]
    outdisk=0
    for j in range(samples):
        phi=2*PI*(j+.5)/samples
        c,s=math.cos(phi),math.sin(phi)
        if any(c*x+s*y>d for x,y in ns):outdisk+=1
    diskoutside=2*PI*outdisk/samples
    diskinside=2*PI-diskoutside
    # On each edge coordinates x=d,y in [-h,h], disk condition d^2+y^2 <=1.
    edgeinside=sum(2*h/samples for j in range(samples) if d*d+(-h+2*h*(j+.5)/samples)**2<1)*n
    edgeoutside=2*n*h-edgeinside
    return p*(diskoutside-edgeinside)+q*(edgeoutside-diskinside)

# The positivity factor at the transition is an exact polynomial identity.
for s0 in [Fraction(1),Fraction(9,8),Fraction(4,3),Fraction(3,2),Fraction(7,4),Fraction(2)]:
    p0=1+s0
    poly=p0**4-2*s0*s0*p0*p0-(s0*s0-1)**2
    factor=2*s0*(2-s0)*(s0+1)**2
    check(poly==factor,'factorization at threshold')
    check(poly>=0,'boundary positivity')

for n in [3,4,5,7,11,20,50]:
    for p in [1.01,1.5,2.,2.1,2.4,2.8,3.,4.,8.,25.,500.]:
        a=PI/n; q=p/(p-1)
        r=optimum(n,p); val=optimum_value(n,p)
        check(1-1e-12<=r<=1/math.cos(a)+1e-12,'radius domain')
        check(close(val,dev_formula(n,p,r),rtol=1e-11,atol=1e-10),'closed form disagreement')
        candidates=[1+i*(1/math.cos(a)-1)/200 for i in range(201)]
        check(all(dev_formula(n,p,R)>=val-1e-10 for R in candidates),'optimality scan')
        if p>1+1/math.cos(a)+1e-10:
            check(val < p*(2*PI-2*n*math.sin(a))-1e-11,'beats best inscribed')
            check(val < q*(2*n*math.tan(a)-2*PI)-1e-11,'beats best circumscribed')

for n,p in [(3,2),(3,4),(5,2.4),(5,6),(7,9),(12,2.4),(12,20)]:
    for R in [1.,optimum(n,p),1/math.cos(PI/n)]:
        f=dev_formula(n,p,R)
        g=sampled_dev(n,p,R)
        check(close(f,g,rtol=.002,atol=.003),'sampled separate-boundary perimeter mismatch')

# Finite verification of strict convexity, including the switching regions.
for p in [1.,1.8,2.,2.01,2.04,2.2,2.5,3.,10.,math.inf]:
    prev=optimum_value(3,p)
    for n in range(4,40):
        curr=optimum_value(n,p)
        nxt=optimum_value(n+1,p)
        check(prev-2*curr+nxt > -1e-11,'discrete convexity test')
        check(curr<prev,'strict decrease test')
        prev=curr

# Sharp asymptotic coefficient in an independently evaluated sequence.
for p in [1.,1.7,2.,2.2,2.7,6.,math.inf]:
    constant=(p*PI**3/3 if p<=2 else 2*PI**3/3*(1 if math.isinf(p) else (p*p-2)/(p*(p-1))))
    for n in [1000,3000]:
        # Direct formula is cancellation-prone; a loose asymptotic tolerance is appropriate.
        val=optimum_value(n,p)
        check(close(n*n*val,constant,rtol=.015,atol=.002),'asymptotic coefficient')

print(f'PASS: {checks} checks (exact rational, independent boundary sampling, radius scan, convexity, asymptotics)')
