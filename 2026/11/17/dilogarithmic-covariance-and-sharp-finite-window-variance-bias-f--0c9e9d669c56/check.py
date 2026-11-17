"""Standalone numerical cross-checks for logarithmic-observable correlations.
Requires Python and mpmath; numerical checks do not replace the proof.
"""
from mpmath import mp
mp.dps = 45

def covariance(m):
    assert isinstance(m, int) and m >= 1
    return (1+mp.fsum(1+j*mp.polylog(2,-mp.mpf(1)/j)
                      for j in range(1,m)))/m

def branch_integral(m):
    # Numerically integrate independently on every branch of x -> m*x mod 1.
    return (mp.fsum(mp.quad(lambda y: mp.log((j+y)/m)*mp.log(y),
                                [mp.mpf('0'),mp.mpf('0.2'),mp.mpf('1')])
                    for j in range(m))/m)-1

for m in [1,2,3,4,5,8]:
    assert abs(covariance(m)-branch_integral(m)) < mp.mpf('1e-35')
for m in range(1,80):
    assert 0<covariance(m+1)<covariance(m)

B = 1 + mp.euler/4 + mp.nsum(
    lambda q: (-1)**q * mp.zeta(q-1)/q**2, [3,mp.inf])
assert abs(B-mp.mpf('1.0102793965954957479772'))<mp.mpf('1e-21')
for m in [32,64,128,256]:
    approximation=(mp.log(m)/4+B)/m-1/(72*m*m)+1/(288*m**3)
    # Tail is fourth order, with a small uniform prefactor here.
    assert abs(covariance(m)-approximation)<mp.mpf('0.2')/m**4

# Finite-N variance identity checked from two independently grouped sums.
for b in [2,3,4]:
    cov = [mp.mpf('0')]+[covariance(b**k) for k in range(1,8)]
    # For this identity test a finite lag list, with missing tail set to zero.
    sigma = 1+2*mp.fsum(cov[1:])
    kappa = 2*mp.fsum(k*cov[k] for k in range(1,len(cov)))
    for N in [2,3,5,9]:
        direct=N+2*mp.fsum((N-k)*cov[k] for k in range(1,min(N,len(cov))))
        remainder=2*mp.fsum((k-N)*cov[k] for k in range(N,len(cov)))
        assert abs(direct-(N*sigma-kappa+remainder))<mp.mpf('1e-38')
print('PASS: independent branch quadrature, strict monotonicity,')
print('      dilogarithm asymptotics, finite-window covariance identity')
print('B =',mp.nstr(B,25))
print('C(2) =',mp.nstr(covariance(2),22))
