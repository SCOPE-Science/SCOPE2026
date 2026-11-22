"""Reproduce exact algebra and finite-sample calibration for inverse-Weibull lower-record comparison.

No external dependencies. Run: python verify.py
The sharp asymptotic statements follow analytically from Poisson tails and Stirling's formula, not the checks here.
"""
import math
import random
from fractions import Fraction

checks=0

def check(ok, detail):
    global checks
    assert ok, detail
    checks += 1

def profile_coefficient(records, beta):
    """Profiled likelihood with common factor exp(-m) omitted."""
    m=len(records)
    rm=records[-1]
    numerator=Fraction((beta*m)**m,1) * rm**(beta*m)
    denom=math.prod(r**(beta+1) for r in records)
    return numerator/denom

def gamma_integer_cdf(z,k):
    """For a Gamma(k,1) variable, integer k>=1."""
    return 1 - math.exp(-z)*math.fsum(z**j/math.factorial(j) for j in range(k))

def gamma_integer_sf(z,k):
    return math.exp(-z)*math.fsum(z**j/math.factorial(j) for j in range(k))

# An exact-rational test for the nonconstant scale-corrected formula.
for m in range(2,16):
    for offset in range(1,17):
        vals=[Fraction(5*m+4*offset+3*(m-i),m+offset+i) for i in range(m)]
        vals=sorted(vals,reverse=True)
        for b1,b2 in [(1,2),(1,3),(2,3),(2,5)]:
            got=profile_coefficient(vals,b2)/profile_coefficient(vals,b1)
            expected=Fraction(b2,b1)**m*math.prod((vals[-1]/v)**(b2-b1) for v in vals)
            check(got==expected,(m,offset,b1,b2,got,expected))

# Exponential-record arrival-time pivot, with both nuisance scale and both models.
rng=random.Random(908172)
for m in [3,7,11]:
    for beta in [1,2,3]:
        for scale in [0.25,4.5]:
            sample_count=25000
            sum_g=0.0
            sum_g2=0.0
            correct=0
            for _ in range(sample_count):
                arrivals=[]
                t=0.0
                for _ in range(m):
                    t+=rng.expovariate(1.0)
                    arrivals.append(t)
                records=[(scale/y)**(1.0/beta) for y in arrivals]
                G=math.fsum(math.log(arrivals[-1]/y) for y in arrivals[:-1])
                logLR=m*math.log(2)+math.fsum(math.log(records[-1]/r) for r in records)
                check(abs(logLR-(m*math.log(2)-G/beta))<2.0e-12,'pivot identity')
                sum_g+=G;sum_g2+=G*G
                if (beta==2 and logLR>0) or (beta==1 and logLR<0):correct+=1
            mean_g=sum_g/sample_count
            var_g=sum_g2/sample_count-mean_g**2
            check(abs(mean_g-(m-1))<6*math.sqrt((m-1)/sample_count),'gamma mean')
            check(abs(var_g-(m-1))<max(0.38,8*(m-1)/math.sqrt(sample_count)),'gamma variance')
            if beta in (1,2):
                true_p=(gamma_integer_cdf(2*m*math.log(2),m-1)
                        if beta==2 else gamma_integer_sf(m*math.log(2),m-1))
                se=math.sqrt(true_p*(1-true_p)/sample_count)
                check(abs(correct/sample_count-true_p)<6*se+0.002,'exact power versus simulation')

# Rates are identical at the two sides of every fixed-shape pair.
for ratio in [1.01,1.1,1.5,2,3,7,50]:
    c=math.log(ratio)/(ratio-1)
    J=lambda x:x-1-math.log(x)
    check(c<1<ratio*c,'strict split')
    check(abs(J(c)-J(ratio*c))<2e-13,'common error exponent')

for m in [3,7,8,9,10,11,50]:
    pcs=gamma_integer_cdf(2*m*math.log(2),m-1)
    power=gamma_integer_sf(m*math.log(2),m-1)
    check(0<pcs<1 and 0<power<1,'valid probability')
    if m in (7,11):
        print('m=%d: exact IR selection %.9f; exact IE selection %.9f'%(m,pcs,power))
print('Shared error exponent for shapes 1 and 2: %.12f'%(
    math.log(2)-1-math.log(math.log(2))))
print('%d reproducibility assertions passed'%checks)
