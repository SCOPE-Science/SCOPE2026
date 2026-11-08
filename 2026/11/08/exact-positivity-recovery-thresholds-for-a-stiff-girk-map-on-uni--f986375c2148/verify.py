"""Exact arithmetic checks for the five-state pure-birth GIRK map.
Run: python3 verify.py (requires SymPy >=1.10). This is supplementary to the written proof.
"""
import sympy as S

h,z=S.symbols('h z', real=True)
D=2*h*h+2*h+1
A=S.Matrix([[1,1],[-1,1]])
b=S.Matrix([[0,1]])
F=S.factor(1+z*(b*(S.eye(2)-z*A).inv()*S.ones(2,1))[0])
assert S.factor(F-(1-z)/(1-2*z+2*z*z))==0

expected_derivatives=[
 (h+1)/D,
 (2*h*h+4*h+1)/D**2,
 4*h*(2*h*h+6*h+3)/D**3,
 12*(4*h**4+16*h**3+12*h*h-1)/D**4,
]
for k in range(4):
 assert S.factor(S.diff(F,z,k).subs(z,-h)-expected_derivatives[k])==0

expected_boundary={
 2: h*(2*h+1)/D,
 3: 4*h**3*(h+1)/D**2,
 4: 2*h**3*(2*h+1)*(2*h*h+2*h-1)/D**3,
 5: 4*h**4*(2*h*h-1)*(2*h*h+4*h+1)/D**4,
}
for n in range(2,6):
 B=S.factor(1-sum(h**k*S.diff(F,z,k).subs(z,-h)/S.factorial(k)
                  for k in range(n-1)))
 assert S.factor(B-expected_boundary[n])==0
 # Direct, independent rational matrix evaluation checks EVERY entry.
 Q=S.zeros(n)
 for i in range(n-1):
  Q[i,i]=-1
  Q[i,i+1]=1
 X=h*Q
 P=(S.eye(n)-X)*(S.eye(n)-2*X+2*X*X).inv()
 for i in range(n):
  assert S.factor(sum(P[i,j] for j in range(n))-1)==0
  for j in range(n):
   if i==n-1:
    target=S.Integer(1) if j==n-1 else S.Integer(0)
   elif j<i:
    target=S.Integer(0)
   elif j<n-1:
    k=j-i
    target=h**k*S.diff(F,z,k).subs(z,-h)/S.factorial(k)
   else:
    target=1-sum(h**k*S.diff(F,z,k).subs(z,-h)/S.factorial(k)
                 for k in range(n-i-1))
   assert S.factor(P[i,j]-target)==0,(n,i,j)
 assert S.factor(P[0,n-1]-expected_boundary[n])==0

# An exact coefficient sign witness and all four row sums in n=5.
n=5
Q=S.zeros(n)
for i in range(n-1):Q[i,i],Q[i,i+1]=-1,1
X=S.Rational(1,2)*Q
P=(S.eye(n)-X)*(S.eye(n)-2*X+2*X*X).inv()
assert P[0,4]==-S.Rational(7,625)
assert P*S.ones(5,1)==S.ones(5,1)
assert F.subs(z,-S.Rational(1,2))==S.Rational(3,5)
assert F.subs(z,0)==1

# Strict signs on both sides of exact algebraic thresholds, and equality.
t4=(S.sqrt(3)-1)/2
t5=S.sqrt(2)/2
assert S.simplify(expected_boundary[4].subs(h,t4))==0
assert S.simplify(expected_boundary[5].subs(h,t5))==0
for n,threshold in [(4,t4),(5,t5)]:
 for hh in [S.Rational(1,10),S.Rational(1,3)]:
  if S.simplify(hh<threshold):assert expected_boundary[n].subs(h,hh)<0
 for hh in [S.Integer(1),S.Integer(2)]:
  assert expected_boundary[n].subs(h,hh)>0
assert expected_boundary[2].subs(h,S.Rational(1,10))>0
assert expected_boundary[3].subs(h,S.Rational(1,10))>0
print('EXACT_VERIFY_OK: stages, derivatives, absorbing factors, n=2..5 full matrices, stiff 5-state witness')
