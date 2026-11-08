"""Independent numerical checks of the right-tetrahedron angle-sum optimum.

Uses only Python's standard library. Results corroborate, but do not replace,
proofs involving exact derivatives and their signs.
"""
import math
import random

PI = math.pi
CHECKS = 0


def ck(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])


def norm(a):
    return math.sqrt(dot(a, a))


def cone_angle(u, v, w):
    """Normalized solid angle from the independent trihedral determinant formula."""
    volume = abs(dot(u, cross(v, w)))
    denominator = (norm(u)*norm(v)*norm(w)
                   + dot(u,v)*norm(w) + dot(v,w)*norm(u)
                   + dot(w,u)*norm(v))
    return math.atan2(volume, denominator) / (2*PI)


def vertex_angle_sum(a, b, c):
    verts = [(0., 0., 0.), (a, 0., 0.), (0., b, 0.), (0., 0., c)]
    result = 0.
    for i in range(4):
        vecs = [tuple(verts[j][k] - verts[i][k] for k in range(3))
                for j in range(4) if j != i]
        result += cone_angle(*vecs)
    return result


def gram_sum(a, b, c):
    inv = [1/a, 1/b, 1/c]
    q = math.sqrt(sum(x*x for x in inv))
    return .5 - sum(math.asin(x/q) for x in inv)/(2*PI)


def sum_at_ratio(R, t):
    """For side lengths (1,R/t,R), with 1 <= t <= R."""
    q = math.sqrt(R*R+t*t+1.)
    return .5 - (math.asin(R/q)+math.asin(t/q)+math.asin(1/q))/(2*PI)


def stationarity(R, t):
    return (R*t/math.hypot(t,1) + t/math.hypot(R,t)
            - math.hypot(R,1))


def optimum(R):
    low, high = 1., R
    ck(stationarity(R,low)<0, 'left derivative')
    ck(stationarity(R,high)>0, 'right derivative')
    for _ in range(100):
        m=(low+high)/2
        if stationarity(R,m)<0:
            low=m
        else:
            high=m
    return (low+high)/2


def stable_sum_at_ratio(R, t):
    # Arcsine cancellation is removed by the identity arcsin(x)=atan(x/sqrt(1-x*x)).
    excess = (math.atan2(t, math.hypot(R,1))
              + math.atan2(1., math.hypot(R,t))
              - math.atan2(math.hypot(t,1), R))
    return .25 - excess/(2*PI)

rng = random.Random(71589)
for _ in range(4000):
    a,b,c = [math.exp(rng.uniform(-5,5)) for j in range(3)]
    ck(abs(vertex_angle_sum(a,b,c)-gram_sum(a,b,c)) < 2e-12,
       'Gram Euler vs trihedral determinant')
for R in (1.0001,1.01,1.2,1.5,2,3,5,10,20,50,100,1000):
    t = optimum(R)
    ck(1<t<R, 'unique internal stationary location')
    ck(abs(stationarity(R,t)) < 1e-11, 'stationary root')
    m = stable_sum_at_ratio(R,t)
    ck(abs(m-sum_at_ratio(R,t))<3e-13, 'stable expression matches Gram')
    ck(m<sum_at_ratio(R,1), 'beats left boundary')
    ck(m<sum_at_ratio(R,R), 'beats right boundary')
    for j in range(100):
        tj = 1+(R-1)*j/99
        ck(m <= stable_sum_at_ratio(R,tj)+1e-14,
           'global minimization on a deterministic mesh')
for R in (10**3, 10**4, 10**5, 10**6):
    t=optimum(R)
    b=R/t
    ck(abs(b/((2*R)**(1/3))-1) < .02,
       'cube-root optimal intermediate length')
    corrected=((stable_sum_at_ratio(R,t) - .25 + 1/(2*PI*R))
               *R**(5/3))
    coefficient=3*2**(-5/3)/(2*PI)
    ck(abs(corrected/coefficient-1) < .06,
       'sharp fractional-power angle-sum correction')
print('ANGLE_SUM_OK', CHECKS)
