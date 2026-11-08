"""Reproducible supplementary checks for the exact bidisc section law.

Only the accompanying geometric and Grassmannian proofs establish the infinite assertion.
Python 3 standard library; no optional dependencies.
"""
from math import sqrt, sin, cos, pi, acos, isclose
from random import Random

rng=Random(192631)

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sample_frame():
    u=[rng.gauss(0,1) for _ in range(4)]
    norm=sqrt(dot(u,u));u=[x/norm for x in u]
    v=[rng.gauss(0,1) for _ in range(4)]
    cross=dot(u,v);v=[y-cross*x for x,y in zip(u,v)]
    norm=sqrt(dot(v,v));v=[y/norm for y in v]
    return u,v

def calc(u,v):
    a=dot(u[:2],u[:2]);b=dot(v[:2],v[:2]);c=dot(u[:2],v[:2]);
    tr=a+b;gap=sqrt(max(0,(a-b)**2+4*c*c));lo=(tr-gap)/2;hi=(tr+gap)/2
    t=max(0.5,lo,1-hi)
    return 2/sqrt(t),lo,hi

def plucker(u,v,i,j):return u[i]*v[j]-u[j]*v[i]

def cdf(s):
    if s<2:return 0.0
    if s>=2*sqrt(2):return 1.0
    gamma=acos(max(-1.,min(1.,8/(s*s)-1)))
    return 1-cos(gamma)-gamma*sin(gamma)/2

# Independently integrate the angular indicator in the two free uniform
# Grassmann coordinates. Quadrature is supplementary, not proof.
def simpson(f,a,b,n=1200):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*j-1)*h) for j in range(1,n//2+1))+2*sum(f(a+2*j*h) for j in range(1,n//2)))
for s in [2.05,2.2,2.4,2.6,2.8]:
    g=acos(8/s**2-1)
    integral=simpson(lambda a:sin(a)*(1-cos(g-a)),0,g)
    assert abs(integral-cdf(s))<3e-9,(s,integral,cdf(s))
assert abs((1-cdf(2*sqrt(2)-1e-8))-pi/4)<0.0002

N=18000
atom=0
thresholds=[2.1,2.3,2.5,2.7,2.81]
counts=[0]*len(thresholds)
for i in range(N):
    u,v=sample_frame();diam,lo,hi=calc(u,v)
    if lo<=0.5<=hi:atom+=1
    for j,s in enumerate(thresholds):counts[j]+=(diam<=s)
    if i<240:
        # independent Pluecker identities for compressed signed projection
        p12=plucker(u,v,0,1);p34=plucker(u,v,2,3)
        U=p12+p34;V=p12-p34
        assert isclose(2*(lo+hi)-2,2*U*V,rel_tol=1e-8,abs_tol=1e-8)
        assert isclose((2*lo-1)*(2*hi-1),U*U+V*V-1,rel_tol=1e-8,abs_tol=1e-8)
    if i<8:
        # Directly calculate physical section radial lengths on a mesh.
        brute=0.0
        for j in range(20001):
            theta=pi*j/10000
            w=[cos(theta)*u[k]+sin(theta)*v[k] for k in range(4)]
            radius=1/max(sqrt(w[0]**2+w[1]**2),sqrt(w[2]**2+w[3]**2))
            brute=max(brute,2*radius)
        assert 0<=diam-brute<0.001,(diam,brute)
assert abs(atom/N-pi/4)<0.02,(atom/N,pi/4)
for j,s in enumerate(thresholds):
    assert abs(counts[j]/N-cdf(s))<0.02,(s,counts[j]/N,cdf(s))
print('PASS: 5 independent quadratures; 240 Pluecker identities; 8 direct section diameters; 18000 Haar frames; 5 CDF and endpoint comparisons.')
