"""Deterministic checks for position-only resetting with Brownian stochastic diffusivity.

Python 3 standard library only. Numerical checks supplement, not replace, proofs.
"""
import math

checks = 0

def near(a, b, atol=1e-8, rtol=1e-8):
    global checks
    assert math.isfinite(a) and math.isfinite(b)
    assert abs(a-b) <= atol+rtol*max(abs(a), abs(b)), (a, b)
    checks += 1

def simpson(fun, lo, hi, n=10000):
    assert n % 2 == 0
    h=(hi-lo)/n
    s=fun(lo)+fun(hi)
    for j in range(1,n):
        s+=(4 if j % 2 else 2)*fun(lo+j*h)
    return s*h/3

def age_moment(n,t,r):
    return n*simpson(lambda a:a**(n-1)*math.exp(-r*a), 0.,t,4000)

def j1(t,r):
    return t/r+math.expm1(-r*t)/r**2

def j2(t,r):
    return t*t/r-2*t/r**2-2*math.expm1(-r*t)/r**3

def second(t,r,L):
    return 4*L*L*j1(t,r)

def fourth(t,r,L):
    return 48*L**4*(3*t*t*age_moment(2,t,r)-11*t*age_moment(3,t,r)/3+1.25*age_moment(4,t,r))

def mixed(t,r,L):
    return 8*L**4*(t*j1(t,r)+2*j2(t,r))

def cross(t,h,r,L):
    e=math.exp(-r*h)
    return (e*fourth(t,r,L)+2*(1-e)*mixed(t,r,L)/r
          +4*L**2*(h-(1-e)/r)*second(t,r,L)/r)

def corr_squared(t,c,r,L):
    h=(c-1)*t
    v0=fourth(t,r,L)-second(t,r,L)**2
    v1=fourth(c*t,r,L)-second(c*t,r,L)**2
    return (cross(t,h,r,L)-second(t,r,L)*second(c*t,r,L))/math.sqrt(v0*v1)

# Conditional last-age integrals independent of the polynomial forms.
for r in (0.7,1.2,2.3):
    for L in (0.75,1.4):
        for t in (0.2,0.8,2.5,7.0):
            J1=simpson(lambda s:s*math.exp(-r*(t-s)),0,t,6000)
            J2=simpson(lambda s:s*s*math.exp(-r*(t-s)),0,t,6000)
            near(j1(t,r),J1,3e-12,3e-11)
            near(j2(t,r),J2,3e-12,3e-11)
            near(second(t,r,L),4*L*L*J1,3e-10)
            near(mixed(t,r,L),8*L**4*(t*J1+2*J2),3e-10)
            integral=simpson(lambda a:r*math.exp(-r*a)*(
                  3*t*t*a*a-11*t*a**3/3+1.25*a**4),0,t,5000)
            integral+=math.exp(-r*t)*(3*t**4-11*t**4/3+1.25*t**4)
            near(fourth(t,r,L),48*L**4*integral,3e-8,5e-8)
            near(cross(t,0,r,L),fourth(t,r,L),1e-10,2e-10)

# Exact free-process small-time limit and large-time moments.
for r,L in ((0.7,0.75),(1.2,1.4),(2.3,0.9)):
    near(second(0.0001,r,L)/(0.0001**2),2*L*L,3e-4)
    near(fourth(0.0004,r,L)/(0.0004**4),28*L**4,0.1)
    for t in (300.,900.):
        near(second(t,r,L)/t,4*L*L/r,0.06)
        near(fourth(t,r,L)/t**2,288*L**4/r**2,atol=0.05,rtol=0.025)
        near(mixed(t,r,L)/t**2,24*L**4/r,atol=0.01,rtol=0.015)
        near(fourth(t,r,L)/second(t,r,L)**2,18.,0.3)
    for c in (1.25,1.5,2.,3.,5.):
        near(corr_squared(500.,c,r,L),2/(17*c),atol=0.002)

# Independent Gaussian quadrature of the normal-times-Laplace CF.
for r,L in ((0.8,1.0),(1.7,0.8),(2.2,1.6)):
    b=math.sqrt(2)*L/math.sqrt(r)
    for k in (0.2,0.6,1.,1.8,3.):
        a=b*b*k*k
        analytic=math.sqrt(math.pi/(2*a))*math.exp(1/(2*a))*math.erfc(1/math.sqrt(2*a))
        numeric=simpson(lambda z: math.exp(-z*z/2)/(1+a*z*z)/math.sqrt(2*math.pi),-12,12,16000)
        near(analytic,numeric,atol=3e-11)
    # Density evaluated via the independent log-coordinate integral.
    def density(x):
        return simpson(lambda v: math.exp(-math.exp(2*v)/2-x/(b*math.exp(v))),-18,5,16000)/(b*math.sqrt(2*math.pi))
    for xratio in (18,35,55):
        x=xratio*b
        approx=(b/x)**(1/3)*math.exp(-1.5*(x/b)**(2/3))/(b*math.sqrt(3))
        assert 0.95<density(x)/approx<1.02
        checks+=1
    for xratio in (0.001,0.0001):
        x=xratio*b
        near(density(x)/(math.log(b/x)/(b*math.sqrt(2*math.pi))),1.,atol=0.14)

print(f"PASS: {checks} deterministic assertions")
