"""Standalone numerical consistency checks for spherical triangle anisotropy constants."""
import math
import random


def quad(n):
    # Midpoint integration on the triangular domain 0 < x < kappa < pi.
    total = moment = sq = triple = 0.0
    for i in range(n):
        k = math.pi * (i + 0.5) / n
        step = k / n
        sk = math.sin(k)
        for j in range(n):
            x = step * (j + 0.5)
            y = k - x
            sx, sy = math.sin(x), math.sin(y)
            v = math.sqrt(sk * sx * sy) * (math.pi / n) * step
            cx, cy, cw = math.cos(x), math.cos(y), math.cos(math.pi - k)
            total += v
            moment += v * cx
            sq += v * (cx * cx + cy * cy + cw * cw)
            triple += v * cx * cy * cw
    return total, moment / total, sq / total, triple / total


def leg2(x):
    return (3*x*x - 1)/2


def consistency():
    I, m, s, tri = quad(450)
    c0 = math.pi * math.gamma(1.75) / (16 * math.gamma(1.25)**3)
    assert abs(math.sqrt(2)*I/(4*math.pi) - c0) < 0.00012
    assert abs(m-0.4296991136262733) < 0.00012
    assert abs(s-1.25) < 0.00012
    assert abs(tri+0.125) < 0.00012
    cube = (2-3*s-9*tri)/35
    assert abs(cube+1/56) < 0.00008
    print('quadrature:', 'C*=', c0, 'm=',m, 'E(sum cos^2)=',s, 'cubic=',cube)


def monte_carlo_rotations():
    # Independently check Haar rotational averages with an importance proposal.
    rng = random.Random(17429)
    a = b = weight = 0.0
    N = 240000
    for _ in range(N):
        t1 = rng.random()*math.pi
        t2 = rng.random()*math.pi
        k, x = max(t1,t2), min(t1,t2)
        y=k-x
        w = math.sqrt(math.sin(x)*math.sin(y)*math.sin(k))
        z=2*rng.random()-1
        phi=2*math.pi*rng.random()
        h=math.sqrt(1-z*z)
        nx,ny = h*math.cos(phi), h*math.sin(phi)
        projections = (nx, nx*math.cos(k)+ny*math.sin(k),-nx*math.cos(x)-ny*math.sin(x))
        dip=math.prod(1+0.65*p for p in projections)
        quad=math.prod(1+1.0*leg2(p) for p in projections)
        weight += w
        a += w*dip
        b += w*quad
    dip_est = a/weight
    quad_est = b/weight
    dip_expected = 1-0.4296991136262733*(0.65**2)
    quad_expected = 1+3/40-1/56
    print('Haar diagnostics:',dip_est,dip_expected,quad_est,quad_expected)
    assert abs(dip_est-dip_expected)<0.019
    assert abs(quad_est-quad_expected)<0.019


if __name__ == '__main__':
    consistency()
    monte_carlo_rotations()
    print('VERIFY_OK')
