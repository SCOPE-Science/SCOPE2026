"""Independent numerical checks for the superelliptic polygon perimeter laws.

Requires Python 3, NumPy and SciPy. Run: python verify_perimeter.py
The tests corroborate finite instances; the asymptotic assertions need the proof.
"""
import math
import numpy as np
from scipy.integrate import quad


def boundary(p, n):
    theta = 2 * np.pi * np.arange(n) / n
    c, s = np.cos(theta), np.sin(theta)
    r = (np.abs(c) ** p + np.abs(s) ** p) ** (-1 / p)
    return np.column_stack((r * c, r * s))


def polygon_perimeter(p, n):
    x = boundary(p, n)
    return float(np.linalg.norm(x - np.roll(x, -1, axis=0), axis=1).sum())


def exact_curve_perimeter(p):
    def integrand(y):
        if y == 1:
            return 0.0
        return math.sqrt(1.0 + y ** (2*p-2) * (1-y**p) ** (2/p-2))
    ans, err = quad(integrand, 0, 1, points=[0, 1], limit=300,
                    epsabs=3e-12, epsrel=3e-12)
    assert err < 5e-10
    return 4 * ans


def q(p, a):
    b = a + 1
    F = lambda x, e: math.copysign(abs(x)**e, x) if x else 0.0
    integral = (F(b, 2*p-1)-F(a, 2*p-1))/(2*p-1)
    mean = (abs(b)**p-abs(a)**p)/p
    return 0.5 * (integral - mean*mean)


def S_approx(p, delta, J=6000):
    # For numerical reference only; the theorem uses an infinite convergent series.
    return sum(q(p, j-delta) for j in range(-J, J))


def curvature_density(theta, p):
    c, s = math.cos(theta), math.sin(theta)
    Q = c**p+s**p
    Q1 = p*(c*s**(p-1) - s*c**(p-1))
    Q2 = p*((p-1)*(s*s*c**(p-2)+c*c*s**(p-2)) - Q)
    r = Q**(-1/p)
    a = -Q1/(p*Q)
    b = ((p+1)*Q1*Q1)/(p*p*Q*Q)-Q2/(p*Q)
    return r * (1+2*a*a-b)**2/(1+a*a)**1.5


def smooth_limit(p):
    total, err = quad(lambda t: curvature_density(t, p),
                      0, math.pi/2, points=[0, math.pi/2],
                      limit=400, epsabs=2e-9, epsrel=2e-9)
    assert err < 2e-6
    return total/6


def main():
    count=0
    for n in (3,4,5,6,10,16,32,128,1024):
        observed=polygon_perimeter(2,n)
        expected=2*n*math.sin(math.pi/n)
        assert abs(observed-expected) < 2e-11
        count+=1
    assert abs(exact_curve_perimeter(2)-2*math.pi)<4e-12
    assert abs(smooth_limit(2)-math.pi/12)<4e-12
    count+=2

    p=1.25
    curve=exact_curve_perimeter(p)
    vals={d:S_approx(p,d) for d in (0, .25, .5)}
    assert 0 < vals[0] < vals[.25] < vals[.5]
    count+=1
    C={0:4*vals[0], 1: vals[0]+2*vals[.25]+vals[.5],
       2: 2*(vals[0]+vals[.5]), 3:vals[0]+2*vals[.25]+vals[.5]}
    for rem in range(4):
        errors=[]
        for base in (2048, 4096, 8192, 16384):
            n=base+rem
            h=2*math.pi/n
            observed=(curve-polygon_perimeter(p,n))/h**(2*p-1)
            errors.append(abs(observed-C[rem]))
            assert observed>0 and abs(observed-C[rem])<0.10*C[rem]
            count+=1
        assert errors[-1]<errors[0]
        count+=1
    assert C[0]<C[2]<C[1]
    count+=1

    p=1.5
    curve=exact_curve_perimeter(p)
    for n in (512,1024,2048,4096,8192):
        h=2*math.pi/n
        scaled=(curve-polygon_perimeter(p,n))/(h*h*math.log(n))
        assert abs(scaled-1/12)<0.004
        count+=1

    for p in (1.7, 2.5):
        curve=exact_curve_perimeter(p)
        target=smooth_limit(p)
        prev=None
        for n in (512,1024,2048):
            h=2*math.pi/n
            scaled=(curve-polygon_perimeter(p,n))/h**2
            assert abs(scaled-target)/target<.1
            if prev is not None:
                assert abs(scaled-target)<prev
            prev=abs(scaled-target)
            count+=1
    print(f"PASS: {count} numerical consistency checks; p<3/2 phase, p=3/2 log, p>3/2 smooth, circle exact.")
    print("p=1.25 approximate lattice coefficients:", {k:round(v,8) for k,v in C.items()})
    print("p=1.7 smooth coefficient:", smooth_limit(1.7))


if __name__=='__main__':
    main()
