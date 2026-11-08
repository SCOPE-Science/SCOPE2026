"""Deterministic finite checks for shared-clock Rabi-spin renewal purity."""
import cmath
import math

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def close(a, b, tol=1e-9):
    check(abs(a-b) <= tol * max(1., abs(a), abs(b)), f"different: {a} {b}")

def mk(k, omega, mean, characteristic):
    if k == 0:
        return complex(1, 0)
    return (characteristic(2 * k * omega) - 1) / (2j * k * omega * mean)

def purity(n, omega, mean, characteristic):
    w0 = math.exp(math.lgamma(2*n+1)-2*math.lgamma(n+1)-2*n*math.log(2))
    out = w0
    for k in range(1, n+1):
        weight = math.exp(math.lgamma(2*n+1)-math.lgamma(n+k+1)-math.lgamma(n-k+1)-2*n*math.log(2))
        out += 2*weight*abs(mk(k, omega, mean, characteristic))**2
    return out

def base(n):
    return math.exp(math.lgamma(2*n+1)-2*math.lgamma(n+1)-2*n*math.log(2))

def phi_deterministic(t):
    return lambda w: cmath.exp(1j*w*t)

def phi_exp(rate):
    return lambda w: rate/(rate-1j*w)

def phi_two(a, b, p):
    return lambda w: (1-p)*cmath.exp(1j*w*a) + p*cmath.exp(1j*w*b)

def quad(n, omega, length, m=300):
    vals=[(j+.5)*length/m for j in range(m)]
    return sum(math.cos(omega*(a-b))**(2*n) for a in vals for b in vals)/(m*m)

def coeff(omega, mean, characteristic, upto):
    return 1+2*sum(abs(mk(k, omega, mean, characteristic))**2 for k in range(1, upto+1))

def run():
    omega=1.3
    tau=math.pi/omega
    for n in (1, 2, 3, 8, 32, 120):
        close(purity(n, omega, tau, phi_deterministic(tau)), base(n), 1e-12)
        close(purity(n, omega, 2*tau, phi_deterministic(2*tau)), base(n), 1e-12)
        check(purity(n, omega, .7*tau, phi_deterministic(.7*tau)) > base(n) + 1e-9, 'strict')
    for n in (1,2,3):
        length=.72*tau
        close(purity(n, omega, length, phi_deterministic(length)), quad(n, omega, length), 2e-5)
    for rate in (.4, 1.2, 3.):
        close(purity(1, omega, 1/rate, phi_exp(rate)), .5*(1+rate**2/(rate**2+4*omega**2)), 1e-11)
        x=math.pi*rate/(2*omega)
        target=x/math.tanh(x)
        close(coeff(omega, 1/rate, phi_exp(rate), 25000), target, 5e-5)
        for n in (2000, 10000):
            approx=math.sqrt(math.pi*n)*purity(n, omega, 1/rate, phi_exp(rate))
            close(approx, target, 0.035)
    mu=.4*tau
    for eps in (.05*tau, .005*tau, .0005*tau):
        p=(mu-eps)/(tau-eps)
        characteristic=phi_two(eps, tau, p)
        check(purity(7, omega, mu, characteristic)>base(7), 'not attained')
        close(purity(7, omega, mu, characteristic), base(7), 2.2*eps/tau)
        direct=tau*(eps+(tau-eps)*p*p)/(mu*mu)
        close(coeff(omega, mu, characteristic, 15000), direct, 0.001)
    for mu in (tau, 1.7*tau, 4.3*tau):
        j=int(mu/tau)
        p=mu/tau-j
        char=phi_two(j*tau, (j+1)*tau, p)
        for n in (1,7,37):
            close(purity(n, omega, mu, char), base(n), 1e-11)
    print(f"PASS {CHECKS} deterministic checks; no infinite proof inferred")

if __name__ == '__main__':
    run()
