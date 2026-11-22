"""Independent hyperboloid-metric checks for a regular-polygon slimness formula.

Run with Python 3: python verify.py
Only the Python standard library is required. Finite checks are supporting
checks; the infinite theorem follows from the accompanying geometric proof.
"""
from math import acosh, asinh, atan, atanh, cos, cosh, exp, isclose, pi, sin, sinh, sqrt, tanh


def formula(n, R):
    assert isinstance(n, int) and n >= 3 and R > 0
    a = pi / n
    s, c = sin(a), cos(a)
    b = s * sinh(R)
    angle = 2 * atan(c / (s * cosh(R)))
    return asinh(b if angle >= pi / 2 else b * sin(angle))


def critical(n):
    if n <= 4:
        return 0.0
    a = pi / n
    return asinh(sqrt(cos(2 * a)) / sin(a))


def dot(p, q):
    return -p[0] * q[0] + p[1] * q[1] + p[2] * q[2]


def vertex(R, angle):
    return (cosh(R), sinh(R) * cos(angle), sinh(R) * sin(angle))


def sub_scaled(a, b, c):
    return (a[0] - c * b[0], a[1] - c * b[1], a[2] - c * b[2])


def hyperboloid_distance_to_segment(p, u, v):
    """Exact 1-variable minimization, not a finite grid on the target edge."""
    ell = acosh(max(1., -dot(u, v)))
    w = tuple(q / sinh(ell) for q in sub_scaled(v, u, cosh(ell)))
    A, B = -dot(p, u), -dot(p, w)
    # Minimum of A cosh(t)+B sinh(t) on [0,ell].
    if B >= 0:
        x = A
    elif -B / A >= tanh(ell):
        x = -dot(p, v)
    else:
        x = sqrt(max(1., A * A - B * B))
    return acosh(max(1., x))


def geodesic_point(u, v, t):
    ell = acosh(max(1., -dot(u, v)))
    weights = sinh((1-t)*ell)/sinh(ell), sinh(t*ell)/sinh(ell)
    return tuple(weights[0] * u[i] + weights[1] * v[i] for i in range(3))


def direct_grid(n, R, count=50):
    a = pi/n
    vs = [vertex(R, 2*j*a-a) for j in range(n)]
    values = []
    for k in range(count+1):
        p = geodesic_point(vs[0], vs[1], k/count)
        d = min(hyperboloid_distance_to_segment(p,vs[j],vs[(j+1)%n]) for j in range(1,n))
        values.append(d)
    return max(values), values[count//2], values


def run():
    checks=0
    for n in (3,4,5,6,7,8,11,20,37):
        for R in (0.15,0.65,1.2,2.1,4.0):
            g, center, vals = direct_grid(n,R)
            target=formula(n,R)
            assert abs(center-target)<3e-10, (n,R,center,target)
            assert abs(g-target)<3e-10, (n,R,g,target)
            assert vals[0]<1e-5 and vals[-1]<1e-5
            checks+=3
        if n>=5:
            rc=critical(n)
            # At threshold the vertex and perpendicular-foot branches agree.
            a=pi/n; b=sin(a)*sinh(rc)
            angle=2*atan(cos(a)/(sin(a)*cosh(rc)))
            assert abs(angle-pi/2)<3e-14
            assert abs(formula(n,rc)-asinh(b))<3e-14
            checks+=2
        else:
            assert critical(n)==0.
            checks+=1
        # Smooth monotone approach to the regular ideal-polygon limit.
        a=pi/n; limit=asinh(2*cos(a)); coeff=4*cos(a)*(2/sin(a)**2-1)/sqrt(1+4*cos(a)**2)
        assert formula(n,5.0)<formula(n,6.0)<limit
        assert abs((limit-formula(n,9.0))*exp(18)/coeff-1)<1e-5
        checks+=2
    print('PASS:',checks,'hyperboloid endpoint, interior projection, threshold, and limit checks')


if __name__=='__main__':
    run()
