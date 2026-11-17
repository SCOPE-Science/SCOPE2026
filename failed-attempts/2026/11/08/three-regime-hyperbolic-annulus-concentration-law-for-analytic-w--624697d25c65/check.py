"""Independent finite checks for the beta-annulus spectral staircase.

Run with Python 3; scientific proof is in RESULT.md. No external packages.
"""
import math

count = 0

def check(condition, description):
    global count
    if not condition:
        raise AssertionError(description)
    count += 1

def simpson(f, a, b, steps=360):
    h = (b-a)/steps
    total = f(a)+f(b)
    for j in range(1, steps):
        total += (4 if j % 2 else 2)*f(a+j*h)
    return total*h/3

def lam(n,a,b,gamma):
    # A quadrature that is independent of the first-difference formula.
    def integrand(t):
        return t**n*(1-t)**(gamma-1)
    return simpson(integrand,a,b)/math.exp(math.lgamma(n+1)+math.lgamma(gamma)-math.lgamma(n+gamma+1))

def gap(n,a,b,gamma):
    den = (n+1)*math.exp(math.lgamma(n+1)+math.lgamma(gamma)-math.lgamma(n+gamma+1))
    return (a**(n+1)*(1-a)**gamma - b**(n+1)*(1-b)**gamma)/den

for gamma in [0.5, 1., 1.7, 2., 3., 6.]:
    for a,b in [(0.12,0.3),(0.2,0.6),(0.6,0.8),(0.75,0.9)]:
        tau = gamma*math.log((1-a)/(1-b))/math.log(b/a)
        vals = [lam(n,a,b,gamma) for n in range(18)]
        for n in range(12):
            actual = vals[n+1]-vals[n]
            expected = gap(n,a,b,gamma)
            check(abs(actual-expected)<3e-8*max(1,abs(expected)),f'gap {gamma,a,b,n}')
            theoretical_sign = (n+1 < tau) - (n+1 > tau)
            if abs(expected) > 1e-12:
                check(theoretical_sign*expected>0,f'gap sign {gamma,a,b,n}')
        if tau<15 and abs(tau-round(tau))>1e-7:
            nmax = math.floor(tau)
            check(vals[nmax]==max(vals),f'mode {gamma,a,b}')

# Exact transition: prescribe a, b, and gamma so tau=k.
a,b=0.2,0.6
for k in (1,2,3,4,8):
    gamma = k*math.log(b/a)/math.log((1-a)/(1-b))
    check(abs(gap(k-1,a,b,gamma))<1e-10,f'exact tie {k}')
    check(gap(k,a,b,gamma)<0,f'descending after tie {k}')
    if k>1:
        check(gap(k-2,a,b,gamma)>0,f'ascending before tie {k}')

# Boundary layer: compare numerical beta integration to gamma-interval limit.
gamma,u,v=2.,7.,2.
kappa=gamma*math.log(u/v)/(u-v)
ref=simpson(lambda t:t**(gamma-1)*math.exp(-t),kappa*v,kappa*u)/math.gamma(gamma)
errors=[]
for R in (60,120,240,480):
    a,b=1-u/R,1-v/R
    tau=gamma*math.log((1-a)/(1-b))/math.log(b/a)
    n=math.floor(tau)
    # Stable gamma limit quadrature via y=R(1-t), including normalization.
    invbeta=math.exp(math.lgamma(n+gamma+1)-math.lgamma(n+1)-math.lgamma(gamma))
    estimate=simpson(lambda y:invbeta/R**gamma*(1-y/R)**n*y**(gamma-1),v,u)
    errors.append(abs(estimate-ref))
    check(abs(n/R-kappa)<3.0/R+0.01,f'index asymptotic {R}')
check(errors[-1] < errors[0]/3, 'boundary limit improving')
check(errors[-1]<0.005,'boundary limit reasonable')
print('WAVELET_ANNULUS_STAIRCASE_CHECKS_PASS',count)
