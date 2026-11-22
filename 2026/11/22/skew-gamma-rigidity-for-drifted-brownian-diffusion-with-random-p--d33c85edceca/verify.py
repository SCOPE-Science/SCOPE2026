"""Exact checks for the drifted Brownian proportional-reset gamma classification.
Only built-in Python libraries; finite checks supplement the analytic proof.
"""
from fractions import Fraction as F
from math import comb

checks = 0

def chk(condition):
    global checks
    assert condition
    checks += 1

def rising(x,n):
    t=F(1)
    for j in range(n): t *= x+j
    return t

def moments_bilateral(p,r,a,b,N):
    return [sum(F(comb(n,k))*rising(p,k)*a**k*(-1)**(n-k)*rising(r,n-k)*b**(n-k) for k in range(n+1)) for n in range(N+1)]

# Exact moment equations for attainable distinct-gamma-shape stationary targets.
for a in range(1,8):
    for b in range(1,8):
        if a==b: continue
        for theta in (F(1,2),F(2,3),F(1),F(2),F(3),F(5)):
            a,b,theta=F(a),F(b),F(theta)
            p=1+theta*a/(a+b)
            r=1+theta*b/(a+b)
            Y=moments_bilateral(p,r,a,b,9)
            X=moments_bilateral(F(1),F(1),a,b,9)
            for n in range(10):
                rhs=sum(F(comb(n,k))*X[n-k]*(theta/(theta+k))*Y[k] for k in range(n+1))
                chk(Y[n]==rhs)
            chk((p-1)*b==(r-1)*a)

# Exact beta CDF crossing at the shape-loss boundary for integer parameters.
# For integer positive p,r, I_x(p,r)=P(Bin(p+r-1,x)>=p).
def beta_cdf_integer(p,r,x):
    n=p+r-1
    return sum(F(comb(n,k))*x**k*(1-x)**(n-k) for k in range(p,n+1))
for p in range(2,14):
    for r in range(2,14):
        x=F(r-1,p+r-2)
        chk(beta_cdf_integer(p,r,x)==beta_cdf_integer(p-1,r-1,x))
        # Opposite signs either side establish unique crossing in these examples.
        if x>F(1,1000):
            d=beta_cdf_integer(p,r,x/2)-beta_cdf_integer(p-1,r-1,x/2)
            chk(d<0)
        if x<F(999,1000):
            y=(x+1)/2
            d=beta_cdf_integer(p,r,y)-beta_cdf_integer(p-1,r-1,y)
            chk(d>0)

print(f"PASS {checks} exact rational moment and beta-CDF checks")
