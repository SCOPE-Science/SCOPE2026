"""Exact finite-sample checks for the uniform Gini/order-quantile result.

Requires Python 3 standard library only; this checker is supplementary to the proof.
"""
from fractions import Fraction as F
from math import isqrt


def formula(n, k):
    N = n + 1
    covariance = F(k*(N-k)*(2*k-N), 3*n*(n-1)*N*(n+2))
    vg = F(n+3, 45*n*(n-1))
    vx = F(k*(N-k), N*N*(n+2))
    r2 = F(5*k*(N-k)*(2*k-N)**2, n*(n-1)*(n+2)*(n+3))
    return covariance, vg, vx, r2


def direct(n, k):
    N = n + 1
    coefs = [F(2*(2*i-N), n*(n-1)) for i in range(1, n+1)]
    def cov_x(i, j):
        return F(min(i,j)*(N-max(i,j)), N*N*(N+1))
    cg = sum((coefs[i-1]*cov_x(i,k) for i in range(1,n+1)),F(0))
    vg = sum((coefs[i-1]*coefs[j-1]*cov_x(i,j)
              for i in range(1,n+1) for j in range(1,n+1)), F(0))
    vx = cov_x(k,k)
    return cg, vg, vx, F(cg*cg,vg*vx)


def score(n, k):
    N=n+1
    return k*(N-k)*(2*k-N)**2


def conditional(n, k):
    m, r = k-1, n-k
    # Count left-left, right-right, left-right, and pairs with the pivot.
    scale = F(2,n*(n-1))
    intercept = scale*(F(r*(r+2),6)+F(m*r,2))
    slope = scale*F(m*(m+2)-r*(r+2),6)
    expected_slope=F((n+1)*(2*k-n-1),3*n*(n-1))
    expected_intercept=F(1,3)-expected_slope*F(k,n+1)
    return intercept,slope,expected_intercept,expected_slope

checks=0
for n in range(2,61):
    for k in range(1,n+1):
        assert formula(n,k) == direct(n,k), (n,k)
        assert conditional(n,k)[:2] == conditional(n,k)[2:], (n,k)
        checks += 6

for n in range(2,601):
    N=n+1
    scores=[score(n,k) for k in range(1,n+1)]
    top=max(scores)
    winners={k for k,s in enumerate(scores,1) if s==top}
    admissible_t={abs(2*k-N) for k in range(1,n+1)}
    tstar=min(admissible_t,key=lambda t: (abs(2*t*t-N*N),t))
    mindist=min(abs(2*t*t-N*N) for t in admissible_t)
    selected={k for k in range(1,n+1)
              if abs(2*(2*k-N)**2-N*N)==mindist}
    assert winners == selected, (n,winners,selected)
    pell_tie=any(N*N-2*j*j==2 for j in range(1,N))
    assert (len(winners)==4)==pell_tie,(n,winners,pell_tie)
    assert len(winners) in (2,4), (n,winners)
    checks+=3

# Independent Pell recurrence check.
N,j=2,1
seen=[]
while N<=601:
    if N>2:
        seen.append(N-1)
    N,j=3*N+4*j,2*N+3*j
assert seen==[9,57,337],seen
assert [ [k for k in range(1,n+1) if score(n,k)==max(score(n,r) for r in range(1,n+1))]
         for n in seen ] == [[1,2,8,9],[8,9,49,50],[49,50,288,289]]
checks+=4
print(f'PASS: {checks} exact rational, integer optimization, and Pell checks')
