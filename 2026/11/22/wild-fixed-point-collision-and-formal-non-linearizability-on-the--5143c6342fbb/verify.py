"""Exact checks for the cyclic-five fixed scheme on a quintic del Pezzo surface.
Run with python3 verify.py; requires SymPy >=1.10.
The boundary argument and identification with stable five-pointed curves
are proved separately in RESULT.md; finite tests are not used to infer them.
"""
from sympy import symbols, Matrix, factor, cancel, diff, resultant, Poly, eye
from itertools import combinations

a,b,t=symbols('a b t')
P=a*a-a-1
F=cancel(a*(b-1)/(b*(a-1)))
G=cancel(a/(a-1))
assert cancel((F-a).subs(b,G) + P/(a-1)) == 0
assert cancel(G-b + (a*b-a-b)/(a-1)) == 0
# The fixed algebra is Z[a,b,units]/(b-a/(a-1), P).
# In this quotient a(a-1)=1, hence b=a^2=a+1 and a-b=-1.
assert cancel((a*a-G)*(a-1)-a*P)==0
assert cancel(P.subs(a,2))==1
assert cancel(P.subs(a,0))==-1
assert cancel(P.subs(a,1))==-1
assert cancel(P.subs(a,-1))==1

# Verify that the cyclic normalization map has exact order five in Q(a,b).
x,y=a,b
for k in range(1,6):
    x,y=cancel(F.subs({a:x,b:y}, simultaneous=True)), cancel(G.subs({a:x,b:y}, simultaneous=True))
assert cancel(x-a)==0 and cancel(y-b)==0

# Tangent linearization and its cyclotomic eigenvalues.
J=Matrix([[diff(F,a),diff(F,b)],[diff(G,a),diff(G,b)]])
Jstar=Matrix([[-a,a**(-2)],[-a*a,0]])
for i in range(2):
 for j in range(2):
    val=cancel((J[i,j]-Jstar[i,j]).subs(b,G))
    num=val.as_numer_denom()[0]
    assert Poly(num,a).rem(Poly(P,a)).is_zero, (i,j,val)
assert cancel(Jstar.det()-1)==0
assert cancel(Jstar.trace()+a)==0
assert factor(resultant(P,t*t+a*t+1,a))== t**4+t**3+t**2+t+1
# Exact Jacobian and Jordan form at the unique characteristic-five point.
def mod5(r):
 from fractions import Fraction
 p=Fraction(str(r));return (p.numerator*pow(p.denominator,-1,5))%5
J5=J.subs({a:3,b:4}).applyfunc(mod5)
assert J5 == Matrix([[2,4],[1,0]])
N=(J5-eye(2)).applyfunc(lambda v:v%5)
assert N!=Matrix.zeros(2)
assert (N*N).applyfunc(lambda v:v%5)==Matrix.zeros(2)
assert ((J5**5)-eye(2)).applyfunc(lambda v:v%5)==Matrix.zeros(2)
assert Poly(P,a,modulus=5)==Poly((a-3)**2,a,modulus=5)

# Each boundary divisor corresponds to a pair of labels; there are two
# free orbits of length five under the cyclic relabeling.
sets={frozenset(c) for c in combinations(range(5),2)}
orb=[]
while sets:
 s=sets.pop()
 o={frozenset((x+i)%5 for x in s) for i in range(5)}
 assert len(o)==5
 sets-=o
 orb.append(o)
assert len(orb)==2
# Base-field root counts of a^2-a-1 at representative primes.
for p in [2,3,5,7,11,13,17,19,23,29,31,41]:
 roots=[z for z in range(p) if (z*z-z-1)%p==0]
 if p==5:
  assert roots==[3]
 else:
  assert len(roots) in (0,2)
  assert len(roots)==(2 if pow(5,(p-1)//2,p)==1 and p%2 else 0) if p!=2 else len(roots)==0
print('QUINTIC_DEL_PEZZO_WILD_FIXED_SCHEME_VERIFIED')
print('order5, boundary:2x5, fixed:Z[a]/(a^2-a-1), discriminant:5, J5:',list(J5))
