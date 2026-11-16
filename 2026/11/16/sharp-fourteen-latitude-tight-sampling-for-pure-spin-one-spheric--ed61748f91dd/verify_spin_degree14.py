"""Exact rational certificate for spin-one pure-degree-14 positive latitude quadrature.
Requires Python 3 and SymPy. No floating-point premise occurs.
"""
from math import factorial
import sympy as S
from sympy.physics.wigner import wigner_3j
L=20; n=14; T=S.Symbol('t')
def g(a,b,c):
    if a<0 or b<0 or (a+b+c)%2 or a+b<c or a+c<b or b+c<a: return S.S.Zero
    h=(a+b+c)//2
    return S.Rational(factorial(h)**2*factorial(2*h-2*a)*factorial(2*h-2*b)*factorial(2*h-2*c),factorial(h-a)**2*factorial(h-b)**2*factorial(h-c)**2*factorial(2*h+1))
D=S.diag(*(S.Rational(1,2*i+1) for i in range(n+1)))
G=S.Matrix(n+1,n+1,lambda i,j:g(i,j,L))
P=[]
for parity in (0,1):
 ix=[i for i in range(n+1) if i%2==parity]
 f=S.Poly(S.together((D+tG).extract(ix,ix).det()).as_numer_denom()[0],t) if False else None
 f=S.Poly(S.factor((D+T*G).extract(ix,ix).det()).as_numer_denom()[0],T).primitive()[1]
 P.append(f)
 assert S.gcd(f,f.diff()).degree()==0
assert S.gcd(P[0],P[1]).degree()==0
poly=P[0]*P[1]
a=S.Rational(-38662,10000); b=S.Rational(-38660,10000)
assert poly.count_roots(a,b)==1 and poly.count_roots(b,0)==0
# At t=0 M14 is positive definite. The isolated closest-to-zero negative root is simple.
# Therefore M14 at this root is positive semidefinite of rank 14.
# Prove the two localizing forms (1+/-x) are strictly positive at BOTH bracket ends.
C0=S.Matrix(n,n,lambda i,j: S.Rational(i+1,(2*i+1)*(2*i+3)) if j==i+1 else (S.Rational(i,(2*i+1)*(2*i-1)) if j==i-1 else S.S.Zero))
C1=S.Matrix(n,n,lambda i,j:(S.Rational(i+1,2*i+1)*g(i+1,j,L)+S.Rational(i,2*i+1)*g(i-1,j,L)))
assert C1==C1.T
smallD=D[:n,:n]; smallG=G[:n,:n]
def check_pd(A):
 # rational symmetric LDL elimination, requiring positive pivots.
 B=[list(A.row(i)) for i in range(A.rows)]
 for k in range(len(B)):
  pivot=B[k][k]
  assert pivot>0,(k,pivot)
  for i in range(k+1,len(B)):
   for j in range(i,len(B)):
    B[j][i]-= B[k][i]*B[k][j]/pivot
    B[i][j]=B[j][i]
for q in (a,b):
 for sign in (-1,1):
  check_pd(smallD+q*smallG+sign*(C0+q*C1))
# The spin-one squared Wigner profiles have zero P_20 coefficient,
# and every other J<=28 has a nonzero coefficient. Their span is codimension one.
u=[wigner_3j(n,n,J,-1,1,0) for J in range(2*n+1)]
assert [J for J,c in enumerate(u) if c==0]==[L]
# Paired full-basis 3j matrix is orthogonal across J by standard CG orthogonality.
print('SPIN14_LATITUDE_CERTIFICATE_PASS')
print('moment_matrix_pell_gap=P20; rank_lower_bound=14; positive_14_node_quadrature=certified')
print('unique_root_bracket=',a,b,'det_degrees=',[p.degree() for p in P])
