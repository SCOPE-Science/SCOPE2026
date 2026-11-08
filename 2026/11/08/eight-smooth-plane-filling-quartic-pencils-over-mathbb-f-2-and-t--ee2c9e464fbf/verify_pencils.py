#!/usr/bin/env python3
"""Exact exhaustive check for binary plane-filling quartic pencils."""
import itertools
from collections import defaultdict
import sympy as S
X,Y,Z=S.symbols('X Y Z')
V=(X,Y,Z)
D=4
MON=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
EXP={m:i for i,m in enumerate(MON)}
POINTS=[p for p in itertools.product(range(2),repeat=3) if any(p)]

def polynomial(mask):
 return sum(X**a*Y**b*Z**c for i,(a,b,c) in enumerate(MON) if (mask>>i)&1)

def ev(mask,p):
 ans=0
 for i,(a,b,c) in enumerate(MON):
  if mask>>i&1: ans^=(p[0]**a)*(p[1]**b)*(p[2]**c)
 return ans

def grad_eval(mask,p):
 return tuple(sum(( (a if k==0 else b if k==1 else c)&1)*p[0]**(a-(k==0))*p[1]**(b-(k==1))*p[2]**(c-(k==2)) for i,(a,b,c) in enumerate(MON) if mask>>i&1 and (a,b,c)[k]>0)%2 for k in range(3))

FILL=[f for f in range(1,1<<len(MON)) if all(ev(f,p)==0 for p in POINTS)]
assert len(FILL)==255
SMOOTH_RATIONAL=[f for f in FILL if all(any(grad_eval(f,p)) for p in POINTS)]
assert len(SMOOTH_RATIONAL)==24
for f in SMOOTH_RATIONAL:
 F=polynomial(f)
 for i in range(3):
  var=[v for j,v in enumerate(V) if j!=i]
  A=F.subs(V[i],1)
  gb=S.groebner([A]+[S.diff(A,u) for u in var],*var,order='lex',modulus=2)
  assert any(g.as_expr()==1 for g in gb.polys),(f,i,gb)
GOOD=set(SMOOTH_RATIONAL)
PENCILS=sorted({tuple(sorted((a,b,a^b))) for a,b in itertools.combinations(SMOOTH_RATIONAL,2) if (a^b) in GOOD})
assert len(PENCILS)==8
assert len(set(sum((list(p) for p in PENCILS),[])))==24

# 3 x 3 matrices and GL_3(F2) action by substitution of linear forms.
def mul(A,B):
 out=defaultdict(int)
 for (a,b,c),u in A.items():
  for (d,e,f),v in B.items():out[a+d,b+e,c+f]^=u&v
 return {k:v for k,v in out.items() if v}
def powpoly(a,n):
 v={(0,0,0):1}
 for _ in range(n):v=mul(v,a)
 return v
def substitute(mask,rows):
 lin=[]
 for row in rows:
  lin.append({tuple(1 if k==i else 0 for k in range(3)):1 for i in range(3) if row[i]})
 powers=[[powpoly(u,j) for j in range(5)] for u in lin]
 o=defaultdict(int)
 for k,(a,b,c) in enumerate(MON):
  if mask>>k&1:
   for t,u in mul(mul(powers[0][a],powers[1][b]),powers[2][c]).items():o[t]^=u
 ret=0
 for t,u in o.items():
  if u:ret ^= 1<<EXP[t]
 return ret

def matmul(a,b):
 return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))
def mdet(m):
 return sum(m[0][i]*m[1][j]*m[2][k] for i,j,k in itertools.permutations(range(3)))%2
GL=[]
for digits in itertools.product(range(2),repeat=9):
 r=tuple(tuple(digits[3*i+j] for j in range(3)) for i in range(3))
 if mdet(r):GL.append(r)
assert len(GL)==168
rep=PENCILS[0]
P_ORBIT={tuple(sorted(substitute(f,B) for f in rep)) for B in GL}
C_ORBIT={substitute(rep[0],B) for B in GL}
assert P_ORBIT==set(PENCILS) and C_ORBIT==GOOD
assert sum(tuple(sorted(substitute(f,B) for f in rep))==rep for B in GL)==21
assert sum(substitute(rep[0],B)==rep[0] for B in GL)==7

# Transverse at every F2 point in every pencil.
for a,b,c in PENCILS:
 for p in POINTS:
  u,v=grad_eval(a,p),grad_eval(b,p)
  assert any(u) and any(v) and u!=v

# Exact geometric base scheme for the representative pencil.
a,b,c=rep
assert rep==(6438,10988,13258)
A=polynomial(a).subs(Z,1)
B=polynomial(b).subs(Z,1)
G=S.groebner([A,B],X,Y,order='lex',modulus=2)
assert len(G.polys)==3
LEAD=[S.Poly(h.as_expr(),X,Y,modulus=2).LM(order='lex') for h in G.polys]
assert [tuple(m.exponents) for m in LEAD]==[(2,0),(1,2),(0,11)]
h=Y**3+Y+1
assert S.Poly(G.polys[-1].as_expr(),Y,modulus=2)==S.Poly(Y*(Y+1)*h**3,Y,modulus=2)
J=S.groebner([X+Y**8+Y**5,h**3],X,Y,order='lex',modulus=2)
K=S.groebner([X**2+X,Y**2+Y],X,Y,order='lex',modulus=2)
for f in [A,B]:assert J.reduce(f)[1]==0 and K.reduce(f)[1]==0
assert S.Poly(h,Y,modulus=2).is_irreducible
# G has affine quotient dimension 11+2=13; J and K disjoint schemes of degrees 9 and 4.
# At infinity check only three reduced F2 points, verified by transverse gradients.
t=S.symbols('t')
Ain=polynomial(a).subs({X:1,Y:t,Z:0})
Bin=polynomial(b).subs({X:1,Y:t,Z:0})
gcd=S.gcd(S.Poly(Ain,t,modulus=2), S.Poly(Bin,t,modulus=2))
assert gcd==S.Poly(t*(t+1),t,modulus=2)
assert ev(a,(0,1,0))==ev(b,(0,1,0))==0
print('SMOOTH_FILLING_QUARTIC_PENCILS_PASS 255 24 8 168 21 7 13 9')
print('PENCILS',PENCILS)
print('REPRESENTATIVE',str(polynomial(a)),str(polynomial(b)))
print('AFFINE_GROEBNER',str([f.as_expr() for f in G.polys]))
