"""Standalone exact-arithmetic diagnostics for a weighted biclique Schur norm formula.
Uses only Python's standard library. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F

def test(m,n,T):
    assert m>=2 and n>=2 and T>=0
    D=2*m*n*T+m+n
    M=F(m*n)
    positive=(M*T*T>1)
    if not positive:
        # Constant one is the exact contractive branch.
        assert M*T*T<=1
        return 2
    z=2*(M*T*T-1)/D
    assert z>0
    # Positive-order upper certificate: the two-dimensional residual determinant.
    assert (2+m*z)*(2+n*z)==m*n*(2*T-z)**2
    assert 2+m*z>0 and 2+n*z>0
    # Sharp trace-norm lower certificate.
    alpha=(n*T+1)/D
    beta=(m*T+1)/D
    assert m*alpha+n*beta==1
    assert (alpha-beta)**2+4*m*n*T*T*alpha*beta==T*T
    assert alpha*beta*(1-m*n*T*T)<0
    witness=(m-1)*alpha+(n-1)*beta+T
    assert witness==1+z
    return 7

checks=0
for m in range(2,36):
 for n in range(2,36):
  for numerator in range(0,31):
   for denominator in (1,3,7,13):
    checks+=test(m,n,F(numerator,denominator*10))
# Known idempotent boundary and additional rational parameter checks.
for m in range(2,80):
 for n in range(2,80):
  T=F(1)
  D=2*m*n+m+n
  L=F(1)+F(2*(m*n-1),D)
  assert L==F(4*m*n+m+n-2,D)
  checks+=1
for m in range(2,80):
 for n in range(2,80):
  for T in (F(1,3),F(1),F(9,7)):
   D=2*m*n*T+m+n
   z=2*(m*n*T*T-1)/D
   if m*n*T*T>1:
    assert z>=0
   checks+=1
print('BICLIQUE_EXACT_IDENTITIES_OK',checks)
