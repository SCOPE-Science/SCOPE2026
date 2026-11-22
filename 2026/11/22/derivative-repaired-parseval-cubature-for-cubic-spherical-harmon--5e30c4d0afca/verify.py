"""Exact checks for derivative-repaired cubic-harmonic cubature.

Run: python verify.py
Requires sympy. Uses algebraic coordinates and exact spherical moments.
"""
import itertools
import sympy as sp
x, y, z, t = sp.symbols('x y z t', real=True)
phi = (1+sp.sqrt(5))/2
R = phi + 2
coords = []
for p in ((0,1,phi),(1,phi,0),(phi,0,1)):
    k = [j for j,a in enumerate(p) if a != 0]
    for a,b in itertools.product((-1,1), repeat=2):
        q=list(p)
        q[k[0]]*=a
        q[k[1]]*=b
        coords.append(tuple(q))
assert len(coords)==12

# A basis for the real seven-dimensional homogeneous harmonic cubics.
F = [x**3-3*x*y*y, 3*x*x*y-y**3,
     x*(4*z*z-x*x-y*y), y*(4*z*z-x*x-y*y),
     z*(2*z*z-3*x*x-3*y*y), z*(x*x-y*y), 2*x*y*z]
assert all(sp.expand(sum(sp.diff(f,u,2) for u in (x,y,z))) == 0 for f in F)
# Exact sphere moments on S^2: E[x^(2a)y^(2b)z^(2c)] = (1/2)_a (1/2)_b (1/2)_c/(3/2)_(a+b+c).
def integral(p):
    poly = sp.Poly(sp.expand(p), x,y,z)
    v = sp.S.Zero
    for powers,coeff in poly.terms():
        if any(k%2 for k in powers):continue
        pp=[k//2 for k in powers]
        v += coeff*sp.prod(sp.rf(sp.Rational(1,2),k) for k in pp)/sp.rf(sp.Rational(3,2),sum(pp))
    return sp.factor(v)

n=len(F)
M=sp.Matrix(n,n,lambda i,j:integral(F[i]*F[j]))
dF = [sp.Matrix([sp.diff(f,u) for u in (x,y,z)]) for f in F]
values = []
grads = []
for p in coords:
    sub=dict(zip((x,y,z),p))
    values.append([sp.expand(f.subs(sub)) for f in F])
    grads.append([[sp.expand(g.subs(sub)) for g in df] for df in dF])

# Polynomial homogeneous scaling for vertices q with |q|^2=R:
# f(q/sqrt(R))=F(q)/R^(3/2), and
# grad_S(f) dot grad_S(g)= (dF(q) dot dG(q)-9F(q)G(q)/R)/R^2.
S0 = sp.zeros(n)
S1 = sp.zeros(n)
for i in range(n):
    for j in range(n):
        vv=sum(v[i]*v[j] for v in values)
        gg=sum(sum(g[i][k]*g[j][k] for k in range(3)) for g in grads)
        S0[i,j]=sp.simplify(vv/(12*R**3))
        S1[i,j]=sp.simplify((gg-9*vv/R)/(12*R**2*12))
        assert sp.simplify(3*S0[i,j]/7 + 4*S1[i,j]/7 - M[i,j]) == 0, (i,j)

# Projector identities entail the full eigenvalues, not numerical guesses.
assert all(sp.simplify(v)==0 for v in (M.inv()*S0)*(M.inv()*S0)-sp.Rational(7,3)*(M.inv()*S0))
assert sp.simplify(sp.trace(M.inv()*S0))==7
assert all(sp.simplify(v)==0 for v in (M.inv()*S1)*(M.inv()*S1)-sp.Rational(7,4)*(M.inv()*S1))
assert sp.simplify(sp.trace(M.inv()*S1))==7

# The zonal argument for necessity uses explicit nonzero degree-2/4 coefficients.
P3=sp.legendre(3,t)
q=sp.expand(P3**2 + (sp.diff((1-t*t)*sp.diff(P3**2,t),t))/42)
assert sp.simplify(q-(sp.Rational(1,7)+sp.Rational(8,49)*sp.legendre(2,t)+sp.Rational(6,49)*sp.legendre(4,t)))==0

print('PASS: 7 harmonic cubics; 49 exact mixed-Parseval entries; exact projector identities; eigenvalue traces; zonal converse polynomial')
print('S0 eigenvalues: 7/3 (3), 0 (4). S1 eigenvalues: 7/4 (4), 0 (3).')
