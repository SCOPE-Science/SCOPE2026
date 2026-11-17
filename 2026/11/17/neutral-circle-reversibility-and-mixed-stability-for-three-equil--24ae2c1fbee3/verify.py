"""Symbolic and exact-inequality cross-checks for the equilateral three-circle theorem.

The proof is analytic; this script independently confirms key polynomial reflection
identities, the symmetric specialization of the characteristic-exponent numerators,
and all six exact hyperbolic sign patterns.
"""
import itertools
import sympy as s

x, y, r, lam, mu, kap = s.symbols('x y r lam mu kap', real=True)
v = s.sqrt(3)/2
C = [s.Matrix([0, 0]), s.Matrix([1, 0]), s.Matrix([s.Rational(1,2), v])]
Z = s.Matrix([x, y]); J = s.Matrix([[0,-1],[1,0]])
f = [s.expand((Z-ci).dot(Z-ci)-r*r) for ci in C]
A = [-lam-mu+kap*(-v*x-y/2-v), lam+kap*(v*x-y/2), mu+kap*y]
F = s.expand(sum((A[i]*s.prod(f[j] for j in range(3) if j != i)*J*(Z-C[i]) for i in range(3)), s.zeros(2,1)))
R=[s.Matrix([[s.Rational(1,2),v],[v,-s.Rational(1,2)]]),
   s.Matrix([[s.Rational(1,2),-v],[-v,-s.Rational(1,2)]]),
   s.diag(-1,1)]
conds=[lam-mu, lam+2*mu+2*kap*v, 2*lam+mu+2*kap*v]
for i in range(3):
    zR=C[i]+R[i]*(Z-C[i])
    reflection=s.simplify(F.subs({x:zR[0],y:zR[1]},simultaneous=True)+R[i]*F)
    for component in reflection:
        assert s.simplify(component.subs({lam:mu} if i==0 else
           {lam:-2*mu-2*kap*v} if i==1 else {mu:-2*lam-2*kap*v}))==0

# Formula from Cao-Llibre, Definition preceding Theorem D.
w=[-lam-mu-kap*v,lam+kap*v,mu+kap*v]
B12=-2*lam-mu-2*kap*v; B13=lam+2*mu+2*kap*v; B23=-B12-B13
S=[B12+B13,B12+B23,B13+B23]
assert all(s.simplify(S[i]-(w[(i+2)%3]-w[(i+1)%3]))==0 for i in range(3))
assert s.simplify(sum(w[i]*S[i] for i in range(3)))==0

signs=set()
for a in itertools.permutations([3,1,-4]):
    omega=[v/3+2*ai for ai in a]
    # all |omega| > r for every 0 < r < 1/2; rational interval bound:
    assert all(abs(float(q))>0.5 for q in omega)
    diff=[omega[(i+2)%3]-omega[(i+1)%3] for i in range(3)]
    signs.add(tuple(s.sign(omega[i]*diff[i]) for i in range(3)))
assert len(signs)==6
assert all((1 in pattern and -1 in pattern) for pattern in signs)
print('VERIFY_OK exact_reflections=3 exact_skew_cancellation=1 all_six_sign_patterns=6')
