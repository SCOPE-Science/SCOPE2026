"""Numerical and exact-arithmetic diagnostics for quartic Lamé boundary triangles.
Run: python verify.py. Requires scipy and sympy.
The analytical small-area limit is proved in RESULT.md, not by this script.
"""
import math
from fractions import Fraction
from scipy.integrate import quad
from scipy.special import gamma


def polynomial_area(y):
    x = [1 - z**4/Fraction(4) for z in y]
    return abs((x[1]-x[0])*(y[2]-y[0])-(x[2]-x[0])*(y[1]-y[0])) / 2


def homogeneous_area(y):
    z = sorted(y)
    a, b = z[1]-z[0], z[2]-z[1]
    mean = sum(z)/3
    return a*b*(a+b)*(6*mean**2+(a*a+a*b+b*b)/3)/8


# Exact rational arithmetic and two independent evaluations of the area.
n = 0
for j in range(-3,4):
    for k in range(j+1,5):
        for l in range(k+1,6):
            y = [Fraction(j, 3), Fraction(k, 4), Fraction(l, 5)]
            if len(set(y)) < 3:
                continue
            assert polynomial_area(y) == homogeneous_area(y), (y, polynomial_area(y), homogeneous_area(y))
            n += 1
assert n >= 50


def polar_terms(t):
    c, s = math.cos(t), math.sin(t)
    q = c**4+s**4
    return q**(-0.25), c*s*(c*c-s*s)*q**(-1.25)


def speed_polar(t):
    r, rp = polar_terms(t)
    return math.hypot(r, rp)

L = 4*quad(speed_polar,0,math.pi/2,epsabs=2e-12)[0]
# Check perimeter via an independent first-quadrant implicit-graph integral.
# Use y=(sin t)**(1/2) to regularize the lower endpoint only; instead,
# integrate along x/y symmetric half quadrants via implicit y'(x).
def speed_graph(x):
    if x<=0: return 1.0
    return math.hypot(1.0, x**3/(1-x**4)**0.75)
L_graph = 4*quad(speed_graph,0,1,epsabs=5e-9,limit=500)[0]
assert abs(L-L_graph)<2e-7, (L, L_graph)

J=quad(lambda z: (z*(1-z))**(-0.6)*(1-z+z*z)**(-0.1),
       0,1,epsabs=1e-10,limit=500)[0]
I=2*8**0.6*math.sqrt(math.pi/6)*gamma(0.1)/gamma(0.6)*3**0.1*J

# Independently integrate the exact gap/mean sublevel geometry, without
# using the Gamma function expression or the w-integral.
def gap_integral(z):
    q=(1-z+z*z)/3
    zz=z*(1-z)
    R=(8/(zz*q))**0.2
    def integrand(w):
        if w==0: return 0.0
        r=R*w*w
        upper=math.sqrt(max(0,(8/(r**3*zz)-r*r*q)/6))
        return 24*R*w*r*upper
    return quad(integrand,0,1,epsabs=1e-9,limit=200)[0]
I_gap=quad(gap_integral,0,1,epsabs=5e-7,limit=150)[0]
assert abs(I-I_gap)/I < 1e-9, (I,I_gap)
C=4*I/L**3
assert 7.0176 < L < 7.0178
assert 153.74 < I < 153.75
assert 1.7793 < C < 1.7795
print('exact-rational identities passed:',n)
print('perimeter L:', format(L,'.14g'), 'independent chart:',format(L_graph,'.14g'))
print('homogeneous sublevel volume I:',format(I,'.14g'), 'gap-integral:',format(I_gap,'.14g'))
print('probability constant C=4I/L**3:', format(C,'.14g'))
print('All diagnostics passed. Numerical checks are not an infinite-limit proof.')
