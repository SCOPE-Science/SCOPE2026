"""Exact elementary-symmetric Bring local-model and dual-graph checks."""
import sympy as S
from itertools import combinations
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

u,v,w=S.symbols('u v w')
x=[u,1+v,1+w,-3-u-v-w,1]
f2=S.expand(sum(x[i]*x[j] for i,j in combinations(range(5),2)))
f3=S.expand(sum(x[i]*x[j]*x[k] for i,j,k in combinations(range(5),3)))
origin={u:0,v:0,w:0}
assert f2.subs(origin)==-6 and f3.subs(origin)==-8
assert [S.diff(f2,t).subs(origin) for t in (u,v,w)]==[-3,-4,-4]
assert [S.diff(f3,t).subs(origin) for t in (u,v,w)]==[-9,-8,-8]
# For the maximal ideal (2,u,v,w), linear initial forms over F2:
# f2 -> 2+u and f3 -> u, so the cotangent space has basis v,w.
assert (S.diff(f3,u).subs(origin)-3*S.diff(f2,u).subs(origin))==0
g=S.Poly(f3-3*f2,u,v,w)
assert g.coeff_monomial(1)==10
assert all(g.coeff_monomial(t)==4 for t in (v,w))
assert [g.coeff_monomial(t) for t in (v**2,v*w,w**2)]==[1,-3,1]
# Over F2, v^2+vw+w^2 has no rational projective root,
# so its two linear factors are conjugate over F4 (node branches).
for a,b in [(1,0),(0,1),(1,1)]:
    assert (a*a+a*b+b*b)%2==1
# Two vertices joined by five edges. Reduced intersection Laplacian is (5).
L=S.Matrix([[5,-5],[-5,5]])
assert L.rank()==1
assert smith_normal_form(L[:1,:1],domain=ZZ)==S.Matrix([[5]])
assert (L*S.Matrix([1,1]))==S.zeros(2,1)
# Arithmetic Frobenius swaps components, taking (1,-1) to its negative.
F=S.Matrix([[0,1],[1,0]])
assert F*S.Matrix([1,-1])==-S.Matrix([1,-1])
# Frob -1 on Z/5 has just the identity fixed, becomes trivial after Frob^2.
assert sum(1 for a in range(5) if (-a-a)%5==0)==1
assert sum(1 for a in range(5) if (a-a)%5==0)==5
print('BRING2_NERON_LOCAL_AND_GRAPH_VERIFIED_OK')
