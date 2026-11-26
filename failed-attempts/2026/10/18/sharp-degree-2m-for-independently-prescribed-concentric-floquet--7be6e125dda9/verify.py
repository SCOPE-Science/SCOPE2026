"""Standalone numerical/algebraic checks for concentric polynomial-cycle synthesis.

Requires Python >=3.9 standard library only.  The all-parameter proof is in RESULT.md.
"""
import math
from functools import reduce


def polynomial_product(p, q):
    r = [0.0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def polynomial_value(p, x):
    return sum(c * x ** i for i, c in enumerate(p))


def interpolate(nodes, values):
    result = [0.0] * len(nodes)
    for i, a in enumerate(nodes):
        p, denom = [1.0], 1.0
        for j, b in enumerate(nodes):
            if i != j:
                p = polynomial_product(p, [-b, 1.0])
                denom *= a - b
        for k, coefficient in enumerate(p):
            result[k] += values[i] * coefficient / denom
    return result


def poly_xy_add(dst, powers, coefficient):
    for j in range(powers + 1):
        c = coefficient * math.comb(powers, j)
        dst[(2 * j, 2 * (powers - j))] = dst.get((2 * j, 2 * (powers - j)), 0) + c


def construct(radii, omegas, logs):
    m = len(radii)
    s = [a * a for a in radii]
    h = reduce(polynomial_product, ([-z, 1.0] for z in s), [1.0])
    hp = [math.prod(s[i] - s[j] for j in range(m) if j != i) for i in range(m)]
    c = 1.0 + max(abs(logs[i]) * omegas[i] / (4 * math.pi * radii[i] * abs(hp[i])) for i in range(m))
    w = [-logs[i] * omegas[i] / (4 * math.pi * c * radii[i] * hp[i]) for i in range(m)]
    av = [omegas[i] * (1 + w[i] ** 2) / (1 - w[i] ** 2) for i in range(m)]
    bv = [2 * omegas[i] * w[i] / (radii[i] * (1 - w[i] ** 2)) for i in range(m)]
    ap = interpolate(s, av)
    bp = interpolate(s, bv)
    return c, h, hp, w, ap, bp


def simpson(fun, n=4096):
    assert n % 2 == 0
    d = 2 * math.pi / n
    total = fun(0.0) + fun(2 * math.pi)
    for k in range(1, n):
        total += (4 if k % 2 else 2) * fun(k * d)
    return d * total / 3


def check_case(m, pattern):
    radii = [float(j + 1) for j in range(m)]
    omegas = [0.75 + 0.31 * j for j in range(m)]
    logs = [(-(0.4 + j * 0.22) if pattern == 'all_attracting' else (-1) ** j * (0.3 + j * 0.19)) for j in range(m)]
    c, h, hp, w, ap, bp = construct(radii, omegas, logs)
    assert len(ap) == len(bp) == m and len(h) == m + 1
    assert all(abs(z) < 1 for z in w)
    for i, radius in enumerate(radii):
        a, b, om = polynomial_value(ap, radius**2), polynomial_value(bp, radius**2), omegas[i]
        assert a > radius * abs(b)
        assert abs(math.sqrt(a*a-radius*radius*b*b) - om) < 2e-8
        period = simpson(lambda theta: 1/(a+radius*b*math.cos(theta)))
        predicted_lambda = 2*c*radius*hp[i]*simpson(lambda theta: math.cos(theta)/(a+radius*b*math.cos(theta)))
        assert abs(period - 2*math.pi/om) < 3e-7
        assert abs(predicted_lambda - logs[i]) < 4e-7
        assert abs(polynomial_value(h, radius*radius)) < 1e-6 * max(1., abs(radius**(2*m)))
    # Expand the Cartesian polynomials in x,y and check that highest monomial degree is 2m.
    px, qy = {}, {}
    for k, coef in enumerate(h):
        for j in range(k+1):
            pair=(2*j,2*(k-j))
            px[pair]=px.get(pair,0.0)+c*coef*math.comb(k,j)
    for k, coef in enumerate(ap):
        for j in range(k+1):
            cc=coef*math.comb(k,j)
            ex,ey=2*j,2*(k-j)
            px[(ex,ey+1)]=px.get((ex,ey+1),0.0)-cc
            qy[(ex+1,ey)]=qy.get((ex+1,ey),0.0)+cc
    for k, coef in enumerate(bp):
        for j in range(k+1):
            cc=coef*math.comb(k,j)
            ex,ey=2*j,2*(k-j)
            px[(ex+1,ey+1)]=px.get((ex+1,ey+1),0.0)-cc
            qy[(ex+2,ey)]=qy.get((ex+2,ey),0.0)+cc
    assert max(ex+ey for (ex,ey), v in list(px.items())+list(qy.items()) if abs(v)>1e-12)==2*m
    # Orthogonality of tangent terms, with no assumption of radial symmetry.
    for radius in radii:
        for theta in (0.0, 0.3, 1.7, 2.6, 4.2):
            x, y = radius*math.cos(theta), radius*math.sin(theta)
            p=sum(v*x**ex*y**ey for (ex,ey),v in px.items())
            q=sum(v*x**ex*y**ey for (ex,ey),v in qy.items())
            scale=max(1.0,abs(p*radius),abs(q*radius))
            assert abs(x*p+y*q)<scale*3e-6
    return m


def run_poincare_check():
    """Independently integrate the *nonlinear* polar equation through one turn."""
    m = 2
    radii = [1.0, 2.0]
    omegas = [1.0, 1.4]
    logs = [-0.3, -0.7]  # two neighboring attracting circles, nonalternating
    c, h, hp, w, ap, bp = construct(radii, omegas, logs)

    def dr_dtheta(theta, r):
        s = r*r
        f = polynomial_value(h, s)
        cos, sin = math.cos(theta), math.sin(theta)
        numerator = c * f * cos
        denominator = polynomial_value(ap, s) + r * cos * polynomial_value(bp, s) - c*f*sin/r
        return numerator/denominator

    for i, radius in enumerate(radii):
        delta = 1.0e-7
        r = radius + delta
        steps = 8192
        dt = 2*math.pi/steps
        for j in range(steps):
            theta=j*dt
            k1=dr_dtheta(theta,r)
            k2=dr_dtheta(theta+dt/2,r+dt*k1/2)
            k3=dr_dtheta(theta+dt/2,r+dt*k2/2)
            k4=dr_dtheta(theta+dt,r+dt*k3)
            r += dt*(k1+2*k2+2*k3+k4)/6
        observed=(r-radius)/delta
        predicted=math.exp(logs[i])
        assert abs(observed-predicted)<1.0e-4, (observed,predicted)


if __name__ == '__main__':
    checks=0
    for n in range(1, 6):
        for stability_pattern in ('alternating', 'all_attracting'):
            check_case(n, stability_pattern)
            checks+=n
    run_poincare_check()
    print(f'VERIFY_OK: {checks} period, Floquet and circle conditions; 10 polynomial degree checks; 2 nonlinear Poincare returns')
