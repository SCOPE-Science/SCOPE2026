from itertools import combinations
from sympy import Matrix, Poly, expand, invert, symbols

a, x = symbols('a x')
p = 11
pol = lambda z: Poly(z, a, modulus=p)
check = lambda X, Y: all(pol(e).is_zero for e in X-Y)
f = x**9+a*x**7-a*x**3-x
cf = Poly(expand(f**5), x)
M = Matrix(4,4,lambda i,j: pol(cf.nth(p*(i+1)-(j+1))).as_expr())
C = 1-5*a**2-3*a**4
J = pol(a**15-2*a**13-4*a**11+a)
u,v = Matrix([6*a,-C]), Matrix([C,-6*a])
r,s = Matrix([[2*a,1]]), Matrix([[1,2*a]])
P,Q = u*r,v*s
I = [0,2,1,3]
Z = Matrix.zeros(2)
assert check(M.extract(I,I), Z.row_join(P).col_join(Q.row_join(Z)))
tw = lambda A: A.subs(a,a**p)
raw = tw(M)*M
want = (tw(u)*s).row_join(Z).col_join(Z.row_join(-tw(v)*r))*5*J.as_expr()
assert check(raw.extract(I,I),want)
assert J.degree()==15 and J.gcd(J.diff()).is_one
assert (J.eval(2),J.eval(-2))==(-1,1)
E=pol(a*(a*a-36))
assert J.gcd(pol(a*a+12)).is_one and J.gcd(E)==E
transforms = [(pol(sign*nn),pol(dd)) for sign in (1,-1)
              for nn,dd in ((a,1),(2*a-12,a+2),(2*a+12,a-2))]
for n,d in transforms:
    z=n*invert(d,J)%J
    assert (J.compose(z)%J).is_zero
for (n,d),(m,e) in combinations(transforms,2):
    assert (n*e-m*d).gcd(J.exquo(E)).is_one
assert {int(n.eval(0))*pow(int(d.eval(0)),-1,p)%p for n,d in transforms}=={0,5,6}
# Compare to the polynomial from the reversed product in the earlier calculation.
G=pol(a**45-2*a**23+a**11-4*a)
q=pol(a**4+3*a**2-3)
assert (G%q).is_zero and J%q==pol(2*a) and q.gcd(pol(a*a-4)).is_one
assert J.gcd(G)==E
print('VERIFIED: rank-zero locus of degree 15, 12 exact Q8 parameters in two classes, and three enhanced parameters in one class')
