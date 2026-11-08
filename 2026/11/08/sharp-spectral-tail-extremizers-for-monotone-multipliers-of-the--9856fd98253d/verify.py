"""Finite standard-library diagnostics for the constrained Cesaro spectral-tail variational formulas.
Run: python verify.py. Finite checks support, but do not prove, infinite-dimensional asymptotics.
"""
import math

N = 0

def ok(condition, tag):
    global N
    assert condition, tag
    N += 1

def beta(L):
    if L <= 1:
        return .5
    a, b = 1e-15, .5
    for _ in range(120):
        x = (a+b)/2
        f = 2*L*(x+x*(1-x)*math.log((1-x)/x))
        if f < 1: a=x
        else: b=x
    return (a+b)/2

def wmax(L):
    if L == 1: return 1.
    b=beta(L)
    I=4*math.sqrt(L)*math.asin(math.sqrt(b))+2*math.sqrt(L*b*(1-b))*math.log((1-b)/b)
    return I*I/math.pi**2

def wmin(L):
    return (4*L/math.pi**2)*math.asin(1/L)**2

def midpoint_integral(f, n=100000):
    return sum(f((i+.5)/n) for i in range(n))/n

for L in [1, 1.1, 1.5, 2, 3, 4, 10, 40, 200]:
    ok(wmin(L) <= wmax(L), 'extrema ordering')
    if L == 1:
        ok(abs(wmin(L)-1)<1e-14 and abs(wmax(L)-1)<1e-14, 'singleton')
        continue
    b=beta(L); k=L*b*(1-b)
    ok(0<b<.5, 'unique root bracket')
    ok(abs(2*L*(b+b*(1-b)*math.log((1-b)/b))-1)<2e-11, 'mass equation')
    def p(x): return min(L,k/(x*(1-x)))
    # Exact mass and an independent finite-grid integral.
    ok(abs(midpoint_integral(p,30000)-1)<.0001,'density normalized')
    def integrand(theta): return 2*math.sqrt(p(math.sin(theta)**2))
    I=(math.pi/2)*midpoint_integral(lambda q: integrand(math.pi*q/2),100000)
    ok(abs(I*I/math.pi**2-wmax(L))<.0001,'independent quadrature')
    ok(abs(p(b)-L)<1e-10 and abs(p(1-b)-L)<1e-10,'interface continuity')
    ok(all(0<=p(x)<=L for x in [.0001,.002,.02,.1,.25,.5,.9,.98,.998,.9999]),'density cap')
    ok(wmax(L)>wmin(L), 'strict gap')
ok(abs(wmin(2)-2/9)<1e-14,'L=2 exact infimum')
for L in [1e5,1e6,1e7]:
    ok(abs(wmin(L)*L*math.pi**2/4-1)<1e-8,'lower large cap')
    ok(1.0<wmax(L)*math.pi**2/(2*math.log(L))<1.8,'upper asymptotic scaling')
print('CESARO_CAP_EXTREMAL_CHECK_OK',N,'finite assertions')
