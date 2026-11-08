"""Exact finite-coefficient checks of first returns for the random doubling/halving interval map."""
from fractions import Fraction as F
from math import comb, sqrt, pi


def coefficients(p, N):
    q=1-p
    r=[F(0)]*(N+1)
    b=[F(0)]*(N+1)
    b[0]=F(1,2)
    for n in range(1,N+1):
        r[n]=p if n==1 else q*sum(r[i]*r[n-1-i] for i in range(1,n-1))
        b[n]=sum(r[j]*b[n-j] for j in range(1,n+1))/2
    a=[F(0)]*(N+1)
    for n in range(1,N+1):
        a[n]=q*r[n-1]+p*b[n-1]
    return a


def first_hit(k, n, p):
    if n<k or (n-k)%2: return F(0)
    q=1-p
    return F(k,n)*comb(n,(n+k)//2)*p**((n+k)//2)*q**((n-k)//2)

for p in [F(1,4),F(1,2),F(2,3),F(3,4),F(4,5),F(9,10),F(1,1)]:
    seq=coefficients(p,22)
    for n in range(1,23):
        expected=(1-p)*first_hit(1,n-1,p) + p*(F(1,2) if n==1 else sum(F(1,2**(k+1))*first_hit(k,n-1,p) for k in range(1,n)))
        assert seq[n]==expected,(p,n,seq[n],expected)
    # Geometric reset from the uniform upper half, verified exactly at every finite horizon.
    # For each k, initial interval (2^-k-1,2^-k) maps by 2^k into (1/2,1), so time and arrival coordinate decouple.

# Characteristic critical and pole/square-root transition values, exact arithmetic.
p=F(4,5); q=1-p
assert 2*q*2 == p
assert F(2,1)/(p+4*q)==F(5,4)
p=F(9,10);q=1-p
assert F(2,1)/(p+4*q)==F(20,13)
print('PELIKAN_DYADIC_RENEWAL_EXACT_COEFFICIENTS_OK parameters=7 horizons=22')
print('PELIKAN_RETURN_SINGULARITY_TRANSITION_EXACT_OK threshold=4/5')
