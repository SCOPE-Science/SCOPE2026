"""Exact identities for lines on the cone over the quadratic Veronese surface.

Run: python verify_veronese_fano.py . No external files or modules beyond sympy.
These finite identity checks corroborate, but do not replace, the general proof.
"""
import sympy as S

s,t,A,B,lam=S.symbols('s t A B lam')
p=S.Matrix([[1,t,s],[t,t*t,t*s],[s,t*s,s*s]])
b=S.Matrix([[0,A,B],[A,2*t*A,t*B+s*A],[B,t*B+s*A,2*s*B]])

# Every 2-by-2 minor of the symmetric matrix at p+lambda*b vanishes
# mod (A^2, AB, B^2), and the three quadratic generators occur directly.
minors=[]
M=p+lam*b
for i in range(3):
 for j in range(i+1,3):
  for k in range(3):
   for l in range(k+1,3):
    minors.append(S.expand(M[i,k]*M[j,l]-M[i,l]*M[j,k]))
assert len(minors)==9
for f in minors:
 poly=S.Poly(f,A,B)
 assert all(sum(mon)>=2 or coeff==0 for mon,coeff in poly.terms()),f
assert S.expand(M[0,0]*M[1,1]-M[0,1]**2)==-lam**2*A**2
assert S.expand(M[0,0]*M[2,2]-M[0,2]**2)==-lam**2*B**2
assert S.expand(M[0,0]*M[1,2]-M[0,1]*M[0,2])==-lam**2*A*B

# Cross-chart coordinates: X_11 is the pivot on the second affine chart.
# Equality of parameterizations in the quotient follows from these identities.
assert S.simplify(b[0,1]-b[1,1]*p[0,1]/p[1,1]+A)==0
assert S.simplify(b[1,2]-b[1,1]*p[1,2]/p[1,1]-(t*B-s*A))==0

# Transition for Omega_{P^2}(2): using t'=1/t, s'=s/t,
# and the O(2) frame scaled by t^2, is (-A, tB-sA).
assert S.simplify(t**2*S.diff(1/t,t)+1)==0
assert S.simplify(t**2*(S.diff(s/t,t)*A+S.diff(s/t,s)*B)-(t*B-s*A))==0

n=S.symbols('n',integer=True)
chi_O=lambda m:S.expand((m+1)*(m+2)*S.Rational(1,2))
chi_Omega=lambda m:S.expand(3*chi_O(m-1)-chi_O(m))
assert S.expand(chi_O(2*n)+chi_Omega(2*n+2) - (6*n**2+11*n+4))==0
assert S.simplify(chi_O(0)+chi_Omega(2)-4)==0
for characteristic in [0,2,3,5,7]:
 for f in minors:
  for term,coefficient in S.Poly(f,A,B,lam).terms():
   if term[0]+term[1]<2:
    if characteristic==0: assert coefficient==0
    else: assert S.Poly(coefficient,s,t,modulus=characteristic).is_zero
 print(f'characteristic={characteristic}: tangent-jet and square-zero identities passed')
print('ALL_CHECKS_PASSED')
