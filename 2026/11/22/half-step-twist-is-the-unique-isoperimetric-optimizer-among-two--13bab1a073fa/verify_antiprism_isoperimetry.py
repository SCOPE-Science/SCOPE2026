"""Independent finite checks for an exact twisted-prismatoid isoperimetric theorem.

Requires Python 3, NumPy, and SciPy. Floating-point tests corroborate, not replace,
the analytical proof of the all-order/global theorem.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull


def invariants(n, radius, height, theta):
    beta = math.pi / n
    c = math.cos(beta)
    delta = min(theta % (2 * beta), 2 * beta - (theta % (2 * beta)))
    a = math.cos(beta - delta) - c
    area = 2 * n * radius**2 * math.sin(beta) * (c + math.hypot(height / radius, a))
    volume = n * radius**2 * height * math.sin(beta) * (c + a / 3)
    return area, volume


def vertices(n, radius, height, theta):
    return np.array([
        (radius * math.cos(2 * math.pi * k / n + j * theta),
         radius * math.sin(2 * math.pi * k / n + j * theta), j * height)
        for j in range(2) for k in range(n)
    ])


def optimal(n):
    beta = math.pi / n
    c = math.cos(beta)
    b = 1 - c
    t = c + math.sqrt(c*c + 3*b*b)
    y = math.sqrt(t*t-b*b)
    quotient = 72*n*math.sin(beta)*(c+t)**3/(y*y*(1+2*c)**2)
    return y, quotient


def main():
    checks = 0
    # Hull calculations do not use any face-area or volume formula from the theorem.
    for n in range(3, 19):
        beta = math.pi/n
        for f in (0, 0.13, 0.39, 0.63, 1, 1.37, 1.86):
            for r,h in ((1, 0.37), (1.41, 0.91), (0.83, 2.28)):
                theta = beta*f
                poly = ConvexHull(vertices(n,r,h,theta))
                s,v = invariants(n,r,h,theta)
                assert math.isclose(s,poly.area,rel_tol=5e-11,abs_tol=3e-11)
                assert math.isclose(v,poly.volume,rel_tol=5e-11,abs_tol=3e-11)
                checks += 2

    # Equality, strictness and independent dense shape-mesh comparisons.
    for n in range(3,101):
        y,q = optimal(n)
        b = math.pi/n
        s,v = invariants(n,1,y,b)
        assert math.isclose(s**3/v**2,q,rel_tol=5e-13)
        checks += 1
        for f in (0,0.1,0.3,0.5,0.7,0.9,1):
            for scale in (0.30,0.62,0.87,1.0,1.15,1.64,3.1):
                t = y*scale
                ss,vv = invariants(n,1,t,b*f)
                qi = ss**3/vv**2
                assert qi >= q-1e-9
                if f != 1 or scale != 1:
                    assert qi > q+1e-9
                checks += 1
    # Closed endpoint and continuum asymptotics.
    assert math.isclose(optimal(3)[0],math.sqrt(2),rel_tol=1e-14)
    assert math.isclose(optimal(3)[1],108*math.sqrt(3),rel_tol=1e-14)
    checks+=2
    for n in (4,5,8,16,100,1000):
        c=math.cos(math.pi/n)
        uniform_y=math.sqrt(2*(1-c)*(1+2*c))
        assert optimal(n)[0] > uniform_y
        checks+=1
    assert abs(optimal(10000)[0]-2)<2e-5
    assert abs(optimal(10000)[1]-54*math.pi)<1e-5
    checks+=2
    print('TWISTED_PRISMATOID_ISOPERIMETRY_OK',checks)

if __name__ == '__main__':
    main()
