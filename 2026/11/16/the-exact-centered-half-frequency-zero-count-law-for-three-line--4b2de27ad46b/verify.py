"""Standalone finite checks for an exact three-line Gaussian-STFT zero count law.
Run: python verify.py. Only Python standard library required.
The analytic proof, not Monte Carlo, establishes the theorem.
"""
import cmath
import math
import random

rng = random.Random(204117)

def gaussian(scale=1.0):
    return scale * complex(rng.gauss(0, 1), rng.gauss(0, 1))/math.sqrt(2)

def polynomial_roots(a,b,c):
    d=cmath.sqrt(b*b-4*a*c)
    return ((-b+d)/(2*c),(-b-d)/(2*c))

def schur_class(a,b,c):
    # Quadratic Schur-Cohn reduction. All tests avoid unit-circle boundary.
    d=abs(c)**2-abs(a)**2
    e=b*c.conjugate()-a*b.conjugate()
    if abs(e)>abs(d):return 1
    return 2 if d>0 else 0

checked=0
for _ in range(9000):
    a=gaussian()
    b=gaussian(1.7)
    c=gaussian()
    roots=polynomial_roots(a,b,c)
    exact_count=sum(abs(z)<1 for z in roots)
    assert exact_count==schur_class(a,b,c)
    checked+=1

for omega in (0.23,0.67,1.11):
    for _ in range(35):
        a=gaussian(); b=gaussian(); c=gaussian()
        # Here the polynomial coefficient of the middle tone is exp(pi*omega**2) times its amplitude.
        B=b*math.exp(math.pi*omega**2)
        for z in polynomial_roots(a,B,c):
            x=(cmath.phase(z)%(2*math.pi))/(2*math.pi*omega)
            w=math.log(abs(z))/(2*math.pi*omega)
            lhs=a*math.exp(-math.pi*(w+omega)**2)*cmath.exp(-2j*math.pi*(w+omega)*x)
            lhs+=b*math.exp(-math.pi*w*w)*cmath.exp(-2j*math.pi*w*x)
            lhs+=c*math.exp(-math.pi*(w-omega)**2)*cmath.exp(-2j*math.pi*(w-omega)*x)
            bound=sum(abs(v) for v in [a,b,c])+1
            assert abs(lhs)<2e-10*bound, (omega,x,w,lhs)
            checked+=1

# General unequal outer powers: the canonical balanced radius exactly
# reduces the half-frequency count to a standard quadratic with variance beta.
for delta,a0,a1,a2 in ((0.3,0.8,2.1,1.3),(0.6,4.0,0.2,0.3),(0.9,1.3,1.4,1.0)):
    radius=math.sqrt(a0/a2)*math.exp(2*math.pi*delta**2)
    beta=a1*a1/(a0*a2)*math.exp(2*math.pi*delta**2)
    for _ in range(900):
        z0,z1,z2=gaussian(),gaussian(),gaussian()
        A=a0*z0
        B=a1*math.exp(-math.pi*delta**2)*z1
        C=a2*math.exp(-4*math.pi*delta**2)*z2
        roots=polynomial_roots(A,B,C)
        actual=sum(abs(z)<radius for z in roots)
        reduced=schur_class(z0,math.sqrt(beta)*z1,z2)
        assert actual==reduced
        checked+=1

for sigma in (0.5,1,2,5):
    n=110000
    counts=[0,0,0]
    for _ in range(n):
        a=gaussian(); b=gaussian(sigma); c=gaussian()
        counts[schur_class(a,b,c)]+=1
    pr1=sigma/math.sqrt(sigma*sigma+2)
    predictions=((1-pr1)/2,pr1,(1-pr1)/2)
    for k in range(3):
        empirical=counts[k]/n
        assert abs(empirical-predictions[k])<0.012, (sigma,k,empirical,predictions[k])
    checked+=n
print('THREE_LINE_HALF_STRIP_CHECKS_PASSED',checked)
