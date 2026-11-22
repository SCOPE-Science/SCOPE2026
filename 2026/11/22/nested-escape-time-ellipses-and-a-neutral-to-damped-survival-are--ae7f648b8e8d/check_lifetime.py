"""Finite algebraic and quadrature diagnostics for exact lifetime-ellipse identities.

Usage: python3 check_lifetime.py. The infinite assertions require the proof.
"""
import math


def entries(k, t):
    if k == 0:
        d = t
        c = math.sin(2*t)/2
        h = (1-math.cos(2*t))/2
        return d-c, h, d+c
    q = math.exp(-2*k*t)
    d = -math.expm1(-2*k*t)/(2*k)
    c = (k*(1-q*math.cos(2*t))+q*math.sin(2*t))/(2*(1+k*k))
    h = (1-q*(math.cos(2*t)+k*math.sin(2*t)))/(2*(1+k*k))
    return d-c, h, d+c


def det_analytic(k, t):
    if k == 0:
        return t*t-math.sin(t)**2
    q = math.exp(-2*k*t)
    return ((1-q)**2-4*k*k*q*math.sin(t)**2)/(4*k*k*(1+k*k))


def simpson(f, t, n=12000):
    h = t/n
    return h/3*(f(0)+f(t)+4*sum(f((2*j-1)*h) for j in range(1,n//2+1))
                +2*sum(f(2*j*h) for j in range(1,n//2)))


def area(k, t):
    return math.pi/math.sqrt(det_analytic(k, t))


def survival(k, t):
    if k == 0:
        return area(k,t)
    q=math.exp(-2*k*t)
    b=1+2*k*k*math.sin(t)**2
    rad=1-2*q*b+q*q
    root=math.sqrt(rad)
    return 2*math.pi*k*math.sqrt(1+k*k)*q*(2*b-q)/(root*(1+root))


def close(actual, expected, tol=2e-8):
    assert math.isclose(actual,expected,rel_tol=tol,abs_tol=tol),(actual,expected)


def main():
    for k,t in [(0.0,.6),(0.0,3.2),(.3,.7),(.7,2.2),(1.4,5.7)]:
        a,b,c=entries(k,t)
        w=lambda s: math.exp(-2*k*s)
        q11=simpson(lambda s:2*w(s)*math.sin(s)**2,t)
        q12=simpson(lambda s:2*w(s)*math.sin(s)*math.cos(s),t)
        q22=simpson(lambda s:2*w(s)*math.cos(s)**2,t)
        for x,y in [(a,q11),(b,q12),(c,q22)]: close(x,y)
        close(a*c-b*b, det_analytic(k,t))
        assert det_analytic(k,t)>0
    for k in [0.,.25,1.5]:
        t=.002
        leading=math.pi*math.sqrt(3)*t**-2*(1+k*t)
        assert abs(area(k,t)/leading-1)<.003
    for k in [.4,1.2]:
        t=17.0
        a_inf=2*math.pi*k*math.sqrt(1+k*k)
        leading=a_inf*math.exp(-2*k*t)*(1+2*k*k*math.sin(t)**2)
        assert abs(survival(k,t)/leading-1)<2e-4
    for u in [.4,1.5,3.0]:
        for k in [.005,.002]:
            observed=survival(k,u/k)/k
            predicted=2*math.pi/math.expm1(2*u)
            assert abs(observed-predicted)<.002
    print('VERIFY_OK: Gram entries, area, small-time, damped tail, crossover')


if __name__ == '__main__':
    main()
