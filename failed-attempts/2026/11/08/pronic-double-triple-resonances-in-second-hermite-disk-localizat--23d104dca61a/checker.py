"""Reproducible checks for the second-Hermite disk resonance theorem.

Requires Python, SymPy and SciPy. Symbolic identities are verified exactly;
finite quadrature checks corroborate, but do not replace, the proof.
"""
from math import exp, factorial
import sympy as sp
from scipy.integrate import quad

checks = 0


def confirm(cond, label):
    global checks
    if not cond:
        raise AssertionError(label)
    checks += 1


def p(k, x):
    return x*x - 2*k*x + k*(k-1)


def eig(k, radius):
    # For k=0,1 the negative powers below cancel exactly.
    if k == 0:
        f = lambda t: exp(-t)*t*t/2
    elif k == 1:
        f = lambda t: exp(-t)*t*(t-2)**2/2
    else:
        f = lambda t: exp(-t)*t**(k-2)*p(k,t)**2/(2*factorial(k))
    return quad(f, 0, radius, epsabs=2e-12, epsrel=2e-12)[0]


N, X = sp.symbols('N X')
P = lambda k: X**2-2*k*X+k*(k-1)
identity = (N+1)*P(N)**2 - X*P(N+1)**2 - (N-1-X)*P(N)*P(N+1) - X*(sp.diff(P(N),X)*P(N+1)+P(N)*sp.diff(P(N+1),X))
confirm(sp.expand(identity) == 0, 'global differential identity')
confirm(sp.expand(P(N+1)-P(N)) == 2*(N-X), 'adjacent polynomial subtraction')
confirm(sp.expand(P(N).subs(X,N)) == -N, 'adjacent roots impossible')
confirm(sp.expand(P(N+2)-P(N)) == 4*N+2-4*X, 'two-step subtraction')
confirm(sp.expand(P(N).subs(X,N+sp.Rational(1,2))) == sp.Rational(1,4)-N, 'two-step roots impossible')

for n in range(0, 29):
    for radius in (0.2, .75, 1.3, 2., 2.7, 6., 11., 23., 38.):
        expected = exp(-radius)*radius**(n-1)*p(n,radius)*p(n+1,radius)/(2*factorial(n+1))
        actual = eig(n,radius)-eig(n+1,radius)
        confirm(abs(actual-expected) < 2.5e-10, f'integrated adjacent gap: n={n} R={radius}; {actual} vs {expected}')

for k in range(1, 25):
    r = k*(k+1)
    m, ell = k*k, (k+1)*(k+1)
    confirm(p(m,r)==0 and p(ell,r)==0, f'two pronic roots k={k}')
    for n in range(max(0,m-2),ell+3):
        confirm((p(n,r)==0)==(n in (m,ell)), f'all pronic roots near k={k} n={n}')

for n in range(1, 40):
    for sg in (-1,1):
        r = n+sg*n**0.5
        if r<=0:
            continue
        confirm(abs(p(n,r))<2e-12*max(1,r*r), f'root branches n={n} sg={sg}')

# The transverse-derivative ratio at every root is exact, not empirical.
# From the integral derivatives it reduces to a polynomial divisible by P_n.
ratio_numerator = X**2*P(N+1)**2-N**2*P(N-1)**2
confirm(sp.rem(ratio_numerator, P(N), X)==0, 'universal slope-ratio divisibility')
for n in range(1, 32):
    for sg in (-1, 1):
        r = n+sg*n**0.5
        if r<=0:
            continue
        derivative_left = exp(-r)*r**(n-3)*p(n-1,r)**2/(2*factorial(n-1))
        derivative_right = exp(-r)*r**(n-1)*p(n+1,r)**2/(2*factorial(n+1))
        confirm(abs(derivative_right/derivative_left-n/(n+1))<3e-12, f'slope ratio n={n} sg={sg}')

for k in range(1,5):
    r=k*(k+1)
    for m in (k*k,(k+1)*(k+1)):
        left,mid,right=eig(m-1,r),eig(m,r),eig(m+1,r)
        confirm(max(abs(left-mid),abs(mid-right))<2e-11, f'quad triple k={k} center={m}')

print(f'SECOND_HERMITE_RESONANCE_CHECKS_PASS {checks}')
