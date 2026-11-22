"""Independent numeric/finite diagnostic for circle-core tube Crofton formulas.
Run: python check.py ; requires Python 3 and SciPy.  This is supplementary,
not a proof of the all-dimensional or high-dimensional statements.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc, gammaln

checks = 0

def require(test, description):
    global checks
    checks += 1
    if not test:
        raise AssertionError(description)


def mu(d):
    return math.exp(math.lgamma(1.5) + math.lgamma(d / 2)
                    - math.lgamma((d + 1) / 2))


def pieces(d, r):
    b = (d - 2) / 2
    m = mu(d)
    i = betainc(1.5, b, 1 / (r*r))
    upper = (1 - 1/(r*r)) ** b
    numerator = 2 * (r*m*i+upper)
    return numerator/(1+r*m), (i-upper)


def optimum(d):
    return brentq(lambda r: pieces(d,r)[1],1+1e-11, max(100.0,10*math.sqrt(d)),xtol=1e-12)


def f_s(d,s):
    b=(d-2)/2
    return 2*b*s*(1-s*s)**(b-1)

for d in [3,4,5,6,7,8,10,15,20,50,100,200,500,1000]:
    rstar=optimum(d)
    pstar, gstar=pieces(d,rstar)
    require(abs(gstar)<1e-10, f'critical equation d={d}')
    require(abs(pstar - 2*(1-1/(rstar*rstar))**((d-2)/2))<1e-10,
            f'optimum probability d={d}')
    require(all(pieces(d,rstar+delta)[0] < pstar for delta in [-0.001,0.001]
                if rstar+delta>1), f'unimodality d={d}')
    require(pieces(d,1+1e-5)[1]>0, f'left derivative sign d={d}')
    require(pieces(d,10*max(rstar,1))[1]<0, f'right derivative sign d={d}')
    for r in [1.001,1.1,1.25,1.7,3,10]:
        # These are direct first-principles orientation integrals.
        val, err = quad(lambda s: min(r*s,1)*f_s(d,s),0,1,
                         epsabs=5e-12, epsrel=5e-12, points=[1/r],limit=300)
        exact=pieces(d,r)[0]
        require(abs(2*val/(1+r*mu(d))-exact)<2e-9,
                f'orientation quadrature d={d} r={r}')
        p_disc = quad(lambda s: max(r*s-1,0)*f_s(d,s),0,1,points=[1/r],limit=300)[0]/(1+r*mu(d))
        p_ann = quad(lambda s: max(1-r*s,0)*f_s(d,s),0,1,points=[1/r],limit=300)[0]/(1+r*mu(d))
        require(abs(exact+p_disc+p_ann-1)<1e-8, f'exhaustive d={d} r={r}')

r3=optimum(3); r4=optimum(4)
require(abs(r3-1.1189047873)<1e-8,'original 3D probability optimizer')
require(abs(r4**3-r4-1)<1e-10,'4D plastic constant')
require(abs(r4-1.324717957244746)<1e-11,'4D optimizer')

a=math.sqrt(math.pi/2)
def limit_eq(t):
    return a*math.erf(t/math.sqrt(2))-(t+a)*math.exp(-t*t/2)
tstar=brentq(limit_eq,0.1,10,xtol=1e-14)
kstar=1/tstar
pstar=2*math.exp(-tstar*tstar/2)
require(abs(kstar-.7349039087481462)<1e-9,'Rayleigh optimum kappa')
require(abs(pstar-.7924426397998108)<1e-9,'Rayleigh optimal chance')
for d in [100,500,1000]:
    require(abs(optimum(d)/math.sqrt(d)-kstar)<0.015,'optimizer near Rayleigh limit')

print(f'PASS {checks} finite checks')
print(f'd=3: radius {r3:.12f}, optimal P {pieces(3,r3)[0]:.12f}')
print(f'd=4: radius {r4:.12f}, optimal P {pieces(4,r4)[0]:.12f}')
print(f'limit: optimal radius / sqrt(d) {kstar:.12f}, optimal P {pstar:.12f}')
