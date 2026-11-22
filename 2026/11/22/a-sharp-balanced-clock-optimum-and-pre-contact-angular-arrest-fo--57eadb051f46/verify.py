"""Reproduce the equilateral quartic-circle physical-time calculations."""
import math
from scipy.integrate import quad

SQ3 = math.sqrt(3.0)
V = SQ3 / 2.0
KAPPA = 2.0 / SQ3
CENTERS = ((0.0, 0.0), (1.0, 0.0), (0.5, V))


def vector(x, y, radius, lam, mu):
    f = [(x-a)**2 + (y-b)**2 - radius**2 for a,b in CENTERS]
    aa = (-lam-mu+KAPPA*(-V*x-y/2.0-V),
          lam+KAPPA*(V*x-y/2.0), mu+KAPPA*y)
    xx = sum(-aa[k]*f[(k+1)%3]*f[(k+2)%3]*(y-CENTERS[k][1]) for k in range(3))
    yy = sum(aa[k]*f[(k+1)%3]*f[(k+2)%3]*(x-CENTERS[k][0]) for k in range(3))
    return xx,yy


def period_formula(w, radius):
    def integrand(t):
        return 1.0 / ((w-KAPPA*radius*math.cos(t))
                      *(1-2*radius*math.cos(t+math.pi/6))
                      *(1-2*radius*math.cos(t-math.pi/6)))
    return quad(integrand, -math.pi, math.pi, epsrel=3e-11)[0]


def period_from_field(k, radius, lam, mu):
    a,b = CENTERS[k]
    def integrand(t):
        x = a+radius*math.cos(t)
        y = b+radius*math.sin(t)
        px,py = vector(x,y,radius,lam,mu)
        speed = (-math.sin(t)*px+math.cos(t)*py)/radius
        assert speed > 0.0
        return 1.0/speed
    return quad(integrand, -math.pi, math.pi, epsrel=3e-11)[0]


def run():
    n=0
    for radius in (0.04, 0.11, 0.21, 0.27):
        for lam,mu in ((-2/3,-2/3),(-2/3+0.004,-2/3)):
            w = (-lam-mu-1,lam+1,mu+1)
            assert all(x>KAPPA*radius for x in w)
            for k in range(3):
                p = period_from_field(k,radius,lam,mu)
                q = period_formula(w[k],radius)
                assert abs(p-q) < 1e-9*max(p,q)
                n+=1
        assert period_formula(1/3-0.01,radius)>period_formula(1/3,radius)
        assert period_formula(1/3+0.01,radius)<period_formula(1/3,radius)
    rc = SQ3/6
    target = 12*math.pi/3**0.25
    errors=[]
    for d in (1e-2,1e-3,1e-4,1e-5):
        ratio = period_formula(1/3,rc-d)*math.sqrt(d)
        errors.append(abs(ratio-target))
    assert all(errors[i+1] < errors[i] for i in range(len(errors)-1))
    assert errors[-1]/target<0.01
    print('PASS: 24 full-field/closed-quadrature comparisons; 8 strict monotonicity checks; four threshold-asymptotic scales')

if __name__ == '__main__':
    run()
