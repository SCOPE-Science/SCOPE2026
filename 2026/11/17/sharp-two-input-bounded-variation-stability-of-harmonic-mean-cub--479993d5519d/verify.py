"""Standalone exact identities and finite stress checks for harmonic-mean Hermite variation.

Run: python3 verify.py. Python standard library only.
The analytic proof in RESULT.md, not finite tests, proves the all-sequence bound.
"""
from fractions import Fraction as Q
from math import sqrt
from random import Random

def polyadd(*polys):
    n=max(len(p) for p in polys)
    return tuple(sum((p[j] if j<len(p) else 0 for p in polys), Q(0)) for j in range(n))
def scale(p,k):return tuple(k*x for x in p)
def deriv(p):return tuple(j*p[j] for j in range(1,len(p)))
def ev(p,t):return sum((a*t**i for i,a in enumerate(p)),0)
S=(Q(0),Q(0),Q(3),Q(-2))
A=(Q(0),Q(1),Q(-2),Q(1))
B=(Q(0),Q(0),Q(-1),Q(1))
assert deriv(S)==(Q(0),Q(6),Q(-6))
assert deriv(A)==(Q(1),Q(-4),Q(3))
assert deriv(B)==(Q(0),Q(-2),Q(3))
assert deriv(polyadd(S,scale(A,2)))==(Q(2),Q(-2),Q(0))
assert deriv(polyadd(S,scale(B,2)))==(Q(0),Q(2),Q(0))
assert deriv(polyadd(S,scale(A,2),scale(B,2)))==(Q(2),Q(-6),Q(6))
assert ev(A,Q(1,3))==Q(4,27)
assert ev(B,Q(2,3))==-Q(4,27)
assert Q(1)+Q(8,27)*(2+2)==Q(59,27)
print('EXACT_HERMITE_CORNER_NONNEGATIVITY_POLYNOMIALS_PASS')
print('EXACT_SIDE_BUMP_EXTREMA_AND_SHARP_GAIN_PASS',Q(59,27))

def harmonic(a,b):
    return 2*a*b/(a+b) if a*b>0 else type(a)(0)
for n in (2,3,5,10,100,10000):
    e=Q(1,n)
    m=harmonic(Q(1),e)
    ratio=Q(1)+Q(16,27)*m/e
    assert ratio==Q(1)+Q(32,27)/(1+e)
    assert ratio<Q(59,27)
assert Q(59,27)-Q(1)==Q(32,27)
print('EXACT_RATIONAL_NEAR_PLATEAU_SHARPNESS_PASS')

# Independently calculate total variation of a finite piecewise-cubic difference
# from its real quadratic critical points; this is a finite numerical check only.
def coefficients(s):
    y=[0.]
    for a in s:y.append(y[-1]+a)
    m=[0.]*len(y)
    for j in range(1,len(y)-1):m[j]=harmonic(s[j-1],s[j])
    return [(y[i],m[i],3*s[i]-2*m[i]-m[i+1],-2*s[i]+m[i]+m[i+1]) for i in range(len(s))]
def var_difference(a,b):
    ans=0.
    for pa,pb in zip(coefficients(a),coefficients(b)):
        p=[x-y for x,y in zip(pa,pb)]
        aa=3*p[3];bb=2*p[2];cc=p[1]
        points=[0.,1.]
        if abs(aa)<1e-13:
            if abs(bb)>1e-13:points.append(-cc/bb)
        else:
            disc=bb*bb-4*aa*cc
            if disc>=0:
                q=sqrt(disc)
                points.extend(((-bb-q)/(2*aa),(-bb+q)/(2*aa)))
        points=sorted(set(x for x in points if 0<=x<=1))
        def f(t):return p[0]+t*(p[1]+t*(p[2]+t*p[3]))
        ans+=sum(abs(f(v)-f(u)) for u,v in zip(points,points[1:]))
    return ans
rng=Random(2026)
max_ratio=0.
for _ in range(3200):
    n=rng.randrange(5,15)
    a=[rng.choice((-1,0,1))*10**rng.uniform(-3,2) for j in range(n)]
    b=[v+rng.choice((-1,1))*10**rng.uniform(-5,1) for v in a]
    denom=sum(abs(v-w) for v,w in zip(a,b))
    ratio=var_difference(a,b)/denom
    assert ratio<=59/27+1e-7,(a,b,ratio)
    max_ratio=max(max_ratio,ratio)
for e in (0.2,0.05,0.001):
    a=[0.,1.,0.,1.,0.]
    b=[0.,1.,e,1.,0.]
    ratio=var_difference(a,b)/e
    assert abs(ratio-(1+32/(27*(1+e))))<2e-9
print('INDEPENDENT_CUBIC_CRITICAL_POINT_NUMERICAL_STRESS_PASS',3200)
print('ALL_HARMONIC_HERMITE_VARIATION_CHECKS_PASS')
