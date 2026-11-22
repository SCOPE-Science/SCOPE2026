"""Reproduce exact-geometry diagnostics for Reuleaux nearest-corner distances.

Python >=3.9; standard library only. These tests corroborate the proof, not
replace its all-radii polar and Voronoi arguments.
"""
import math
import random

PI = math.pi
AREA = (PI - math.sqrt(3.0)) / 2
R0 = math.sqrt(2 - math.sqrt(3.0))
R = 1 / math.sqrt(3.0)
VERTICES = ((0.0, R), (-0.5, -R/2), (0.5, -R/2))


def phi(r):
    return math.acos(r/2) - PI/6


def alpha(r):
    return math.acos(1/(2*r))


def angle_length(r):
    if r <= 0 or r >= R:
        return 0.0 if r else 2*PI/3
    if r <= 0.5:
        return 2*phi(r)
    if r <= R0:
        return 2*(phi(r) - 2*alpha(r))
    return PI/3 - 2*alpha(r)


def H(r):
    return r*r*phi(r)/2 + math.asin(r/2) - r*math.sqrt(4-r*r)/4


def Q(r):
    if r < 0.5:
        raise ValueError('Q only defined for r >= 1/2')
    return r*r*alpha(r)/2 - math.sqrt(4*r*r-1)/8


def cdf(r):
    if r <= 0:
        return 0.0
    if r >= R:
        return 1.0
    if r <= 0.5:
        value = 2*H(r)
    elif r <= R0:
        value = 2*H(r) - 4*Q(r)
    else:
        value = (2*H(R0)-2*Q(R0)+PI*(r*r-R0*R0)/6-2*Q(r))
    return 3*value/AREA


def density(r):
    return 3*r*angle_length(r)/AREA


def simpson(function, a, b, steps=10000):
    if b <= a:
        return 0.0
    steps += steps % 2
    h = (b-a)/steps
    total = function(a) + function(b)
    for k in range(1, steps):
        total += (4 if k % 2 else 2)*function(a+k*h)
    return h*total/3


def measured_angle(r, num=30000):
    # Independent geometric inequalities, not the angular-length formulas.
    if r <= 0:
        return 2*PI/3
    count = 0
    for i in range(num):
        t = -PI/3 + (i+0.5)*(2*PI/3)/num
        x, y = r*math.sin(t), r*math.cos(t)
        in_disks = ((x-0.5)**2+(y-math.sqrt(3)/2)**2 <= 1
                    and (x+0.5)**2+(y-math.sqrt(3)/2)**2 <= 1)
        near_origin = (x*x+y*y <= (x-0.5)**2+(y-math.sqrt(3)/2)**2
                       and x*x+y*y <= (x+0.5)**2+(y-math.sqrt(3)/2)**2)
        if in_disks and near_origin:
            count += 1
    return (2*PI/3)*count/num


def main():
    assert 0.5 < R0 < R
    assert abs(alpha(R0)-PI/12)<1e-13
    assert abs(phi(R0)-PI/4)<1e-13
    assert abs(alpha(R)-PI/6)<1e-13
    assert abs(R0**2+1/R0**2-4)<1e-12
    assert abs(cdf(R)-1)<1e-14

    # Exact primitive relations checked numerically, at many radii.
    for k in range(1, 501):
        r = .02+(.5-.02)*k/501
        h = 2e-6
        assert abs((H(r+h)-H(r-h))/(2*h)-r*phi(r))<1e-8
        r = .505+(.57-.505)*k/501
        assert abs((Q(r+h)-Q(r-h))/(2*h)-r*alpha(r))<1e-8

    # Quadrature integrates each smooth regime separately to avoid the
    # sqrt contact at one-half and the disappearing outer angular band.
    splits = (0, .5, R0, R)
    mass = 0
    for a, b in zip(splits[:-1], splits[1:]):
        portion = simpson(density, a, b, 20000)
        mass += portion
        assert abs(portion-(cdf(b)-cdf(a)))<2e-7
    assert abs(mass-1)<2e-7

    for r in [0.05,0.25,0.49,0.5,0.501,0.51,R0,0.53,0.55,0.575]:
        assert abs(measured_angle(r)-angle_length(r)) < 0.00016

    # The one-sided second-derivative jump is 24/A, computed as a
    # derivative of the explicit angular branches at the transition.
    jump = (6*R0/AREA)*(1/(R0*math.sqrt(4*R0**2-1))
                              + 1/math.sqrt(4-R0**2))
    assert abs(jump-24/AREA)<1e-12
    for eps in [1e-4,2e-5,3e-6]:
        difference = (cdf(0.5+eps)-6*H(0.5+eps)/AREA)
        assert abs(difference / eps**1.5+8/AREA) < 0.08
    for eps in [0.01, 0.002, 0.0004]:
        assert abs((1-cdf(R-eps))/eps**2-3*math.sqrt(3)/AREA)<0.16

    # Independent planar sampler: X uniform on K by rejection from its
    # enclosing axis-aligned rectangle; evaluate nearest of three centers.
    rng = random.Random(931070)
    distances=[]
    for _ in range(300000):
        x = rng.uniform(-.5,.5)
        y = rng.uniform(R-1,R)
        d2=[(x-vx)**2+(y-vy)**2 for vx,vy in VERTICES]
        if max(d2) <= 1:
            distances.append(math.sqrt(min(d2)))
    assert len(distances)>210000
    for r in [0.2,0.4,0.5,0.505,R0,0.53,0.55,0.57]:
        empirical = sum(v<=r for v in distances)/len(distances)
        expected = cdf(r)
        assert abs(empirical-expected)<0.004

    print('REULEAUX_NEAREST_VERTEX_DISTRIBUTION_OK')
    print('number_uniform_points',len(distances))
    print('area',format(AREA,'.15f'))
    print('transition_radii',format(0.5,'.15f'),format(R0,'.15f'))
    print('support_maximum',format(R,'.15f'))
    print('CDF_at_transitions',format(cdf(.5),'.15f'),format(cdf(R0),'.15f'))
    print('second_derivative_jump',format(24/AREA,'.15f'))
    print('upper_tail_coefficient',format(3*math.sqrt(3)/AREA,'.15f'))

if __name__=='__main__':
    main()
