"""Colon I : q, I : s, and saturation checks; plus primality probe via random numeric
irreducibility: use Bertini-style monodromy? Too heavy. Instead do exact dimension/count:

1. Compute I:s colon similarly (expect symmetric result).
2. Compute saturation I : pqrs^inf by iterating colons.
3. KEY TEST: check whether I is prime by testing if R/I localized at pqrs is a domain
   and whether pqrs is a nonzerodivisor... Actually simplest obstruction: find minimal primes
   containing I of different dimensions, or two disjoint nonempty opens.

Alternative sharp tool: compute a lex GB and count standard monomials mod low-degree slice?
Better: compute Hilbert-style dimension via random linear sections solved with nsolve/polynomial homotopy.

Cheap exact approach: intersect V with random rational lines/planes and factor the resulting
univariate polynomial. If for a general line the section polynomial's Galois/splitting behavior
suggests... not conclusive for irreducibility but extra components often show as persistent factors.

STRONGER: look at the symmetric determinantal structure. Known theorem (Kutz? / Conca?):
For generic symmetric matrix, I_{n-1} is prime (it's the ideal of submaximal minors, prime since
symmetric determinantal rings are domains - due to Kutz 197... / Goto?). For SPARSE case the map
K[x_G] -> K[y_ik] (X_G = Y^T Y type parametrization?) may have kernel strictly bigger.

Parametrization approach: rank<=n-2 symmetric matrices with pattern G. Consider
phi: K[u_{ik}] -> K[x_G], x_ij = sum_k u_{ik} u_{jk} for (n-2) factors? Kernel P_G = prime of
rank<=n-2 locus intersected with pattern. Always I_{n-1}(X_G) subset P_G. Question: equality
(up to radical)? If V(I) strictly bigger than rank locus, extra components exist.

Dimension count: space of (n-2) x n matrices U modulo O(n-2): dim = (n-2)n - (n-2)(n-3)/2... in symmetric case.
For n=4: U is 2x4, x_ij = u_i.u_j. Impose sparsity u1.u3=0, u2.u4=0 (two bilinear constraints in P^? ).
Ambient A^8, rank<=2 image dim? generic fiber O(2) 1-dim... compute: U has 8 params, constraints 2 -> 6, minus O(2) 1 -> image dim 5? So main component dim 5, codim 3.
Extra components of dim >... let's test dimension of V(I3) numerically via Jacobian at smooth points of the parametrized locus.

Do: construct explicit rank-2 C4 point over QQ (find u,v with u1u3+v1v3... need u.v-orthogonality at (1,3),(2,4)):
pick u=(1,0,0,1), v=(0,1,1,0): u.v = 1*0+0*1+0*1+1*0=0? that's full dot; need per-pair: u1v1'... x13=u1u3+v1v3=1*0+0*1=0 ok; x24=u2u4+v2v4=0*1+1*0=0 ok. 
So X: a=1,b=1,c=1,d=1,p=0,q=0,r=0,s=1. Check all 3-minors vanish (rank<=2 by construction).
Jacobian rank there = codim of component (if smooth point).
"""
import sympy as sp

a, b, c, d, p, q, r, s = sp.symbols('a b c d p q r s')
M = sp.Matrix([
    [a, p, 0, s],
    [p, b, q, 0],
    [0, q, c, r],
    [s, 0, r, d],
])
rows4 = list(range(4))
gens = []
keys = []
for di in range(4):
    for dj in range(di, 4):
        rr = [x for x in rows4 if x != di]
        cc = [x for x in rows4 if x != dj]
        gens.append(sp.expand(M.extract(rr, cc).det()))
        keys.append((di, dj))

vars8 = [a, b, c, d, p, q, r, s]
J = sp.Matrix([[sp.diff(g, v) for v in vars8] for g in gens])

def rank_at(pt):
    return J.subs(pt).rank()

# rank-2 structured point
pt1 = {a: 1, b: 1, c: 1, d: 1, p: 0, q: 0, r: 0, s: 1}
print("gens at pt1:", [g.subs(pt1) for g in gens])
print("jacobian rank at pt1:", rank_at(pt1))

# more rank-2 points from random U with exact orthogonality: parametrize.
# u=(u1..u4), v=(v1..v4) with u1u3+v1v3=0, u2u4+v2v4=0.
import random
random.seed(1)
tests = [
    ((1, 2, 3, 4), (3, 1, -1, 2)),   # check: 1*3+3*(-1)=0 ok (1,3); 2*4+1*2=10 !=0 fail
]
# construct: choose u free, then v1,v2 free, v3=-u1u3/v1 (if v1!=0), v4=-u2u4/v2
def mkpt(u, v1, v2):
    u1, u2, u3, u4 = u
    v3 = -u1*u3/v1
    v4 = -u2*u4/v2
    v = (v1, v2, v3, v4)
    X = {}
    dg = [u1*u1+v1*v1, u2*u2+v2*v2, u3*u3+v3*v3, u4*u4+v4*v4]
    X[a], X[b], X[c], X[d] = [sp.Rational(x) for x in dg]
    X[p] = sp.Rational(u1*u2+v1*v2); X[q] = sp.Rational(u2*u3+v2*v3)
    X[r] = sp.Rational(u3*u4+v3*v4); X[s] = sp.Rational(u1*u4+v1*v4)
    return X

for u, v1, v2 in [((1,2,3,4), 3, 1), ((2,-1,1,3), 1, 2), ((1,1,2,1), 2, 1)]:
    pt = mkpt(u, v1, v2)
    print("pt:", pt)
    print("  gens vanish:", [sp.simplify(g.subs(pt)) for g in gens])
    print("  jac rank:", rank_at(pt))
