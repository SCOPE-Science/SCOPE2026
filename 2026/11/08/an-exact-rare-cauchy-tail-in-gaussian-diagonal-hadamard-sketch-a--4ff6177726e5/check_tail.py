"""Standalone arithmetic checks for the Gaussian-diagonal Hadamard regression law.

Run: python check_tail.py.  These finite checks supplement, not replace,
the analytic probability and moment proofs in RESULT.md.
"""
import math
from fractions import Fraction
from scipy.integrate import quad


def rho_distribution(m):
    return [(Fraction(2*j-m, m), Fraction(math.comb(m,j), 2**m))
            for j in range(m+1)]


def cdf_cond(z, rho):
    a=float(rho)
    if abs(a)==1:
        return 0.5+math.atan(z)/math.pi
    bound=1/math.sqrt(1-a*a)
    if z <= -bound:return 0.0
    if z >= bound:return 1.0
    return 0.5 + math.asin(z/math.sqrt(1+a*a*z*z))/math.pi


def density_cond(z,rho):
    a=float(rho)
    if abs(a)==1:return 1/(math.pi*(1+z*z))
    bound=1/math.sqrt(1-a*a)
    if abs(z)>=bound:return 0.0
    return 1/(math.pi*(1+a*a*z*z)*math.sqrt(1-(1-a*a)*z*z))


def full_tail(t,m):
    assert t>=0
    return sum(float(w)*2*(1-cdf_cond(t,a)) for a,w in rho_distribution(m))


def cauchy_tail(t):
    return 2*math.atan(1/t)/math.pi if t>0 else 1.0

checks=0
for m in range(1,15):
    dist=rho_distribution(m)
    assert sum(w for _,w in dist)==1
    collision=sum(w for a,w in dist if abs(a)==1)
    assert collision == Fraction(2,2**m)
    threshold=0.0 if m==1 else m/(2*math.sqrt(m-1))
    for t in [threshold+0.1,threshold+1,threshold+10,threshold+100]:
        got=full_tail(t,m)
        expected=float(collision)*cauchy_tail(t)
        assert abs(got-expected) < 5e-14,(m,t,got,expected)
        checks+=1
    # Stable scaled tail at increasing t approaches exact coefficient.
    t=1e7
    assert abs(t*full_tail(t,m)-float(collision)*2/math.pi)<1e-8
    checks+=1

for a in [-.95,-.7,-.3,0,.2,.75,.99]:
    bound=1/math.sqrt(1-a*a)
    # Density normalization via endpoint-regularized substitution z=bound*sin(theta).
    norm=quad(lambda theta: 1/(math.pi*(1+a*a*(bound*math.sin(theta))**2)),
              -math.pi/2,math.pi/2,epsabs=1e-12)[0]*bound
    assert abs(norm-1)<2e-10,(a,norm)
    checks+=1
    # For a symmetric law P(Z <= 0) = 1/2, test exact CDF vs density integration.
    for z in [0.0,.1,.5,.9*bound]:
        # analytic partial integral in endpoint-substitution coordinates
        upper=math.asin(z/bound)
        cdf_num=quad(lambda th:bound/(math.pi*(1+a*a*bound*bound*math.sin(th)**2)),
                     -math.pi/2,upper,epsabs=1e-12)[0]
        assert abs(cdf_num-cdf_cond(z,a))<2e-10,(a,z,cdf_num,cdf_cond(z,a))
        checks+=1

print(f"PASS: {checks} finite arithmetic checks, plus exact fraction collision counts for m=1..14")
