"""Exact checks for a two-state BDF2 positivity theorem.

Requires Python 3 and SymPy. This script supplements a written analytic proof;
finite tests do not certify its all-parameter or all-index assertions.
"""
import sympy as s
from fractions import Fraction

x,t=s.symbols('x t', real=True)
D=3+2*x
N={1:s.Integer(1),2:3-x}
for n in range(3,7):
    N[n]=s.expand(4*N[n-1]-D*N[n-2])
expected={2:3-x,3:9-6*x,4:2*x*x-27*x+27,
          5:(2*x-9)*(10*x-9),6:-4*x**3+128*x*x-405*x+243}
for n in range(2,7):
    assert s.expand(N[n]-expected[n])==0

# Compare the exact first six scalar coefficients with the BDF2 recurrence.
z=[s.Integer(1),1/(1+x)]
for n in range(2,7):
    z.append(s.factor((4*z[-1]-z[-2])/D))
    assert s.simplify(z[n]-N[n]/((1+x)*D**(n-1)))==0

# Polynomial positivity certificates needed for n=3,...,6.
shift_coeffs={
3:[116,638,-4840,6696],
4:[232,1740,6872,-18968,16784],
5:[464,4408,16704,51552,-58304,43136],
6:[928,10672,51040,125920,307600,-138944,116544]}
for n in range(3,7):
    P=s.expand(1000*N[n]+29*(1+x)*D**(n-1))
    assert s.Poly(s.expand(P.subs(x,t+s.Rational(1,2))),t).all_coeffs()==shift_coeffs[n]
for a,b,c in [(6872,18968,16784),(51552,58304,43136),(307600,138944,116544),
              (1334,896,496)]:
    assert b*b-4*a*c<0
assert s.simplify((17-12*s.sqrt(2))-(s.Rational(29,1000)))>0
assert s.Rational(5,192)<s.Rational(29,1000)

# Sharp two-step minimum and rate threshold.
gamma=17-12*s.sqrt(2)
rstar=3+3*s.sqrt(2)
r2=(3-x)/((1+x)*D)
assert s.simplify(s.diff(r2,x)-2*(x*x-6*x-9)/((1+x)**2*D**2))==0
assert s.simplify(r2.subs(x,rstar)+gamma)==0
assert s.simplify((17+12*s.sqrt(2))*gamma)==1

# Direct matrix BDF2 checks for multiple rational rate and timestep choices.
checks=0
for a in [1,2,5,34,40]:
 for b in [1,3]:
  Q=s.Matrix([[-a,a],[b,-b]])
  pi=s.Matrix([[s.Rational(b,a+b),s.Rational(a,a+b)],
               [s.Rational(b,a+b),s.Rational(a,a+b)]])
  for h in [s.Rational(1,20),s.Rational(1,2),s.Rational(7,a+b),s.Rational(20,3)]:
   X=s.eye(2);Y=(s.eye(2)-h*Q).inv()
   R=s.Rational(1,1);S=1/(1+h*(a+b))
   assert X==pi+R*(s.eye(2)-pi)
   assert Y==pi+S*(s.eye(2)-pi)
   for n in range(2,16):
    Z=(3*s.eye(2)-2*h*Q).inv()*(4*Y-X)
    T=s.factor((4*S-R)/(3+2*h*(a+b)))
    assert all(s.simplify(u)==0 for u in (Z-(pi+T*(s.eye(2)-pi))))
    checks+=1
    X,Y=Y,Z;R,S=S,T

# Rational negative stochastic diagonal at the second completed BDF2 step.
a,b=40,1
h=s.Rational(7,41)
Q=s.Matrix([[-a,a],[b,-b]])
T=(3*s.eye(2)-2*h*Q).inv()*(4*(s.eye(2)-h*Q).inv()-s.eye(2))
assert T[0,0]==-s.Rational(3,697)
assert all(s.simplify(sum(T.row(i))-1)==0 for i in range(2))
print('PASS: exact scalar rational functions n=2..6, shifted-polynomial certificates,')
print('      gamma and critical minimizer,',checks,'direct rational Markov-matrix identities,')
print('      and the rational negative entry -3/697 at rates (40,1), step 7/41.')
