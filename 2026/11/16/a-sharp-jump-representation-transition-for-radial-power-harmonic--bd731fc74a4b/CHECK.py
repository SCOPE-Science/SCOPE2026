"""Finite checks for radial-power harmonic Dirichlet Fourier and jump formulas.

Run: python CHECK.py. These checks are supplementary; the proof is analytic.
"""
from fractions import Fraction
from math import factorial, cos, sin, log, pi, isclose

count = 0

def check(ok, detail):
    global count
    assert ok, detail
    count += 1

def symbol(n, alpha):
    if n == 0:
        return Fraction(0)
    p = Fraction(1)
    for j in range(1,n+1):
        p *= alpha+j
    return Fraction(n*n*factorial(n-1),1)/p

def beta_increment(n, alpha):
    # alpha * B(n+1,alpha) * [1-alpha*(n+1)/(n+alpha+1)]
    d = Fraction(1)
    for j in range(1,n+1):
        d *= alpha+j
    return Fraction(factorial(n),1)/d*(1-alpha*Fraction(n+1,1)/(n+alpha+1))

for alpha in map(Fraction,['0','1/8','1/4','1/2','3/4','7/8','1','3/2','2','3']):
    for n in range(0,35):
        check(symbol(n+1,alpha)-symbol(n,alpha)==beta_increment(n,alpha), ('beta-increment',n,alpha))
        if 0 <= alpha <= 1:
            check(symbol(n+1,alpha)>symbol(n,alpha), ('monotonicity',n,alpha))
    check(symbol(1,alpha)==1/(alpha+1), ('first eigenvalue',alpha))

for n in range(1,30):
    check(symbol(n,Fraction(0))==n, ('Cauchy symbol',n))
    check(symbol(n,Fraction(1))==Fraction(n,n+1),('bounded symbol',n))

try:
    import mpmath as mp
    mp.mp.dps=32
    for angle in (mp.mpf('0.02'),mp.mpf('0.11'),mp.mpf('0.37'),mp.mpf('1.2'),mp.pi):
        formula=-1-mp.cos(angle)*mp.log(4*mp.sin(angle/2)**2)+(mp.pi-angle)*mp.sin(angle)
        integral=mp.quad(lambda t:(1-t*t)/(1-2*t*mp.cos(angle)+t*t),[0,mp.mpf('0.5'),mp.mpf('0.95'),1])
        check(abs(formula-integral)<mp.mpf('1e-22'),('finite-rate jump density',angle))
    for alpha in (mp.mpf('0.25'),mp.mpf('0.50'),mp.mpf('0.75')):
        target=mp.pi*alpha*(1-alpha)/mp.sin(mp.pi*alpha/2)
        for angle in (mp.mpf('0.003'),mp.mpf('0.001')):
            def density(t):
                return (1-t*t)/(1-2*t*mp.cos(angle)+t*t)*alpha*(1-alpha*t)*((1-t)**(alpha-2))
            val=mp.quad(density,[0,mp.mpf('0.5'),mp.mpf('0.95'),mp.mpf('0.995'),1])
            ratio=val*angle**(2-alpha)/target
            check(abs(ratio-1)<mp.mpf('0.06'),('jump singularity',alpha,angle,ratio))
except ImportError:
    print('mpmath unavailable: skipped supplementary quadrature.')

print('PASS:',count,'finite assertions. This is not an infinite proof.')
