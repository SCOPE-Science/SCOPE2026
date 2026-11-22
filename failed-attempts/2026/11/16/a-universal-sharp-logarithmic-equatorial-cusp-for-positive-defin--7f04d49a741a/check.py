"""Independent finite checks for the logarithmic Legendre equator cusp.

Run: python check.py
Only numerical tests; the analytic estimates are in RESULT.md.
"""
import math
import mpmath as mp

Z=float(mp.zeta(mp.mpf('1.5')))
C=math.sqrt(8/math.pi)/Z

def Pprime_formula(j):
    m=2*j
    return math.exp(math.lgamma(2*m+3)-(2*m+1)*math.log(2)-math.lgamma(m+1)-math.lgamma(m+2))

def Pprime_recurrence(j):
    n=4*j+1
    # Differentiate Bonnet's three-term recurrence at x=0.
    a,b,da,db=1.,0.,0.,1.
    if n==1:return db
    for k in range(1,n):
        c=-(k/(k+1))*a
        dc=((2*k+1)*b-k*da)/(k+1)
        a,b,da,db=b,c,db,dc
    return db

# Exact Legendre derivatives agree with recurrence, independently of factorials.
for j in range(80):
    u=Pprime_formula(j);v=Pprime_recurrence(j)
    assert abs(u-v)<2e-11*(1+abs(u)),(j,u,v)

# Bulk recurrence computes the full Legendre sum through a chosen index.
def partial_phi(h,J):
    x=-math.sin(h)
    a,b=1.,x
    acc=b
    for n in range(1,4*J+1):
        c=((2*n+1)*x*b-n*a)/(n+1)
        a,b=b,c
        if (n+1)%4==1:
            j=(n+1-1)//4
            acc+=b/(j+1)**1.5
    return acc/Z

# The bounded residual (phi(h)+C*h*log(1/h))/h tests the predicted O(h) term.
rows=[]
J=75000
for h in (0.04,0.02,0.01,0.005,0.0025):
    v=partial_phi(h,J)
    residual=(v+C*h*math.log(1/h))/h
    rows.append((h,v,-v/(h*math.log(1/h)),residual))
    assert v<0
    assert abs(residual)<1.5
    # All partial terms are odd in cos(theta) and hence exactly odd around equator.
    if h in (0.04,0.01):
        vneg=partial_phi(-h,J)
        assert abs(vneg+v)<1e-11

# The logarithmic derivative coefficient is exact by Stirling, with subleading bounded sums.
for N in (1000,10000,100000):
    import numpy as np
    from scipy.special import gammaln
    j=np.arange(1,N+1,dtype=float)
    m=2*j
    g=np.exp(gammaln(2*m+3)-(2*m+1)*math.log(2)-gammaln(m+1)-gammaln(m+2))
    terms=g/(j+1)**1.5
    v=(1+terms.sum())/Z
    assert abs(v-C*math.log(N))<3.0
print('cusp_C',format(C,'.15f'))
print('h phi(h) estimated_C residual_over_h')
for row in rows:print(*['%.12g'%v for v in row])
print('PASS: 80 exact-identity comparisons; 5 cusp residual checks; 2 reflection checks; 3 logarithmic slope checks')
