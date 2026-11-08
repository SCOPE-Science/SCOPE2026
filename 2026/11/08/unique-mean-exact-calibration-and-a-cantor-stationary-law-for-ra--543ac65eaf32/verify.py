"""Standalone checks for the two-state randomized exact-flow splitting theorem.
Only standard-library arithmetic; finite checks supplement, not replace, the analytic proof.
Run: python verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log, tanh, isclose

checks = 0

def check(ok, note):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(note)

# Exact Bernoulli-convolution finite-horizon identities.
# The parameter q is e^{-(a+b)h}, and p=a/(a+b).
for p in (F(1,5), F(2,5), F(1,2), F(3,5), F(4,5)):
    r = 1-p
    for q in (F(1,4), F(1,3), F(1,2), F(2,3), F(3,4)):
        for z0 in (F(0),F(1,5),F(1,2),F(1)):
            for n in range(1,8):
                mean = F(0)
                mean2 = F(0)
                for path in product((0,1),repeat=n):
                    z = z0
                    w = F(1)
                    for bit in path:
                        z = q*z+(1-q)*bit
                        w *= r if bit else p
                    mean += w*z
                    mean2 += w*z*z
                target_mean = q**n*z0+(1-q**n)*r
                target_var = p*r*(1-q)**2*(1-q**(2*n))/(1-q**2)
                check(mean==target_mean,('mean',p,q,z0,n))
                check(mean2-mean**2==target_var,('variance',p,q,z0,n))
                check(q**n * abs(z0-r) + (1-q**n)*r >= 0, 'range')
# General sampling exact stationary mean and uniqueness checks.
for a,b in ((1,1),(2,3),(1,7),(5,2),(3,9)):
    s = a+b
    for h in (0.02, 0.1, 0.4, 1.0, 2.3):
        pstar = a/s
        for p in (0.1,0.25,0.4,0.5,0.6,0.75,0.9,pstar):
            qa = exp(-a*h/p)
            qb = exp(-b*h/(1-p))
            avg = (1-p)*(1-qb)/(p*(1-qa)+(1-p)*(1-qb))
            exact = b/s
            check((abs(avg-exact)<1e-11)==(abs(p-pstar)<1e-13),('unique',a,b,h,p,avg))
            if abs(p-pstar)<1e-13:
                q = exp(-s*h)
                check(isclose(qa,q,abs_tol=1e-12),('qa',a,b,h))
                check(isclose(qb,q,abs_tol=1e-12),('qb',a,b,h))
                check(isclose(avg,exact,abs_tol=1e-12),('mean_exact',a,b,h))
                check(isclose(pstar*(1-pstar)*(1-q)/(1+q),pstar*(1-pstar)*tanh(s*h/2),abs_tol=1e-13),'var')
# Exact cover and gap benchmark for q=1/3, p=2/5, a=2, b=3.
p,q,r = F(2,5),F(1,3),F(3,5)
check(p*r*(1-q)/(1+q)==F(3,25),'stationary variance 3/25')
check(min(p,r)-q==F(1,15),'exact gap 1/15')
for n in range(1,10):
    for z0 in (F(0),F(1,3),F(3,5),F(1)):
        for path in product((0,1),repeat=n):
            z=z0
            for bit in path:
                z=q*z+(1-q)*bit
            check(abs(z-r)>=F(1,15)-q**n,('gap',n,z0,path,z))
# Shannon/mass dimension and support dimensions in separated regime.
for prob,ratio in ((.4,1/3),(.5,1/3),(.4,.5),(.5,.5)):
    H=-prob*log(prob)-(1-prob)*log(1-prob)
    dim=H/(-log(ratio))
    check(0<dim<=1+1e-12,('dimension',prob,ratio))
    if ratio<0.5:
        check(dim<=log(2)/(-log(ratio))+1e-12,('measure vs support',prob,ratio))
    if ratio==0.5 and prob==0.5:
        check(isclose(dim,1,abs_tol=1e-14),'critical uniform')
print('VERIFIED checks=',checks)
print('exact_example: p=2/5, q=1/3, stationary mean=3/5, variance=3/25, gap=1/15')
print('analytic proof required for all n, real rates and Hausdorff dimension')
