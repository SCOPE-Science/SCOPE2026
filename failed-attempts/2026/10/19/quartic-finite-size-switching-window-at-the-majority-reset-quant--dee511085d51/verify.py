"""Independent numerical checks for a binomial-majority quantum-reset asymptotic law.

Requirements: Python 3, NumPy, SciPy. Runs finite-N quadrature; the
infinite-N classifications are established in the accompanying proof.
"""
import math
from scipy.integrate import quad
from scipy.special import betainc, gamma, ndtr

COUNT = 0


def check(condition, label):
    global COUNT
    COUNT += 1
    if not bool(condition):
        raise AssertionError(label)


def rate(n, a, beta):
    if n % 2 != 1 or n < 1 or not 0 < a < 1 or beta <= 0:
        raise ValueError("odd n, 0<a<1, beta>0 required")
    m = (n + 1) // 2
    integrand = lambda t: math.exp(-beta*t)*betainc(m, m, a*math.sin(t)**2)
    val, err = quad(integrand, 0, math.pi, points=[math.pi/2],
                    epsabs=1e-13, epsrel=1e-12, limit=350)
    return beta / (-math.expm1(-beta*math.pi))*val


def params(a, delta=1.0, reset_rate=0.8):
    omega = delta/math.sqrt(1-a)
    return reset_rate/omega


def prefactor(a, beta):
    s = math.exp(-beta*math.pi/2)/(-math.expm1(-beta*math.pi))
    if a < .5:
        return beta*s*2*math.sqrt(a)*(1-a)/(1-2*a)**1.5
    if a == .5:
        return beta*s*2**.25*gamma(.75)/math.sqrt(math.pi)
    raise ValueError


# Independent numerical Gaussian integration and Gamma evaluation.
area = 2*quad(lambda u: ndtr(-u*u), 0, 7, epsabs=2e-13)[0]
gamma_area = 2**.25*gamma(.75)/math.sqrt(math.pi)
check(abs(area-gamma_area) < 1e-12, 'quartic Gaussian area')
check(abs(gamma_area-0.8221789586624584) < 1e-12, 'closed form')

# Three distinct regimes and progressive agreement with analytic limits.
for a in (.3, .5, .7):
    b = params(a)
    ns = [51, 101, 201, 401, 801, 1601]
    values = [rate(n, a, b) for n in ns]
    check(all(0 < q < 1 for q in values), f'probabilities {a}')
    if a < .5:
        I = -.5*math.log(4*a*(1-a))
        target = prefactor(a,b)
        norms = [q*n*math.exp(n*I) for q,n in zip(values,ns)]
        check(all(0 < x < target for x in norms), 'subcritical below limit')
        check(all(x < y for x,y in zip(norms,norms[1:])), 'subcritical converging')
        check(abs(norms[-1]/target-1)<.015, 'subcritical 1601 accuracy')
    elif a == .5:
        target = prefactor(a,b)
        norms = [q*n**.25 for q,n in zip(values,ns)]
        check(all(target < x < target*1.05 for x in norms), 'critical bound')
        check(all(x > y for x,y in zip(norms,norms[1:])), 'critical converging')
        check(abs(norms[-1]/target-1)<.01, 'critical 1601 accuracy')
    else:
        theta = math.asin(1/math.sqrt(2*a))
        target = (math.exp(-b*theta)-math.exp(-b*(math.pi-theta)))/(-math.expm1(-b*math.pi))
        check(all(0<q<target for q in values), 'supercritical below limit')
        check(all(x<y for x,y in zip(values,values[1:])), 'supercritical converging')
        check(abs(values[-1]/target-1)<.002, 'supercritical 1601 accuracy')

# Critical finite-N window: compare a_N=1/2 + xi/sqrt(N) with its
# predicted continuous profile at fixed detuning and physical reset rate.
for xi in [-.7, 0.0, .7]:
    F = quad(lambda u: ndtr(2*xi-u*u), -7, 7, epsabs=1e-12)[0]
    bc = params(.5)
    target = bc*math.exp(-bc*math.pi/2)/(-math.expm1(-bc*math.pi))*F
    values = []
    for n in [401,801,1601]:
        a = .5+xi/math.sqrt(n)
        values.append(n**.25*rate(n,a,params(a)))
    check(all(x > 0 for x in values), f'positive scaling profile {xi}')
    check(abs(values[-1]/target-1) < .08,
          f'critical window convergence xi={xi}: {values[-1]}, {target}')
    check(abs(values[-1]-target) < abs(values[0]-target),
          f'critical window improving xi={xi}')

print(f'{COUNT} assertions passed: exact finite-N integrals, three limits and critical window.')
