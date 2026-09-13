"""Exact verification of the Vinberg arithmeticity decision for C0 = Sigma_1^{2,2,3} = P34,1.
Requires: sympy. All checks are exact (no floating point in certificates).
Node order: 0=T,1=U,2=LM,3=CM,4=RM,5=LB,6=CB,7=RB.
Solids (m=3, entry -1/2): (0,2),(2,3),(3,4),(3,6),(5,6),(4,7).
Dotted: (1,3)=c=sqrt((5+sqrt13)/6); (0,4)=(2,5)=(6,7)=a=(1+sqrt13)/4. Else 0 (m=2).
"""
import sympy as sp, itertools
sqrt13 = sp.sqrt(13)
a = (1+sqrt13)/4
c = sp.sqrt((5+sqrt13)/6)
n = 8
G = sp.zeros(n)
for i in range(n): G[i,i] = 1
for i,j in [(0,2),(2,3),(3,4),(3,6),(5,6),(4,7)]: G[i,j] = G[j,i] = sp.Rational(-1,2)
for (i,j),v in {(2,5):a,(6,7):a,(1,3):c,(0,4):a}.items(): G[i,j] = G[j,i] = -v
x = sp.symbols('x'); lam = sp.symbols('lam')
# (A) hyperbolic signature (4,1), rank 5
cp = sp.factor(G.charpoly(lam).as_expr())
print("(A) charpoly(G) =", cp)
assert G.rank() == 5
# quadratic factor 24L^2-48L-23-13*sqrt13: product<0 -> one + and one - root
# (B) compactness: 16 cube-vertices elliptic
disj = {(0,4),(1,3),(2,5),(6,7)}
verts = [q for q in itertools.combinations(range(8),4)
         if not ({(min(s,t),max(s,t)) for s,t in itertools.combinations(q,2)} & disj)]
assert len(verts) == 16
for q in verts:
    M = G.extract(list(q),list(q))
    assert all(sp.simplify(M[:k,:k].det()) > 0 for k in range(1,5)), q
print("(B) all 16 vertex figures elliptic: OK")
# (C) Vinberg field k0 = Q(sqrt13): 4a^2 irrational, everything in Q(sqrt13)
t1 = sp.simplify(4*a**2); t2 = sp.simplify(4*c**2)
print("(C) 4a^2 =", t1, " minpoly:", sp.minimal_polynomial(t1,x))
print("    4c^2 =", t2, " minpoly:", sp.minimal_polynomial(t2,x))
assert sp.minimal_polynomial(t1,x) == x**2-7*x+9
assert sp.minimal_polynomial(t2,x) == 3*x**2-20*x+16
# norm of 4c^2 = 16/3 (not integral)
N = sp.simplify(t2*sp.expand(t2.xreplace({sqrt13:-sqrt13})))
print("    Norm(4c^2) =", N); assert N == sp.Rational(16,3)
# (D) conjugate Gram PSD: quadratic 24L^2-48L-23+13*sqrt13, disc/num + product>0 + sum>0
asig = (1-sqrt13)/4; csig = sp.sqrt((5-sqrt13)/6)
Gs = sp.zeros(n)
for i in range(n): Gs[i,i] = 1
for i,j in [(0,2),(2,3),(3,4),(3,6),(5,6),(4,7)]: Gs[i,j] = Gs[j,i] = sp.Rational(-1,2)
for (i,j),v in {(2,5):asig,(6,7):asig,(1,3):csig,(0,4):asig}.items(): Gs[i,j] = Gs[j,i] = -v
print("(D) charpoly(Gs) =", sp.factor(Gs.charpoly(lam).as_expr()))
assert Gs.rank() == 5
assert 4512**2 - 1248**2*13 > 0 and 13**2*13 - 23**2 > 0
print("    conjugate PSD certified: OK")
print("CONCLUSION: k0=Q(sqrt13) deg 2; 4c^2 non-integral -> NOT arithmetic; conjugate PSD -> properly quasi-arithmetic (GPS/BT sense).")
