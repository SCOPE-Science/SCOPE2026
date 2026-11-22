"""Supplementary finite checks for a seasonal Levins occupancy theorem.

The proof is analytical; these tests are not a substitute for its limiting arguments.
Run: python3 CHECK.py
"""
import math


def theta(u):
    if u <= 0:
        return 0.0
    if u >= 1:
        return 1.0
    a, b = -1/u, -1/(1-u)
    # Stable evaluation of exp(a)/(exp(a)+exp(b)).
    if a >= b:
        return 1/(1+math.exp(b-a))
    v = math.exp(a-b)
    return v/(1+v)


def ramp_additive(eps, rising, subdivisions=512):
    """Midpoint quadrature for additive inverse-occupancy increment.

    Zero integral of r across either symmetric ramp gives exact unit multiplier.
    """
    h = eps/subdivisions
    vals = [(-1+2*theta((j+0.5)/subdivisions))*(1 if rising else -1)
            for j in range(subdivisions)]
    assert abs(sum(vals)*h) < 1e-12
    tail = 0.0
    total = 0.0
    for v in reversed(vals):
        total += 2*h*math.exp(-tail-0.5*h*v)
        tail += h*v
    assert 2*eps*math.exp(-eps)-1e-14 <= total <= 2*eps*math.exp(eps)+1e-14
    return total


def cycle(y, H, F, eps):
    q = math.exp(H-F)
    B = ramp_additive(eps, True)
    E = ramp_additive(eps, False)
    eF = math.exp(-F)
    b = 2*q*(1-math.exp(-H))+2*(1-eF)+eF*B+E
    return q*y+b, b


def sequence(delta, count=120):
    y=3.0
    endpoints=[]
    errors=[]
    for n in range(1,count+1):
        H=n; F=n+delta; eps=2**(-n)
        assert F>0
        y,b=cycle(y,H,F,eps)
        endpoints.append(1/y)
        errors.append(abs(b-2*(1+math.exp(-delta))))
    return endpoints,errors


def main():
    for delta in (0.3, 0.6, 1.0, 2.0):
        vals, errs=sequence(delta)
        target=0.5*math.tanh(delta/2)
        assert abs(vals[-1]-target) < 1e-10,(delta,vals[-1],target)
        assert errs[-1] < 1e-12
    z,errs=sequence(0.0)
    assert abs(120*z[-1] - 0.25) < 0.005
    assert abs(120*z[-1] - 0.25) < abs(60*z[59] - 0.25)
    for delta in (-0.2,-0.5,-0.9):
        vals,_=sequence(delta)
        assert vals[-1] < vals[59] < vals[29]
        assert vals[-1] < 1e-7
    # The smooth ramp has exactly zero signed growth integral by symmetry.
    for n in range(1,16):
        eps=2**(-n)
        for u in (0.0,0.01,0.2,0.43,0.5,0.89,1.0):
            assert abs(theta(u)+theta(1-u)-1)<1e-12
        for rising in (True,False):
            ramp_additive(eps,rising)
    print('PASS: 4 supercritical, 1 critical, 3 subcritical long-season trajectories;')
    print('ramp reflection and additive bounds checked for 30 ramps;')
    print('critical example n*p(T_(n+1)) at n=120 =', format(120*z[-1],'.12g'))

if __name__=='__main__':
    main()
