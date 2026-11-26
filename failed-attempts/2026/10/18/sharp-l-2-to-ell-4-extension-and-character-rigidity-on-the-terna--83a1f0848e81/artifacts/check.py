#!/usr/bin/env python3
"""Reproduce algebraic identities and finite Fourier checks for a ternary split conic."""
import cmath
import math
import random
import sympy as sp

S = [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)]
G = [(i, j) for i in range(3) for j in range(3)]


def conv(f):
    return {
        z: sum(f.get(x, 0) * f.get(((z[0] - x[0]) % 3, (z[1] - x[1]) % 3), 0)
               for x in S)
        for z in G
    }


def energy(f):
    return sum(abs(v) ** 2 for v in conv(f).values())


def extension_moment(f):
    om = cmath.exp(2j * math.pi / 3)
    return sum(abs(sum(f.get(x, 0) * om ** ((xi[0] * x[0] + xi[1] * x[1]) % 3)
                           for x in S) / 5) ** 4 for xi in G)


c, a, d, b, e = sp.symbols('c a d b e', nonnegative=True, real=True)
fs = dict(zip(S, [c, a, d, b, e]))
Q = sp.expand(sum(conv(fs)[z] ** 2 for z in G))
claimed = ((c * c + 2 * a * d + 2 * b * e) ** 2 +
           (2 * c * a + d ** 2) ** 2 + (2 * c * d + a ** 2) ** 2 +
           (2 * c * b + e ** 2) ** 2 + (2 * c * e + b ** 2) ** 2 +
           4 * (a * a + d * d) * (b * b + e * e))
assert sp.expand(Q - claimed) == 0
X, P, Y, V, L = sp.symbols('X P Y V L', nonnegative=True)
# Algebraic reconstruction of the dependence on a,d, holding X, b, e, c fixed.
rest = ((c ** 2 + 2 * V) ** 2 +
        4 * (c ** 2 + 2 * V) * P + 2 * P ** 2 +
        4 * c ** 2 * X + X ** 2 + 4 * c * P * L +
        (2 * c * b + e ** 2) ** 2 + (2 * c * e + b ** 2) ** 2 +
        4 * X * (b * b + e * e))
assert sp.expand(rest.subs({X:a*a+d*d, P:a*d, V:b*e, L:a+d}) - Q) == 0
A, B = sp.symbols('A B', real=True, nonnegative=True)
Qbal = sp.factor(Q.subs({a:A,d:A,b:B,e:B}))
assert sp.expand(Qbal - (c**4 + 12*c**2*(A**2+B**2)
                        + 6*(A**2+B**2)**2 +12*A**2*B**2
                        +8*c*(A**3+B**3))) == 0
u, tau, z = sp.symbols('u tau z', positive=True)
u_dep = 12*u**2 + 8*tau*(1-u)*sp.sqrt(1+2*u)
assert sp.simplify(sp.diff(u_dep,u) - 24*u*(1-tau/sp.sqrt(1+2*u))) == 0
F = (z**4+24*z**2+16*z+36)/(z**2+4)**2
assert sp.factor(sp.diff(F,z)+16*(z+1)*(2*z**2+z-4)/(z**2+4)**3)==0
star=(sp.sqrt(33)-1)/4
K=(729+33*sp.sqrt(33))/296
assert sp.simplify(F.subs(z,star)-K)==0
assert sp.simplify((sp.Rational(9,25)*K)-(6561+297*sp.sqrt(33))/7400)==0
assert sp.simplify(K-3)>0

r=random.Random(27)
for case in range(350):
    f={x:complex(r.randrange(-4,5),r.randrange(-4,5)) for x in S}
    M=sum(abs(v)**2 for v in f.values())
    Qactual=energy(f)
    assert abs(extension_moment(f)-(9/625)*Qactual)<1e-8
    assert Qactual <= float(K)*M*M + 1e-7

for alpha in range(3):
    for beta in range(3):
        f={x:(float(star) if x==(0,0) else 1.0)*cmath.exp(2j*math.pi*(alpha*x[0]+beta*x[1])/3) for x in S}
        M=sum(abs(v)**2 for v in f.values())
        assert abs(energy(f)/M**2-float(K))<1e-12
        assert abs(extension_moment(f)/(M/5)**2-(9/25)*float(K))<1e-12

f={x:1 for x in S}
assert energy(f)==77
print('VERIFY_OK symbolic_identities=7 random_complex_cases=350 Fourier_values=3150 equality_modulations=9 constant_energy=77')
