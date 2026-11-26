#!/usr/bin/env python3
import math

X0 = math.sqrt(3.0/5.0)
T0 = math.atan(X0)
TARGET = 0.6390804227921295

def original_product(u, v):
    return ((2.0*math.cos(2.0*u+v)+math.cos(v))
            *(math.cos(u)+2.0*math.cos(u+2.0*v))
            *(math.cos(v-u)+2.0*math.cos(u+v)))

def qpoly(x, y):
    return (3.0-x*y)*(3.0-x*x-4.0*x*y)*(3.0-y*y-4.0*x*y)

def check_factorization():
    grid = (-1.2, -0.7, -0.2, 0.15, 0.55, 1.1)
    worst = 0.0
    for u in grid:
        for v in grid:
            x, y = math.tan(u), math.tan(v)
            lhs = original_product(u, v)
            rhs = qpoly(x, y)/((1.0+x*x)**2*(1.0+y*y)**2)
            worst = max(worst, abs(lhs-rhs))
    assert worst < 2e-14, worst
    return worst

def roots(x):
    rA = 3.0/x
    rB = (3.0-x*x)/(4.0*x)
    root = math.sqrt(4.0*x*x+3.0)
    cm = -2.0*x-root
    cp = -2.0*x+root
    return cm, cp, rB, rA

def check_ordering():
    cm, cp, rB, rA = roots(0.5*X0)
    assert cm < cp < rB < rA
    cm, cp, rB, rA = roots(2.0*X0)
    assert cm < rB < cp < rA
    x = X0
    cm, cp, rB, rA = roots(x)
    assert abs(cp-rB) < 2e-15

def angular_length_x(x):
    if x == 0.0:
        return 2.0*math.pi/3.0
    if x < X0:
        return math.pi-math.atan(math.sqrt(4.0*x*x+3.0))+math.atan(x)
    return (math.atan(3.0/x)
            +math.atan((3.0-x*x)/(4.0*x))
            +math.atan(x))

def ft(t):
    if t <= 0.0:
        return 2.0*math.pi/3.0
    if t >= math.pi/2.0:
        return 0.0
    return angular_length_x(math.tan(t))

def simpson(a, b, n):
    assert n % 2 == 0
    h = (b-a)/n
    total = ft(a)+ft(b)
    for j in range(1, n):
        total += (4.0 if j % 2 else 2.0)*ft(a+j*h)
    return total*h/3.0

def density(n):
    left = simpson(0.0, T0, n//2)
    right = simpson(T0, math.pi/2.0, n//2)
    return 2.0*(left+right)/(math.pi*math.pi)

def main():
    worst = check_factorization()
    check_ordering()
    p1 = density(1 << 12)
    p2 = density(1 << 14)
    assert abs(p1-p2) < 1e-11, (p1,p2)
    assert abs(p2-TARGET) < 2e-13, p2
    print('VERIFY_OK factor_error={:.3e} density={:.15f}'.format(worst,p2))

if __name__ == '__main__':
    main()
