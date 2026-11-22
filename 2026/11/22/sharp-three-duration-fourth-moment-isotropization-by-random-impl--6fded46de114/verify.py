"""Independent symbolic and numerical checks for a fourth-moment rotation-design theorem.

Only the displayed algebra and finite examples are checked computationally;
the universal probability-law assertions follow from the written proof.
"""
import math
import random
import sympy as s

u = s.symbols('u', nonnegative=True)
r3 = s.sqrt(3)
C = (1-u*u)/(1+u*u)
S = 2*u/(1+u*u)
c2 = 2*C*C-1
s2 = 2*C*S
c4 = 2*c2*c2-1
s4 = 2*c2*s2
g = (8*r3-4*r3*(c2+c4)-16*s2-4*s4)/9
positive = (2*u*(u-r3)**2*(u-1/r3)**2
            *(3*u**4+8*r3*u**3+38*u*u+24*r3*u+19)
            /(3*(1+u*u)**4))
assert s.simplify(2*u-g-positive) == 0
assert s.simplify(positive.subs(u,0)) == 0
assert s.simplify(positive.subs(u,1/r3)) == 0
assert s.simplify(positive.subs(u,r3)) == 0

# Rotation rationalization from the Cayley transform.
J = s.Matrix([[0, 1],[-1,0]])
M = (s.eye(2)-u*J).inv()*(s.eye(2)+u*J)
assert s.simplify(M.T*M-s.eye(2)) == s.zeros(2)
assert s.simplify(M[0,0]-C)==0
assert s.simplify(M[0,1]-S)==0

# Complex phase multipliers on the three optimal duration options.
Z = ((1+s.I*u)/(1-s.I*u))**2
zs = [s.simplify(Z.subs(u,x)) for x in (0,1/r3,r3)]
assert s.simplify(sum(zs)) == 0
assert s.simplify(sum(z*z for z in zs)) == 0
assert s.simplify(sum((2*x for x in (0,1/r3,r3)))/3-8/(3*r3)) == 0

# The strictly-positive approximants are common rotations of the triangle.
for delta in (0.03,0.1,0.25):
    theta = [delta+j*math.pi/3 for j in range(3)]
    z = [complex(math.cos(2*t), math.sin(2*t)) for t in theta]
    assert abs(sum(z))<1e-13
    assert abs(sum(zz*zz for zz in z))<1e-13
    assert all(2*math.tan(t/2)>0 for t in theta)

# Check the circular cap polynomial's expectation for a valid design.
alpha = 2*math.pi/3
vals = [j*math.pi/3 for j in range(3)]
t = [2*th-alpha for th in vals]
pvals = [(math.cos(v)-math.cos(alpha))*(1-math.cos(v)) for v in t]
assert max(map(abs,pvals))<1e-13
assert abs((-math.cos(alpha)-0.5))<1e-13

# Supplementary LP discretizations (not used as infinite-dimensional proofs).
try:
    import numpy as np
    from scipy.optimize import linprog
    for n in (100,300,600):
        theta = np.linspace(0, math.pi-0.001, n)
        h = 2*np.tan(theta/2)
        A = np.array([np.ones(n),np.cos(2*theta),np.sin(2*theta),
                      np.cos(4*theta),np.sin(4*theta)])
        r = linprog(h,A_eq=A,b_eq=[1,0,0,0,0],bounds=(0,None),method='highs')
        assert r.success and r.fun >= 8/(3*math.sqrt(3))-1e-7
        assert r.fun < 8/(3*math.sqrt(3))+0.002
    print('Symbolic certificate, support geometry, strict-positive limits, and LP checks: PASS')
except ImportError:
    print('Symbolic certificate and support geometry: PASS; optional LP check skipped')
