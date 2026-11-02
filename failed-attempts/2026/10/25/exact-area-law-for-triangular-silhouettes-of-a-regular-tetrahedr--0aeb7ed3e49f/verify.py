"""Numerical consistency checks for the marked tetrahedral shadow-area theorem.
Run: python verify_tetra_silhouette.py (numpy, scipy required).
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad
from numpy.random import default_rng
V=np.array([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)],float)
S0=4*math.sqrt(2/3)
Smin=2*math.sqrt(2)
S3max=2*math.sqrt(3)
r=math.asin(1/3)

def area(u):
    return np.abs(np.asarray(u)@V.T).sum(axis=-1)
def triangle(u):
    q=np.abs(np.asarray(u))
    return q.sum(axis=-1)>2*q.max(axis=-1)

def segment(s):
    if s>=S0:return 0.0
    b=math.acos(s/S3max)
    z=math.sin(b)
    A=math.acos(np.clip(math.cos(b)/(2*math.sqrt(2)*z),-1,1))
    C=math.acos(np.clip(1/(3*z),-1,1))
    return 2*(C-math.cos(b)*A)

def marked_triangle_tail(s):
    if s>=S3max:return 0.0
    if s<=Smin:return 2/math.pi*(math.pi/2-3*math.asin(1/3))
    return 4*(1-s/S3max)-6/math.pi*segment(s)

rng=default_rng(210531)
U=rng.normal(size=(160000,3));U/=np.linalg.norm(U,axis=1)[:,None]
for i in range(500):
    u=U[i]
    a=np.array([0.,1.,0.])
    if abs(a@u)>0.95:a=np.array([0.,0.,1.])
    p=np.cross(u,a);p/=np.linalg.norm(p)
    q=np.cross(u,p)
    pts=np.stack((V@p,V@q),axis=1)
    hull=ConvexHull(pts)
    assert (len(hull.vertices)==3)==bool(triangle(u)), (i,len(hull.vertices),triangle(u))
    assert abs(hull.volume-area(u))<1e-11
print('PROJECTED_HULL_SILHOUETTE_AND_AREA_GEOMETRIC_IDENTITIES_OK')

# Compare spherical cap segment formula with direct spherical polar integral.
for s in [Smin+1e-4,2.88,3,3.18,3.25,S0-1e-4]:
    b=math.acos(s/S3max)
    # cap around (1,1,1)/sqrt(3), outside side normal n: dot(c,n)=-1/3.
    d=math.acos(-1/3)
    def integrand(t):
        k=(math.cos(math.pi/2)-math.cos(t)*math.cos(d))/(math.sin(t)*math.sin(d))
        return 2*math.acos(np.clip(k,-1,1))*math.sin(t)
    val=quad(integrand,d-math.pi/2,b,epsabs=1e-11)[0]
    assert abs(val-segment(s))<2e-10, (s,val,segment(s))
print('SPHERICAL_SEGMENT_EXACT_FORMULA_AGREES_WITH_DIRECT_QUADRATURE_OK')

N=1900000
U=rng.normal(size=(N,3));U/=np.linalg.norm(U,axis=1)[:,None]
A=area(U)
tri=triangle(U)
for s in [Smin+1e-4,2.85,2.9,3,3.12,3.20,3.26,3.29,3.40,S3max-1e-4]:
    p=marked_triangle_tail(s)
    emp=np.mean((A>s)&tri)
    sd=math.sqrt(max(p*(1-p)/N,1e-12))
    assert abs(emp-p)<5.5*sd+4e-4,(s,p,emp,sd)
assert abs(np.mean(tri)-marked_triangle_tail(Smin))<0.002
print('HAAR_MARKED_TRIANGULAR_SHADOW_TAIL_AGREES_WITH_FORMULA_OK',N)

# Check the marginal moment consistency independently of Monte Carlo.
from scipy.integrate import quad
M3=quad(marked_triangle_tail,Smin,S3max,epsabs=1e-9)[0] + Smin*marked_triangle_tail(Smin)
# M3 is E[S*I(N=3)]. From area-weighted silhouette identity it equals 2*pi/sqrt(3)?
# Existing moment formula E[B|N=3]=pi/(sqrt(3)*Omega), p3=2*Omega/pi -> 2/sqrt(3).
assert abs(M3-2/math.sqrt(3))<1e-8,(M3,2/math.sqrt(3))
print('MARKED_FIRST_MOMENT_RECONCILES_WITH_KNOWN_CONDITIONAL_IDENTITY_OK')
Omega=math.pi/2-3*math.asin(1/3)
M32=quad(lambda s: 2*s*marked_triangle_tail(s),Smin,S3max,epsabs=1e-9)[0] + Smin**2*marked_triangle_tail(Smin)
prior2=8*Omega/math.pi+16*math.sqrt(2)/(3*math.pi)
assert abs(M32-prior2)<1e-8,(M32,prior2)
print('MARKED_SECOND_MOMENT_RECONCILES_WITH_KNOWN_CONDITIONAL_IDENTITY_OK')
print('ALL_MARKED_TETRAHEDRAL_SHADOW_CHECKS_OK')
