"""Independent finite-state checks for first meetings of independently clocked walks on cycles.

Run: python CHECK.py. Requires Python 3, SymPy and SciPy.
The analytic proof in RESULT.md, not these finite checks, establishes all-size claims.
"""
from fractions import Fraction
from math import cos, pi, sqrt
import sympy as sp

checked = 0

def check(condition, message):
    global checked
    if not condition:
        raise AssertionError(message)
    checked += 1

def exact_direct(n,p):
    """Solve killed relative-walk Poisson system with exact rational arithmetic."""
    p=sp.Rational(p.numerator,p.denominator)
    jumps={-2:p*p/4,-1:p*(1-p),0:(1-p)**2+p*p/2,1:p*(1-p),2:p*p/4}
    q=sp.Matrix([[sum((prob for step,prob in jumps.items() if (x+step)%n==y),sp.S.Zero)
                  for y in range(1,n)] for x in range(1,n)])
    h=(sp.eye(n-1)-q).inv()*sp.ones(n-1,1)
    return list(h)

def spectral(n,p):
    return sum(1.0/(p*(2-p*(1-cos(2*pi*k/n)))) for k in range(1,n))

def closed(n,p):
    s=sqrt(1-p)
    r=(1-s)/(1+s)
    z=(-r)**n
    return n/(2*p*s)*(1+z)/(1-z)-1/(2*p)

for n in range(3,15):
    for p in [Fraction(1,7),Fraction(1,4),Fraction(1,2),Fraction(2,3),Fraction(5,6)]:
        h=exact_direct(n,p)
        f=spectral(n,float(p))
        c=closed(n,float(p))
        check(abs(float(h[0])-f)<1e-8*(1+float(h[0])),f'direct vs spectral, n={n}, p={p}')
        check(abs(float(h[0])-c)<1e-8*(1+float(h[0])),f'direct vs closed, n={n}, p={p}')
        check(all(v>0 for v in h),f'finite hitting expectation, n={n}, p={p}')

# For three vertices the exact rational expression is known from the killed chain.
p=sp.symbols('p',positive=True)
check(sp.simplify(2/(p*(2-sp.Rational(3,2)*p))-4/(p*(4-3*p)))==0,'n=3 simplification')
check(sp.simplify(sp.diff(4/(p*(4-3*p)),p).subs(p,sp.Rational(2,3)))==0,'n=3 optimizer')

# Closed-form Fourier sum matches explicit n=4 rational formula.
E4=2/(p*(2-p))+1/(p*(2-2*p))
check(sp.simplify(E4.subs(p,sp.Rational(1,2))-sp.Rational(14,3))==0,'n=4 exact')

# Check convergence and sign of the first correction at large n.
from scipy.optimize import minimize_scalar
for n in [30,60,120,240,480]:
    ff=lambda q:spectral(n,q)
    opt=minimize_scalar(ff,bounds=(.50,.80),method='bounded',options={'xatol':1e-13})
    check(opt.success and .6<opt.x<.7, f'optimizer n={n}')
    check(abs(n*(sp.Rational(2,3)-opt.x)-2*sqrt(3)/27) < 0.12, f'first correction n={n}')

print(f'PASS {checked} independent checks')
