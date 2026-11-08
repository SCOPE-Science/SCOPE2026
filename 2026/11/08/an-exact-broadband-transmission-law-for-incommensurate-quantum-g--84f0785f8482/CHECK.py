"""Reproduce finite-array phase averages and limiting formulas.

Standard Python 3 only. This is a numerical diagnostic, not a proof of infinite-array
or equidistribution assertions.
"""
import math

def cheb_u(n, x):
    if n == 0:
        return 1.0
    u0, u1 = 1.0, 2.0*x
    if n == 1:
        return u1
    for _ in range(2, n+1):
        u0, u1 = u1, 2*x*u1-u0
    return u1

def mean_phase(n, b, a=280, c=420):
    acc = 0.0
    for i in range(a):
        phi = math.pi*(i+0.5)/a
        v = b*math.tan(phi)
        z = 1.0+v*v
        sub = 0.0
        for j in range(c):
            psi = math.pi*(j+0.5)/c
            u = cheb_u(n-1, math.sqrt(z)*math.cos(psi))
            sub += 1/(1+(z-1)*u*u)
        acc += sub/c
    return acc/a

def limit_g(b):
    if b < 1:
        L = b/math.sqrt(1-b*b)*math.asinh(math.sqrt(1-b*b)/b)
    elif b == 1:
        L = 1.0
    else:
        L = b/math.sqrt(b*b-1)*math.asin(math.sqrt(b*b-1)/b)
    return 1-2*L/math.pi

def main():
    checks=0
    for b in (0.25, 0.5, 1.0, 2.0):
        for n, expected in ((1,1/(1+b)),(2,1/(1+math.sqrt(2)*b))):
            got=mean_phase(n,b)
            assert abs(got-expected)<0.004, (b,n,got,expected)
            checks+=1
        n=30
        got=mean_phase(n,b,a=330,c=560)
        lim=limit_g(b)
        # Finite-size residual is not expected to vanish at N=30.
        assert abs(got-lim)<0.03, (b,got,lim)
        checks+=1
    for b in (1e-4,1e-5):
        actual=1-limit_g(b)
        leading=2*b*math.log(2/b)/math.pi
        assert abs(actual/leading-1)<0.001
        checks+=1
    for b in (1000,10000):
        actual=limit_g(b)
        leading=2/(math.pi*b)-1/(2*b*b)
        assert abs(actual/leading-1)<0.001
        checks+=1
    assert abs(limit_g(1)-(1-2/math.pi))<1e-14
    checks+=1
    print(f'PASS: {checks} deterministic quadrature and asymptotic checks')

if __name__=='__main__':
    main()
