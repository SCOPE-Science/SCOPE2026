"""Finite diagnostics for two-term power-weight Aluthge asymptotics (Python 3)."""
from math import comb, exp, expm1, fsum, log, log1p


def corrections(alpha, p, t, n, J):
    m, s = n*t, alpha*p
    pmf = [comb(n,k)*t**k*(1-t)**(n-k) for k in range(n+1)]
    assert abs(fsum(pmf)-1) < 2e-13

    def mean_log(j):
        return fsum(prob*log1p(k/j) for k,prob in enumerate(pmf)) + log(j)

    initial = fsum(exp(-s*mean_log(j)) for j in range(1,J+1))
    q = J+m
    tail_lo = q**(1-s)/(s-1)-q**(-s)/2
    trapezoid_error = s*q**(-s-1)/8
    # If Y=X-m, Taylor's inequality from |log''(u)| <= j^-2 for u>=j
    # bounds the log-mean defect by Var(X)/(2j^2). Jensen bounds it below by zero.
    v = s*m*(1-t)/2
    geometric_error = exp(v/(J+1)**2)*v*J**(-s-1)/(s+1)
    leading = m**(1-s)/(s-1)
    lo = (initial+tail_lo-leading)*m**s
    hi = lo+(trapezoid_error+geometric_error)*m**s
    op = m*expm1(-alpha*(mean_log(1)-log(m)))
    return lo, hi, op


for alpha,p,t in ((1.5,2,.3),(.8,2,.7),(1.,2,.5),(.25,5.,.8),(2.,.75,.6)):
    s = alpha*p
    expected_mass = -(1+s*t)/(2*(1+s))
    expected_op = -alpha*(1+t)/2
    for n in (160,360):
        lo,hi,op = corrections(alpha,p,t,n,3000)
        assert hi-lo < 0.002, (alpha,p,t,n,lo,hi)
        assert max(abs(lo-expected_mass),abs(hi-expected_mass)) < 0.02, (alpha,p,t,n,lo,hi)
        assert abs(op-expected_op) < 0.03, (alpha,p,t,n,op)
print('PASS: two finite correction diagnostics at each of 10 parameter choices')
