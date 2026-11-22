"""Independent exact-generator and numerical asymptotic checks for the fitness-cumulant theorem."""
from fractions import Fraction as F
from math import factorial, exp, log, log1p, expm1, isfinite

checks = 0

def check(condition, detail):
    global checks
    if not condition:
        raise AssertionError(detail)
    checks += 1

def falling(n, k):
    p = 1
    for j in range(k):
        p *= n - j
    return p

def moment(k, lam, death, reset, immigration):
    m = F(1)
    gap = death-lam
    for j in range(1,k+1):
        m *= j*((j-1)*lam + immigration)/(j*gap+reset)
    return m

def limit_factorial_cumulant(k, lam, death, reset, amplitude):
    gap=death-lam
    value=F(amplitude*factorial(k)*factorial(k-1))*lam**(k-1)
    for j in range(1,k+1):
        value /= j*gap + reset
    return value

# Exact finite-state generator calculations: these identities hold at EVERY n,
# so verification over small n is a consistency test, not an infinite proof.
for lam, death, reset, amp in [(F(1,3),F(4,3),F(2,3),F(2,5)),(F(2,3),F(5,4),F(1,2),F(3,7)),(F(4,5),F(6,5),F(1,9),F(1,11))]:
    for k in range(1,8):
        u=amp/F(17)
        for n in range(0,13):
            lhs=(lam*n+u)*(falling(n+1,k)-falling(n,k))
            lhs+=death*n*(falling(n-1,k)-falling(n,k))
            lhs+=reset*(0-falling(n,k))
            rhs=-(k*(death-lam)+reset)*falling(n,k)+k*((k-1)*lam+u)*falling(n,k-1)
            check(lhs==rhs, ('generator',k,n))
        m=moment(k,lam,death,reset,u)
        previous=moment(k-1,lam,death,reset,u)
        check((k*(death-lam)+reset)*m==k*((k-1)*lam+u)*previous,('recurrence',k))
        # Compare the first immigration coefficient of the all-order exact product.
        tiny=F(1,10**5)
        scaled=moment(k,lam,death,reset,amp*tiny)/tiny
        exact=limit_factorial_cumulant(k,lam,death,reset,amp)
        check(abs(scaled-exact)<F(1,10), ('small-immigration coefficient',k))

# Numerical integral helper for independent near-critical clan-size checks.
def simpson(f,a,b,n=10000):
    h=(b-a)/n
    sm=f(a)+f(b)
    for j in range(1,n):
        sm+=(4 if j%2 else 2)*f(a+j*h)
    return sm*h/3

# A separate immigrant-family calculation probes the near-critical Bessel cutoff.
# At death rate one, birth rate 1-w and elapsed time t, the one-founder
# branching population has an explicit zero-modified geometric law.
def clan_scaled(n, w, nu):
    rate=w**nu
    s=n*rate
    lam=1-w
    def integrand(y):
        t=n*y
        d=w+lam*(-expm1(-w*t))
        if d<=0:
            return 0.0
        alpha=w/d
        if alpha>=1:
            return 0.0
        p=alpha**2 * exp(-w*t+(n-1)*log1p(-alpha))
        return exp(-s*y)*n*n*p
    return simpson(integrand,1e-5,35,10000)

def critical_scaled(s):
    return simpson(lambda y:y**(-2)*exp(-1/y-s*y),1e-5,35,10000)

for w,nu,s in [(1e-8,.5,1.),(1e-8,.4,2.),(1e-7,.6,.7)]:
    n=round(s/w**nu)
    empirical=clan_scaled(n,w,nu)
    target=critical_scaled(n*w**nu)
    check(abs(empirical/target-1)<.008,('clan cutoff',w,nu,empirical,target))
check(abs(critical_scaled(1.)-0.2797317636330449)<3e-7,'standard Bessel K1 integral')
print('PASS:',checks,'exact-generator, rare-immigration, cutoff, and asymptotic checks')
