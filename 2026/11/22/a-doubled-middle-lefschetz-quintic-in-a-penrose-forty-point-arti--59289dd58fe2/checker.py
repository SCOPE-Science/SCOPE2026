#!/usr/bin/env python3
"""Exact symbolic verification of a Penrose section's middle determinant. Requires SymPy."""
import sympy as s
x,y,z,w=s.symbols('x y z w'); U,V,W=s.symbols('U V W')
f=[x*y*z*w,w*(x**3-y**3+z**3),z*(x**3+y**3+w**3),y*(-x**3+z**3+w**3),x*(y**3+z**3-w**3)]
G=s.groebner([s.expand(p.subs(w,-x-2*y-3*z)) for p in f],x,y,z,order='grlex')
assert G.is_zero_dimensional
for d,want in enumerate((1,3,6,10,10,6,3,1,0)):
 ms=[x**i*y**j*z**(d-i-j) for i in range(d+1) for j in range(d-i+1)]
 reduced=[s.Poly(G.reduce(m)[1],x,y,z) for m in ms]
 terms=sorted(set(e for p in reduced for e,c in p.terms()))
 mat=s.Matrix([[p.coeff_monomial(x**e[0]*y**e[1]*z**e[2]) for p in reduced] for e in terms])
 assert mat.rank()==want,(d,mat.rank(),want)
ms3=[x**i*y**j*z**(3-i-j) for i in range(4) for j in range(4-i)]
ms4=[x**i*y**j*z**(4-i-j) for i in range(5) for j in range(5-i)]
red={(m,v):s.Poly(G.reduce(m*v)[1],x,y,z) for m in ms3 for v in (x,y,z)}
std=[t for t in ms4 if any(p.coeff_monomial(t) for p in red.values())]
assert std==[z**4,y*z**3,y**2*z**2,y**3*z,y**4,x*z**3,x*y*z**2,x*y**2*z,x*y**3,x**2*y**2]
M=s.Matrix(10,10,lambda i,j:sum(a*red[(ms3[j],v)].coeff_monomial(std[i]) for a,v in zip((U,V,W),(x,y,z))))
Q=(15*U**4*V-47*U**4*W+36*U**3*V**2-34*U**3*V*W+54*U**3*W**2-18*U**2*V**3-18*U**2*W**3+45*U*V**4-54*U*V**3*W+30*U*V*W**3-7*U*W**4-27*V**4*W+54*V**3*W**2-36*V**2*W**3+7*V*W**4)
assert s.cancel(27*M.det(method='domain-ge')-Q**2)==0
assert s.factor_list(Q)[1]==[(Q,1)]
assert s.gcd(Q,s.diff(Q,U))==1
for a,b,c in ((1,0,0),(0,1,0),(0,0,1),(1,2,3)):
 assert M.subs({U:a,V:b,W:c}).rank()==8
assert M.subs({U:2,V:3,W:5}).rank()==10
print('PASS: exact Hilbert vector, determinant polynomial, quintic factor, ranks')
