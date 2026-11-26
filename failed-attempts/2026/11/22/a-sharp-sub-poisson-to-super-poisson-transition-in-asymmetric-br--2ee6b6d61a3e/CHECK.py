"""Independent finite-difference and exact-algebra checks for threshold-activated Brownian reset counts.

Python 3 standard library only. All stochastic-process claims are proved in RESULT.md;
this script is a finite-resolution consistency check, not an infinite-state certificate.
"""
from fractions import Fraction
import math

checks = 0

def ok(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def analytic(L, D, r):
    a = L * math.sqrt(r / D)
    mean = (1 + a) / r
    variance = (1 + a + a*a + 2*a**3/3) / (r*r)
    fano = variance / (mean*mean)
    return a, mean, variance, fano


def transform(s, L, D, r):
    if s == 0:
        return 1.0
    return r / (r+s+math.sqrt(s*(s+r))*math.tanh(L*math.sqrt(s/D)))


def tridiagonal(lower, diagonal, upper, rhs):
    n = len(rhs)
    d = diagonal[:]
    c = upper[:]
    y = rhs[:]
    for j in range(1,n):
        z = lower[j] / d[j-1]
        d[j] -= z*c[j-1]
        y[j] -= z*y[j-1]
    sol = [0.0]*n
    sol[-1] = y[-1]/d[-1]
    for j in range(n-2,-1,-1):
        sol[j] = (y[j]-c[j]*sol[j+1])/d[j]
    return sol


def discrete_operator(L, D, r, s, points_per_L=150):
    h = L/points_per_L
    extra = int(math.ceil(13*math.sqrt(D/(r+s))/h))
    n = points_per_L + extra + 1
    c = D/h**2
    lower = [0.0]*n
    diagonal = [0.0]*n
    upper = [0.0]*n
    hazards = [0.0]*n
    for j in range(n):
        hazard = r if j > points_per_L else (r/2 if j == points_per_L else 0.0)
        hazards[j] = hazard
        diagonal[j] = 2*c + s + hazard
        if j:
            lower[j] = -c
        if j+1 < n:
            upper[j] = -c
    # Neumann endpoint stencils; remote endpoint is 13 decay lengths away.
    upper[0] = -2*c
    lower[-1] = -2*c
    return lower, diagonal, upper, hazards, points_per_L


for L, D, r in [(0.3,1.0,1.0),(0.5,1.0,1.0),(1.0,1.0,1.0),
                 (1.5,1.0,1.0),(2.0,1.0,1.0),(1.5,2.0,3.0)]:
    a,m,v,f = analytic(L,D,r)
    ok(a>0 and m>0 and v>0 and f>0, "positive moments")
    ok(abs(f-(1+a+a*a+2*a**3/3)/(1+a)**2)<1e-14,"Fano algebra")
    low,diag,up,hazards,at = discrete_operator(L,D,r,0.0)
    n = len(diag)
    moment1 = tridiagonal(low,diag,up,[1.0]*n)
    moment2 = tridiagonal(low,diag,up,[2*y for y in moment1])
    nummean=moment1[at]
    numvar=moment2[at]-nummean*nummean
    ok(abs(nummean-m)<6e-4,"mean against independently discretized killed generator")
    ok(abs(numvar-v)<1e-3,"variance against independently discretized killed generator")
    for s in [0.05,0.2,0.9]:
        lo,di,uu,hz,idx=discrete_operator(L,D,r,s)
        numeric=tridiagonal(lo,di,uu,hz)[idx]
        exact=transform(s,L,D,r)
        ok(0<exact<1,"Laplace transform probability bound")
        ok(abs(exact-numeric)<3e-4,"Laplace transform independently discretized boundary-value problem")

# Rational arithmetic: the Fano sign is exactly the sign of a*(2*a*a-3).
for i in range(1,31):
    a=Fraction(i,20)
    f=(1+a+a*a+Fraction(2,3)*a*a*a)/(1+a)**2
    ok(f-1 == a*(Fraction(2,3)*a*a-1)/(1+a)**2,"exact rational Fano identity")
    deriv=(2*a**3+6*a*a+3*a-3)/(3*(a+1)**3)
    step=Fraction(1,20000)
    p=(1+(a+step)+(a+step)**2+Fraction(2,3)*(a+step)**3)/(1+a+step)**2
    m=(1+(a-step)+(a-step)**2+Fraction(2,3)*(a-step)**3)/(1+a-step)**2
    ok(abs(float((p-m)/(2*step)-deriv))<1e-6,"rational central difference versus derivative")

lo,hi=0.0,1.0
for _ in range(90):
    mid=(lo+hi)/2
    q=2*mid**3+6*mid**2+3*mid-3
    if q<0:lo=mid
    else:hi=mid
amin=(lo+hi)/2
fmin=(1+amin+amin**2+2*amin**3/3)/(1+amin)**2
ok(abs(amin-0.4756865177957207)<5e-14,"unique cubic positive root")
ok(abs(fmin-0.8145118671977507)<5e-14,"sharp minimum")
ok(abs(2*amin**3+6*amin**2+3*amin-3)<1e-12,"optimality equation")
ac=math.sqrt(1.5)
ok(abs((1+ac+ac**2+2*ac**3/3)/(1+ac)**2-1)<1e-14,"exact Poisson crossing")
for a in (0.0001,0.2,0.9,1.224745,2.0,10.0):
    f=(1+a+a*a+2*a**3/3)/(1+a)**2
    ok((f<1)==(a<ac),"global side of crossing")
print(f"PASS: {checks} exact-algebra and independent finite-difference assertions")
print(f"a_min={amin:.15f}; Fano_min={fmin:.15f}; a_cross={ac:.15f}")
