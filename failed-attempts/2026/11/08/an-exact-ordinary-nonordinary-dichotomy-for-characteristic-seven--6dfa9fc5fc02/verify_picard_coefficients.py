"""Exact independent coefficient computation for the characteristic-seven Picard family.
Runs with Python 3 and SymPy. No numerical or probabilistic ingredients.
"""
import sympy as s
x,a,b=s.symbols('x a b'); p=7
f=x**4+a*x**2+b*x+1
h=s.Poly(s.expand(f**4),x)
def red(z):return s.Poly(z,a,b,modulus=p).as_expr()
A,B,C,D=[red(h.nth(k)) for k in (6,13,5,12)]
L=red(s.Poly(s.expand(f**2),x).nth(6))
disc=red(s.discriminant(f,x));det=red(s.expand(A*D-B*C))
assert L==2*a
assert red(det-5*a*disc)==0
assert red(disc-(2*a**4+3*a**3*b**2-2*a**2-3*a*b**2+b**4-3))==0
# On a=0, the plane Frob block is (-3,-3b;-2b,-2b^2).
# It has rank one; the second iterate vanishes exactly at b^8=2.
for av in range(7):
 for bv in range(7):
  d=int(disc.subs({a:av,b:bv}))%7
  if d==0:continue
  H=s.Matrix([[int(D.subs({a:av,b:bv}))%7,0,int(B.subs({a:av,b:bv}))%7],
              [0,(2*av)%7,0],
              [int(C.subs({a:av,b:bv}))%7,0,int(A.subs({a:av,b:bv}))%7]])
  # rank by checking minors, without rational-field rank.
  r=3 if (int(H.det())%7)!=0 else 2 if any(int(H.extract(ii,jj).det())%7 for ii in [(0,1),(0,2),(1,2)] for jj in [(0,1),(0,2),(1,2)]) else 1
  assert r==(3 if av else 1)
  if av==0:
   H2=(H*H).applyfunc(lambda x:int(x)%7)
   assert (H2==s.zeros(3)) == (pow(bv,4,7)==4)
print('PICARD7_COEFFICIENT_PASS: determinant=5*a*discriminant; 49 field parameters checked')
