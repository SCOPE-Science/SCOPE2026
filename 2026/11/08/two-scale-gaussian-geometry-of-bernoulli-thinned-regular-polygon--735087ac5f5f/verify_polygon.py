#!/usr/bin/env python3
"""Independent finite geometry and renewal-moment checks for Bernoulli-thinned circular polygons."""
import math
import random
from fractions import Fraction
from itertools import combinations


def st2(n, k):
    if n == k == 0: return 1
    if n == 0 or k == 0: return 0
    return k * st2(n - 1, k) + st2(n - 1, k - 1)


def geom_moment(r, p):
    q = 1-p
    return sum((Fraction(st2(r,j)*math.factorial(j)) * q**(j-1) / p**j for j in range(1,r+1)), Fraction())


def coeff(p):
    M = {r: geom_moment(r, p) for r in range(1,11)}
    rho3, rho5 = p*M[3], p*M[5]
    s33 = p*(M[6] - 2*rho3*M[4] + rho3**2*M[2])
    s35 = p*(M[8] - rho3*M[6] - rho5*M[4] + rho3*rho5*M[2])
    s55 = p*(M[10] - 2*rho5*M[6] + rho5**2*M[2])
    return rho3,rho5,s33,s35,s55


def gaps(selected, n):
    if not selected: return []
    return [b-a for a,b in zip(selected, selected[1:]+[selected[0]+n])]


def geometry(selected, n):
    if len(selected)<2: return 0.,0.
    points = [(math.cos(2*math.pi*i/n), math.sin(2*math.pi*i/n)) for i in selected]
    if len(points)==2:
        dx=points[1][0]-points[0][0];dy=points[1][1]-points[0][1]
        return 0.,2*math.hypot(dx,dy)
    area = abs(math.fsum((x*y2-y*x2 for (x,y),(x2,y2) in zip(points,points[1:]+points[:1]))))/2
    perimeter = math.fsum(math.hypot(x2-x,y2-y) for (x,y),(x2,y2) in zip(points,points[1:]+points[:1]))
    return area,perimeter


def gap_formulas(selected,n):
    g=gaps(selected,n)
    return .5*math.fsum(math.sin(2*math.pi*k/n) for k in g), 2*math.fsum(math.sin(math.pi*k/n) for k in g)

for n in range(3,10):
    for mask in range(1,1<<n):
        idx=[i for i in range(n) if mask&(1<<i)]
        a,l=geometry(idx,n); aa,ll=gap_formulas(idx,n)
        assert abs(a-aa)<2e-12,(n,idx,a,aa)
        assert abs(l-ll)<2e-12,(n,idx,l,ll)
print('EXHAUSTIVE_SMALL_POLYGON_GEOMETRY_PASSED')

p=Fraction(1,2)
r3,r5,s33,s35,s55=coeff(p)
assert (r3,r5,s33,s35,s55)==(13,541,3240,465480,98058600)
assert s33*s55-s35*s35==101038233600
print('EXACT_RENEWAL_MOMENTS_PASSED', r3,r5,s33,s35,s55,'det',s33*s55-s35*s35)

# Direct evaluation of the fourth-order and sixth-order cancellation, without stochastic approximation.
random.seed(128834)
for n in (70,200,500):
    for _ in range(160):
        selected=[i for i in range(n) if random.random()<.5]
        if len(selected)<2: continue
        ar, per=geometry(selected,n)
        gs=gaps(selected,n)
        d=(math.pi-ar)-2*(2*math.pi-per)
        v5=sum(g**5 for g in gs)
        v7=sum(g**7 for g in gs)
        # Bound from sine's fifth-order Taylor remainder, plus floating-point slack.
        assert abs(d + (math.pi**5/(10*n**5))*v5) <= (17*math.pi**7/(1260*n**7))*v7 + 5e-12,(n,d,v5,v7)
print('ANISOTROPIC_GEOMETRIC_CANCELLATION_PASSED')

# Independent Monte Carlo check for nondegenerate two-scale fluctuations.
# The expectation and covariance are computed from exact symbolic geometric moments above.
n=2500
z=[]
for _ in range(3600):
    selected=[i for i in range(n) if random.random()<.5]
    gs=gaps(selected,n)
    z.append(((sum(g**3 for g in gs)-int(r3)*n)/math.sqrt(n),
              (sum(g**5 for g in gs)-int(r5)*n)/math.sqrt(n)))
mean=[math.fsum(v[j] for v in z)/len(z) for j in range(2)]
var=[math.fsum((v[j]-mean[j])**2 for v in z)/(len(z)-1) for j in range(2)]
cross=math.fsum((v[0]-mean[0])*(v[1]-mean[1]) for v in z)/(len(z)-1)
print('MONTE_CARLO_RENEWAL_CHECK', 'means',mean, 'variances',var, 'covariance',cross)
for actual, exact in [(var[0],s33),(var[1],s55),(cross,s35)]:
    assert abs(actual-float(exact)) / float(exact)<.20,(actual,exact)
print('BERNOULLI_POLYGON_TWO_SCALE_CHECKS_PASSED')
