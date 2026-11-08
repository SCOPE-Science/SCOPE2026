"""Finite reproducibility checks for Gaussian mixed-norm displacement formulas.

These tests supplement, but do not replace, the analytical proof in RESULT.md.
Standard library only. Run: python CHECK.py
"""
import cmath
import math
import random

checks = 0

def verify(cond, description):
    global checks
    if not cond:
        raise AssertionError(description)
    checks += 1


def J(A, v):
    return ((A+v+1)**2 - max(0, abs(A-v)-1)**2) / 2

# Exact radial-transport weight bound: numerical stress test only.
for A in [0, .001, .1, .5, 1, 2, 10, 100, 1000]:
    for v in [1e-8, .001, .01, .1, .5, 1, 1.1, 2, 10, 100, 1e4]:
        verify(min(1,v)*J(A,v) <= 8*(A+1)*v + 1e-8, 'radial transport')


def norm_ratio_test(q, alpha, A):
    c = q*alpha/2
    return math.exp(-c*A*A) + A*math.sqrt(math.pi*c)*(1+math.erf(A*math.sqrt(c)))

# Coherent-state integral compared with independent Simpson quadrature.
def simpson(f, a, b, n=10000):
    h=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+(2*j-1)*h) for j in range(1,n//2+1))
            +2*sum(f(a+2*j*h) for j in range(1,n//2)))*h/3

for q in [1, 1.5, 2, 4]:
    for alpha in [.5, 1, 3]:
        for A in [0, .2, 1, 3, 8]:
            c=q*alpha/2
            integral = simpson(lambda r:r*math.exp(-c*(r-A)**2), 0,
                               A+max(18,18/math.sqrt(c)))
            value=q*alpha*integral
            verify(abs(value-norm_ratio_test(q,alpha,A))<1e-7*(1+value), 'coherent integral')

# Exact algebraic group law on exponential test functions.
seed = random.Random(328291)
for _ in range(200):
    a=complex(seed.uniform(-2,2),seed.uniform(-2,2))
    b=complex(seed.uniform(-2,2),seed.uniform(-2,2))
    z=complex(seed.uniform(-2,2),seed.uniform(-2,2))
    c=complex(seed.uniform(-1,1),seed.uniform(-1,1))
    # W_a acting on exp(c*z), then composition.
    left=cmath.exp(a.conjugate()*z-abs(a)**2/2
                   +b.conjugate()*(z-a)-abs(b)**2/2+c*(z-a-b))
    right=cmath.exp(1j*(a.conjugate()*b).imag
                    +(a+b).conjugate()*z-abs(a+b)**2/2+c*(z-a-b))
    verify(abs(left-right)<2e-10*(1+abs(left)), 'Weyl cocycle')

# Endpoint witness, choosing real x with phase -1.
for t in [.001,.02,.1,.5,1]:
    x=math.pi/(2*t)
    norm_difference=abs(math.exp(-t*t)*cmath.exp(-2j*t*x)-1)
    verify(abs(norm_difference-(1+math.exp(-t*t)))<1e-12,
           'infinite endpoint discontinuity')

# The lower-bound coherent ratio grows with the correct power.
for q in [1, 2, 3, 5]:
    for A in [100, 200, 400]:
        quotient=norm_ratio_test(q,1,A)/A
        verify(abs(quotient-math.sqrt(2*math.pi*q))<.03,
               'large-shift coherent asymptotic')

print(f'PASS: {checks} independent finite checks')
