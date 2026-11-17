"""Reproduce symbolic and finite geometric checks for integral twisted-cubic polytopes.
Requires sympy; intended for scientific reproducibility.
"""
import itertools
import math
import sympy as sp
x,y,z,u,v,w=sp.symbols('x y z u v w', integer=True)
L=x+y+z
volume3=x*y*z*(x+y)*(y+z)*L/6
area2=(x*(x+y)*y+(x+y)*L*z)/2
I=sp.expand(volume3-area2+L-1)
lower=(L-1)*(L-2)*(L-3)/3
D=sp.expand(6*(I-lower))
p=sp.Poly(sp.expand(D.subs({x:u+1,y:v+1,z:w+1})),u,v,w)
assert all(coeff>0 for (_,coeff) in p.terms()), 'positive certificate failed'
q=sp.Poly(p.as_expr(),v)
assert q.degree()==4
q0=sp.factor(q.coeff_monomial(1))
assert sp.expand(q0-u*w*(u*u*w+3*u*u+u*w*w+9*u*w+11*u+3*w*w+11*w+9))==0
for j in range(1,5):
 assert sp.Poly(q.coeff_monomial(v**j),u,w).coeffs() and all(c>0 for c in sp.Poly(q.coeff_monomial(v**j),u,w).coeffs())
assert sp.expand(I.subs({x:1,y:1,z:w+1})-lower.subs({x:1,y:1,z:w+1}))==0
assert sp.expand(I.subs({x:u+1,y:1,z:1})-lower.subs({x:u+1,y:1,z:1}))==0

def formula(g):
 a,b,c=g
 return int(I.subs({x:a,y:b,z:c}))

def enumerate_interior(g):
 T=[0]
 for gap in g:T.append(T[-1]+gap)
 M=sp.Matrix([[1]*4, T, [t*t for t in T], [t*t*t for t in T]])
 adj=M.adjugate();det=int(M.det())
 A=[[int(adj[i,j])*(1 if det>0 else -1) for j in range(4)] for i in range(4)]
 c=abs(det);N=T[-1];cnt=0
 for xx in range(1,N):
  for yy in range(1,N*N):
   # Simple necessary parabola inequality y > x^2 is irrelevant for mixtures; omit
   for zz in range(1,N*N*N):
    vec=(1,xx,yy,zz)
    if all(0<sum(A[i][j]*vec[j] for j in range(4))<c for i in range(4)):
     cnt+=1
 return cnt

cases=[(1,1,1),(1,1,2),(2,1,1),(1,2,1),(1,1,3),(2,2,1),(1,2,2)]
for g in cases:
 assert enumerate_interior(g)==formula(g),(g,enumerate_interior(g),formula(g))
for span in range(3,12):
 vals=[]
 for aa in range(1,span-1):
  for bb in range(1,span-aa):
   cc=span-aa-bb
   vals.append((formula((aa,bb,cc)),(aa,bb,cc)))
 mi=min(v for v,g in vals)
 assert mi==2*math.comb(span-1,3)
 assert {g for v,g in vals if v==mi} == ({(1,1,1)} if span==3 else {(1,1,span-2),(span-2,1,1)})
print('PASS: 48 positive-coefficient certificate terms; independent integer-point enumeration on',len(cases),'tetrahedra; all-gap minimization for spans 3..11.')
